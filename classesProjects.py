class Movie:
    def __init__(self, title, year, director, rating, genre, cast):
        self.title = title
        self.genre = genre
        self.rating = rating
        self.director = director
        self.cast = cast
        self.year = year

    def __str__(self):
        return f"{self.title}, [{self.year}]\n[{self.genre}] [{self.rating}]\nDIRECTOR: {self.director}\nCAST: {self.cast}"



class MovieList:
    def __init__(self, movies = []):
        self.movies = movies

    def sortAlpha(movies):
        ansList = []
        titleList = []
        for i in movies:
            titleList += i.title
        titleList = titleList.sort
        for i in titleList:
            for a in movies:
                if a.title == titleList[i]:
                    ansList.append(a)
        for item in ansList:
            print(item)
    
    def sortYear(movies):
        yearList = []
        ansList = []
        yearList = yearList.sort
        for i in len(movies):
            for a in movies:
                if a.year == i:
                    ansList.append(a)
        for item in ansList:
            print(item)
    
    def listGenre(movies):
        searchGenre = input("Enter the genre: ")
        ansList = []
        for i in movies:
            if searchGenre == i.genre:
                ansList.append(i)
        for item in ansList:
            print(item)
    
    def searchDirector(movies):
        searchDirector = input("Enter the name of the director: ")
        ansList = []
        for i in movies:
            if searchDirector == i.director:
                ansList.append(i)
        for item in ansList:
            print(item)
    
    def searchCast(movies):
        searchCast = input("Enter the cast member: ")
        ansList = []
        for i in range(len(movies)):
            if search(i.cast(searchCast)):
                ansList.append(i)
        for item in ansList:
            print(item)

listMovies = MovieList([
    Movie("The Godfather", 1972, "Francis Ford Coppola", "R", "Crime", ["Marlon Brando", "Al Pacino", "James Caan"]),
    Movie("Inception", 2010, "Christopher Nolan", "PG-13", "Sci-Fi", ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"]),
    Movie("The Matrix", 1999, "Lana Wachowski", "R", "Sci-Fi", ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"]),
    Movie("Forrest Gump", 1994, "Robert Zemeckis", "PG-13", "Drama", ["Tom Hanks", "Robin Wright", "Gary Sinise"]),
    Movie("The Dark Knight", 2008, "Christopher Nolan", "PG-13", "Action", ["Christian Bale", "Heath Ledger", "Aaron Eckhart"]),
    Movie("Schindler's List", 1993, "Steven Spielberg", "R", "Drama", ["Liam Neeson", "Ben Kingsley", "Ralph Fiennes"]),
    Movie("Fight Club", 1999, "David Fincher", "R", "Drama", ["Brad Pitt", "Edward Norton", "Helena Bonham Carter"]),
    Movie("Goodfellas", 1990, "Martin Scorsese", "R", "Crime", ["Robert De Niro", "Ray Liotta", "Joe Pesci"]),
    Movie("The Silence of the Lambs", 1991, "Jonathan Demme", "R", "Thriller", ["Jodie Foster", "Anthony Hopkins", "Scott Glenn"]),
    Movie("Titanic", 1997, "James Cameron", "PG-13", "Romance", ["Leonardo DiCaprio", "Kate Winslet", "Billy Zane"]),
    Movie("The Lord of the Rings: The Fellowship of the Ring", 2001, "Peter Jackson", "PG-13", "Fantasy", ["Elijah Wood", "Ian McKellen", "Orlando Bloom"]),
    Movie("Gladiator", 2000, "Ridley Scott", "R", "Action", ["Russell Crowe", "Joaquin Phoenix", "Connie Nielsen"]),
    Movie("The Green Mile", 1999, "Frank Darabont", "R", "Drama", ["Tom Hanks", "Michael Clarke Duncan", "David Morse"]),
    Movie("Saving Private Ryan", 1998, "Steven Spielberg", "R", "War", ["Tom Hanks", "Matt Damon", "Tom Sizemore"]),
    Movie("Jurassic Park", 1993, "Steven Spielberg", "PG-13", "Adventure", ["Sam Neill", "Laura Dern", "Jeff Goldblum"]),
    Movie("The Departed", 2006, "Martin Scorsese", "R", "Crime", ["Leonardo DiCaprio", "Matt Damon", "Jack Nicholson"]),
    Movie("The Lion King", 1994, "Roger Allers", "G", "Animation", ["Matthew Broderick", "Jeremy Irons", "James Earl Jones"]),
    Movie("Eternal Sunshine of the Spotless Mind", 2004, "Michel Gondry", "R", "Romance", ["Jim Carrey", "Kate Winslet", "Kirsten Dunst"]),
    Movie("The Sixth Sense", 1999, "M. Night Shyamalan", "PG-13", "Thriller", ["Bruce Willis", "Haley Joel Osment", "Toni Collette"]),
    Movie("The Usual Suspects", 1995, "Bryan Singer", "R", "Mystery", ["Kevin Spacey", "Gabriel Byrne", "Chazz Palminteri"])
])

def main():
    print("Key,\nA = Alphabetical Sort\nY = Year Sort\nG = Search Genre\nD = Search Director\nC = Search Cast")
    choice = input("Which one would you like to do? ")
    if choice == "A":
        MovieList.sortAlpha(listMovies.movies)
    if choice == "Y":
        MovieList.sortYear(listMovies.movies)
    if choice == "G":
        MovieList.listGenre(listMovies.movies)
    if choice == "D":
        MovieList.searchDirector(listMovies.movies)
    if choice == "C":
        MovieList.searchCast(listMovies.movies)

main()
    