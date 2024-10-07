default: fmt fix

# Startup Commands
run:
	python -m bot.main

# Code Styling Commands
fmt:
	ruff format

lint:
	ruff check

fix:
	ruff check --fix
