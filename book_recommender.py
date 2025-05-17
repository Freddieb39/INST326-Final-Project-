import csv
import sys

class Recommender:
    """ 
    this class gathers the data from the csv, takes in the users input for book reccomendations, and outputs
    the results
    """
    def __init__(self, csv_filepath='processed_books.csv'):
         """starts the system

        Args:
            csv_filepath - path to the csv that stores the book data
        """
        self.books = self._load_books(csv_filepath)
        if not self.books:
            print(f"Error: No books loaded from {csv_filepath}. Cannot proceed.", file=sys.stderr)
            sys.exit(1)
        if self.books and all('genre' in book for book in self.books):
             self.genres = sorted(list(set(book['genre'].lower() for book in self.books)))
        else:
             print("Warning: Could not determine available genres from the data.", file=sys.stderr)
             self.genres = []

    def _load_books(self, csv_filepath):
        """loads the data from the csv and puts it into a list of dictionaries

        Args:
            csv_filepath - path to the csv that stores the book data

        """
        books = []
        valid_lengths = {'short', 'average', 'long'}
        try:
            with open(csv_filepath, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                required_columns = {'title', 'author', 'genre', 'length_category'}
                if not reader.fieldnames:
                    print(f"Error: CSV file '{csv_filepath}' appears to be empty or has no header.", file=sys.stderr)
                    return []
                if not required_columns.issubset(reader.fieldnames):
                    missing = required_columns - set(reader.fieldnames)
                    print(f"Error: CSV file '{csv_filepath}' is missing required columns: {missing}", file=sys.stderr)
                    return []

                for i, row in enumerate(reader, start=2):
                    try:
                        if not row['title'] or not row['author'] or not row['genre'] or not row['length_category']:
                             print(f"Warning: Skipping row {i} due to empty essential field(s): {row}")
                             continue

                        length_cat = row['length_category'].lower()
                        if length_cat not in valid_lengths:
                            print(f"Warning: Skipping row {i} due to invalid length_category '{row['length_category']}'. Expected one of {valid_lengths}: {row}")
                            continue
                        row['length_category'] = length_cat

                        books.append(row)
                    except ValueError:
                         print(f"Warning: Skipping row {i} due to invalid data format: {row}")
                    except KeyError as e:
                        print(f"Warning: Skipping row {i} due to missing column '{e}': {row}")

                if not books:
                     print(f"Warning: No valid book data found in {csv_filepath}.")

            return books
        except FileNotFoundError:
            print(f"Error: The file {csv_filepath} was not found.", file=sys.stderr)
            return []
        except Exception as e:
            print(f"An unexpected error occurred while reading {csv_filepath}: {e}", file=sys.stderr)
            return []

    def _get_genre_preference(self):
        
        if not self.genres:
             print("\nError: No genres available to choose from. Cannot get preference.", file=sys.stderr)
             return None

        print("\nAvailable genres:")
        for genre in self.genres:
            print(f"- {genre.capitalize()}")
        while True:
            user_input = input("Please enter your preferred genre: ").strip().lower()
            if user_input in self.genres:
                return user_input
            else:
                print(f"Invalid genre. Please choose from the list above.")

    def _get_length_preference(self):
        valid_lengths = ['short', 'average', 'long']
        while True:
            print("\nSelect book length preference:")
            print("- Short")
            print("- Average")
            print("- Long")
            user_input = input("Enter 'short', 'average', or 'long': ").strip().lower()
            if user_input in valid_lengths:
                return user_input
            else:
                print("Invalid input. Please enter 'short', 'average', or 'long'.")

    def find_recommendations(self, genre, length_preference):
        recommended_books = []
        if not genre or not length_preference:
            return []
        for book in self.books:
            if book['genre'].lower() == genre and book['length_category'] == length_preference:
                recommended_books.append(book)
        return recommended_books

    def display_recommendations(self, recommended_books):
        print("\n--- Recommendations ---")
        if not recommended_books:
            print("No books found matching your criteria.")
        else:
            print("Here are some books you might like:")
            for book in recommended_books:
                print(f"- {book['title']} by {book['author']} (Genre: {book['genre'].capitalize()}, Length: {book['length_category'].capitalize()})")
        print("---------------------")

    def run(self):
        print("Welcome to the Book Recommender!")
        genre = self._get_genre_preference()
        if genre is None:
            print("Exiting due to inability to determine genre preference.")
            return

        length = self._get_length_preference()

        recommendations = self.find_recommendations(genre, length)
        self.display_recommendations(recommendations)
        print("\nThank you for using the recommender!")

if __name__ == "__main__":
    print("Starting Book Recommender...")
    csv_file_path = 'processed_books.csv'
    recommender = Recommender(csv_filepath=csv_file_path)
    if recommender.books:
        recommender.run()
    else:
        print("Exiting due to issues loading book data.") 
