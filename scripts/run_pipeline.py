import subprocess
import os
import sys

def run_pipeline(module_name):
    print(f"\n🚀 Running full pipeline for module: {module_name}")

    # 0. Unzip files for module first
    subprocess.run(["python", "scripts/unzip_module.py", module_name], check=True)

    old_path = f"Modules/{module_name}/old"
    new_path = f"Modules/{module_name}/new"
    result_path = f"Results/{module_name}"
    report_path = os.path.join(result_path, "report.md")
    diff_prefix = os.path.join(result_path, "diff_graph")  # We will create diff_graph.png and diff_graph.dot

    os.makedirs(result_path, exist_ok=True)

    # 1. Generate call graphs
    subprocess.run(["python", "scripts/generate_callgraph.py", module_name], check=True)

    # 2. Generate textual comparison report
    subprocess.run(["python", "scripts/compare_callgraphs.py", old_path, new_path, report_path], check=True)

    # 3. Generate visual diff graph (no pygraphviz)
    subprocess.run(["python", "scripts/diff_callgraph_plain.py",
                    os.path.join(result_path, "old_callgraph.dot"),
                    os.path.join(result_path, "new_callgraph.dot"),
                    diff_prefix], check=True)

    print(f"🎉 Pipeline completed for module: {module_name}\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scripts/run_pipeline.py <module_name>")
        sys.exit(1)

    run_pipeline(sys.argv[1])
