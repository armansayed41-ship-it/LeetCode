import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(bonus, on="empId", how="left")

    result = df[
        (df["bonus"] < 1000) |
        (df["bonus"].isna())
    ]

    return result[["name", "bonus"]]