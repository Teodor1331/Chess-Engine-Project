def build_ranks_to_rows_notation() -> dict:
    return {str(i) : abs(i - 8) for i in range(1, 9)} 


def build_files_to_columns_notation() -> dict:
    return {str('abcdefgh')[i] : i for i in range(8)}
