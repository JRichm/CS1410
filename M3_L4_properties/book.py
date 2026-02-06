"""
Complete Lab 4 and update the following information:

Author: James Richmond
Date: 01/19/2026
"""

class Book:
    def __init__(self, title: str = "", author: str = "", description: str = ""):
        self._title = title
        self._author = author
        self._description = description

    
    # title getter
    def _get_title(self):
        return self._title
    

    # title setter
    def _set_title(self, new_title: str = ""):
        # make sure new title value is a string
        if not isinstance(new_title, str):
            raise TypeError(f"`{new_title}` ({type(new_title)}) is not a valid title")
        
        # make sure new title value is not an empty string
        if not new_title:
            raise ValueError("Cannot change title to an empty string")

        # set book title
        print(f"Changing book title from `{self._title}` to `{new_title}`")
        self._title = new_title


    # expose private variable `_title` using getter and setter methods under the `title` property
    title = property(_get_title, _set_title)


    # author getter
    @property
    def author(self):
        return self._author

    # author setter
    @author.setter
    def author(self, new_author: str = ""):
        # make sure new author value is a string
        if not isinstance(new_author, str):
            raise TypeError(f"`{new_author}` ({type(new_author)}) is not a valid author")
        
        # make sure new author value is not an empty string
        if not new_author:
            raise ValueError("Cannot change author to an empty string")

        # set book author
        print(f"Changing book author from `{self._author}` to `{new_author}`")
        self._author = new_author

    
    # description getter (no setter)
    @property
    def description(self):
        return f"{self._title} was written by {self._author}."


    def __str__(self):
        return f"{self._title} by {self._author}"
    


def main():
    my_book = Book("Book", "Author", "Description")
    my_book.title = "Unwind"
    my_book.author = "Neal Shusterman"
    print(my_book.description)

    # my_book.description = f"{my_book.title} is a book written by {my_book.author}" # AttributeError: can't set attribute


if __name__ == "__main__":
    main()