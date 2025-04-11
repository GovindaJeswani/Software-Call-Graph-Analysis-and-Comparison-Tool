# call_graph.py
import sys
import os
from get_files import get_python_files
from pycallgraph2 import PyCallGraph
from pycallgraph2.output import GraphvizOutput

def generate_graph(py_files, output_dot, output_png):
    if not py_files:
        print(f"❌ No Python files found for {output_dot}")
        return

    with PyCallGraph(output=GraphvizOutput(output_file=output_png)):
        for file in py_files:
            with open(file, "r", encoding="utf-8") as f:
                try:
                    code = compile(f.read(), file, 'exec')
                    exec(code, {})
                except Exception as e:
                    print(f"⚠️ Skipped {file}: {e}")

    # PyCallGraph2 only generates PNG; adding dummy DOT
    with open(output_dot, "w") as f:
        f.write("digraph G {\n")
        f.write("// Call graph not available as DOT in PyCallGraph2\n")
        f.write("}\n")

if __name__ == "__main__":
    module = sys.argv[1]
    old_files = get_python_files(module, "old")
    new_files = get_python_files(module, "new")

    os.makedirs(f"../Results/{module}", exist_ok=True)

    generate_graph(old_files, f"../Results/{module}/old_callgraph.dot", f"../Results/{module}/old_callgraph.png")
    generate_graph(new_files, f"../Results/{module}/new_callgraph.dot", f"../Results/{module}/new_callgraph.png")
