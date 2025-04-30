import os
import zipfile

# Define folders
ZIP_DIR = "../Zips"
EXTRACT_DIR = "../Modules"

def extract_zip_files():
    """Extracts ZIP files from Zips/ into Modules/."""
    os.makedirs(EXTRACT_DIR, exist_ok=True)

    for zip_file in os.listdir(ZIP_DIR):
        if zip_file.endswith(".zip"):
            zip_path = os.path.join(ZIP_DIR, zip_file)
            extract_folder = os.path.join(EXTRACT_DIR, zip_file.replace(".zip", ""))

            print(f"📦 Extracting {zip_file} to {extract_folder}...")

            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_folder)

            print(f"✅ Extraction complete: {extract_folder}")

if __name__ == "__main__":
    extract_zip_files()
