import requests
from bs4 import BeautifulSoup
def parse():
    page = requests.get('https://www.omgtu.ru/general_information/faculties/',verify= False)
    print(page.status_code)
    page_parsed = BeautifulSoup(page.text, 'html.parser')
    cafedra = page_parsed.findAll('div', id='pagecontent')

    with open('result1.txt', 'w') as f:
        for caf in cafedra:
            f.write(caf.text)
if __name__ == '__main__':
    parse()