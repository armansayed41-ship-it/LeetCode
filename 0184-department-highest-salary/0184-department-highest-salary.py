import pandas as pd

def department_highest_salary(
    employee: pd.DataFrame,
    department: pd.DataFrame
) -> pd.DataFrame:

    df = employee.merge(
        department,
        left_on="departmentId",
        right_on="id",
        suffixes=("_employee", "_department")
    )

    max_salary = df.groupby(
        "name_department"
    )["salary"].transform("max")

    result = df[df["salary"] == max_salary]

    return result[
        ["name_department", "name_employee", "salary"]
    ].rename(columns={
        "name_department": "Department",
        "name_employee": "Employee",
        "salary": "Salary"
    })