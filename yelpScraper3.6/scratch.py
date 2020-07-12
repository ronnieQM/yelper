from bs4 import BeautifulSoup
import requests

url = 'https://www.redfin.com/zipcode/92801'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
page_response = requests.get(url, headers, timeout=10)

soup = BeautifulSoup(page_response.content, "html.parser")


phoneWWW = soup.find_all('p', attrs={"class": phoneNum0})
all_map_home_cards = soup.find_all('div', attrs={'class': 'homecardv2'})

