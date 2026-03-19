pytest:
    pytest

flask:
    cd flaskr && \
    flask --app main.py run --debug

format:
  cd "{{justfile_directory()}}" && \
    ruff format . && \
    ruff check . --fix --select I --select F401

# Lint
lint:
  cd "{{justfile_directory()}}" && \
    ruff format --check . && \
    ruff check . && \
    mypy .

test: format lint pytest