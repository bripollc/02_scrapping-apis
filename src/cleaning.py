import pandas as pd
import numpy as np
import os
import re
import emoji


import requests




#1
def setting_columns (df):

    df.columns = ["col"]

    #df.iloc[23]["col"].split(",")[0].replace("[","") 
    df["Date"] = df["col"].str.split(",").str[0].str.replace("[", "")

    #df.iloc[23]["col"].split(",")[1].split("]")[0].strip()
    df["Time"] = df["col"].str.split(",").str[1].str.split("]").str[0].str.strip()

    #df.iloc[22]["col"].split(":")[2].split("]")[1].strip()
    df["Name"] = df["col"].str.split(":").str[2].str.split("]").str[1].str.strip()
    df['Name'] = df['Name'].str.replace('🐥', 'Bego')

    # df.iloc[0]["col"].split(":")[3].strip()
    df["Message"] = df["col"].str.split(":").str[3].str.strip()

    df.drop(columns=["col"], axis=1, inplace=True)
    df.dropna(subset=['Message'], inplace=True) 

    return df


#2
def emoji_extraction (df):

    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U0001F900-\U0001F9FF"  # supplemental symbols and pictographs
        u"\U0001F1F2-\U0001F1F4"  # country flags
        u"\U0001F1E6-\U0001F1FF"  # regional indicator symbols
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U00002702-\U000027B0"  # dingbats
        u"\U000024C2-\U0001F251" 
        "]+", flags=re.UNICODE)
    

    df['Emojis'] = df['Message'].str.findall(emoji_pattern)
    df = df[df['Emojis'].apply(lambda x: len(x) > 0)]
    df.drop(columns=["Message"], axis=1, inplace=True)
    #df = df.reset_index(drop=True)

    return df


#3
def emoji_unique (df):

    # converts the row from a list of strings into a set of unique strings
    df["Emojis"] = [''.join(set(row)) for row in df["Emojis"]]

    # Split each string in the column into a list of characters
    df['Emojis'] = df['Emojis'].apply(list)

    # Explode the list of characters into separate rows
    df = df.explode('Emojis')

    # Reset the index
    df.reset_index(drop=True)

    # Convert each character back to a string
    df['Emojis'] = df['Emojis'].apply(str)

    return df

#4
def emoji_clean (df):

    df['Emojis'] = df['Emojis'].replace('️', np.nan)
    df['Emojis'] = df['Emojis'].replace('nan', np.nan)
    df['Emojis'] = df['Emojis'].replace('♀', np.nan)
    df['Emojis'] = df['Emojis'].replace('♂', np.nan)
    df['Emojis'] = df['Emojis'].replace('🏽', np.nan)
    df['Emojis'] = df['Emojis'].replace('🏼', np.nan)
    df['Emojis'] = df['Emojis'].replace('🇦', np.nan)
    df['Emojis'] = df['Emojis'].replace('🇩', np.nan)

    df = df.dropna(subset=['Emojis'])

    return df


#5
def date_extraction (df):

    # Convert Date into a datetime format
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # Create new columns 
    df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S', errors='coerce')
    df['Time'] = df['Time'].dt.time

    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day
    df['Year'] = df['Date'].dt.year
    df['Hour'] = df['Time'].apply(lambda x: x.hour)

    sort_cols = ['Date', 'Day', 'Month', 'Year', 'Hour', 'Name', 'Emojis']
    df = df.reindex(columns=sort_cols)

    return df



#6
def date_limit (df):

    fecha_limite = pd.to_datetime("2023-04-23")
    df = df.loc[df['Date'] < fecha_limite]
    df = df.reset_index(drop=True)


    return df


#7
def API_open_meteo (df):

    init_date = str(df["Date"].min().date())
    #end_date = str(df.iloc[df.shape[0]]["Date"])
    end_date = str(df["Date"].max().date())


   # print(end_date)


    url_weather = f"https://archive-api.open-meteo.com/v1/archive?latitude=41.39&longitude=2.16&start_date={init_date}&end_date={end_date}&daily=temperature_2m_mean,rain_sum&timezone=auto"
    res = requests.get(url_weather).json()


    df_weather = pd.DataFrame(res['daily'])


    df_weather.dropna(subset=['temperature_2m_mean'], inplace=True) 
    df_weather = df_weather.rename(columns={'time': 'Date', 'temperature_2m_mean': 'Temp_mean', 'rain_sum': 'Rain'})

    #df_weather['Date'] = pd.to_datetime(df['Date'], errors='coerce') 
    df_weather['Rain'] = df_weather['Rain'] > 0.0


    return df_weather




#8
def merged_df (df, df_weather):

    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df_weather['Date'] = pd.to_datetime(df_weather['Date'], errors='coerce')

    df_merged = df.set_index("Date").join(df_weather.set_index("Date"), how='left')
    
    return df_merged




