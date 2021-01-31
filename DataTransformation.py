import pandas as pd

'''
This method combines all the character data, with the base table being the characters dataframe
'''


def combine_character_data(characters_df, characters_stats_df, superheroes_power_matrix_df, marvel_characters_info_df):
    df_merged = pd.merge(characters_df, characters_stats_df, on='name', how='left')
    df_merged = pd.merge(df_merged, superheroes_power_matrix_df, on='name', how='left')
    df_merged = pd.merge(df_merged, marvel_characters_info_df, on='name', how='left')

    return df_merged


'''
This method takes the comics data and comics_to_characters data and aggregates it so there will be one row per character
'''


def aggregate_comic_data(comics_df, characters_to_comics_df):
    combined_comic_characters = pd.merge(characters_to_comics_df, comics_df, on="comicID", how='left')

    # aggregate the comics data so there is one record (json array) per character
    character_comic_df = (combined_comic_characters.groupby('characterID', as_index=True)
                          .apply(lambda x: x[['comicID', 'title', 'issueNumber', 'description']].to_dict('r'))
                          .reset_index()
                          .rename(columns={0: 'Comics'}))

    return character_comic_df


def combine_full_character_comic_data(comics_aggregated_df, characters_aggregated_df):
    return pd.merge(characters_aggregated_df, comics_aggregated_df, on='characterID', how='left')


def combine_all_superhero_data(characters, characters_to_comics, characters_stats, comics, marvel_characters_info, superheroes_power_matrix):
    combined_characters = combine_character_data(characters, characters_stats, superheroes_power_matrix, marvel_characters_info)
    aggregated_comics = aggregate_comic_data(comics, characters_to_comics)
    return combine_full_character_comic_data(aggregated_comics, combined_characters)