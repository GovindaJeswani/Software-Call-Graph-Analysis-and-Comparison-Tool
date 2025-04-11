import os
import ast
import sys
import networkx as nx
from networkx.drawing.nx_pydot import write_dot
import subprocess

def filter_python_files(all_files):
    """
    Filters out template files, test/config/setup files, and __init__.py.
    """
    filtered = []
    for f in all_files:
        fname = os.path.basename(f)

        # Skip Jinja2 template placeholders
        with open(f, "r", encoding="utf-8", errors="ignore") as file:
            content = file.read()
            if "{{" in content or "{%" in content:
                print(f"⚠️ Skipping template file: {f}")
                continue

        # Skip unimportant files
        if (
            fname == "__init__.py"
            or fname.startswith("test_")
            or fname in {"config.py", "setup.py"}
        ):
            continue

        filtered.append(f)
    return filtered


def extract_calls(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        tree = ast.parse(file.read(), filename=filepath)

    calls = []
    current_function = None

    class CallVisitor(ast.NodeVisitor):
        def visit_FunctionDef(self, node):
            nonlocal current_function
            current_function = node.name
            self.generic_visit(node)
            current_function = None

        def visit_Call(self, node):
            if current_function and isinstance(node.func, ast.Name):
                calls.append((current_function, node.func.id))
            self.generic_visit(node)

    CallVisitor().visit(tree)
    return calls

def build_call_graph(path):
    graph = nx.DiGraph()
    all_py_files = []

    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                all_py_files.append(os.path.join(root, file))

    filtered_files = filter_python_files(all_py_files)

    for file_path in filtered_files:
        edges = extract_calls(file_path)
        graph.add_edges_from(edges)

    return graph

def generate(path, output_prefix, module_name):
    output_dir = f"Results/{module_name}"
    os.makedirs(output_dir, exist_ok=True)

    graph = build_call_graph(path)
    dot_path = os.path.join(output_dir, f"{output_prefix}_callgraph.dot")
    png_path = os.path.join(output_dir, f"{output_prefix}_callgraph.png")
    write_dot(graph, dot_path)
    subprocess.run(["dot", "-Tpng", dot_path, "-o", png_path])
    print(f"✅ Saved {dot_path} and PNG graph")

def analyze_python_files(path):
    """Returns a dictionary mapping each function to its callees."""
    call_map = {}
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                calls = extract_calls(file_path)
                for caller, callee in calls:
                    if caller not in call_map:
                        call_map[caller] = set()
                    call_map[caller].add(callee)
    return call_map


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("❌ Usage: python generate_callgraph.py <module_name>")
        sys.exit(1)

    module_name = sys.argv[1]
    old_path = f"Modules/{module_name}/old"
    new_path = f"Modules/{module_name}/new"

    if not os.path.exists(old_path) or not os.path.exists(new_path):
        print("❌ Error: 'old' or 'new' folder not found.")
        sys.exit(1)

    generate(old_path, "old", module_name)
    generate(new_path, "new", module_name)
