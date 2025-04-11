import os
import sys
import ast
import networkx as nx
from pygraphviz import AGraph

def get_function_calls(filepath):
    with open(filepath, "r") as file:
        tree = ast.parse(file.read(), filename=filepath)

    calls = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            func_name = node.name
            for child in ast.walk(node):
                if isinstance(child, ast.Call) and isinstance(child.func, ast.Name):
                    calls.add((func_name, child.func.id))
    return calls

def collect_calls(folder):
    edges = set()
    for root, _, files in os.walk(folder):
        for f in files:
            if f.endswith(".py"):
                edges.update(get_function_calls(os.path.join(root, f)))
    return edges

def generate_diff_graph(old_edges, new_edges, output_path):
    G = AGraph(directed=True)

    all_funcs = set()
    for a, b in old_edges.union(new_edges):
        all_funcs.add(a)
        all_funcs.add(b)

    for func in all_funcs:
        in_old = any(func in edge for edge in old_edges)
        in_new = any(func in edge for edge in new_edges)
        if in_old and in_new:
            G.add_node(func, color="green", style="filled", fillcolor="#b6fcb6")
        elif in_old:
            G.add_node(func, color="red", style="filled", fillcolor="#ffc0c0")
        elif in_new:
            G.add_node(func, color="blue", style="filled", fillcolor="#b0d9ff")

    for edge in old_edges:
        if edge in new_edges:
            G.add_edge(*edge, color="green")
        else:
            G.add_edge(*edge, color="red", style="dashed")

    for edge in new_edges:
        if edge not in old_edges:
            G.add_edge(*edge, color="blue")

    G.layout(prog="dot")
    G.draw(output_path)

if __name__ == "__main__":
    old_path = sys.argv[1]
    new_path = sys.argv[2]
    out_path = sys.argv[3]

    old_calls = collect_calls(old_path)
    new_calls = collect_calls(new_path)

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    generate_diff_graph(old_calls, new_calls, out_path)
    print(f"Diff graph saved to {out_path}")
