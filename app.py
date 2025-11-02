"""
=================================================================
                  Library Management System 101
               A Simple Library Management System
=================================================================
"""

import streamlit as st


# =================================================================
#                          Book Class
# =================================================================
class Book:
    """
    A class to represent a book in the library.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        available (bool): Availability status of the book.

    Methods:
        checkout(): Marks the book as checked out.
        return_book(): Marks the book as available.
        display_info(): Displays the book information.
    """

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def checkout(self):
        """
        Marks the book as checked out if available.
        Returns True if successful, False if already checked out.
        """
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        """
        Marks the book as available.
        """
        self.available = True

    def display_info(self):
        """
        Displays the book information using Streamlit.
        """
        st.write(
            f"**Title:** {self.title}  \n"
            f"**Author:** {self.author}  \n"
            f"**Available:** {'Yes' if self.available else 'No'}"
        )


# Sample books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("Pride and Prejudice", "Jane Austen")


# =================================================================
#                        Library Class
# =================================================================
class Library:
    """
    A class to represent a library containing multiple books.

    Attributes:
        books (list): A list of Book objects.

    Methods:
        add_book(book): Adds a book to the library.
        display_books(): Displays all books in the library.
        get_book_by_title(title): Retrieves a book by its title.
    """

    def __init__(self):
        self.books = []

    def add_book(self, book):
        """
        Adds a book to the library.

        Args:
            book (Book): The book to add.
        """
        self.books.append(book)

    def display_books(self):
        """
        Displays all books in the library.
        """
        for i, book in enumerate(self.books, 1):
            st.subheader(f"Book {i}")
            book.display_info()
            st.divider()

    def get_book_by_title(self, title):
        """
        Retrieves a book by its title.

        Args:
            title (str): The title of the book to retrieve.

        Returns:
            Book: The book object if found, None otherwise.
        """
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None


# =================================================================
#                        Streamlit App
# =================================================================
st.title("📚 Library Management System")
st.write("This is a simple library system to manage books.")

# Initialize session state for library
if "library" not in st.session_state:
    library = Library()
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    st.session_state.library = library

# Display all books
st.header("📖 Books in Library")
st.session_state.library.display_books()

# Add interactive features
st.header("🔍 Search and Checkout")
search_title = st.text_input("Enter book title to search:")

if search_title:
    found_book = st.session_state.library.get_book_by_title(search_title)
    if found_book:
        st.success(f"Found: {found_book.title}")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Checkout this book"):
                if found_book.checkout():
                    st.success(f"Successfully checked out: {found_book.title}")
                    st.rerun()
                else:
                    st.warning("This book is already checked out")
        with col2:
            if st.button("Return this book"):
                found_book.return_book()
                st.success(f"Successfully returned: {found_book.title}")
                st.rerun()
    else:
        st.error("Book not found in library")
