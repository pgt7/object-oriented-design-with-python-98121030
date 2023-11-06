# define a class named Fraction
class Fraction:

    # define constructor with 2 parameter : nr, dr=1
    # check dr > 0
    def __init__(self, nr, dr=1) -> None:
        
        if (dr == 0):
            print("Exception : devide by zero")
        elif (dr < 0):
            self.nr = -1 * nr
            self.dr = -1 * dr
        else:
            self.nr = nr
            self.dr = dr

        self.__reduce()

    # define a method named show
    def show(self):
        return "{0}/{1}".format(self.nr, self.dr)

    # override mul function
    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.nr * other.nr, self.dr * other.dr)
        else:
            print("Unsupported operand type. Must be an instance of MyClass.")

    # define hcf based on question
    @staticmethod
    def hcf(x,y):
        x=abs(x)
        y=abs(y)
        smaller = y if x>y else x
        s = smaller
        while s>0:
            if x%s==0 and y%s==0:
                break
            s-=1
        return s
    
    def __reduce(self):
        # call hcf
        s = self.hcf(self.nr, self.dr)

        self.nr /= s
        self.dr /= s


# instanciation
fraction1 = Fraction(12)
fraction2 = Fraction(13, -5)
fraction3 = Fraction(-16, -12)
fraction4 = fraction1 * fraction3

# show them
print("The first fraction = {0}".format(fraction1.show()))
print("The second fraction = {0}".format(fraction2.show()))
print("The third fraction = {0}".format(fraction3.show()))
print("The forth fraction = {0}".format(fraction4.show()))
