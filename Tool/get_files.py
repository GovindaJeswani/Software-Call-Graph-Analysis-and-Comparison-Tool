import os
import sys

def get_relevant_files(module_name):
    base_path = f"../Modules/{module_name}"
    versions = ["old", "new"]
    
    for version in versions:
        version_path = os.path.join(base_path, version)
        print(f"\n=== {version.capitalize()} Version ===")
        
        py_files = []
        for root, _, files in os.walk(version_path):
            for file in files:
                if file.endswith(".py"):
                    py_files.append(os.path.join(root, file))

        print(f"Total Python Files: {len(py_files)}")
        print("Python Files:", py_files)

def get_python_files(module_name, version):
    base_path = f"../Modules/{module_name}/{version}"
    py_files = []
    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(".py"):
                py_files.append(os.path.join(root, file))
    return py_files


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a module name as argument.")
        sys.exit(1)

    module = sys.argv[1]
    get_relevant_files(module)
