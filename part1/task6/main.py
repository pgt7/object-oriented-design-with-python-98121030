# define a class named SalesPerson
class SalesPerson:
    total_revenue = 0
    names = []

    # define a constructor that has name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sales_amount = 0
        self.addNewName(name)

    def makeSale(self, amount):
        self.sales_amount = amount
        self.calTotalRevenue(amount)

    def show(self):
        print(self.name, self.age, self.sales_amount)

    @classmethod
    def addNewName(cls, name):
        cls.names.append(name)

    @classmethod
    def calTotalRevenue(cls, amount):
        cls.total_revenue += amount


# instanciation
s1 = SalesPerson('Bob', 25)
s2 = SalesPerson('Ted', 22)
s3 = SalesPerson('Jack', 27)

s1.makeSale(1000)
s1.makeSale(1200)
s2.makeSale(5000)
s3.makeSale(3000)
s3.makeSale(8000)

s1.show()
s2.show()
s3.show()

print("Total Revenue: ", SalesPerson.total_revenue)
print("Names: ", SalesPerson.names)