import sys
import re
import unicodedata
reload(sys)
sys.setdefaultencoding('utf8')
from bs4 import BeautifulSoup
import requests

links=[]

for k in range(5000):
    number=4155+k
    tmp="https://www.imdb.com/title/tt011"+str(number)+"/reviews"
    links.append(tmp)
 
#use this to remove links ^.*https.*$\n 
for i in range(len(links)):
    #print(links[i])
    page = requests.get(links[i])

    beausoup = BeautifulSoup(page.content,"html.parser")
    for data in beausoup.find_all(class_="review-container"):
        review_text = data.find(class_="text").text
        try:
            rating_number = data.find(class_="point-scale").previous_sibling.text
        except:
            rating_number = ""
        word_count=len(review_text.split(" "))
        if rating_number!="" and word_count>49 and word_count<251:
            print("{}\t{}\n".format(rating_number,review_text))
