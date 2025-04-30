# scripts/compare_callgraphs.py
import json
from generate_callgraph import analyze_python_files

def flatten_call_map(call_map):
    return set((caller, callee) for caller, callees in call_map.items() for callee in callees)

def generate_report(old_map, new_map, output_txt):
    old_flat = flatten_call_map(old_map)
    new_flat = flatten_call_map(new_map)

    added_calls = new_flat - old_flat
    removed_calls = old_flat - new_flat

    added_funcs = set(new_map.keys()) - set(old_map.keys())
    removed_funcs = set(old_map.keys()) - set(new_map.keys())

    with open(output_txt, "w") as f:
        f.write("# 📊 Function Call Difference Report\n\n")

        f.write("## ➕ Added Function Calls\n")
        for c in sorted(added_calls):
            f.write(f"- {c[0]} → {c[1]}\n")
        if not added_calls:
            f.write("None\n")

        f.write("\n## ➖ Removed Function Calls\n")
        for c in sorted(removed_calls):
            f.write(f"- {c[0]} → {c[1]}\n")
        if not removed_calls:
            f.write("None\n")

        f.write("\n## 🔼 Newly Introduced Functions\n")
        for f_new in sorted(added_funcs):
            f.write(f"- {f_new}\n")
        if not added_funcs:
            f.write("None\n")

        f.write("\n## 🔽 Removed Functions\n")
        for f_old in sorted(removed_funcs):
            f.write(f"- {f_old}\n")
        if not removed_funcs:
            f.write("None\n")

if __name__ == "__main__":
    import sys
    old_dir = sys.argv[1]      # Modules/sudoku/old
    new_dir = sys.argv[2]      # Modules/sudoku/new
    output_report = sys.argv[3]  # Results/sudoku/report.md

    old_map = analyze_python_files(old_dir)
    new_map = analyze_python_files(new_dir)

    generate_report(old_map, new_map, output_report)
    print(f"[✔] Report generated at {output_report}")
