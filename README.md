
1. Create and activate a virtual environment and then install FastAPI
	python -m venv .venv
	
	
    python: use the program called python
    -m: call a module as a script, we'll tell it which module next
    venv: use the module called venv that normally comes installed with Python
    .venv: create the virtual environment in the new directory .venv

	source .venv/bin/activate
	* Do this every time you start a new terminal session to work on the project
	* Every time you install the package in that environment, activate the environment again.
	
	Check The Virtual Environment is Active:
	which python
	
	
	python -m pip install --upgrade pip
	
	
Create a .gitignore
echo "*" > .venv/.gitignore




2. pip install "fastapi[standard]"
3. Create a main.py
