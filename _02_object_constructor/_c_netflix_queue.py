
class Movie:
    def __init__(self, title, stars):
        self.title = title
        self.stars = stars

    def to_string(self):
        return "\"" + self.title + "\" - " + str(self.stars) + " stars"

    def get_ticket_price(self):
        if self.stars > 2:
            return "That will be $12 please."
        elif 'twilight' in self.title.lower():
            return "This movie is so bad, we'll pay YOU to watch it!"
        else:
            return "Don't waste your money on this horrible rubbish."


class NetflixQueue:
    def __init__(self):
        self.movies = list()

    def get_best_movie(self):
        self.sort_movies_by_rating()
        return self.movies[0]

    def add_movie(self, movie):
        self.movies.append(movie)

    def get_movie(self, movie_number):
        return self.movies[movie_number]

    def sort_movies_by_rating(self):
        self.movies.sort(key=lambda movie: movie.stars, reverse=True)

    def print_movies(self):
        print("Your Netflix queue contains: ")

        for movie in self.movies:
            print(movie.to_string())


if __name__ == '__main__':
    pass
    # Use Movie and NetflixQueue classes above to complete the following changes:

    # TODO 1) Instantiate (create) at least 5 Movie objects.
    M1 = Movie("M1", 1)
    M2 = Movie("M2", 2)
    M3 = Movie("M3", 3)
    M4 = Movie("M4", 4)
    M5 = Movie("M5", 5)
    # TODO 2) InstaUse the Movie class to get the ticket price of one of your movies.
    M5.get_ticket_price()
    # TODO 3) initiate a NetflixQueue object.
    Netflix = NetflixQueue()
    # TODO 4) Add your movies to the Netflix queue.
    Netflix.add_movie(M1)
    Netflix.add_movie(M2)
    Netflix.add_movie(M3)
    Netflix.add_movie(M4)
    Netflix.add_movie(M5)
    # TODO 5) Print all the movies in your queue.
    Netflix.print_movies()
    # TODO 6) Use your NetflixQueue object to finish the sentence "the best movie is...."
    Netflix.sort_movies_by_rating()
    List = Netflix.movies
    print("The best movie is", List[0].to_string())
    print("The second best movie is", List[1].to_string())
    # TODO 7) Use your NetflixQueue to finish the sentence "the second best movie is...."
