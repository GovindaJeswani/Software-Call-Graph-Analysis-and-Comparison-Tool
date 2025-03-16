import os

def get_relevant_files(project_folder):
    """Finds all Python source files inside the 'src/' directory."""
    dependency_files = []
    source_files = []

    for root, _, files in os.walk(project_folder):  
        # Skip unwanted folders like docs, tests, examples
        if "docs" in root or "tests" in root or "examples" in root:
            continue  

        for file in files:
            file_path = os.path.join(root, file)
            
            # Identify dependency files
            if file in ["requirements.txt", "setup.py", "pyproject.toml"]:
                dependency_files.append(file_path)
            
            # Identify Python files (only from src/)
            elif file.endswith(".py") and "src" in root:
                source_files.append(file_path)

    return dependency_files, source_files

if __name__ == "__main__":
    old_deps, old_src = get_relevant_files("../old_version")
    new_deps, new_src = get_relevant_files("../new_version")

    print("\n=== Old Version ===")
    print("Dependencies:", old_deps)
    print("Total Python Files:", len(old_src))
    print("Python Files:", old_src[:10])  

    print("\n=== New Version ===")
    print("Dependencies:", new_deps)
    print("Total Python Files:", len(new_src))
    print("Python Files:", new_src[:10])  
