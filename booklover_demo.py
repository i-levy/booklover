from booklover_package.booklover import Booklover

demo = Booklover('Isaac', 'gbz6qn@virginia.edu', 'Sci-Fi')

demo.add_book('The Obelisk Gate', 4)

print(demo.num_books_read())