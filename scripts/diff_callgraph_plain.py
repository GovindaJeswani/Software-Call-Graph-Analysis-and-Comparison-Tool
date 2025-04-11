import sys
import os
import re
import graphviz

def extract_edges(dot_file):
    """Extract edges from a .dot file (Graphviz format)."""
    edges = set()
    with open(dot_file, 'r', encoding='utf-8') as file:
        for line in file:
            match = re.search(r'"?(\w+)"?\s+->\s+"?(\w+)"?', line)
            if match:
                edges.add((match.group(1), match.group(2)))
    print(f"✅ Extracted {len(edges)} edges from {dot_file}")
    return edges

def generate_diff_graph(old_edges, new_edges, output_path_prefix):
    dot = graphviz.Digraph(comment="Call Graph Diff", format='png')

    all_nodes = set()
    for a, b in old_edges.union(new_edges):
        all_nodes.add(a)
        all_nodes.add(b)

    for node in all_nodes:
        dot.node(node)

    for edge in old_edges - new_edges:
        dot.edge(edge[0], edge[1], color="red", label="removed")

    for edge in new_edges - old_edges:
        dot.edge(edge[0], edge[1], color="green", label="added")

    for edge in old_edges & new_edges:
        dot.edge(edge[0], edge[1], color="gray", style="dotted", label="unchanged")

    # Save both PNG and DOT
    dot.render(output_path_prefix, cleanup=False)  # Leaves the .dot file too
    dot.save(output_path_prefix + ".dot")

    print(f"✅ Diff PNG saved: {output_path_prefix}.png")
    print(f"✅ Diff DOT saved: {output_path_prefix}.dot")

def main(old_dot, new_dot, output_prefix):
    old_edges = extract_edges(old_dot)
    new_edges = extract_edges(new_dot)
    generate_diff_graph(old_edges, new_edges, output_prefix)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python diff_callgraph_plain.py <old.dot> <new.dot> <output_prefix>")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2], sys.argv[3])
