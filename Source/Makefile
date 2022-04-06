make: pylint pylama pycodestyle pydocstyle pyflakes pytest

pylint:
	@echo "Running PyLint:"
	pylint game_helpers.py
	pylint game_graphics.py
	pylint game_main.py

	pylint test_game_helpers.py
	pylint test_game_graphics.py
	pylint test_game_engine.py
	@echo "\n"


pylama:
	@echo "Running PyLama:"
	pylama game_helpers.py
	pylama game_graphics.py
	pylama game_main.py

	pylama test_game_helpers.py 
	pylama test_game_graphics.py
	pylama test_game_engine.py
	@echo "\n"


pycodestyle:
	@echo "Running PyCodeStyle:"
	pycodestyle game_helpers.py
	pycodestyle game_graphics.py
	pycodestyle game_main.py

	pycodestyle test_game_helpers.py
	pycodestyle test_game_graphics.py
	pycodestyle test_game_engine.py
	@echo "\n"


pydocstyle:
	@echo "Running PyDocStyle:"
	pydocstyle game_helpers.py
	pydocstyle game_graphics.py
	pydocstyle game_main.py

	pycodestyle test_game_helpers.py
	pycodestyle test_game_graphics.py
	pycodestyle test_game_engine.py
	@echo "\n"


pyflakes:
	@echo "Running PyFlakes:"
	pyflakes game_helpers.py
	pyflakes game_graphics.py
	pyflakes game_main.py

	pyflakes test_game_helpers.py
	pyflakes test_game_graphics.py
	pyflakes test_game_engine.py
	@echo "\n"

pytest:
	@echo "Running PyTest:"
	pytest

clean:
	@rm -r -f __pycache__
	@rm -r -f .pytest_cache