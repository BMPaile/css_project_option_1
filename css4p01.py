import pandas as pd

df = pd.read_csv("movie_dataset.csv")
# Data Cleaning
# removing spaces in column names
df.rename(columns = lambda x: x.replace(" ",""), inplace = True)

# fill nans with mean values
ave_rev = df["Revenue(Millions)"].mean()
ave_metascore = df["Metascore"].mean()
df["Revenue(Millions)"].fillna(ave_rev, inplace = True)
df["Metascore"].fillna(ave_metascore, inplace = True)


# Question 1
highest_rated_movie = (max(df["Rating"]))
print(df[df["Rating"] == highest_rated_movie])


# Question 2
print("Average revenue for all movies in the dataset: " + str(ave_rev) + " Million \n")


# Question 3
year2015 = (df[df["Year"] == 2015])
year2016 = (df[df["Year"] == 2016])
revenue2015 = year2015["Revenue(Millions)"].mean()
revenue2016 = year2016["Revenue(Millions)"].mean()
ave_rev201516 = ((revenue2015 + revenue2016)/2)
print("Average revenue of movies from 2015 to 2017 in the dataset: " + str(ave_rev201516) + " Million \n")


# Question 4
movies_in_2016 = len(year2016)
print("Number of movies released in 2016: " + str(movies_in_2016) + "\n")


# Question 5
cn_movies = df[df["Director"] == "Christopher Nolan"]
print("Movies directed by Christopher Nolan: " + str(len(cn_movies)) + "\n")


# Question 6
rating_of_atleast_8 = df[df["Rating"] >= 8]
print("Movies with a rating of at least 8: " + str(len(rating_of_atleast_8)) + "\n")
      

# Question 7
med_rating_cn_movies = cn_movies["Rating"].median()
print("Median rating of Christopher Nolan movies: " + str(med_rating_cn_movies) + "\n")


# Question 8
year2006 = (df[df["Year"] == 2006])
year2007 = (df[df["Year"] == 2007])
year2008 = (df[df["Year"] == 2008])
year2009 = (df[df["Year"] == 2009])
year2010 = (df[df["Year"] == 2010])
year2011 = (df[df["Year"] == 2011])
year2012 = (df[df["Year"] == 2012])
year2013 = (df[df["Year"] == 2013])
year2014 = (df[df["Year"] == 2014])
count = 2005
for years in [year2006, year2007, year2008, year2009, year2010, year2011, year2012, year2013, year2014, year2015, year2016]:
    ave_rating = years["Rating"].mean()
    count = count + 1
    print(count, str(ave_rating))


# Question 9
percentage_increase = 100*(len(year2016)-len(year2006))/len(year2006)
print("\nPercentage increease: " + str(percentage_increase) + "\n")


# Question 10
# Split actors into different columns
df[["Actor1", "Actor2", "Actor3", "Actor4"]] = df["Actors"].str.split("," , expand = True)
col_actor1 = df["Actor1"].value_counts()
col_actor2 = df["Actor2"].value_counts()
col_actor3 = df["Actor3"].value_counts()
col_actor4 = df["Actor4"].value_counts()
for actors in [col_actor1, col_actor2, col_actor3, col_actor4]:
    print(str(actors) + "\n")
    

# Question 11
# Split genres into diifferent columns
df[["Genre1", "Genre2", "Genre3"]] = df["Genre"].str.split("," , expand = True)
col_genre1 = df["Genre1"].value_counts()
col_genre2 = df["Genre2"].value_counts()
col_genre3 = df["Genre3"].value_counts()
for genres in [col_genre1, col_genre2, col_genre3]:
    print(str(genres) + "\n")


# Question 12
import matplotlib.pyplot as plt
# Bar graph of number of movies released from 2006 to 2016
x = ["2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016"]
y = [len(year2006), len(year2007), len(year2008), len(year2009), len(year2010), len(year2011), len(year2012), len(year2013), len(year2014), len(year2015), len(year2016)]
plt.bar(x, y)
plt.xlabel("Year")
plt.ylabel("Number of movies released")
plt.title("Number of movies released from 2006 to 2016")
plt.show()

# fetching top ten highest and lowest grossing movies from dataset
df1 = df.nlargest(n = 10, columns = ["Revenue(Millions)"])
df2 = df.nsmallest(n = 10, columns = ["Revenue(Millions)"])
df3 = pd.concat([df1, df2], ignore_index = True)

# Scatter plot of top 10 highest and lowest grossing movies from 2006 to 2016
df3.plot.scatter(x = "Year", y = "Revenue(Millions)", s = "Rank", title = "Top 10 highest and lowest grossing movies from 2006 to 2016")



