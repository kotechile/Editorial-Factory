#!/usr/bin/env python3
"""Build and deploy Support / Contact Customer Service feature in software-factory-core."""
import pathlib

# 1. Write src/app/api/support/route.ts
support_route = """import { NextRequest, NextResponse } from "next/server";
import { createAdminClient } from "@/lib/supabase/admin";

export type TicketStatus = "new" | "in_progress" | "resolved" | "dismissed";
export type TicketCategory = "complaint" | "comment" | "billing" | "bug" | "general";

function generateTicketId(): string {
  const dateStr = new Date().toISOString().slice(0, 10).replace(/-/g, "");
  const rand = Math.random().toString(36).substring(2, 6).toUpperCase();
  return `TKT-${dateStr}-${rand}`;
}

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const {
      email,
      name = "",
      category = "general",
      product = "factory",
      subject,
      message,
      priority = "medium",
    } = body;

    if (!email || typeof email !== "string" || !email.includes("@")) {
      return NextResponse.json({ error: "A valid email address is required." }, { status: 400 });
    }

    if (!subject || typeof subject !== "string" || subject.trim().length === 0) {
      return NextResponse.json({ error: "Subject is required." }, { status: 400 });
    }

    if (!message || typeof message !== "string" || message.trim().length < 5) {
      return NextResponse.json({ error: "Message must be at least 5 characters long." }, { status: 400 });
    }

    const ticketId = generateTicketId();
    const now = new Date().toISOString();

    const payload = {
      ticket_id: ticketId,
      name: String(name).trim(),
      email: String(email).trim().toLowerCase(),
      category: String(category).trim() as TicketCategory,
      product: String(product).trim(),
      subject: String(subject).trim(),
      message: String(message).trim(),
      status: "new" as TicketStatus,
      priority: String(priority).trim(),
      notes: [],
      created_at: now,
      updated_at: now,
    };

    const supabase = createAdminClient();
    const { data, error } = await supabase
      .from("events")
      .insert({
        event: "customer_service",
        product: String(product).trim(),
        payload,
      })
      .select("id, created_at")
      .single();

    if (error) {
      console.error("[support] failed to insert into Supabase:", error);
      return NextResponse.json(
        { error: `Database error: ${error.message}` },
        { status: 500 }
      );
    }

    return NextResponse.json({
      success: true,
      ticket_id: ticketId,
      status: "new",
      id: data?.id,
      created_at: data?.created_at || now,
      message: "Your message has been submitted. Our team will review it shortly.",
    });
  } catch (err: unknown) {
    const message = err instanceof Error ? err.message : "Internal server error";
    return NextResponse.json({ error: message }, { status: 500 });
  }
}

export async function GET(req: NextRequest) {
  try {
    const { searchParams } = new URL(req.url);
    const query = searchParams.get("query")?.trim() || "";
    const ticketId = searchParams.get("ticket_id")?.trim() || "";
    const email = searchParams.get("email")?.trim().toLowerCase() || "";
    const status = searchParams.get("status")?.trim() || "";
    const limit = Math.min(Number(searchParams.get("limit") || 50), 100);

    const supabase = createAdminClient();

    let dbQuery = supabase
      .from("events")
      .select("id, event, product, payload, created_at")
      .eq("event", "customer_service")
      .order("created_at", { ascending: false })
      .limit(limit);

    if (ticketId) {
      dbQuery = dbQuery.eq("payload->>ticket_id", ticketId);
    } else if (email) {
      dbQuery = dbQuery.eq("payload->>email", email);
    } else if (status) {
      dbQuery = dbQuery.eq("payload->>status", status);
    }

    const { data, error } = await dbQuery;

    if (error) {
      return NextResponse.json({ error: error.message }, { status: 500 });
    }

    const tickets = (data || []).map((row) => {
      const p = (row.payload as Record<string, unknown>) || {};
      return {
        id: row.id,
        ticket_id: (p.ticket_id as string) || `TKT-${row.id}`,
        name: (p.name as string) || "",
        email: (p.email as string) || "",
        category: (p.category as string) || "general",
        product: row.product || (p.product as string) || "factory",
        subject: (p.subject as string) || "",
        message: (p.message as string) || "",
        status: (p.status as TicketStatus) || "new",
        priority: (p.priority as string) || "medium",
        created_at: (p.created_at as string) || row.created_at,
        updated_at: (p.updated_at as string) || row.created_at,
      };
    });

    const filtered = query
      ? tickets.filter(
          (t) =>
            t.ticket_id.toLowerCase().includes(query.toLowerCase()) ||
            t.email.toLowerCase().includes(query.toLowerCase()) ||
            t.subject.toLowerCase().includes(query.toLowerCase()) ||
            t.message.toLowerCase().includes(query.toLowerCase())
        )
      : tickets;

    return NextResponse.json({
      success: true,
      count: filtered.length,
      tickets: filtered,
    });
  } catch (err: unknown) {
    const message = err instanceof Error ? err.message : "Internal server error";
    return NextResponse.json({ error: message }, { status: 500 });
  }
}

export async function PATCH(req: NextRequest) {
  try {
    const body = await req.json();
    const { ticket_id, id, status, note } = body;

    if (!status || !["new", "in_progress", "resolved", "dismissed"].includes(status)) {
      return NextResponse.json(
        { error: "Invalid status. Allowed: 'new', 'in_progress', 'resolved', 'dismissed'." },
        { status: 400 }
      );
    }

    if (!ticket_id && !id) {
      return NextResponse.json(
        { error: "Either 'ticket_id' or 'id' is required to update a ticket." },
        { status: 400 }
      );
    }

    const supabase = createAdminClient();

    let fetchQuery = supabase
      .from("events")
      .select("id, payload")
      .eq("event", "customer_service");

    if (id) {
      fetchQuery = fetchQuery.eq("id", id);
    } else {
      fetchQuery = fetchQuery.eq("payload->>ticket_id", ticket_id);
    }

    const { data: rows, error: fetchErr } = await fetchQuery.limit(1);

    if (fetchErr || !rows || rows.length === 0) {
      return NextResponse.json({ error: "Ticket not found." }, { status: 404 });
    }

    const targetRow = rows[0];
    const currentPayload = (targetRow.payload as Record<string, unknown>) || {};
    const now = new Date().toISOString();

    const notes = Array.isArray(currentPayload.notes) ? [...currentPayload.notes] : [];
    if (note && typeof note === "string") {
      notes.push({ text: note.trim(), timestamp: now });
    }

    const updatedPayload = {
      ...currentPayload,
      status,
      notes,
      updated_at: now,
    };

    const { error: updateErr } = await supabase
      .from("events")
      .update({ payload: updatedPayload })
      .eq("id", targetRow.id);

    if (updateErr) {
      return NextResponse.json({ error: updateErr.message }, { status: 500 });
    }

    return NextResponse.json({
      success: true,
      ticket_id: (updatedPayload.ticket_id as string) || ticket_id,
      status,
      updated_at: now,
      message: `Ticket status updated to '${status}'.`,
    });
  } catch (err: unknown) {
    const message = err instanceof Error ? err.message : "Internal server error";
    return NextResponse.json({ error: message }, { status: 500 });
  }
}
"""

target = pathlib.Path("/root/software-factory-core/src/app/api/support/route.ts")
target.parent.mkdir(parents=True, exist_ok=True)
target.write_text(support_route)
print(f"Wrote {target}")
