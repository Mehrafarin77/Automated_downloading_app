from bs4 import BeautifulSoup
import requests

counter = 0
url = 'https://www.doostihaa.com/post/1396/12/22/%D8%AF%D8%A7%D9%86%D9%84%D9%88%D8%AF-%D8%B3%D8%B1%DB%8C%D8%A7%D9%84-%D9%82%D9%87%D9%88%D9%87-%D8%AA%D9%84%D8%AE.html'
web_page = requests.get(url).text
soup = BeautifulSoup(web_page, 'lxml')
container = soup.find('div', class_='textkian0')
all_links = container.find_all('a')
with open('Ghahve_Talkh/links.txt', 'w') as f:
    for link in all_links:
        link = link['href']
        if 'files' in link and 'mkv' in link:
            counter += 1
            f.write(f'episode {counter}: {link}\n')


