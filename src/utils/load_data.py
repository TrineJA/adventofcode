import pandas as pd
from typing import List


def read_csv(input_file_path:str, col_names: List, sep=',', dtype=None, skip_blank_lines=True, engine='c')->pd.DataFrame:
    df = pd.read_csv(input_file_path, names=col_names, sep=sep, dtype=dtype, skip_blank_lines=skip_blank_lines, engine=engine)
    return df