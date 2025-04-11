# compare_graph.py
import json
import sys

def load(path):
    with open(path, "r") as f:
        return set((x["caller"], x["callee"]) for x in json.load(f))

if __name__ == "__main__":
    module = sys.argv[1]
    old_path = f"../Results/{module}/old_callgraph.json"
    new_path = f"../Results/{module}/new_callgraph.json"
    out_path = f"../Results/{module}/comparison.json"

    old = load(old_path)
    new = load(new_path)

    comparison = {
        "removed": list(old - new),
        "added": list(new - old)
    }

    with open(out_path, "w") as f:
        json.dump(comparison, f, indent=2)

    print(f"✅ Compared call graphs and saved to {out_path}")
