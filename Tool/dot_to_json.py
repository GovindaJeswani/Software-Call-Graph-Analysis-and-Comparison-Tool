import json

def load_json(file):
    """Loads a JSON file."""
    with open(file, 'r') as f:
        return json.load(f)

def generate_diff(old_data, new_data):
    """Generates a diff of function calls between two JSON data."""
    old_calls = {f"{call['caller']} -> {call['callee']}" for call in old_data['function_calls']}
    new_calls = {f"{call['caller']} -> {call['callee']}" for call in new_data['function_calls']}

    diff = {
        'added_calls': list(new_calls - old_calls),
        'removed_calls': list(old_calls - new_calls)
    }

    return diff

def save_diff_to_json(diff, output_json):
    """Saves the diff to a JSON file."""
    with open(output_json, 'w') as f:
        json.dump(diff, f, indent=4)
    print(f"✅ Diff saved as {output_json}")

if __name__ == "__main__":
    # Load the old and new JSON files
    old_json = "old_callgraph.json"
    new_json = "new_callgraph.json"

    old_data = load_json(old_json)
    new_data = load_json(new_json)

    # Generate the diff
    diff = generate_diff(old_data, new_data)

    # Save the diff to a new file
    save_diff_to_json(diff, "call_graphdiff.json")
