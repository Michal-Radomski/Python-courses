import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
res = requests.get(url)

# print(res)  # Response 200 means everything is good
# print(res.text)
# this will have the entire html data in it. Exactly the same thing which we get when we click 'View Page Source'

soup = BeautifulSoup(res.text, "html.parser")

# print(soup)
# this will also have the exact same thing as res.text, but it will keep in html format, and not in string format,
# and it will be easier to manipulate it

# print(soup.body)
# print(
#     soup.body.contents
# )  # result comes in a 'list' in this case. But not with the previous cases.

# print(soup.find_all("div"))
# print(soup.find_all("a"))  # find all the 'a' tags - all the links
# print(soup.title)
# print(soup.a)  # it finds the first a tag
# print(soup.find("a"))  # it finds the first a tag

# print(soup.find(id="score_24273602"))
# print(soup.select("#score_24273602"))  # outputs in a list
# select grabs the data using a CSS selector, where '.' means 'class', '#' means 'id', etc.

# print(soup.select("a")[0])
# grabs all the 'a' tags, and print only the first one, as this is a list, and we want the 0th item

print(soup.select(".score")[0])  # grabs all the class="score" tags
