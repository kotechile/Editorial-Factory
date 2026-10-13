#!/usr/bin/env python3
"""Complete Customer Support feature in software-factory-core: patch, test, build, and deploy."""
import os
import subprocess
import pathlib
import sys

CORE_DIR = pathlib.Path("/root/software-factory-core")
PORTAL_FILE = CORE_DIR / "src/components/factory-billing-portal.tsx"

def patch_portal():
    print("--- 1. Patching factory-billing-portal.tsx ---")
    content = PORTAL_FILE.read_text()

    # Import
    if "import CustomerSupportSection" not in content:
        content = 'import CustomerSupportSection from "@/components/customer-support-section";\n' + content
        print("Added CustomerSupportSection import")
    else:
        print("CustomerSupportSection import already present")

    # Header nav link
    if 'href="#contact-service"' not in content:
        anchor = 'Showcase Directory\n            </Link>'
        replacement = 'Showcase Directory\n            </Link>\n            <span className="text-border">|</span>\n            <a href="#contact-service" className="text-xs font-medium text-muted hover:text-foreground transition-colors">\n              Contact Support\n            </a>'
        if anchor in content:
            content = content.replace(anchor, replacement, 1)
            print("Added Contact Support header link")
        else:
            print("Warning: could not find Showcase Directory link in header")
    else:
        print("Contact Support header link already present")

    # Component mount
    if "<CustomerSupportSection />" not in content:
        legal_anchor = "{/* Legal Disclaimers & Operating Conditions */}"
        if legal_anchor in content:
            replacement = "{/* Customer Support & Complaint Tracker */}\n          <CustomerSupportSection />\n\n          " + legal_anchor
            content = content.replace(legal_anchor, replacement, 1)
            print("Mounted <CustomerSupportSection /> before Legal Disclaimers")
        else:
            print("Warning: could not find Legal Disclaimers anchor")
    else:
        print("<CustomerSupportSection /> already mounted")

    PORTAL_FILE.write_text(content)
    print("Portal file updated successfully.")

def run_cmd(cmd, cwd=CORE_DIR):
    print(f"\n--- Running: {cmd} in {cwd} ---")
    res = subprocess.run(cmd, shell=True, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    print(res.stdout)
    if res.returncode != 0:
        print(f"FAILED (code {res.returncode}): {cmd}")
        sys.exit(res.returncode)
    return res.stdout

def main():
    patch_portal()

    # Design tokens check
    run_cmd("node scripts/check-design-tokens.mjs")

    # Vitest unit tests
    run_cmd("npm test")

    # Build production bundle
    run_cmd("npm run build")

    # Git commit and push
    run_cmd("git status")
    run_cmd("git add src/app/api/support/route.ts src/components/customer-support-section.tsx src/components/factory-billing-portal.tsx")
    run_cmd('git commit -m "feat(support): add customer service contact form with Supabase status tracking"')
    run_cmd("git push origin main")

    print("\n=== SUCCESS: Support feature deployed to factory main ===")

if __name__ == "__main__":
    main()
