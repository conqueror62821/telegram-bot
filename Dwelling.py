class Dwelling():
    def __init__(self,title,description,stars,price,price_discount=None):
        self.title = title
        self.description = description
        self.stars = stars
        self.price = price
        self.price_discount = price_discount

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self,title):
        self.__title = title

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self,description):
        self.__description = description

    @property
    def stars(self):
        return self.__stars

    @stars.setter
    def stars(self,stars):
        if stars != 'Nuevo' and stars != None:
            start_index = stars.find("(")
            end_index = stars.find(")")
            content = stars[start_index + 1 : end_index]
            self.reviews = content
            self.__stars = float(stars.replace('(','').replace(')','').replace(content,'').strip())
        else: 
            self.reviews,self.__stars = 0,float(0)

    @property
    def reviews(self):
        return self.__reviews

    @reviews.setter
    def reviews(self,reviews):
        self.__reviews = reviews

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,price):
        self.__price = None        
        if not price: return
        string = price.replace('$','').replace(',','').replace('CLP','').strip()
        if not string.isnumeric(): raise ValueError('El valor debe ser un número válido.')
        self.__price = int(string)


    @property
    def price_discount(self):
        return self.__price_discount

    @price_discount.setter
    def price_discount(self,price_discount):
        self.__price_discount = None        
        if not price_discount: return
        string = price_discount.replace('$','').replace(',','').replace('CLP','').strip()
        if not string.isnumeric(): raise ValueError('El valor debe ser un número válido.')
        self.__price_discount = int(string)


    def __str__(self) -> str:
        return f'Title {self.title} - Price {self.price}'


if __name__ == '__main__':
    x = Dwelling(0,0,'Nuevo',0,'1')
    print(x.stars)
    print(x.reviews)