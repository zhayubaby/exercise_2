import sqlite3

# Read the file and copy its content to a list
stephen_king_adaptations_list = []
with open('stephen_king_adaptations.txt', 'r') as file:
    stephen_king_adaptations_list = file.readlines()

# Establish a connection to the SQLite database
newConnection = sqlite3.Connection('stephen_king_adaptations.db')
cursor = newConnection.cursor()

# Create a table in the database
cursor.execute('''
    CREATE TABLE IF NOT EXISTS stephen_king_adaptations_table (
        movieID INTEGER PRIMARY KEY AUTOINCREMENT,
        movieName TEXT,
        movieYear INTEGER,
        imdbRating REAL
    )
''')

# Insert data from the list into the database table
for line in stephen_king_adaptations_list:
    movie_data = line.strip().split(',')
    cursor.execute('INSERT INTO stephen_king_adaptations_table (movieName, movieYear, imdbRating) VALUES (?, ?, ?)',
                   (movie_data[1], int(movie_data[2]), float(movie_data[3])))

newConnection.commit()

#cursor.close()

while True:
    print("\nOptions:")
    print("1. Search by Movie Name")
    print("2. Search by Movie Year")
    print("3. Search by Movie Rating")
    print("4. STOP")
    option = input("Enter your choice: ")

    if option == '1':
        movie_name = input("Enter the name of the movie: ")
        cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieName = ?", (movie_name,))
        result = cursor.fetchone()
        if result:
            print("Movie found:")
            print(f"Movie Name: {result[1]}")
            print(f"Movie Year: {result[2]}")
            print(f"IMDB Rating: {result[3]}")
        else:
            print("No such movie exists in our database")

    elif option == '2':
        movie_year = input("Enter the year: ")
        cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieYear = ?", (int(movie_year),))
        results = cursor.fetchall()
        if results:
            print("Movies found:")
            for result in results:
                print(f"Movie Name: {result[1]}")
                print(f"Movie Year: {result[2]}")
                print(f"IMDB Rating: {result[3]}")
        else:
            print("No movies were found for that year in our database.")

    elif option == '3':
        rating_limit = float(input("Enter the minimum rating: "))
        cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE imdbRating >= ?", (rating_limit,))
        results = cursor.fetchall()
        if results:
            print("Movies found:")
            for result in results:
                print(f"Movie Name: {result[1]}")
                print(f"Movie Year: {result[2]}")
                print(f"IMDB Rating: {result[3]}")
        else:
            print("No movies at or above that rating were found in the database.")

    elif option == '4':
        print("Thank you for using the Stephen King Adaptations Database!")
        break

# Close the database connection
    #if newConnection():
newConnection.close()