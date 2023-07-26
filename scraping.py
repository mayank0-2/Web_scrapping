import requests
from bs4 import BeautifulSoup

file = open('data.html','w')
Base_url = "https://www.amazon.in"
url_extension = '/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1'

head = { 
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.0.0'
}

no_of_pages = 20

product_data = []

for _ in range(0, no_of_pages) :
    try :
        url = Base_url + url_extension
        page = requests.get(url, headers= head)
        soup = BeautifulSoup(page.content, 'html.parser')
        if page.status_code == 200 :
            # file.write(page.text)
            # print(page.text)
            product = soup.find_all('span')
            # file.write(str(product))
            # print(product['href'])
            for container in product:
                try :
                    product_link = container.find('a', {"class": "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"}, href = True)
                    # product_name = container.find('span', {"class" : "a-size-medium a-color-base a-text-normal"}).text
                    product_price = container.find('span', {'class': 'a-price-whole'}).text
                    product_rating = container.find('span', {'class': 'a-icon-alt'}).text
                    number_of_reviews = container.find('span', {'class': 'a-size-base s-underline-text'}).text
                    product_data.append({
                                            'link':Base_url + product_link['href'],
                                            'name': product_name,
                                            'price': product_price,
                                            'rating' : product_rating,
                                            'no_of_review': number_of_reviews,
                                            'description': None,
                                            'asin' : None,
                                            'manufacturer': None,
                })
                except :
                    pass
            
            print(product_data)
        else :
            print("status code error")
        
        # next_page = soup.find('a', {"class":"s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"}, href = True)
        # url_extension = next_page['href']
        
        
    except :
        print('Runnng except value')
    
# code for part 2 of the assignment section   

for i in product_data :
    # print('running product iterations')
    # print (i['link'])
    url = i['link']
    page = requests.get(url, headers=head)
    soup = BeautifulSoup(page.content, 'html.parser')
    product_description = soup.find_all('li', {'class': 'a-list-item'})
    product_descriptions = [tag.string for tag in product_description]
    print(product_descriptions)
    i['description'] = product_descriptions.text