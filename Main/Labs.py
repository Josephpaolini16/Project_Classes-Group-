class labs:
    def __init__(self, labName, cost):
        self.labName = labName
        self.cost = cost

    def enterLabInfo(self):
        self.labname = input("enter lab name: ")
        self.cost = input("enter cost: ")

        
    def formatLabInfo(self):
        self.formated = str(self.labname) + "_" + str(self.cost)
        return self.formated
        
    def readLabFile(self):
        self.labFile = open("Project_Data/files/laboratories.txt").read().splitlines()
        return self.labFile
    def addLabToFile(self):
        with open("Project_Data/files/laboratories.txt", "a") as f:
            f.write("\n")
        with open("Project_Data/files/laboratories.txt", "a") as f:
            f.write(self.formated)

    def writeListOflabsToFile(self):
        with open("Project_Data/files/laboratories.txt", "w") as f:
            f.write(self.labFile)
            

    def displayLabs(self):
        
        text = "{name:<30}{cost:30}"
        for x in self.labFile:
            split = x.split("_")
            self.labName = split[0]
            self.cost = split[1]
            print(text.format(name=self.labName,cost=self.cost))
        


