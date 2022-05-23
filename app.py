# Web scraping .
import requests 
from bs4 import BeautifulSoup
 
response = requests.get('https://stackoverflow.com/questions')
soup= BeautifulSoup(response.text, 'html.parser') 

questions = soup.select('.s-post-summary')


for question in questions:
    print(question.select_one('.s-link').text) 
    print('Votes:',question.select_one('.s-post-summary--stats-item-number').text,'\n')

