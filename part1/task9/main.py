# define a class named Course
class Course:

    # define a constructor with title, instructor, price, letures attribute
    def __init__(self, title, instructor, price, lectures):
        self.title = title
        self.instructor = instructor
        self.price = price
        self.lectures = lectures
        self.users = []
        self.ratings = []
        self.avg_rating = None

    def __str__(self) -> str:
        return "Course [\ntitle = {0}, \ninstructor = {1}, \nprice = {2}, \nlectures = {3}\n]".format(self.title, self.instructor, self.price, self.lectures)

    def addNewUser(self, user, rating):
        self.users.append(user)

        self.ratings.append(rating)
        self.avg_rating = sum(self.ratings) / len(self.ratings)

    def showDetails(self):

        user_str = "users = [ " + " ".join(map(str, self.users)) + " ], \n"
        ratings_str = "ratings = [ " + " ".join(map(str, self.ratings)) + " ], \n"

        return self.__str__()[:-1] + user_str + ratings_str + "average rating = " + str(self.avg_rating) + "\n]"


class VideoCourse(Course):
    def __init__(self, title, instructor, price, lectures, length_video):
        super().__init__(title, instructor, price, lectures)
        self.length_video = length_video


class PdfCourse(Course):
    def __init__(self, title, instructor, price, lectures, pages):
        super().__init__(title, instructor, price, lectures)
        self.pages = pages


# instanciation
course1 = Course("python crash course", None, 100000, "Mohammad Ali")
course2 = VideoCourse("java full course", None, 250000, "Koroush", 250)
course3 = PdfCourse("python crash course", None, 50000, "Mohammad Ali", 100)

# add some users
course1.addNewUser("pouria", 12)
course1.addNewUser("hossein", 20)
print(course1)
print("=======================")
print(course1.showDetails())
print("=======================")
print(course2)
print("=======================")
print(course3)
