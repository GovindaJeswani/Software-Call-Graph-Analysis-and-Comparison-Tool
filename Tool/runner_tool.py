# runner_tool.py
import os
import subprocess
import zipfile

MODULES = "../Zips"
MODULES_DIR = "../Modules"
RESULTS_DIR = "../Results"
TOOL_DIR = os.getcwd()

def extract_zip_files(module_name):
    old_zip = f"{MODULES}/{module_name}_old.zip"
    new_zip = f"{MODULES}/{module_name}_new.zip"
    out_old = f"{MODULES_DIR}/{module_name}/old"
    out_new = f"{MODULES_DIR}/{module_name}/new"

    os.makedirs(out_old, exist_ok=True)
    os.makedirs(out_new, exist_ok=True)

    with zipfile.ZipFile(old_zip, 'r') as zip_ref:
        zip_ref.extractall(out_old)
    with zipfile.ZipFile(new_zip, 'r') as zip_ref:
        zip_ref.extractall(out_new)

    print(f"✅ Extracted {module_name} versions")

def run_script(script, module_name):
    print(f"🚀 Running {script} for {module_name}...")
    subprocess.run(["python", script, module_name], check=True)

def run_pipeline():
    for file in os.listdir(MODULES):
        if file.endswith("_old.zip"):
            module = file.replace("_old.zip", "")
            print(f"\n🔹 Processing {module}...")

            extract_zip_files(module)

            run_script("get_files.py", module)
            run_script("call_graph.py", module)
            run_script("dot_to_json.py", module)
            run_script("compare_graph.py", module)
            run_script("generate_report.py", module)

if __name__ == "__main__":
    run_pipeline()
