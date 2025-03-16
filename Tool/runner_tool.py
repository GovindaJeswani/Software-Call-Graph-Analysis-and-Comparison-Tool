import subprocess
import os
import shutil
import zipfile

BASE_DIR = os.path.abspath("..")  # Adjust if needed
ZIP_DIR = os.path.join(BASE_DIR, "Zips")
MODULES_DIR = os.path.join(BASE_DIR, "Modules")
RESULTS_DIR = os.path.join(BASE_DIR, "Results")
TOOL_DIR = os.path.join(BASE_DIR, "Tool")


def detect_module():
    """Detects module names dynamically from the Zips folder."""
    zip_files = os.listdir(ZIP_DIR)
    modules = set()

    for file in zip_files:
        if file.endswith(".zip"):
            module_name = file.split("_")[0]  # Extract module name before "_old" or "_new"
            modules.add(module_name)

    return list(modules)  # Return unique module names


def extract_zip_files(module_name):
    """Extracts the module's old and new versions."""
    print(f"📌 Extracting {module_name}...")

    module_path = os.path.join(MODULES_DIR, module_name)
    os.makedirs(module_path, exist_ok=True)

    for version in ["old", "new"]:
        zip_path = os.path.join(ZIP_DIR, f"{module_name}_{version}.zip")
        extract_path = os.path.join(module_path, version)

        if os.path.exists(zip_path):
            shutil.rmtree(extract_path, ignore_errors=True)  # Ensure fresh extraction
            os.makedirs(extract_path, exist_ok=True)

            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_path)
            
            print(f"✅ Extracted {zip_path} to {extract_path}")
        else:
            print(f"⚠️ Warning: {zip_path} not found!")


def run_script(script_name, module_name):
    """Runs a script while ensuring output goes into the correct module folder."""
    print(f"🚀 Running {script_name} for {module_name}...")
    
    env = os.environ.copy()
    env["MODULE_NAME"] = module_name  # Pass module name to scripts

    subprocess.run(["python", os.path.join(TOOL_DIR, script_name)], check=True, env=env)


def clean_up():
    """Cleans up intermediate files if necessary."""
    print("🧹 Cleaning up temporary files... (Not implemented yet)")


if __name__ == "__main__":
    # 1️⃣ Detect modules
    detected_modules = detect_module()

    if not detected_modules:
        print("❌ No modules detected in Zips folder. Please add zip files and retry.")
        exit(1)

    for module in detected_modules:
        print(f"\n🔹 Processing {module}...")

        # 2️⃣ Extract files
        extract_zip_files(module)

        # 3️⃣ Run Processing Scripts
        run_script("get_files.py", module)
        run_script("call_graph.py", module)
        run_script("dot_to_json.py", module)
        run_script("compare_graph.py", module)
        run_script("generate_report.py", module)

    # 4️⃣ Clean up (if required)
    clean_up()

    print("\n✅ All modules processed successfully! Check Results folder.")
