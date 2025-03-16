import os
import subprocess

# Paths
CPG_DIR = "../CPG"
CALL_GRAPHS_DIR = "../CallGraphs"

def extract_call_graph():
    """Extracts function call graphs from the generated CPG files."""
    os.makedirs(CALL_GRAPHS_DIR, exist_ok=True)

    for cpg_file in os.listdir(CPG_DIR):
        if cpg_file.endswith(".cpg.bin"):
            project_name = cpg_file.replace(".cpg.bin", "")
            call_graph_output = os.path.join(CALL_GRAPHS_DIR, f"{project_name}.dot")

            if not os.path.exists(call_graph_output):
                print(f"🔍 Extracting Call Graph for {project_name}...")

                # Joern command to extract call graph
                joern_query = f'''
                importCpg("{os.path.join(CPG_DIR, cpg_file)}")
                cpg.callIn.method.fullName.p
                '''
                command = f'echo "{joern_query}" | joern --script'
                subprocess.run(command, shell=True, check=True, stdout=open(call_graph_output, "w"))

                print(f"✅ Call Graph saved as {call_graph_output}\n")
            else:
                print(f"⚠️ Call Graph for {project_name} already exists, skipping...\n")

if __name__ == "__main__":
    extract_call_graph()
