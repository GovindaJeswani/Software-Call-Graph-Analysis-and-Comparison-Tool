import os
import subprocess

# Paths
PROJECTS_DIR = "../Projects"
CPG_DIR = "../CPG"

def generate_cpg():
    """Runs Joern on each extracted project to generate a CPG."""
    os.makedirs(CPG_DIR, exist_ok=True)

    for project in os.listdir(PROJECTS_DIR):
        project_path = os.path.join(PROJECTS_DIR, project)
        cpg_output = os.path.join(CPG_DIR, f"{project}.cpg.bin")

        if not os.path.exists(cpg_output):
            print(f"🔍 Generating CPG for {project}...")

            # Run Joern on the project
            joern_cmd = f"joern --import {project_path} --output {cpg_output}"
            subprocess.run(joern_cmd, shell=True, check=True)

            print(f"✅ CPG saved as {cpg_output}\n")
        else:
            print(f"⚠️ CPG for {project} already exists, skipping...\n")

if __name__ == "__main__":
    generate_cpg()
