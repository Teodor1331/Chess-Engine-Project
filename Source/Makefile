make:
	@echo "Running PyLint:"
	pylint game_helpers.py
	pylint game_graphics.py
	pylint game_main.py

	pylint test_game_helpers.py
	pylint test_game_graphics.py
	pylint test_game_engine.py
	@echo "\n"

	@echo "Running PyLama:"
	pylama game_helpers.py
	pylama game_graphics.py
	pylama game_main.py

	pylama test_game_helpers.py 
	pylama test_game_graphics.py
	pylama test_game_engine.py
	@echo "\n"

	@echo "Running PyCodeStyle:"
	pycodestyle game_helpers.py
	pycodestyle game_graphics.py
	pycodestyle game_main.py

	pycodestyle test_game_helpers.py
	pycodestyle test_game_graphics.py
	pycodestyle test_game_engine.py
	@echo "\n"

	@echo "Running PyDocStyle:"
	pydocstyle game_helpers.py
	pydocstyle game_graphics.py
	pydocstyle game_main.py

	pycodestyle test_game_helpers.py
	pycodestyle test_game_graphics.py
	pycodestyle test_game_engine.py
	@echo "\n"

	@echo "Running PyTest:"
	pytest

clean:
	@rm -r __pycache__
	@rm -r .pytest_cache