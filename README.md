# Software-Call-Graph-Analysis-and-Comparison-Tool

This project is a modular Python tool to **compare two versions of any Python-based software project** using static code analysis. It generates **function call graphs**, highlights **differences** visually, and produces a **markdown report** of code changes — helping you understand architectural modifications clearly.

---

## 📁 Folder Structure

RP_project/ ├── Zips/ # Input zipped versions: <module>_old.zip and <module>_new.zip 
			├── Modules/ # Extracted contents of each version 
			│ 		└── <module>/ 
			│				├── old/ 
			│ 				└── new/ 
			├── Results/ # Output: call graphs, diff graphs, markdown report 
			│ 		└── <module>/ 
			│ 		├── old_callgraph.dot/png 
			│ 		├── new_callgraph.dot/png 
			│		├── diff_graph.dot/png 
			│ 		└── report.md 
			├── scripts/ # Core analysis and automation scripts 
			│ 		├── generate_callgraph.py 
			│ 		├── compare_callgraphs.py 
			│ 		├── diff_callgraph_plain.py 
			│ 		└── run_pipeline.py 
			├── requirements.txt # Python dependencies 
			└── README.md

---

## 🚀 How to Run

### 1️⃣ Install Requirements

```bash
pip install -r requirements.txt

Also, make sure Graphviz is installed and available in your system path:
dot -V
# Example: dot - graphviz version 2.49.0 (20221004.0001)


2️⃣ Add Input ZIP Files
Put your zipped module versions inside the Zips/ folder using this naming format:

Zips/
├── <module_name>_old.zip
└── <module_name>_new.zip

``Example:

	Zips/
├── flask_old.zip
└── flask_new.zip
``

3️⃣ Run the Pipeline
python scripts/run_pipeline.py flask

Replace flask with your actual module name (the prefix of your ZIPs). The tool will:

Extract zip files

Generate call graphs

Compare and highlight differences

Generate a markdown report

📦 Output (Results/<module>)

File					Description
old_callgraph.dot/png	Function call graph of the old version
new_callgraph.dot/png	Function call graph of the new version
diff_graph.dot/png		Color-coded graph showing changes
report.md				Markdown summary of added/removed calls


⚒️  What It Does
📌 Extracts function definitions and calls using ast

📌 Builds static call graphs using networkx and graphviz

📌 Highlights changes in call flow using
	📌 Highlights changes with:
		🟢 Green: unchanged	
		🔴 Red: removed
		🔵 Blue: added 

📌 Generates an easy-to-read report.md


🔧 Dependencies

networkx
pydot
graphviz
matplotlib
pygraphviz

install them using:
pip install -r requirements.txt



👨‍💻 Author
Govinda Jeswani
🧑‍💻 Developer | 
📍 India

->> “Code is change. Know the difference.”