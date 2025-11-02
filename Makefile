install:
	uv sync
brain-games:
	uv run VD_games/scripts/VD_even.py

build:
	uv build

package-install:
	uv tool install dist/*.whl
lint:
	uv run ruff check VD_games
