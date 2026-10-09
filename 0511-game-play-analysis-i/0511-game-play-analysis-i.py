import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    result = activity.groupby("player_id").agg(
        first_login=("event_date", "min")
    ).reset_index()

    return result