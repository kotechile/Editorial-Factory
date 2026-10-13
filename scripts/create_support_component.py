#!/usr/bin/env python3
"""Write CustomerSupportSection component to software-factory-core."""
import pathlib

code = '''"use client";

import * as React from "react";
import {
  Send,
  Search,
  CheckCircle2,
  Clock,
  AlertCircle,
  Loader2,
  Check,
  RefreshCw,
} from "lucide-react";
import { Badge } from "@/components/ui/badge";
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from "@/components/ui/card";

export interface SupportTicket {
  id: number;
  ticket_id: string;
  name: string;
  email: string;
  category: "complaint" | "comment" | "billing" | "bug" | "general";
  product: string;
  subject: string;
  message: string;
  status: "new" | "in_progress" | "resolved" | "dismissed";
  priority: string;
  created_at: string;
  updated_at: string;
}

export default function CustomerSupportSection() {
  const [activeTab, setActiveTab] = React.useState<"submit" | "track">("submit");

  // Form state
  const [name, setName] = React.useState("");
  const [email, setEmail] = React.useState("");
  const [category, setCategory] = React.useState<string>("complaint");
  const [product, setProduct] = React.useState<string>("general");
  const [subject, setSubject] = React.useState("");
  const [message, setMessage] = React.useState("");
  const [submitting, setSubmitting] = React.useState(false);
  const [submitError, setSubmitError] = React.useState<string | null>(null);
  const [submittedTicket, setSubmittedTicket] = React.useState<string | null>(null);

  // Tracking state
  const [searchQuery, setSearchQuery] = React.useState("");
  const [statusFilter, setStatusFilter] = React.useState<string>("all");
  const [loadingTickets, setLoadingTickets] = React.useState(false);
  const [trackError, setTrackError] = React.useState<string | null>(null);
  const [tickets, setTickets] = React.useState<SupportTicket[]>([]);
  const [updatingId, setUpdatingId] = React.useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setSubmitError(null);

    if (!email.trim() || !email.includes("@")) {
      setSubmitError("Please enter a valid email address.");
      return;
    }
    if (!subject.trim()) {
      setSubmitError("Please enter a subject.");
      return;
    }
    if (!message.trim() || message.trim().length < 5) {
      setSubmitError("Please provide at least 5 characters in your message.");
      return;
    }

    setSubmitting(true);
    try {
      const res = await fetch("/api/support", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          name: name.trim(),
          email: email.trim(),
          category,
          product,
          subject: subject.trim(),
          message: message.trim(),
        }),
      });

      const data = await res.json();
      if (!res.ok || !data.success) {
        throw new Error(data.error || "Failed to submit support request.");
      }

      setSubmittedTicket(data.ticket_id);
      setSubject("");
      setMessage("");
    } catch (err: unknown) {
      setSubmitError(err instanceof Error ? err.message : "Failed to submit support request.");
    } finally {
      setSubmitting(false);
    }
  };

  const loadTickets = React.useCallback(async (query = "") => {
    setLoadingTickets(true);
    setTrackError(null);
    try {
      const params = new URLSearchParams();
      if (query.trim()) params.set("query", query.trim());
      if (statusFilter !== "all") params.set("status", statusFilter);

      const res = await fetch(`/api/support?${params.toString()}`);
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || "Failed to fetch tickets.");
      setTickets(data.tickets || []);
    } catch (err: unknown) {
      setTrackError(err instanceof Error ? err.message : "Failed to fetch tickets.");
    } finally {
      setLoadingTickets(false);
    }
  }, [statusFilter]);

  const handleStatusUpdate = async (ticketId: string, newStatus: string) => {
    setUpdatingId(ticketId);
    try {
      const res = await fetch("/api/support", {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ticket_id: ticketId, status: newStatus }),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || "Failed to update status.");

      setTickets((prev) =>
        prev.map((t) => (t.ticket_id === ticketId ? { ...t, status: newStatus as SupportTicket["status"] } : t))
      );
    } catch (err: unknown) {
      alert(err instanceof Error ? err.message : "Failed to update status");
    } finally {
      setUpdatingId(null);
    }
  };

  React.useEffect(() => {
    if (activeTab === "track") {
      loadTickets(searchQuery);
    }
  }, [activeTab, statusFilter, loadTickets, searchQuery]);

  return (
    <div id="contact-service" className="space-y-4 pt-6 border-t border-border/60">
      <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3">
        <div>
          <div className="flex items-center gap-2">
            <h3 className="text-lg font-bold text-foreground">Contact Customer Service</h3>
            <Badge variant="outline" className="font-mono text-[10px]">
              SUPABASE TRACKED
            </Badge>
          </div>
          <p className="text-xs text-muted mt-0.5">
            Submit complaints, bug reports, and billing questions with real-time status tracking.
          </p>
        </div>

        {/* Tab Switcher */}
        <div className="flex items-center gap-1 rounded-xl bg-muted/40 p-1 border border-border/60 text-xs font-semibold">
          <button
            type="button"
            onClick={() => setActiveTab("submit")}
            className={`px-3 py-1.5 rounded-lg transition-all cursor-pointer ${
              activeTab === "submit"
                ? "bg-card text-foreground shadow-xs ring-1 ring-border/80"
                : "text-muted hover:text-foreground"
            }`}
          >
            Submit Request
          </button>
          <button
            type="button"
            onClick={() => {
              setActiveTab("track");
              loadTickets();
            }}
            className={`px-3 py-1.5 rounded-lg transition-all cursor-pointer ${
              activeTab === "track"
                ? "bg-card text-foreground shadow-xs ring-1 ring-border/80"
                : "text-muted hover:text-foreground"
            }`}
          >
            Track Status
          </button>
        </div>
      </div>

      {activeTab === "submit" ? (
        <Card className="rounded-2xl border border-border/80 bg-card shadow-2xs overflow-hidden p-0">
          <div className="h-1.5 w-full bg-primary" />
          <CardHeader className="p-6 pb-2">
            <CardTitle className="text-base font-bold">Submit a Complaint, Comment, or Inquiry</CardTitle>
            <CardDescription className="text-xs">
              Every request is assigned a persistent reference ID stored in Supabase with audited resolution timestamps.
            </CardDescription>
          </CardHeader>

          <CardContent className="p-6 pt-4 space-y-4">
            {submittedTicket ? (
              <div className="rounded-xl bg-success/10 border border-success/30 p-5 text-center space-y-3">
                <div className="mx-auto w-10 h-10 rounded-full bg-success/20 text-success flex items-center justify-center">
                  <CheckCircle2 className="h-6 w-6" />
                </div>
                <div>
                  <h4 className="font-bold text-sm text-foreground">Request Submitted Successfully</h4>
                  <p className="text-xs text-muted mt-1">
                    Your reference ticket has been logged to Supabase:
                  </p>
                  <p className="mt-2 font-mono font-bold text-sm text-primary select-all">
                    {submittedTicket}
                  </p>
                </div>
                <div className="flex justify-center gap-3 pt-2">
                  <button
                    type="button"
                    onClick={() => {
                      setSubmittedTicket(null);
                    }}
                    className="rounded-lg border border-border px-3 py-1.5 text-xs font-semibold hover:bg-muted/20 cursor-pointer"
                  >
                    Submit Another
                  </button>
                  <button
                    type="button"
                    onClick={() => {
                      setSearchQuery(submittedTicket);
                      setActiveTab("track");
                    }}
                    className="rounded-lg bg-primary text-white px-3 py-1.5 text-xs font-semibold hover:bg-primary/90 cursor-pointer"
                  >
                    Track This Ticket
                  </button>
                </div>
              </div>
            ) : (
              <form onSubmit={handleSubmit} className="space-y-4">
                {submitError && (
                  <div className="flex items-start gap-2 rounded-xl bg-destructive/10 border border-destructive/30 p-3 text-xs text-destructive">
                    <AlertCircle className="h-4 w-4 shrink-0 mt-0.5" />
                    <span>{submitError}</span>
                  </div>
                )}

                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div>
                    <label htmlFor="support-email" className="block text-xs font-semibold text-foreground mb-1">
                      Email Address <span className="text-destructive">*</span>
                    </label>
                    <input
                      id="support-email"
                      type="email"
                      required
                      value={email}
                      onChange={(e) => setEmail(e.target.value)}
                      placeholder="name@company.com"
                      className="w-full rounded-xl border border-border/80 bg-background px-3 py-2 text-xs text-foreground placeholder:text-muted/60 focus:outline-hidden focus:ring-2 focus:ring-primary"
                    />
                  </div>

                  <div>
                    <label htmlFor="support-name" className="block text-xs font-semibold text-foreground mb-1">
                      Full Name
                    </label>
                    <input
                      id="support-name"
                      type="text"
                      value={name}
                      onChange={(e) => setName(e.target.value)}
                      placeholder="Optional"
                      className="w-full rounded-xl border border-border/80 bg-background px-3 py-2 text-xs text-foreground placeholder:text-muted/60 focus:outline-hidden focus:ring-2 focus:ring-primary"
                    />
                  </div>
                </div>

                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div>
                    <label htmlFor="support-category" className="block text-xs font-semibold text-foreground mb-1">
                      Request Category <span className="text-destructive">*</span>
                    </label>
                    <select
                      id="support-category"
                      value={category}
                      onChange={(e) => setCategory(e.target.value)}
                      className="w-full rounded-xl border border-border/80 bg-background px-3 py-2 text-xs text-foreground focus:outline-hidden focus:ring-2 focus:ring-primary"
                    >
                      <option value="complaint">Complaint / Issue</option>
                      <option value="comment">Comment / Feedback</option>
                      <option value="billing">Billing &amp; Subscription</option>
                      <option value="bug">Bug / Accuracy Discrepancy</option>
                      <option value="general">General Inquiry</option>
                    </select>
                  </div>

                  <div>
                    <label htmlFor="support-product" className="block text-xs font-semibold text-foreground mb-1">
                      Relevant Product
                    </label>
                    <select
                      id="support-product"
                      value={product}
                      onChange={(e) => setProduct(e.target.value)}
                      className="w-full rounded-xl border border-border/80 bg-background px-3 py-2 text-xs text-foreground focus:outline-hidden focus:ring-2 focus:ring-primary"
                    >
                      <option value="general">General Factory / Platform</option>
                      <option value="billing">Factory Billing Portal</option>
                      <option value="ledgerlink">LedgerLink (Stripe Recon)</option>
                      <option value="facturgate">FacturGate (EU E-Invoice)</option>
                      <option value="parcelproof">ParcelProof (Carrier Audit)</option>
                      <option value="caseproof">CaseProof (Automation Capex)</option>
                      <option value="spendproof">SpendProof (AI FinOps)</option>
                    </select>
                  </div>
                </div>

                <div>
                  <label htmlFor="support-subject" className="block text-xs font-semibold text-foreground mb-1">
                    Subject Summary <span className="text-destructive">*</span>
                  </label>
                  <input
                    id="support-subject"
                    type="text"
                    required
                    value={subject}
                    onChange={(e) => setSubject(e.target.value)}
                    placeholder="Brief summary of your complaint or comment"
                    className="w-full rounded-xl border border-border/80 bg-background px-3 py-2 text-xs text-foreground placeholder:text-muted/60 focus:outline-hidden focus:ring-2 focus:ring-primary"
                  />
                </div>

                <div>
                  <label htmlFor="support-message" className="block text-xs font-semibold text-foreground mb-1">
                    Details &amp; Description <span className="text-destructive">*</span>
                  </label>
                  <textarea
                    id="support-message"
                    required
                    rows={4}
                    value={message}
                    onChange={(e) => setMessage(e.target.value)}
                    placeholder="Provide specific details, error messages, or feedback..."
                    className="w-full rounded-xl border border-border/80 bg-background px-3 py-2 text-xs text-foreground placeholder:text-muted/60 focus:outline-hidden focus:ring-2 focus:ring-primary"
                  />
                </div>

                <div className="flex items-center justify-between pt-2">
                  <p className="text-[11px] text-muted">
                    Stored securely in Supabase • Confidential &amp; SLA tracked
                  </p>
                  <button
                    type="submit"
                    disabled={submitting}
                    className="flex items-center gap-2 rounded-xl bg-primary hover:bg-primary/90 px-4 py-2.5 text-xs font-semibold text-white shadow-xs transition-all cursor-pointer disabled:opacity-50"
                  >
                    {submitting ? (
                      <Loader2 className="h-4 w-4 animate-spin" />
                    ) : (
                      <Send className="h-4 w-4" />
                    )}
                    <span>Submit Request</span>
                  </button>
                </div>
              </form>
            )}
          </CardContent>
        </Card>
      ) : (
        <Card className="rounded-2xl border border-border/80 bg-card shadow-2xs overflow-hidden p-0">
          <CardHeader className="p-6 pb-4">
            <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3">
              <div>
                <CardTitle className="text-base font-bold">Customer Request &amp; Complaint Tracker</CardTitle>
                <CardDescription className="text-xs">
                  Track resolution status across all logged tickets in Supabase.
                </CardDescription>
              </div>

              {/* Status Filter */}
              <div className="flex items-center gap-2 text-xs">
                <select
                  value={statusFilter}
                  onChange={(e) => setStatusFilter(e.target.value)}
                  className="rounded-lg border border-border/80 bg-background px-2.5 py-1.5 text-xs text-foreground focus:outline-hidden focus:ring-2 focus:ring-primary"
                >
                  <option value="all">All Statuses</option>
                  <option value="new">New</option>
                  <option value="in_progress">In Progress</option>
                  <option value="resolved">Resolved</option>
                  <option value="dismissed">Dismissed</option>
                </select>
                <button
                  type="button"
                  onClick={() => loadTickets(searchQuery)}
                  disabled={loadingTickets}
                  className="p-1.5 rounded-lg border border-border hover:bg-muted/20 text-muted hover:text-foreground cursor-pointer"
                  title="Refresh tickets"
                >
                  <RefreshCw className={`h-3.5 w-3.5 ${loadingTickets ? "animate-spin" : ""}`} />
                </button>
              </div>
            </div>

            {/* Search Input */}
            <div className="mt-4 flex gap-2">
              <div className="relative flex-1">
                <Search className="absolute left-3 top-2.5 h-3.5 w-3.5 text-muted" />
                <input
                  type="text"
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  onKeyDown={(e) => {
                    if (e.key === "Enter") loadTickets(searchQuery);
                  }}
                  placeholder="Search by Ticket ID (TKT-...), email, or keywords..."
                  className="w-full rounded-xl border border-border/80 bg-background pl-9 pr-3 py-2 text-xs text-foreground placeholder:text-muted/60 focus:outline-hidden focus:ring-2 focus:ring-primary"
                />
              </div>
              <button
                type="button"
                onClick={() => loadTickets(searchQuery)}
                disabled={loadingTickets}
                className="rounded-xl bg-primary text-white px-4 py-2 text-xs font-semibold hover:bg-primary/90 cursor-pointer disabled:opacity-50"
              >
                Search
              </button>
            </div>
          </CardHeader>

          <CardContent className="p-6 pt-0">
            {trackError && (
              <div className="mb-4 p-3 rounded-xl bg-destructive/10 border border-destructive/30 text-xs text-destructive flex items-center gap-2">
                <AlertCircle className="h-4 w-4 shrink-0" />
                <span>{trackError}</span>
              </div>
            )}

            {loadingTickets ? (
              <div className="p-12 text-center text-xs text-muted flex items-center justify-center gap-2">
                <Loader2 className="h-4 w-4 animate-spin text-primary" />
                <span>Loading tickets from Supabase...</span>
              </div>
            ) : tickets.length === 0 ? (
              <div className="p-8 text-center rounded-xl border border-dashed border-border/80 bg-muted/10 space-y-2">
                <p className="text-xs font-semibold text-foreground">No matching support tickets found</p>
                <p className="text-[11px] text-muted">
                  Submit a request via the form or clear search filters to view recorded tickets.
                </p>
              </div>
            ) : (
              <div className="space-y-3">
                {tickets.map((ticket) => {
                  let statusBadge = (
                    <Badge variant="outline" className="font-mono text-[10px]">
                      {ticket.status}
                    </Badge>
                  );
                  if (ticket.status === "new") {
                    statusBadge = (
                      <span className="inline-flex items-center gap-1 rounded-md bg-warning/10 text-warning px-2 py-0.5 text-[10px] font-mono font-bold">
                        <Clock className="h-3 w-3" />
                        NEW
                      </span>
                    );
                  } else if (ticket.status === "in_progress") {
                    statusBadge = (
                      <span className="inline-flex items-center gap-1 rounded-md bg-primary/10 text-primary px-2 py-0.5 text-[10px] font-mono font-bold">
                        <RefreshCw className="h-3 w-3" />
                        IN PROGRESS
                      </span>
                    );
                  } else if (ticket.status === "resolved") {
                    statusBadge = (
                      <span className="inline-flex items-center gap-1 rounded-md bg-success/10 text-success px-2 py-0.5 text-[10px] font-mono font-bold">
                        <Check className="h-3 w-3" />
                        RESOLVED
                      </span>
                    );
                  }

                  return (
                    <div
                      key={ticket.ticket_id}
                      className="rounded-xl border border-border/80 bg-card p-4 space-y-2.5 transition-all hover:border-border"
                    >
                      <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-1 text-xs">
                        <div className="flex items-center gap-2">
                          <span className="font-mono font-bold text-foreground">{ticket.ticket_id}</span>
                          {statusBadge}
                          <span className="text-[10px] font-mono uppercase text-muted">
                            • {ticket.category}
                          </span>
                        </div>
                        <span className="text-[11px] text-muted font-mono">
                          {new Date(ticket.created_at).toLocaleString()}
                        </span>
                      </div>

                      <div>
                        <h4 className="font-semibold text-xs text-foreground">{ticket.subject}</h4>
                        <p className="text-xs text-muted mt-1 leading-relaxed whitespace-pre-wrap">
                          {ticket.message}
                        </p>
                      </div>

                      <div className="pt-2 border-t border-border/60 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-2 text-[11px]">
                        <div className="text-muted">
                          <span>From: </span>
                          <span className="text-foreground font-medium">
                            {ticket.name ? `${ticket.name} (${ticket.email})` : ticket.email}
                          </span>
                          <span className="ml-2">• Product: </span>
                          <span className="text-foreground font-mono font-semibold">{ticket.product}</span>
                        </div>

                        {/* Status Update Control */}
                        <div className="flex items-center gap-1.5">
                          <label htmlFor={`status-${ticket.ticket_id}`} className="text-muted text-[10px]">Status:</label>
                          <select
                            id={`status-${ticket.ticket_id}`}
                            value={ticket.status}
                            disabled={updatingId === ticket.ticket_id}
                            onChange={(e) => handleStatusUpdate(ticket.ticket_id, e.target.value)}
                            className="rounded-md border border-border bg-background px-2 py-1 text-[11px] font-semibold text-foreground focus:ring-1 focus:ring-primary cursor-pointer disabled:opacity-50"
                          >
                            <option value="new">New</option>
                            <option value="in_progress">In Progress</option>
                            <option value="resolved">Resolved</option>
                            <option value="dismissed">Dismissed</option>
                          </select>
                        </div>
                      </div>
                    </div>
                  );
                })}
              </div>
            )}
          </CardContent>
        </Card>
      )}
    </div>
  );
}
'''

target = pathlib.Path("/root/software-factory-core/src/components/customer-support-section.tsx")
target.parent.mkdir(parents=True, exist_ok=True)
target.write_text(code)
print(f"Successfully wrote {target} ({len(code)} bytes)")
