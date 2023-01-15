
a = """Shoe = 50€
Jacket = 75€
Phone  = 200€
Beans  = 100€
Book   = 30€
"""
print(a)


class Goods:

    def __init__(self, goods, price) -> None:
        self.goods = goods
        self.price = price



x = ["shoe", "jacket", "phone", "beans", "book"]
commodity = [
    Goods(x[0], 50),
    Goods(x[1], 75),
    Goods(x[2], 200),
    Goods(x[3], 100),
    Goods(x[4], 30)

]

def run_test(commodity):
    for i in commodity:
        name_of_goods = input("Name of goods: ")
        quantity = int(input("Quantity: "))
        if name_of_goods.lower() in i.goods:
            print(str(quantity) + " piece(s) of " + name_of_goods + ": " + str(quantity * i.price) + "€")
            quit()
        else:
            print("Not Available")
            quit()


run_test(commodity)
