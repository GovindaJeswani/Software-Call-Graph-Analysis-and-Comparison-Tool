import json
import re

def extract_function_names(dot_file):
    """Extracts function names from a DOT file, mapping node IDs to real names."""
    function_map = {}  # Maps node ID -> function name

    with open(dot_file, "r", encoding="utf-8", errors="ignore") as file:
        for line in file:
            match = re.search(r'(\w+)\s+\[label="([^"]+)"', line)
            if match:
                node_id, function_name = match.groups()
                function_map[node_id] = function_name  # Store real function name

    return function_map

def parse_dot_file(dot_file, function_map):
    """Extracts function calls from a DOT file with real function names."""
    function_calls = []

    with open(dot_file, "r", encoding="utf-8", errors="ignore") as file:
        for line in file:
            match = re.search(r'(\w+)\s+->\s+(\w+)', line)
            if match:
                caller, callee = match.groups()
                function_calls.append({
                    "caller": function_map.get(caller, caller),  # Get real name
                    "callee": function_map.get(callee, callee)   # Get real name
                })

    return function_calls

def compare_graphs(static_graph, dynamic_graph, output_json):
    """Compares static and dynamic call graphs."""
    static_function_map = extract_function_names(static_graph)
    dynamic_function_map = extract_function_names(dynamic_graph)

    static_calls = parse_dot_file(static_graph, static_function_map)
    dynamic_calls = parse_dot_file(dynamic_graph, dynamic_function_map)

    static_set = {(c["caller"], c["callee"]) for c in static_calls}
    dynamic_set = {(c["caller"], c["callee"]) for c in dynamic_calls}

    only_in_static = static_set - dynamic_set
    only_in_dynamic = dynamic_set - static_set

    result = {
        "unused_static_functions": [{"caller": c[0], "callee": c[1]} for c in only_in_static],
        "new_dynamic_functions": [{"caller": c[0], "callee": c[1]} for c in only_in_dynamic]
    }

    with open(output_json, "w") as file:
        json.dump(result, file, indent=4)

    print(f"✅ Comparison saved in {output_json}")

if __name__ == "__main__":
    static_graph = "static_callgraph.gv"
    dynamic_graph = "runtime_callgraph.gv"
    output_json = "comparison_static_vs_dynamic.json"
    
    compare_graphs(static_graph, dynamic_graph, output_json)








