import os
import zipfile

# Paths
ZIP_DIR = "../ZIPs"
EXTRACT_DIR = "../Projects"

def extract_zip_files():
    """Extracts all ZIP files in ZIPs/ to Projects/."""
    os.makedirs(EXTRACT_DIR, exist_ok=True)

    for zip_file in os.listdir(ZIP_DIR):
        if zip_file.endswith(".zip"):
            project_name = zip_file.replace(".zip", "")  # Extract project name
            project_path = os.path.join(EXTRACT_DIR, project_name)

            if not os.path.exists(project_path):
                print(f"📦 Extracting {zip_file} to {project_path}...")
                with zipfile.ZipFile(os.path.join(ZIP_DIR, zip_file), 'r') as zip_ref:
                    zip_ref.extractall(project_path)
                print(f"✅ Extracted {zip_file} successfully!\n")
            else:
                print(f"⚠️ {project_name} already extracted, skipping...\n")

if __name__ == "__main__":
    extract_zip_files()
