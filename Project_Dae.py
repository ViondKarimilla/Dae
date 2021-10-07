import pandas as pd


name_basics = pd.read_csv('name.basics.tsv', sep='\t', low_memory=False)
title_akas = pd.read_csv('title.akas.tsv', sep='\t', low_memory=False)
title_basics = pd.read_csv('title.basics.tsv', sep='\t', low_memory=False)
title_crew = pd.read_csv('title.crew.tsv', sep='\t', low_memory=False)
title_episode = pd.read_csv('title.episode.tsv', sep='\t', low_memory=False)
title_principals = pd.read_csv('title.principals.tsv', sep='\t', low_memory=False)
title_ratings = pd.read_csv('title.ratings.tsv', sep='\t', low_memory=False)

def cal_top15 ():

    #Merging the title_ratings and title_basics dataframes
    merged_frame = pd.merge(title_ratings, title_basics[['tconst', 'originalTitle']], on = 'tconst', how='inner')


    #retriving ones with number of votes about 100
    merged_frame_100 = merged_frame.loc[merged_frame['numVotes'] >= 100]


    #restrict from chaining
    pd.options.mode.chained_assignment = None

    #calculate the average number of votes
    averageNumberOfVotes = merged_frame_100["numVotes"].mean() #4020.0313450597114

    #averageNumberOfVotes

    # Calculating ranking = (numVotes / averageNumberOfVotes) * averageRating
    merged_frame_100['ranking'] = merged_frame_100.apply(lambda row: (row.numVotes / averageNumberOfVotes) * row.averageRating, axis=1)


    top_15 = merged_frame_100.nlargest(15, 'ranking')

    title_list = list(top_15['originalTitle'])

    #Task B:List of the Title of top 15 Movies
    return title_list

print(cal_top15())











