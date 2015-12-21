import media
import fresh_tomatoes
# Importing media and fresh_tomatoes libraries

# This file stores the movie information. (Title, Image URL, Youtube URL)

toystory = media.Movie(
    "Toy Story",
    "Toy Story is an American computer-animated buddy-comedy adventure film",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=4KPTXpQehio")

avatar = media.Movie(
    "Avatar",
    "Avatar epic science fiction film set in the mid-22nd century,\
    when humans are colonizing Pandora, a lush habitable moon of a gas giant \
    in the Alpha Centauri star system to mine the mineral unobtanium.",
    "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=d1_JBMrrYw8")

school_of_rock = media.Movie(
    "School of Rock",
    "School of Rock is a comedy film about a struggling rock singer, \
    Dewey Finn (portrayed by Black), who is kicked out of his band \
    and subsequently disguises himself as a substitute teacher.",
    "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie(
    "Ratatouille",
    "Ratatouille is a 2007 American computer-animated comedy film \
    and released by Walt Disney Pictures.",
    "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
    "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie(
    "Midnight in Paris",
    "Midnight in Paris is an American 2011 romantic comedy fantasy film. \
    Set in Paris, the film follows Gil Pender, a screenwriter, \
    who is forced to confront the shortcomings of his relationship with\
    his materialistic fiancee and their divergent goals, which become \
    increasingly exaggerated as he travels back in time each night.",
    "http://tinyurl.com/7zebr4h",
    "https://www.youtube.com/watch?v=5nOF93SzX6s")

hunger_games = media.Movie(
    "Hunger Games",
    "The Hunger Games is a science fiction adventure film. \
    The story takes place in a dystopian post-apocalyptic \
    future in the nation of Panem, where boys and girls \
    between the ages of 12 and 18 must take part in the Hunger Games",
    "http://tinyurl.com/79m8ppm",
    "https://www.youtube.com/watch?v=mfmrPu43DF8")


movies = [toystory, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]


# Calling open_movies_page definition from fresh_tomatoes library.
# This definition will create a static webpage for the list of movies

fresh_tomatoes.open_movies_page(movies)
