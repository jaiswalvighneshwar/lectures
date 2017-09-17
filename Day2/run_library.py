from book import Book
from author import Author
print Author.count

a1 = Author('abc','m',5)

print Author.count
a2 = Author('jane','f',4)
a2.__gender = 'T'			# will have no effect on the original private attributes
a2.__rating = -1

a2.set_gender('m')

#print a2.__gender
#print a2.get_details()

print Author.count
b1 = Book('book1',100,400,authors=[])

b2 = Book('book2',pages=400,price = 700,authors=[a1,a2])

print b1.has_authors() 
print b2.has_authors()

print b2.get_details()
print b1.get_details()
