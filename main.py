
import src.extraction as extract
import src.cleaning as clean
import src.visualization as viz
import os
import pandas as pd


df = extract.open_df("chat_ju")

df_clean = clean.setting_columns(df)
df_clean = clean.emoji_extraction(df_clean)
df_clean = clean.emoji_unique(df_clean)
df_clean = clean.emoji_clean(df_clean)
df_clean = clean.date_extraction(df_clean)
df_clean = clean.date_limit(df_clean)

df_api = clean.API_open_meteo(df_clean)

df_final = clean.merged_df(df_clean, df_api)


df_final.to_csv("data/clean.csv")
os.system("open data/clean.csv")



viz.graph_top15 (df_final)
viz.graph_rain (df_final) 
viz.graph_top_emojis_year (df_final) 
viz.graph_top_emojis_temp (df_final) 
viz.graph_num_emojis_temp (df_final)

