#!/usr/bin/env python3
"""Apply exact patch to factory-billing-portal.tsx."""
import pathlib

portal_path = pathlib.Path("/root/software-factory-core/src/components/factory-billing-portal.tsx")
content = portal_path.read_text()

# 1. Header link: insert after Showcase Directory link
if 'href="#contact-service"' not in content:
    target_header = """            <Link
              href="/"
              className="text-xs font-medium text-muted hover:text-foreground transition-colors"
            >
              Showcase Directory
            </Link>"""
    replacement_header = """            <Link
              href="/"
              className="text-xs font-medium text-muted hover:text-foreground transition-colors"
            >
              Showcase Directory
            </Link>
            <span className="text-border">|</span>
            <a
              href="#contact-service"
              className="text-xs font-medium text-muted hover:text-foreground transition-colors"
            >
              Contact Support
            </a>"""
    if target_header in content:
        content = content.replace(target_header, replacement_header, 1)
        print("Inserted Contact Support header link")
    else:
        print("ERROR: could not find target_header")

# 2. Mount component: right before Legal Disclaimers & Operating Conditions
if "<CustomerSupportSection />" not in content:
    target_mount = "{/* Legal Disclaimers & Operating Conditions */}"
    replacement_mount = """{/* Customer Support & Complaint Tracker */}
          <CustomerSupportSection />

          {/* Legal Disclaimers & Operating Conditions */}"""
    if target_mount in content:
        content = content.replace(target_mount, replacement_mount, 1)
        print("Mounted <CustomerSupportSection /> before Legal Disclaimers")
    else:
        print("ERROR: could not find target_mount")

portal_path.write_text(content)
print("Saved factory-billing-portal.tsx")
