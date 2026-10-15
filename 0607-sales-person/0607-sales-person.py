import pandas as pd

def sales_person(
    sales_person: pd.DataFrame,
    company: pd.DataFrame,
    orders: pd.DataFrame
) -> pd.DataFrame:

    red_company_ids = company.loc[
        company["name"] == "RED", "com_id"
    ]

    red_sales_ids = orders.loc[
        orders["com_id"].isin(red_company_ids), "sales_id"
    ]

    result = sales_person[
        ~sales_person["sales_id"].isin(red_sales_ids)
    ]

    return result[["name"]]