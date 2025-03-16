import subprocess
import os
from pycallgraph2 import PyCallGraph
from pycallgraph2.output import GraphvizOutput
import flask  # Ensure Flask is imported after installation

def install_dependencies():
    """Automatically installs dependencies from requirements.txt"""
    requirements_path = "../new_version/flask-3.0.0/requirements.txt"

    if os.path.exists(requirements_path):
        print("📌 Installing dependencies from requirements.txt...")
        subprocess.run(["pip", "install", "-r", requirements_path], check=True)
        print("✅ Dependencies installed successfully!")
    else:
        print("⚠️ No requirements.txt found! Dependencies may be missing.")

def run_flask():
    """Run Flask server with dynamic function call tracing"""
    app = flask.Flask(__name__)

    @app.route("/")
    def home():
        return "Hello, Flask!"

    app.run(debug=False)  # Running Flask server

if __name__ == "__main__":
    install_dependencies()  # Step 1: Install dependencies

    # Generate PNG and GV files
    png_output = GraphvizOutput(output_file="runtime_callgraph.png")
    gv_output = GraphvizOutput(output_file="runtime_callgraph.gv")

    with PyCallGraph(output=png_output):
        with PyCallGraph(output=gv_output):
            run_flask()

    print("✅ Dynamic call graph saved as runtime_callgraph.png and runtime_callgraph.gv")
