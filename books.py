books = { "the cat in the hat": "Dr Seuss", "captain underpants": "Dav Pilky", "diary of a wimpy kid" : "Jeff Kinney" }

books_dict = {"author1": ["book1", "book2"], "author2": ["book3", "book4"]}

y= input ("enter author name")
print(", ".join(books_dict[y]))
