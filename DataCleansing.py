import pandas as pd

'''
As the name column is used in many joins, the column is refactored to have a lower case name with lower case contents
'''


def clean_name_column(df):
    if "Name" in df.columns:
        renamed_df = df.rename(columns={"Name": "name"})
    else:
        renamed_df = df

    df_with_lower_case_name = renamed_df
    df_with_lower_case_name['name'] = df_with_lower_case_name['name'].str.lower()

    return df_with_lower_case_name


def clean_comics_data(comics_df):
    comics_deduplicated = comics_df.drop_duplicates()
    # comics data has some missing descriptions which cannot be loaded as JSON into database
    # these are converted to none so they are valid json
    comics = comics_deduplicated.where(pd.notnull(comics_deduplicated), None)
    return comics


def clean_characters_data(characters_df):
    characters_deduplicated = characters_df.drop_duplicates()
    print(characters_deduplicated.head(5))
    characters_cleaned = clean_name_column(characters_deduplicated)
    print(characters_cleaned.head(5))
    return characters_cleaned


def clean_characters_to_comics_data(characters_to_comics_df):
    characters_to_comics_deduplicated = characters_to_comics_df.drop_duplicates()
    return characters_to_comics_deduplicated


def clean_characters_stats_data(characters_stats_df):
    characters_stats_deduplicated = characters_stats_df.drop_duplicates()

    # rename columns used in other data frames
    characters_stats_clean_column_names = characters_stats_deduplicated.rename(columns=
    {
        "Alignment": "Alignment_CharactersStats",
        "Intelligence": "Intelligence_CharactersStats",
        "Durability": "Durability_CharactersStats"
    })

    characters_stats_cleaned = clean_name_column(characters_stats_clean_column_names)

    return characters_stats_cleaned


def clean_marvel_characters_info_data(marvel_characters_info_df):
    marvel_characters_info_deduplicated = marvel_characters_info_df.drop_duplicates()

    # the id column is not required as the characterID from the characters table is being used as the ID
    # rename alignment since it is used in another dataframe
    marvel_characters_info_clean_columns = marvel_characters_info_deduplicated.drop(columns='ID').rename( \
        columns={"Alignment": "Alignment_MarvelCharactersInfo"})

    marvel_characters_info_cleaned = clean_name_column(marvel_characters_info_clean_columns)

    return marvel_characters_info_cleaned


def clean_superheroes_power_matrix_data(superheroes_power_matrix_df):
    superheroes_power_matrix_deduplicated = superheroes_power_matrix_df.drop_duplicates()

    # rename these columns since they are in other data frames
    superheroes_power_matrix_clean_columns = superheroes_power_matrix_deduplicated.rename(columns=
    {
        "Intelligence": "Intelligence_SuperHeroesPowerMatrix",
        "Durability": "Durability_superHeroesPowerMatrix"
    })

    superheroes_power_matrix_cleaned = clean_name_column(superheroes_power_matrix_clean_columns)

    return superheroes_power_matrix_cleaned
