# Python Superheroes

This project takes data from the kaggle marvel superheroes dataset and aims to join relevant data into a document structure and saved down as a file and to postres.

## Installation
- Create docker container for PostreSQL
- update configuration file to reflect PostreSQL connection details
- install requirements.txt
- run main.py

## Data Model
![Image of architecture](https://github.com/stevewb1993/pythonsuperheroes/blob/master/marveldatamodel.svg)

- Sentiment and entities analysis using AWS Comprehend of tweets by users with a large number of followers. 
- Word counts for showing how language being used in tweets is changing over time.