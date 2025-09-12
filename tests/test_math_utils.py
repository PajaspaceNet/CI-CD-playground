from src.math_utils import add, subtract

- name: Run pytest
  run: PYTHONPATH=. pytest -v


def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 4) == 6
