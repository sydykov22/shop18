class Product:
    __id = 1

    def __init__(self, tittle, desc, price):
        self.id = Product.__id
        self.tittle = tittle
        self.desc = desc
        self.price = price
        Product.__id += 1

class Order:
    def error(self, user):
            print(f"извините {user.name} у вас не достадочно средств")
            print("пополните баланс, или уберите что-то из корзины")
            if input("пополните баланс? (y):") == 'y':
                amount = int(input("Введите сумму: "))
                user.add_bill(amount)
        def __init__(self, user):
            while user.bill < user.cart.get("total_price"):
                
            user.bill -= user.cart.get("total_price")
            print(f"ваш заказ едет по адресу {user.adress}")
            user.show_cart()
            user.clear_cart()
            print(f"у вас не достадочно средств")

class User:
    class Cart: ...

    def __init__(self, name, adress,):
        self.name = name
        self.adress = adress
        self.bill = 0
        self.cart = {"total_price":0}

    def add_bill(self, amount):
        self.bill += amount

    def add_to_cart(self, *products):
        for product in products:
            self.cart[product.id] = {"title": product.title, "price": product.title}
            self.cart["total_price"] += product.price
    
    def remove_from_cart(self, *products):
        for products in products:
            try:
                self.cart.pop(product.id)
                self.cart["total_price"] -= product.price
            except:
                print(f"{product.title} в вашей карзине нет")
    
    def show_cart(self):
        from pprint import pprint
        print(f"===================\n{self.name}")
        pprint(self.cart)
        print("====================")
    
    def clear_cart(self):
        self.cart.clear()
        self.cart['total_price'] = 0

 
ice_cream1 = Product("Магнат", "очень вкусное морожное", 96)
ice_cream2 = Product("Смак", "C кунжутом, тоже вкусное", 15)
plov = Product("Плов", "Узгенский плов  с бараниной", 150)
salatik = Product("Шакарап", "Помидорки", 50)

nurkamila = User("Нуркамила", "Аламедин 1")
nurkamila.add_bill(1000)
nurkamila.add_to_cart(ice_cream1, ice_cream1, ice_cream1)

uluk = User("улук", "тунгуч")
uluk.add_bill(300)
uluk.add_to_cart(ice_cream2, plov)

nurkamila.show_cart()
uluk.show_cart()

nurkamila.remove_from_cart(plov)
nurkamila.show_cart()


