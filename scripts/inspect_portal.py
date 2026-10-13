#!/usr/bin/env python3
"""Refine patch for factory-billing-portal.tsx."""
import pathlib

portal_path = pathlib.Path("/root/software-factory-core/src/components/factory-billing-portal.tsx")
content = portal_path.read_text()

# Find header navigation links
idx_header = content.find("Showcase Directory")
if idx_header != -1:
    print("Around header:")
    print(content[idx_header-100:idx_header+400])

# Find Legal Disclaimers
idx_legal = content.find("Legal Disclaimers")
if idx_legal != -1:
    print("\nAround Legal Disclaimers:")
    print(content[idx_legal-100:idx_legal+200])
