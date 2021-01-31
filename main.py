import pandas as pd
import DataCleansing as dc
import DataTransformation as dt
import DataOutput as do
import DatabaseConfig


def main():

    characters = pd.read_csv("Data/characters.csv")
    characters_to_comics = pd.read_csv("Data/charactersToComics.csv")
    characters_stats = pd.read_csv("Data/charcters_stats.csv")
    comics = pd.read_csv("Data/comics.csv")
    marvel_characters_info = pd.read_csv("Data/marvel_characters_info.csv")
    superheroes_power_matrix = pd.read_csv("Data/superheroes_power_matrix.csv")

    # Clean Data
    characters_cleaned = dc.clean_characters_data(characters)
    characters_to_comics_cleaned = dc.clean_characters_to_comics_data(characters_to_comics)
    characters_stats_cleaned = dc.clean_characters_stats_data(characters_stats)
    comics_cleaned = dc.clean_comics_data(comics)
    marvel_characters_info_cleaned = dc.clean_marvel_characters_info_data(marvel_characters_info)
    superheroes_power_matrix_cleaned = dc.clean_superheroes_power_matrix_data(superheroes_power_matrix)

    # join the data
    joined_data = dt.combine_all_superhero_data(
        characters_cleaned,
        characters_to_comics_cleaned,
        characters_stats_cleaned,
        comics_cleaned,
        marvel_characters_info_cleaned,
        superheroes_power_matrix_cleaned
    )

    # Output data
    # Write to parquet
    do.save_to_parquet(joined_data, 'final_data.parquet')
    do.save_to_postgres(
        joined_data,
        DatabaseConfig.data_sink_config['server'],
        DatabaseConfig.data_sink_config['database'],
        DatabaseConfig.data_sink_config['username'],
        DatabaseConfig.data_sink_config['password'],
        DatabaseConfig.data_sink_config['table_name']
    )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()