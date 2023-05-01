import pandas as pd


def open_df (name):

    df = pd.read_csv(f"data/{name}.txt", delimiter='\t', encoding='utf-8')
    df = df.to_csv(f"data/{name}.csv", index=False)
    df = pd.read_csv(f"data/{name}.csv")

    return df