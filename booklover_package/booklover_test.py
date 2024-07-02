import pandas as pd
from booklover import Booklover
import unittest


class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        test_obj = Booklover('Isaac', 'gbz6qn@virginia.edu', 'Sci-Fi')
        test_obj.add_book('Regenesis', 7)
        test_book_name = 'Regenesis'
        self.assertTrue(test_book_name in list(test_obj.book_list.book_name))

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        test_obj = Booklover('Isaac', 'gbz6qn@virginia.edu', 'Sci-Fi')
        test_book_name = 'Regenesis'
        test_obj.add_book(test_book_name, 7)
        test_obj.add_book(test_book_name, 5)
        
        self.assertTrue(test_obj.book_list[test_obj.book_list.book_name==test_book_name].shape[0]==1)
        
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        test_obj = Booklover('Isaac', 'gbz6qn@virginia.edu', 'Sci-Fi')
        test_book_name = 'Regenesis'
        test_obj.add_book(test_book_name, 7)

        self.assertTrue(test_obj.has_read(test_book_name))
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        test_obj = Booklover('Isaac', 'gbz6qn@virginia.edu', 'Sci-Fi')
        test_book_name = 'Regenesis'
        test_obj.add_book(test_book_name, 7)

        self.assertFalse(test_obj.has_read('Kakfa on the Shore'))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        test_obj = Booklover('Isaac', 'gbz6qn@virginia.edu', 'Sci-Fi')
        test_obj.add_book('Regenesis', 7)
        test_obj.add_book('Cyteen', 10)
        test_obj.add_book('Project Hail Mary', 10)
        expected = 3

        self.assertEqual(test_obj.num_books_read(), expected)
        
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        test_obj = Booklover('Isaac', 'gbz6qn@virginia.edu', 'Sci-Fi')
        test_obj.add_book('Regenesis', 7)
        test_obj.add_book('Cyteen', 10)
        test_obj.add_book('Project Hail Mary', 10)
        test_obj.add_book('Bad Book', 2)
        test_obj.add_book('Horrible Book', 1)
        favorites = test_obj.fav_books()

        self.assertEqual(favorites[favorites.book_rating <= 3].shape[0], 0)
        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)