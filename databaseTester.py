import requests, sqlite3
from bs4 import BeautifulSoup

  #Setup connection to database
connect = sqlite3.connect("animeDatabase.db")
c = connect.cursor()


c.execute("SELECT * FROM anime")
print(c.fetchall())

connect.commit()
connect.close()



# c.execute("INSERT INTO anime VALUES ('Nisekoi', '6.12', 'Romance')")
# connect.commit()


# nameComparator = c.execute('SELECT title FROM anime WHERE title = ?', (animeTitle,)).fetchall()[0]






# animeTitle = "abc"
# try:
#   nameComparator = c.execute('SELECT title FROM anime WHERE title = ?', (animeTitle,)).fetchall()[0]
# except:
#   print("Not in Database")
# try:
#   print(nameComparator)
#   print(animeTitle)

#   if animeTitle in nameComparator:
#     print("Yes its in!")
#   else:
#     print("Not in")
# except:
#   print("Not in Database!")








# if c.fetchone() is None:


# if c.execute('SELECT title FROM anime WHERE title = ?', (animeTitle,)).fetchall() is None:
#   print("The anime has been added to the database!")
# else:
#   #E
#   print("Already exists in database!")


# if nameComparator == animeTitle:
#   print("Already exists in Table!")
# else: 
#   with connect:
#     c.execute("INSERT INTO anime VALUES ('444', '4444', 'aaaas')")
#     print("The anime has been added to the database!")
  



# if c.fetchone() == animeTitle:
#   #DNE
#   with connect:
#     c.execute("INSERT INTO anime VALUES ('444', '4444', 'aaaas')")
#     print("The anime has been added to the database!")
# else:
#   #E
#   print("Already exists in database!")



# Delet
# with connect:
#   c.execute("DELETE from anime WHERE rowid=1")
#   c.execute("DELETE from anime WHERE rowid=2")
#   c.execute("DELETE from anime WHERE rowid=3")
#   c.execute("DELETE from anime WHERE rowid=4")


# c.execute("SELECT rowid, * FROM anime")
# print(c.fetchall())
# r = 'ROMANCE'

# c.execute("SELECT * from anime where genre like '%" + str(r) + "%'")


# print(c.fetchall()[1][2][2:20])




# for i in range(len(c.fetchall())):
#   print(c.fetchall())

# print(c.fetchall())



# with connect:
#   c.execute("DELETE from anime WHERE rowid=1")
# 


