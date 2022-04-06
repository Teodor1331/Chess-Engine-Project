"""Module with helper methods for the logic of the project."""


def build_ranks_to_rows_notation() -> dict:
    """Return a dictionary with ranks to rows notation."""
    return {str(i): abs(i - 8) for i in range(1, 9)}


def build_files_to_columns_notation() -> dict:
    """Return a dictionary with ranks to rows notation."""
    return {str('abcdefgh')[i]: i for i in range(8)}
