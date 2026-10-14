import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    result = courses.groupby("class")["student"].count()
    result = result[result >= 5]

    return result.reset_index()[["class"]]