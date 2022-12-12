class Patient:

    patient_list = []

    def __init__(self, pid="", name="", disease="", gender="", age=""):
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    def formatPatientInfo(self):
        return f"{self.pid}_{self.name}_{self.disease}_{self.gender}_{self.age}"

    def enterPatientInfo(self):
        self.pid = input("Enter Patient id:\n")
        self.name = input("Enter Patient name:\n")
        self.disease = input("Enter Patient disease\n")
        self.gender = input("Enter Patient gender:\n")
        self.age = input("Enter Patient age:\n")
        data = Patient(self.pid, self.name, self.disease, self.gender, self.age)
        return data.formatPatientInfo()

    def readPatientFile(self):
        f = open("patients.txt", "r")
        lines = f.readlines()
        for line in lines:
            inx = line.split("_")
            patientObject = Patient(inx[0], inx[1], inx[2], inx[3], inx[4])
            self.patient_list.append(patientObject)

    def searchPatientById(self):
        self.pid = input("Enter the Patient ID:\n")
        f = open("patients.txt", "r")
        lines = f.readlines()
        for line in lines:
            inx = line.split("_")
            patientObject = Patient(inx[0], inx[1], inx[2], inx[3], inx[4])
            if self.pid in inx:
                self.patient_list.append(patientObject)
                break
        else:
            print("Can't find the Patient with the same id on the system")

    def displayPatientInfo(self):
        for i in range(len(self.patient_list)):
            print("{:<5}{:<23}{:<16}{:<16}{:<15}".format(self.patient_list[i].pid, self.patient_list[i].name,
                                                         self.patient_list[i].disease, self.patient_list[i].gender,
                                                         self.patient_list[i].age))
        self.patient_list.clear()

    def editPatientInfo(self):
        self.pid = input("Please enter the id of the Patient that you want to edit their information:\n")
        f = open("patients.txt", "r")
        lines = f.readlines()
        for line in lines:
            inx = line.split("_")
            if self.pid in inx:
                self.name = input("Enter new Name:\n")
                self.disease = input("Enter new disease:\n")
                self.gender = input("Enter new gender:\n")
                self.age = input("Enter new age:\n")
                newpatientsObject = line.replace(inx[1], self.name).replace(inx[2], self.disease)\
                    .replace(inx[3], self.gender).replace(inx[4], self.age)

    def displayPatientList(self):
        for i in range(len(self.patient_list)):
            print("{:<5}{:<23}{:<16}{:<16}{:<15}".format(self.patient_list[i].pid, self.patient_list[i].name,
                                                         self.patient_list[i].disease, self.patient_list[i].gender,
                                                         self.patient_list[i].age))
        self.patient_list.clear()

    def writeListOfPatientInfo(self):
        f = open("patients.txt", "w")
        for lines in self.patient_list:
            f.write(lines)

    def addPatientToFile(self):
        f = open("patients.txt", "a")
        f.write("\n" + Patient().enterPatientInfo())
