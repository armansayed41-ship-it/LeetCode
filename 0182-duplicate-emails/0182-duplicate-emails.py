import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:

    email_count = person["email"].value_counts()

    duplicate = email_count[email_count > 1]

    result = pd.DataFrame({
        "Email": duplicate.index
    })

    return result