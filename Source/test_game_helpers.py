"""Tests on the module with helper method for the logic of the project."""

from inspect import isfunction

import pytest

from game_helpers import build_ranks_to_rows_notation
from game_helpers import build_files_to_columns_notation


@pytest.fixture(name='ranks_to_rows_notation')
def fixture_ranks_to_rows_dictionary():
    """Return fixture with dictionary about ranks to rows notation."""
    return {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}


@pytest.fixture(name='files_to_columns_notation')
def fixture_files_to_columns_notation():
    """Return fixture with dictionary about files to columns notation."""
    return {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}


def test_build_ranks_to_rows_notation_method(ranks_to_rows_notation):
    """Tests ranks to rows notation builder method."""
    assert isfunction(build_ranks_to_rows_notation)
    result = build_ranks_to_rows_notation()

    assert isinstance(result, dict)
    assert len(result.keys()) == 8
    assert len(result.values()) == 8

    assert 'result' in locals()
    assert locals()['result'] == result
    assert result == ranks_to_rows_notation


def test_build_files_to_columns_notation(files_to_columns_notation):
    """Tests files to columns notation builder method."""
    assert isfunction(build_files_to_columns_notation)
    result = build_files_to_columns_notation()

    assert isinstance(result, dict)
    assert len(result.keys()) == 8
    assert len(result.values()) == 8

    assert 'result' in locals()
    assert locals()['result'] == result
    assert result == files_to_columns_notation
