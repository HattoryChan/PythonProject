#html
import requests
from bs4 import BeautifulSoup
import csv
#diagrams
import pandas as pd
import matplotlib.pyplot as plt

'''
Work alghoritm:
1. How much page?
2. Whats link on product
3. Get Data
'''
distric_list = []
count_list = []

def get_html(url):
    r = requests.get(url)
    return r.text

def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')

    pages = soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-page')[-1].get('href')
    total_pages = pages.split('=')[1].split('&')[0]

    return int(total_pages)    

def write_csv(data):
    with open('avito.csv', 'a',encoding='utf-8') as f:
        writer = csv.writer(f)

        writer.writerow( (data['title'],
                          data['price'],
                          data['address'],
                          data['url']) )

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    ads = soup.find('div', class_='catalog-list').find_all('div', class_='item_table')

    for ad in ads:
        # title, price, adres, url
        
        #title
        try:
            title = ad.find('div', class_='description').find('h3').text.strip()            
        except:
            title = ''            
        #url
        try:
            url = 'https://www.avito.ru' + ad.find('div', class_='description').find('h3').find('a').get('href')
        except:
            url = ''
        #price
        try:
            price = ad.find('div', class_='about').text.strip()
        except:
            price = ''
        #address
        try:
            address = ad.find('div', class_='data').find_all('p')[-1].text.strip()
        except:
            address = ''

        data_diagrams_add(address)
        
        data = { 'title': title,
                 'price': price,
                 'address': address,
                 'url': url}
        write_csv(data)

    
    
    
def data_diagrams_add(address):
    
    if address in distric_list:
        count_list[distric_list.index(address)] += 1 
    else:
        distric_list.append(address)
        count_list.append(1)
     
def create_diagrams():

    df = pd.DataFrame({
        'Distric': distric_list,
        'Count': count_list })
    
    sums = df.Count.groupby(df.Distric).sum()
    #diagrams
    ax1 = plt.subplot(121, aspect = 'equal')    
    df.plot(kind = 'pie', y ='Count',ax=ax1, autopct='%1.1f%%',
            startangle=90, shadow=False, labels= sums.index,
            legend = False, fontsize=14,
            explode = [i/100 for i in range(0, len(count_list))])

    plt.legend(labels=sums.index, loc="best")
    plt.axis('equal')
    '''
    axis('equal');
    pie(sums, labels=sums.index);
    pie.legeng()
    '''
    plt.tight_layout()
    plt.show()
            
         

def main():
    # https://www.avito.ru/chelyabinsk/telefony?p=1&q=iphone
    phone_name = 'iphone'
    url = 'https://www.avito.ru/chelyabinsk/telefony?p=1&q=i' + phone_name
    base_url = "https://www.avito.ru/chelyabinsk/telefony?"
    page_part = 'p='
    query_part = '&q=iphone'

         
    total_pages = get_total_pages(get_html(url))    
    
    for i in range(1, 2):
        url_gen = base_url + page_part + str(i) + query_part
        
        html = get_html(url_gen)
        
        get_page_data(html)
        

    create_diagrams()

if __name__ == '__main__':
    main()
