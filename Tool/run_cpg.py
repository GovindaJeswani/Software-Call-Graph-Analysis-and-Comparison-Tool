import os
import subprocess

# Set the full path to Joern's batch file.
JOERN_PATH = "D:/joern-cli/joern-cli/joern.bat"

# Absolute paths for Modules and Results directories.
MODULES_DIR = os.path.abspath("../Modules")
RESULTS_DIR = os.path.abspath("../Results")

def run_cpg_analysis(module_name):
    """Runs Joern to generate a Code Property Graph (CPG) for the given module."""
    module_path = os.path.join(MODULES_DIR, module_name)
    result_path = os.path.join(RESULTS_DIR, module_name)
    os.makedirs(result_path, exist_ok=True)

    print(f"Running CPG analysis for {module_name}...")
    
    # Create a minimal Joern script that explicitly uses the Python frontend.
    # Make sure the paths use forward slashes.
    joern_script_content = (
        f'importCode.python("{module_path}");\n'
        f'cpg.save("{result_path}/cpg.bin");'
    )
    
    # Write the script to a file, stripping extra whitespace.
    script_path = os.path.abspath("joern_analysis.sc")
    with open(script_path, "w", encoding="utf-8") as script_file:
        script_file.write(joern_script_content.strip())

    # Debug: print the content of the generated Joern script.
    print("Joern script content:")
    print(joern_script_content)

    # Run Joern with the script.
    try:
        subprocess.run([JOERN_PATH, "--script", script_path], check=True)
        print(f"CPG analysis completed: {result_path}/cpg.bin")
    except subprocess.CalledProcessError as e:
        print(f"Joern failed with error: {e}")

if __name__ == "__main__":
    for module in os.listdir(MODULES_DIR):
        if os.path.isdir(os.path.join(MODULES_DIR, module)):
            run_cpg_analysis(module)
