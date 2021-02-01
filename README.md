# Python Superheroes

This project takes data from the kaggle marvel superheroes dataset and aims to join relevant data into a document structure to be saved down as a file and to PostreSQL.

## Installation
- Create docker container for PostreSQL
  ```
  docker run --rm --name pg-docker -e POSTGRES_PASSWORD=docker -d -p 5432:5432 postgres
  ```
- Update DatabaseConfig.py to reflect PostreSQL container connection details
- install requirements.txt
  ```
  pip install -r requirements.txt
  ```

- run main.py

## Data Model
![Image of architecture](https://github.com/stevewb1993/pythonsuperheroes/blob/master/marveldatamodel.svg)

- There are quite clean relationships between the characters, characters_to_comics, and comics datasets. 
- There are three additional character level datasets which can be joined from the character dataset on character name. However, each table contains records that the others do not.
- The marvel dc characters table was not used for the analysis as the join to this table was not clear

## Data Quality
- Several pure duplicates were identified in some tables, for simplicity, a remove_duplicates call was therefore made on all tables
- Several tables include multiple records for single characters, but with different values for each column
- Some tables included common columns, but these did not always tally even for a given character
- The marvel dc characters dataset is available in csv and excel formats. Upon inspection, these contained the same data except for the FirstAppearance Column

## Extensions that could be taken
- UPSERT or TRUNCATE/INSERT method for loading data into PostgreSQL
- Handling of duplicate records in datasets. Either identify correct values or take averages?
- Unit testing of data transformations
- Incorporate character data for characters in the character_stats, character_info, and superhero_power_matrix tables
- Incorporate the Marvel_DC_Characters dataset
- Data Validation steps on the input data

## Querying the data
- Once the data is landed in postgres, the comic data can be queried by using json_to_recordset, for example:
  ```
    SELECT 
	    s."characterID",
	    t."title"
    FROM
        public."MarvelHeroes" s
	CROSS JOIN LATERAL
	    json_to_recordset(s."Comics") as t("title" text)
  ```

