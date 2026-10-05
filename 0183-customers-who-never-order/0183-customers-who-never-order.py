import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    ordered_ids = orders["customerId"].unique()

    result = customers[
        ~customers["id"].isin(ordered_ids)
    ]

    return result[["name"]].rename(
        columns={"name": "Customers"}
    )