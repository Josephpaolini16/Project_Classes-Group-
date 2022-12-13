# This class will show you the laboratory and their cost depending on what Lab number you are in
class Laboratory:

    laboratory_list = []

    def __init__(self, facility="", cost=""):
        self.facility = facility
        self.cost = cost

    def addLabToFile(self):
        f = open("laboratories.txt", "a")
        f.write("\n" + Laboratory().enterLaboratoryInfo())

    def writeListOfLabsToFile(self):
        f = open("laboratories.txt", "w")
        for lines in self.laboratory_list:
            f.write(lines)
# Display laboratories with their number and costing
    def displayLabsList(self):
        for i in range(len(self.laboratory_list)):
            print("{:<15}{:<15}".format(self.laboratory_list[i].facility, self.laboratory_list[i].cost))

    def formatLabInfo(self):
        return f"{self.facility}_{self.cost}"
# The system will ask you to enter the Laboratory facility and its cost.
    def enterLaboratoryInfo(self):
        self.facility = input("Enter Laboratory facility:\n")
        self.cost = input("Enter Laboratory cost:\n")
        data = Laboratory(self.facility, self.cost)
        return data.formatLabInfo()

    def readLaboratoriesFile(self):
        f = open("laboratories.txt", "r")
        lines = f.readlines()
        for line in lines:
            inx = line.split("_")
            laboratoryObject = Laboratory(inx[0], inx[1])
            self.laboratory_list.append(laboratoryObject)