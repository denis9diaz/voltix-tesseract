
# Create and activate a virtual environment
	python -m venv .venv
	
	
``python``: use the program called python
``-m``: call a module as a script, we'll tell it which module next
``venv``: use the module called venv that normally comes installed with Python
``.venv``: create the virtual environment in the new directory .venv

	source .venv/bin/activate
	
* Do this every time you start a new terminal session to work on the project
* Every time you install the package in that environment, activate the environment again.
	
# Check The Virtual Environment is Active:
	which python
	
# upgrade pip
	python -m pip install --upgrade pip
	
	
# Create a .gitignore
	echo "*" > .venv/.gitignore



# Run the server
	fastapi dev main.py
# Interactive API docs
	/docs
# Alternative APi docs
	/redoc
