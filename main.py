from bs4 import BeautifulSoup
import requests
import time
from Dwelling import Dwelling

class AirbnbScrapper():
    BASE_URL = 'https://www.airbnb.cl/s'
    BASE_URL_DETAIL = 'https://www.airbnb.cl'

    def __init__(self, location,min_beds=None,min_bathrooms=None,min_bedrooms=None,price_min=None,price_max=None):
        self.location:str = location
        self.__current_endpoint:str = self._user_custom_url()
        self.__size:int = 1
        self.__dwellings:list[Dwelling] = []
    # Filtro tipo de propiedad
    # l2_property_type_ids[]=1&l2_property_type_ids[]=3&l2_property_type_ids[]=2&l2_property_type_ids[]=4

    # Filtro servicios
    # amenities[]=4&amenities[]=9&amenities[]=7&amenities[]=8&amenities[]=33&amenities[]=46
    @property
    def location(self):
        return self.__location
    
    @property
    def dwellings(self):
        return self.__dwellings
    
    @location.setter
    def location(self,location):
        if not location: raise ValueError('La ubicacion no puede ser nula.') 
        self.__location = location

    def _verify_response(self,response)  -> bool:
        return response.status_code == 200

    def _next_page(self): 
        response = {'response':False,'url' : ''}
        disabled = self.__html.find('button',class_=['l1j9v1wn','c1ytbx3a','dir','dir-ltr'],attrs={'aria-label':'Siguiente','aria-disabled':'true'})
        if disabled: return response
        link = self.__html.find('a',class_=['l1j9v1wn','c1ytbx3a','dir','dir-ltr'], attrs={'aria-label':'Siguiente'})
        response.update({'response' : True,'url' : link['href'][2:]})
        self.__size+=1
        return response
    
    def _user_custom_url(self):
        return f'{self.BASE_URL}/{self.location}--Chile/homes'

    def _set_request(self):
        # Avoid making too many requests in a short time
        time.sleep(2)
        response = requests.get(self.__current_endpoint)
        if not self._verify_response(response): raise ValueError('Error con el servicio de Airbnb.')
        self.__html = BeautifulSoup(response.content, "html.parser")

    def _get_dwelling_cards(self):
        return self.__html.find_all('div',class_=['cy5jw6o','dir','dir-ltr'], attrs={'data-testid':'card-container'})

    def _get_price(self,container):
        
        span_tag = container.find('span',class_='_tyxjp1')
        data = {}
        if span_tag:
            # Only price
            price = span_tag.text
        else:
            price = container.find('span',class_='_1y74zjx').text
            discount = container.find('span',class_='_1ks8cgb').text
            data.update({'price_discount':discount})
        data.update({'price':price})
        return data


    def _get_value_or_none(self,element):
        return element.text if element else None


    def _get_dwelling_info(self,container) -> Dwelling:
        # Title
        title = self._get_value_or_none(container.find('div',class_=['t1jojoys','dir','dir-ltr'], attrs={'data-testid': 'listing-card-title'}))
        # Basic Description
        description = self._get_value_or_none(container.find('span',class_=['t6mzqp7','dir','dir-ltr'], attrs={'data-testid': 'listing-card-name'}))
        # Stars
        stars = self._get_value_or_none(container.find('span',class_=['r1dxllyb','dir','dir-ltr'], attrs={'aria-hidden': 'true'}))
        # Url link
        url = '{}{}'.format(self.BASE_URL_DETAIL,container.find('a',class_=['l1j9v1wn','bn2bl2p','dir','dir-ltr'])['href']) 
        # Price
        price_container = container.find('div',class_=['pquyp1l','dir','dir-ltr'])
        price_dict = self._get_price(price_container)
        data = {'title':title,'description':description,'stars':stars,'url':url}
        data.update(price_dict)
        return Dwelling(**data) 

    def _pagination(self):
        next_page = self._next_page()
        if not next_page.get('response') : return print('Se recorrieron todas las paginas.')
        # Siguiente pagina 
        # Recursiva
        url = next_page.get('url')
        self.__current_endpoint = f'{self.BASE_URL}{url}'
        self.search()
    
    def search(self): 
        self._set_request()
        for container in self._get_dwelling_cards():
            dwelling = self._get_dwelling_info(container)
            self.__dwellings.append(dwelling.to_dict())
        self._pagination()

    def get_number_pages(self):
        print(f'Nro total de paginas consultadas {self.__size}')


if __name__ == '__main__':
    x = AirbnbScrapper('Santiago')
    x.search()
    import pandas as pd
    df = pd.DataFrame(x.dwellings)
    stars_reviews_filter = (df['stars'] >= 3) & (df['reviews'] >= 10)
    top_10 = df.loc[stars_reviews_filter].nlargest(10,'price')
    print(top_10)
    # Export to csv
    df.to_csv('total_dwelling.csv')
    top_10.to_csv('top_10.csv')
