import pandas as pd
import numpy as np
import seaborn as sns

import plotly.express as px
import plotly.graph_objs as go

import kaleido

import os






# GRAPH TOP 15
def graph_top15 (df_final):
        

    # GROUP: by coubnting the 15 emojis more used
    top_emojis = df_final['Emojis'].value_counts(sort=True, dropna=False).head(10)

    # ATTRIBUTES
    fig = go.Figure(
        go.Bar(
            x=top_emojis.index,
            y=top_emojis.values,
            text=top_emojis.values,
            textposition='inside',
            marker=dict(
                color=['#FFC300', '#FF5733', '#C70039', '#900C3F', '#581845', '#DAF7A6', '#FFC300', '#FF5733', '#C70039', '#900C3F', '#581845', '#DAF7A6', '#FFC300', '#FF5733', '#C70039']
            )
        )
    )

    # LABELS
    fig.update_layout(title='Top 15 Emojis',
                    xaxis_title='Emojis',
                    yaxis_title='Number of Emojis')

    # SAVE
    fig.write_image("figures/graph_top15.png", width=1600, height=800, scale=2)
    fig.show()

    # OPEN FILE
    os.system("open figures/graph_top15.png")





# GRAPH RAIN
def graph_rain (df_final):

    # GROUP: by the "Rain" column and count the emoticons in each group
    emojis_by_rain = df_final.groupby("Rain")["Emojis"].count().reset_index(name="Count")

    # ATTRIBUTES
    fig = px.bar(emojis_by_rain, x="Rain", y="Count", color="Rain",
                title="Number of Emojis according to rainfall")

    # LABELS
    fig.update_layout(xaxis=dict(tickmode="array", tickvals=[0, 1], ticktext=["No Rain", "Rain"], title="Weather"))

     # SAVE
    fig.write_image("figures/graph_rain.png", width=1600, height=800, scale=2)
    fig.show()

    # OPEN FILE
    os.system("open figures/graph_rain.png")





# GRAPH TOP EMOJIS BY YEAR
def graph_top_emojis_year (df_final):

    #GROUP: Agroup the data by year and emoji, count the frequency of each combination and reset the index
    top_emojis_by_year = df_final.groupby(["Year", "Emojis"]).size().reset_index(name="Count")
    # Sort data by year and by the frequency of each emoji within the year
    top_emojis_by_year = top_emojis_by_year.sort_values(["Year", "Count"], ascending=[True, False])
    # Keep the 3 most frequent emojis for each year
    top_emojis_by_year = top_emojis_by_year.groupby("Year").head(3)

    # ATTRIBUTES
    fig = px.bar(top_emojis_by_year, x="Year", y="Count", color="Emojis",
                title="Top 5 Most Sent Emojis by Year")
   
   
   # LABELS
    fig.update_layout(xaxis_title="Year", yaxis_title="Number of Emojis",
                    xaxis=dict(tickvals=[2021, 2022, 2023]))
    
    fig.update_traces(texttemplate='%{y}', textposition='inside')
    
    # SAVE
    fig.write_image("figures/graph_top_emojis_year.png", width=1600, height=800, scale=2)
    fig.show()

    # OPEN FILE
    os.system("open figures/graph_top_emojis_year.png")




# GRAPH TOP EMOJIS BY TEMPERATURE
def graph_top_emojis_temp (df_final):

    # #GROUP: group by temperature and count the number of emojis
    temp_counts = df_final.groupby('Temp_mean')['Emojis'].count()
    # get the top 5 emojis by count
    top_emojis = df_final.groupby('Emojis')['Temp_mean'].count().sort_values(ascending=False).head(3).index
    # filter the DataFrame to include only the top 5 emojis
    df_top_emojis = df_final[df_final['Emojis'].isin(top_emojis)]

    # HISTOGRAM
    fig = px.histogram(df_top_emojis, x="Temp_mean", color="Emojis", nbins=3)

    # LABELS
    fig.update_layout(
        title='Top 5 Emojis sent by temperature',
        xaxis_title='Mean temperature',
        yaxis_title='Number of Emojis',
        bargap=0.1
    )

    fig.update_traces(
        texttemplate='%{y}', # establece el formato del texto
        text=df_top_emojis.groupby(['Emojis', 'Temp_mean']).size().reset_index(name='Count')['Count']
    )

    # SAVE
    fig.write_image("figures/graph_top_emojis_temp.png", width=1600, height=800, scale=2)
    fig.show()

    # OPEN FILE
    os.system("open figures/graph_top_emojis_temp.png")



# GRAPH NUM EMOJIS by TEMP
def graph_num_emojis_temp (df_final):

    # GROUP: group by date and calculate the number of emojis and the average temperature
    df_temp_emojis = df_final.groupby('Date').agg({'Temp_mean': 'mean', 'Emojis': 'count'}).reset_index()

    # create a scatter plot
    fig = go.Figure(
        go.Scatter(
            x=df_temp_emojis['Temp_mean'],
            y=df_temp_emojis['Emojis'],
            mode='markers',
            marker=dict(
                size=8,
                color=df_temp_emojis['Temp_mean'],
                colorbar=dict(title='Mean temp'),
                colorscale='Viridis')
        )
    )

    # LABELS
    fig.update_layout(
        title='Number of Emojis sent per temperature',
        xaxis_title='Mean temperature',
        yaxis_title='Number of emojis',
        showlegend=False
    )

     # SAVE
    fig.write_image("figures/graph_num_emojis_temp.png", width=1600, height=800, scale=2)
    fig.show()

    # OPEN FILE
    os.system("open figures/graph_num_emojis_temp.png")
