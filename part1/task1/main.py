# define libs
import math
import re

# define a class for Distance in 2D
class Distance:

    # define a constructor to get parameter x1, y1, x2, y2
    def __init__(self, point1, point2):

        self.__point1 = point1
        self.__point2 = point2

    # define a method to caculate Distance in 2D
    def __euclideanDistance(self):

        x1, y1 = self.__point1
        x2, y2 = self.__point2

        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return distance

    # define a print method 
    def __str__(self):
        return "point1 = ({0})\npoint2 = ({1})\ndistance = {2}".format(self.__point1, self.__point2, self.__euclideanDistance())


# instanciation
while(True):
    option = 0
    print("\n1.Run the application\n2.Exit\n")

    option = int(input("Enter your option: "))

    if (option == 1):

        input_point1 = input("Enter point 1 ('x1, y1'): ")
        input_point2 = input("Enter point 2 ('x2, y2'): ")

        pattern = re.compile(r'[,\s]+')
        x1, y1 = map(float, re.split(pattern, input_point1))
        x2, y2 = map(float, re.split(pattern, input_point2))

        obj = Distance((x1, y1), (x2, y2))
        print(obj)
    else:
        break