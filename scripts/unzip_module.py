# scripts/unzip_module.py
import os
import zipfile
import sys

def extract_zip(zip_path, extract_to):
    os.makedirs(extract_to, exist_ok=True)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"✅ Extracted {zip_path} → {extract_to}")

def unzip_module(module_name):
    base_dir = os.getcwd()
    zips_dir = os.path.join(base_dir, "Zips")
    modules_dir = os.path.join(base_dir, "Modules", module_name)

    for version in ["old", "new"]:
        zip_filename = f"{module_name}_{version}.zip"
        zip_path = os.path.join(zips_dir, zip_filename)
        extract_to = os.path.join(modules_dir, version)

        if not os.path.exists(zip_path):
            print(f"❌ Zip file not found: {zip_path}")
            continue

        extract_zip(zip_path, extract_to)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scripts/unzip_module.py <module_name>")
        sys.exit(1)

    unzip_module(sys.argv[1])
