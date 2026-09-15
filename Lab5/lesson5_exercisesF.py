
# ============================================================
# PART F - Applied challenge: Report builder
# ============================================================

# 1. create_report(title, *sections, **metadata) - returns a dictionary.
# 2. Each section can be a string OR a small dictionary.
# Design choice: a plain string section is treated as a simple
# paragraph of text; a dictionary section is treated as a titled
# sub-section with its own heading and body, e.g.
# {"heading": "Summary", "body": "..."} - this keeps simple sections
# simple while still allowing structure where it's useful.
def create_report(title, *sections, **metadata):
    return {
        "title": title,
        "sections": list(sections),
        "metadata": metadata,
    }


# 3. Metadata may include author, department, version, confidential, date.
sales_report = create_report(
    "Q3 Sales Report",
    "Overall performance was strong this quarter.",
    {"heading": "Regional Breakdown", "body": "EMEA led growth at 12%."},
    author="Alice Smith",
    department="Sales",
    version="1.0",
    confidential=True,
    date="2026-09-15",
)
print(sales_report)


# 4. summarize_report(report) - a readable multi-line string.
def summarize_report(report):
    lines = [f"REPORT: {report['title']}", ""]

    for section in report["sections"]:
        if isinstance(section, dict):
            lines.append(f"-- {section['heading']} --")
            lines.append(section["body"])
        else:
            lines.append(section)
        lines.append("")

    if report["metadata"]:
        lines.append("Metadata:")
        for key, value in report["metadata"].items():
            lines.append(f"  {key}: {value}")

    return "\n".join(lines)


print(summarize_report(sales_report))


# 5. count_words(*sections): counts words across all supplied textual sections.
def count_words(*sections):
    total_words = 0
    for section in sections:
        if isinstance(section, dict):
            total_words += len(section["body"].split())
        else:
            total_words += len(section.split())
    return total_words


print(count_words(
    "Overall performance was strong this quarter.",
    {"heading": "Regional Breakdown", "body": "EMEA led growth at 12%."},
))


# 6. Use dictionary unpacking to create at least two reports from
# predefined metadata dictionaries.
finance_metadata = {"author": "Diana Hunter", "department": "Finance", "version": "2.1"}
hr_metadata = {"author": "Hermes Maker", "department": "HR", "confidential": True}

finance_report = create_report(
    "Q3 Finance Report",
    "Expenses remained within budget.",
    **finance_metadata,
)

hr_report = create_report(
    "Q3 HR Report",
    "Headcount grew by 5%.",
    **hr_metadata,
)

print(summarize_report(finance_report))
print()
print(summarize_report(hr_report))


# 7. Demonstrate at least one case where the function deliberately
# ignores or handles a missing optional metadata field.
# finance_metadata above has no "confidential" key at all, and
# hr_metadata above has no "version" key. summarize_report() only
# prints whatever keys happen to be present in report["metadata"] -
# it never assumes a specific key exists, so a missing optional field
# is simply absent from the output rather than causing an error.
minimal_report = create_report("Minimal Report", "Just one line of text.")
print(summarize_report(minimal_report))  # no metadata section printed at all
