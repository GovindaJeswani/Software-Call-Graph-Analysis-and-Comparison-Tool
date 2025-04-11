# dot_to_json.py
import sys
import re
import json

def dot_to_edges(dot_path):
    edges = []
    with open(dot_path, "r", encoding="utf-8") as f:
        for line in f:
            match = re.search(r'"(.+?)" -> "(.+?)"', line)
            if match:
                caller, callee = match.groups()
                edges.append({"caller": caller, "callee": callee})
    return edges

if __name__ == "__main__":
    module = sys.argv[1]
    old_dot = f"../Results/{module}/old_callgraph.dot"
    new_dot = f"../Results/{module}/new_callgraph.dot"

    old_json = f"../Results/{module}/old_callgraph.json"
    new_json = f"../Results/{module}/new_callgraph.json"

    with open(old_json, "w") as f:
        json.dump(dot_to_edges(old_dot), f, indent=2)
    with open(new_json, "w") as f:
        json.dump(dot_to_edges(new_dot), f, indent=2)

    print(f"✅ Converted to JSON for {module}")
