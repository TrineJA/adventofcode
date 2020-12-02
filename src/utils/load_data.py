import pandas as pd
from typing import List


def read_csv(input_file_path:str, col_names: List, sep=',')->pd.DataFrame:
    df = pd.read_csv(input_file_path, names=col_names, sep=sep)
    return df