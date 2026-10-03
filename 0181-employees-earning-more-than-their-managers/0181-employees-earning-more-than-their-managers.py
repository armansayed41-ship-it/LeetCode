import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:

    manager = employee[["id", "salary"]].copy()

    manager = manager.rename(columns={
        "id": "managerId",
        "salary": "managerSalary"
    })

    df = employee.merge(
        manager,
        on="managerId",
        how="inner"
    )

    result = df[df["salary"] > df["managerSalary"]]

    return result[["name"]].rename(columns={
        "name": "Employee"
    })