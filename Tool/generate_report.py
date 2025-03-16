import json
import os

def load_json(file_path):
    """Loads a JSON file if it exists, otherwise returns an empty dictionary."""
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    else:
        print(f"⚠️ Warning: {file_path} not found.")
        return {}

def generate_report():
    """Generates a final report from analysis results."""

    # Load JSON data
    version_changes = load_json("call_graphdiff.json")  # Ensure correct filename
    static_vs_dynamic = load_json("comparison_static_vs_dynamic.json")

    # Initialize the report content
    report = "# Flask Version Comparison Report\n\n"

    # Section 1: Version Changes
    report += "## 1️⃣ Version Changes (Added/Removed Functions)\n"
    
    report += "### ➕ Added Functions:\n"
    for func in version_changes.get("added_calls", []):
        report += f"- `{func}`\n"
    
    report += "\n### ❌ Removed Functions:\n"
    for func in version_changes.get("removed_calls", []):
        report += f"- `{func}`\n"

    # Section 2: Static vs Dynamic Analysis
    report += "\n## 2️⃣ Static vs Dynamic Analysis\n"

    report += "### 🔹 Unused Static Functions (Defined but Never Executed)\n"
    for func in static_vs_dynamic.get("unused_static_functions", []):
        report += f"- `{func['caller']} -> {func['callee']}`\n"

    report += "\n### 🔸 New Dynamic Functions (Executed but Not Found in Static Analysis)\n"
    for func in static_vs_dynamic.get("new_dynamic_functions", []):
        report += f"- `{func['caller']} -> {func['callee']}`\n"

    # Section 3: Call Graphs
    report += "\n## 3️⃣ Call Graphs\n"
    report += "### 📌 Static Call Graph (Flask 2.2.0)\n"
    report += "![Static Call Graph](static_callgraph.png)\n\n"
    report += "### 🔥 Dynamic Call Graph (Flask 3.0.0)\n"
    report += "![Dynamic Call Graph](runtime_callgraph.png)\n\n"

    # Save the report as a Markdown file
    with open("final_report.md", "w") as f:
        f.write(report)

    print("✅ Final report generated: `final_report.md`")

if __name__ == "__main__":
    generate_report()
