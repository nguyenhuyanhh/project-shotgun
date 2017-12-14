import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.facebook.com/bobbibrown.sg/")
soup = BeautifulSoup(page.content, 'html.parser')

#Gets all the posts in the page:

divs = soup.find_all('div', class_="_5pcr fbUserStory")
for div in divs:
    print(div)

# TASK: Create a code thats prints each the post's status and all other useful information in the post in a manner similar to the original facebook page (separate each post with a newline) 
# Website: https://www.facebook.com/bobbibrown.sg/



