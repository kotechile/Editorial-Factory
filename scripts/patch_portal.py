#!/usr/bin/env python3
"""Inspect and patch factory-billing-portal.tsx to include CustomerSupportSection."""
import pathlib

portal_path = pathlib.Path("/root/software-factory-core/src/components/factory-billing-portal.tsx")
content = portal_path.read_text()

# Check imports
if "CustomerSupportSection" not in content:
    import_stmt = 'import CustomerSupportSection from "@/components/customer-support-section";\n'
    # Add after the last import
    idx = content.find('import {')
    # Let's insert at top imports
    first_import = content.find("import ")
    content = content[:first_import] + import_stmt + content[first_import:]
    print("Added import CustomerSupportSection")

# Check header link
if 'href="#contact-service"' not in content:
    # Look for mcp.json link or similar in header
    target_link = '<a\n            href="/mcp.json"'
    replacement_link = '''<a
            href="#contact-service"
            className="text-muted hover:text-foreground text-xs font-semibold flex items-center gap-1 transition-colors"
          >
            Contact Support
          </a>
          <a
            href="/mcp.json"'''
    if target_link in content:
        content = content.replace(target_link, replacement_link, 1)
        print("Added Contact Support header nav link")
    else:
        print("Warning: target_link not matched verbatim, looking for mcp.json...")
        if 'href="/mcp.json"' in content:
            content = content.replace('href="/mcp.json"', 'href="#contact-service" className="text-muted hover:text-foreground text-xs font-semibold">Contact Support</a>\n          <a href="/mcp.json"', 1)
            print("Added Contact Support near mcp.json")

# Mount component before Legal Disclaimers or at the bottom before closing container
if "<CustomerSupportSection />" not in content:
    legal_target = "{/* Statutory Legal Disclaimers"
    if legal_target in content:
        content = content.replace(legal_target, "{/* Customer Support & Complaint Tracker */}\n      <CustomerSupportSection />\n\n      " + legal_target, 1)
        print("Mounted <CustomerSupportSection /> before legal disclaimers")
    else:
        # Search for Legal Disclaimers
        if "Legal Disclaimers" in content:
            idx = content.find("Legal Disclaimers")
            print(f"Found 'Legal Disclaimers' at index {idx}")
        else:
            print("Could not find legal disclaimers section")

portal_path.write_text(content)
print("Updated factory-billing-portal.tsx successfully")
