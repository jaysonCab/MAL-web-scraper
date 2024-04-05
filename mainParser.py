import requests, sqlite3
from bs4 import BeautifulSoup

  #Setup connection to database
connect = sqlite3.connect("animeDatabase.db")
c = connect.cursor()

  #Creates table ---- Comment out at all times
# c.execute("""CREATE TABLE anime (
#           title text,
#           ranking real,
#           genre text
#           )""")

  #Variables used to compare anime
animeTitle = ""
animeScore = 0.0
animeGenre = []

  #User enters the URL of a MAL website to be parsed and entered into the database
urlPrompt = input("Enter the MAL URL: ")

  #Obtains the HTML code of the website entered in the prompt
requestURL = requests.get(urlPrompt)

  #Saves content of HTML into document
document = BeautifulSoup(requestURL.content, "lxml")

  #Grabs title of anime
# titleDocument = document.title
# animeTitle = titleDocument.prettify()[9:-28]

animeTitle = str(document.find_all(class_="title-name h1_bold_none")[0])[44:-14]

  #Grabs score of anime
scoreDocument = str(document.find_all(itemprop="ratingValue")[0])
animeScore = float(scoreDocument[-11:-7])

  #Grabs genre of anime
genreDocument = list(document.find_all(itemprop="genre"))

for i in range(len(genreDocument)):
  animeGenre.append((str(genreDocument[i])[45:-7]))

  #Lists cant be stored in database
animeGenre = str(animeGenre)

  #Inserts scraped values into animeDatabase.db if it doesn't exist in file
try:
  #Exists in database
  nameComparator = c.execute('SELECT title FROM anime WHERE title = ?', (animeTitle,)).fetchall()[0]
  if animeTitle in nameComparator:
    print("The anime is already in the database!")
except:
  #Does not exist in database
  with connect:
    c.execute("INSERT INTO anime VALUES (:title, :ranking, :genre)", {'title': animeTitle, 'ranking': animeScore, 'genre': animeGenre})
  print("The anime has been added to the database!")
