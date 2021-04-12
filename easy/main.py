class Info:
    def __init__(self):
        self.name = input("Enter your Name: ")
        self.age = input("Enter your Age: ")

    def printMyInfo(self):
        print("Hello " + self.name + "\nToday you are " + self.age)


if __name__ == '__main__':
    user = Info()
    user.printMyInfo()
