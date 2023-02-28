import requests
from bs4 import BeautifulSoup

#all pages from toscrape.com
res = requests.get('http://books.toscrape.com/')
res.status_code
soup = BeautifulSoup(res.text, 'lxml')

#select divs from the soup for example 
div = soup.select('div')

#objective: scrape all the books with two stars from all pages
base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
#base_url is the url format for the pages

#properly scrape one page and apply to the rest
res = requests.get(base_url.format(1))

#create a soup of the first page for example
soup= BeautifulSoup(res.text, 'lxml')

#confirm the number of products per page to test code
print(len(soup.select('.product_pod')))

product = soup.select('.product_pod')
example = product[0]
example.select('.star-rating.three')

#grabbing the book title from the page
title = example.select('a')[1]['title']

two_star_titles = [] #books with two star ratings

#toscrape range is 50 pages
for n in range(1, 51):
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    
    soup = BeautifulSoup(res.text, 'lxml')
    books = soup.select('.product_pod')
    for book in books:
        if len(book.select('.star-rating.Two')) != 0: # or if 'star rating Two' in book.select('.star-rating.Two')
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)


print(two_star_titles, len(two_star_titles))
