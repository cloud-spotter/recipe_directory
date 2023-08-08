from lib.album import Album

class AlbumRepository():
    # Initialise with a database connection
    def __init__(self, connection):
        self._connection = connection


    # Selecting all records
    # No arguments
    def all(self):
        # Executes the SQL query:
        # SELECT id, title, release_year, artist_id FROM albums;

        # Returns an array of Album objects.

        # Gets a single record by its ID
        # One argument: the id (number)
        rows = self._connection.execute('SELECT * from albums')
        albums = []
        for row in rows:
            item = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(item)
        return albums

    def find(self, artist_id):
        # Executes the SQL query:
        # SELECT id, title, release_year, artist_id FROM albums WHERE id = $1;
        # Returns a single Album object.
        # Add more methods below for each operation you'd like to implement.
        rows = self._connection.execute(
            'SELECT * from albums WHERE id = %s', [artist_id])
        row = rows[0]
        return Album(row["id"], row["title"], row["release_year"], row["artist_id"])

    def create(self, album):
        # Executes the SQL query:
        # INSERT INTO albums
        # (title, release_year, artist_id)
        # VALUES( album.title, album.release_year, album.artist_id );

        # Create a new album
        self._connection.execute('INSERT INTO albums(title, release_year, artist_id) VALUES(%s, %s, %s)', [album.title, album.release_year, album.artist_id])
        return None


    #def update(album)
        # Executes the SQL query: 

    def delete(album):
        # Executes the SQL query:
        # DELETE FROM albums WHERE id = $1;

        # Delete an album by its id
        pass