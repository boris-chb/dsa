watch FILE:
    echo {{ FILE }} | entr -cc uv run python /_

test:
    uv run pytest
