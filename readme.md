Book Recommender System

This Python script is a command-line book recommender system. It loads book information from a CSV file, prompts the user for their genre and length preferences, and outputs recommended book(s) that match these values.

Features

CSV Data source - Loads book information(title, author, genre, length) from a Comma Separated Value (CSV) file.

Genre and Length filtering - Recommends books from the loaded book data based on the user's specified genre and length preference (short, average or long).

Error Handling - Handles errors for file not found, csv format, and invalid user input.

Command-line Interface - Basic command-line interface for user to interact with.

Dependencies

A CSV file (with book info) to load into the recommender system.

Setup

Get Book Data

Create a CSV file (you can name it whatever you want, e.g. `processed_books.csv`) that has the following column headers and data:

`title`: title of the book.

`author`: author of the book.

`genre`: genre of the book (for example "Fiction", "Science Fiction", "Romance", etc.).

`length_category`: length of the book must be one of the following: `short`, `average`, `long`.

You must have a header row with the exact column titles listed above as your CSV file will be opened with the row headers as its column names

You should put this CSV file in the same directory as the Python script.

Save the Script

Save Python code below as a .py file (for example, `recommender.py`).

Using the Script

1. Open your terminal/ command prompt

2. Change directory to the directory that has the saved .py file and CSV file

3. Run the script:

4. The script then prompts you for a the genre of a book and for the length of the book.

5. The script will output a list of books, or a message if no books are found that match the requested preferences.

Sample CSV data (processed_books.csv):

csv -

title,author,genre,length_category

Pride and Prejudice,Jane Austen,Romance,long

The Hitchhiker's Guide to the Galaxy,Douglas Adams,Science Fiction,short

To Kill a Mockingbird,Harper Lee,Classic,long

The Great Gatsby,F. Scott Fitzgerald,Fiction,average
