<img src="https://www.emagister.com/assets/es/logos/centro/id/136150/size/l.jpg" alt="logo ironhack" style="width:150px;height:100px;">

# Emotional state based on sent emojis

## Table of Contents

- [Project Description](#project-description)
- [Database](#database)
- [Workflow](#workflow)
- [Organization](#organization)
- [Conclusions](#conclusions)
- [Links](#links)

## Project Description
WhatsApp and emojis are fundamental elements of modern communication. As one of the most popular messaging applications worldwide, WhatsApp enables users to communicate effectively through text, voice and video messages. Emojis, on the other hand, serve as a tool to express emotions, feelings or actions quickly and efficiently, either as a complement or a replacement to written text.

By analyzing data from our WhatsApp conversations, including the use of emojis, we can obtain valuable information about our communication behaviors with others. This can help us better understand trends and patterns in our way of communicating.


<center>Which is the emoticon we send more frequently?

Do we send more emojis depending on the temperature?

Do we send more emoticons when the weather is good??</center>


## Database
The goal of this project is to enrich a dataset using tools such as web scraping and APIs. To achieve this, the main dataset consists of extracted conversations from a personal Whatsapp account. In parallel, an open-source API called "Open-Meteo" was used to obtain a historical weather report of the average temperature and amount of rainfall for the days on which the Whatsapp conversations took place.


## Workflow
* Data Acquisition: Collect data from WhatsApp conversations and the Open-Meteo API.

* Data Management: Clean, transform, and merge both dataframes.

* Data Analysis: Create visualizations to graphically represent the data, extract patterns, and test hypotheses.

* Conclusion: Draw conclusions based on the results of the visualizations.

![workflow](/images/workflow.png)

## Organization
The repository consists of a README file, a .gitignore file and the following folders:

* src/: contains the .py files for the different executables: ```extraction.py``` for the extraction of the data, ```cleaning.py``` for cleaning and merge both datasets and ```visualization.py``` to show the charts.

* figures/: contains the graphics extracted from the visualization executable.



## Conclusions
The number of conversations analyzed should be increased in order to obtain more conclusive correlations and increase the reliability of the results.

It would be interesting to analyze conversations from different social relationships (family, friends, partner, co-workers...) to identify patterns of behavior and to observe the dynamics of communication in each type of relationship.

Additional graphs could be generated with different types of visualization and grouping variables in different ways to obtain new hypotheses.

## Links
![API](https://open-meteo.com/)


