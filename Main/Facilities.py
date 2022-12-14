class facilities:
    def __init__(self, facilityName):
        self.facilityName = facilityName

    def addFacility(self):
        self.facilityName = input("what is the name of this new facility?")

        return self.facilityName

    def writeListOffacilitiesToFile(self):
        with open("Project_Data/files/facilities.txt", "a") as f:
            f.write("\n")
        with open("Project_Data/files/facilities.txt", "a") as f:
            f.write(self.facilityName)
            

    def displayFacilities(self):
        facilitiesList = open("Project_Data/files/facilities.txt").read().splitlines()
        for x in facilitiesList:
            print(x)



