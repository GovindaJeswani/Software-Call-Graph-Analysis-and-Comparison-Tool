import subprocess
import os
import time
from get_files import get_relevant_files
from pycallgraph2 import PyCallGraph
from pycallgraph2.output import GraphvizOutput
import flask

def generate_call_graph(source_files, output_dot, output_png):
    """Generates a static call graph using code2flow."""
    if not source_files:
        print(f"❌ No Python files found for {output_dot}")
        return

    cmd = ["code2flow", "-o", output_png] + source_files  # Ensure PNG file is created
    
    with open(output_dot, "w") as dot_file:
        subprocess.run(cmd, stdout=dot_file, check=True)  # Run code2flow command
    
    print(f"✅ Static call graph saved as {output_dot}")
    print(f"✅ PNG saved as {output_png}")

def run_flask_for_4_seconds():
    """Run Flask server for 4 seconds using subprocess."""
    app = flask.Flask(__name__)

    @app.route("/")
    def home():
        return "Hello, Flask!"

    # Set FLASK_APP before running Flask
    os.environ["FLASK_APP"] = "dynamic_trace.py"  

    flask_process = subprocess.Popen(["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000", "--no-reload"])
    print("✅ Flask server running at http://127.0.0.1:5000")

    # Wait for 4 seconds before terminating the server
    time.sleep(4)

    flask_process.terminate()
    flask_process.wait()  # Wait for full termination

    print("✅ Flask server stopped.")

def generate_runtime_call_graph():
    """Generates a runtime call graph using PyCallGraph2 and saves .gv & .png."""
    
    # PNG file
    png_output = GraphvizOutput(output_file="runtime_callgraph.png")

    # DOT (Graphviz) file
    gv_output = GraphvizOutput(output_file="runtime_callgraph.gv")

    with PyCallGraph(output=png_output):
        with PyCallGraph(output=gv_output):
            run_flask_for_4_seconds()

    print("✅ Runtime call graph saved as runtime_callgraph.gv and runtime_callgraph.png")

# Run and generate static and dynamic graphs
if __name__ == "__main__":
    # Get all Python files
    _, old_src = get_relevant_files("../old_version/flask-2.2.0")
    _, new_src = get_relevant_files("../new_version/flask-3.0.0")

    # Step 1: Generate Static Call Graphs first
    generate_call_graph(old_src, "static_callgraph.dot", "static_callgraph.png")
    generate_call_graph(new_src, "new_callgraph.dot", "new_callgraph.png")

    # Step 2: Generate Runtime Call Graph
    generate_runtime_call_graph()
