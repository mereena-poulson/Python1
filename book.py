class publisher:
  def __init__(self,title,author):
    self.title=title
    self.author=author
  def display(self):
    print("title:",self.title)
    print("author:",self.author)
class book(publisher):
  def __init__(self,price,no_of_page):
    self.price=price
    self.no_of_page=no_of_page
  def display(self):
    print("price",price)
    print("no of page",no_of_page)
class python(book):
  def __init__(self,title,author,price,no_of_page):
    publisher.__init__(self,title,author)
    book.__init__(self,price,no_of_page)
  def display(self):
       print("Title:",self.title)
       print("Author:",self.author)
       print("Price:",self.price)
       print("No. of Pages:",self.no_of_page)
p=python("java script","Brendan Eich",1000,120)
p.display()