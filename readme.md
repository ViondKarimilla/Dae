##Dae.mn Code Challenge

I included both a Jupyter notebook for demonstration of the steps taken, as well as a python file which is testable with the included pytest file.


#Objective
To fetch top 15 movies wiht the minimum of 100 votes as we need to know the average number votes

#Method
For this given task we need to know the number of Votes and Movie details, so I selected two data sets 

1)title_ratings with columns
 tconst	¦averageRating¦ numVotes

2)title_basics with columns
tconst	titleType	primaryTitle	originalTitle	isAdult	startYear	endYear	runtimeMinutes	genres

then merged the title_ratings and title_basics dataframes.
in title_basics ,I select two columns ('tconst', 'originalTitle) and tconst column was the common column in both datasets. 

I just did inner join, then calculated the mean of numVotes column.

I calculated the rank by using the below Formula:
(numVotes / averageNumberOfVotes) * averageRating

Then selected the top_15.
top_15 = merged_frame_100.nlargest(15, 'ranking')





#Built With
pandas
matplotlib.pyplot


Project Link: https://github.com/ViondKarimilla/Dae