# Quantum_gates
Welcome to the Quantum Gate Simulator repository, a comprehensive collection of Python scripts designed to empower quantum enthusiasts and programmers alike. Delve into the fascinating world of quantum computing concepts and simulations, where classical and quantum gates converge to enhance your understanding.
>Key Features:
1. Classical & Quantum Simulations: Seamlessly switch between classical and quantum simulations to grasp the foundations of quantum gates and harness the potential of quantum computing.
2. Interactive Learning: Our Jupyter notebooks and Python scripts offer an interactive learning experience. Explore a wide range of quantum gates, dissect quantum circuits, and gain practical insights into their applications.
3. Real-World Quantum Implementations: Connect with quantum hardware or utilize popular quantum simulators like IBM Qiskit to bring quantum computations to life.
4. Educational Resources: Benefit from educational materials provided alongside the code. Understand the theory and practical aspects of quantum gates with ease.

## Installation
For running the Python scripts and Jupyter notebook, one needs to install Qiskit.
Qiskit supports Python 3.7 or later.

You will need to [download Python](https://www.python.org/downloads/) on your local system to get started. [Jupyter](https://jupyter.org/install) is recommended for interacting with Qiskit to run the .ipynb files.

Now that you've installed the required tools, let's install Qiskit:
1. Create a minimal environment with only Python installed in it.
```
python3 -m venv /path/to/virtual/environment
```
2. Activate your new environment.
```
source /path/to/virtual/environment/bin/activate
```
3. Note: For Windows users, the following commands are to be used in powershell.
```
python3 -m venv c:\path\to\virtual\environment
c:\path\to\virtual\environment\Scripts\Activate.ps1
```
4. Next, install the Qiskit package.
```
pip install qiskit
```
5. If you intend to use visualization functionality or Jupyter notebooks it is recommended to install Qiskit with the extra visualization support:
```
pip install qiskit[visualization]
```
For a zsh user (the default shell on newer versions of macOS), you’ll need to put qiskit[visualization] in quotes:
```
pip install 'qiskit[visualization]'
```
## Usage
> To run .ipynb files :
One needs to run Jupyter Notebook. To do so , one must type ``` jupyter-notebook``` in the shell , and then locate to the required directory.

> To run python .py scripts :
One needs to use the command :
```
python3 <filename>
```

