class Facility:

    facilities_list = []

    def __init__(self, facility=""):
        self.facility = facility

    def addFacility(self):
        self.facility = input("Enter Facility name:\n")
        file = open("facilities.txt", "a")
        file.write("\n" + self.facility)

    def displayFacilities(self):
        file = open("facilities.txt", "r")
        lines = file.readlines()
        for line in lines:
            self.facilities_list.append(line)
            print(line)

    def writeLisstOffacilitiesToFile(self):
        file = open("facilities.txt", "w")
        for lines in self.facilities_list:
            file.write(lines)



