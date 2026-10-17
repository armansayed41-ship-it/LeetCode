import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    single_numbers = my_numbers.drop_duplicates(
        subset="num", keep=False
    )

    largest = single_numbers["num"].max()

    return pd.DataFrame({"num": [largest]})