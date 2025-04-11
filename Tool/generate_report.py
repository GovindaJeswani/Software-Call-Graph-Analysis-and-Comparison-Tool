# generate_report.py
import json
import sys

if __name__ == "__main__":
    module = sys.argv[1]
    path = f"../Results/{module}/comparison.json"

    with open(path, "r") as f:
        data = json.load(f)

    print(f"\n📊 === REPORT for {module} ===")
    print(f"\n➕ Added Functions: {len(data['added'])}")
    for f in data["added"]:
        print(f"   + {f}")

    print(f"\n➖ Removed Functions: {len(data['removed'])}")
    for f in data["removed"]:
        print(f"   - {f}")
