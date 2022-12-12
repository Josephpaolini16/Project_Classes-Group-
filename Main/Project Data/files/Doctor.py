class Doctor:

    doctors_list = []

    def __init__(self, id="", name="", specialist="", timing="", qualification="", roomNb=""):
        self.id = id
        self.name = name
        self.specialist = specialist
        self.timing = timing
        self.qualification = qualification
        self.roomNb = roomNb

    def formatDrInfo(self):
        return f"{self.id}_{self.name}_{self.specialist}_{self.timing}_{self.qualification}_{self.roomNb}"

    def enterDrInfo(self):
        self.id = input("Enter the doctor's ID:\n")
        self.name = input("Enter the doctor's name:\n")
        self.specialist = input("Enter the doctor's speciality:\n")
        self.timing = input("Enter the doctor's timing (e.g., 7am-10pm):\n")
        self.qualification = input("Enter the doctor's qualification:\n")
        self.roomNb = input("Enter the doctor's room number:\n")
        data = Doctor(self.id, self.name, self.specialist, self.timing, self.qualification, self.roomNb)
        return data.formatDrInfo()

    def readDoctorsFile(self):
        f = open("doctors.txt", "r")
        lines = f.readlines()
        for line in lines:
            inx = line.split("_")
            doctorsObject = Doctor(inx[0], inx[1], inx[2], inx[3], inx[4], inx[5])
            self.doctors_list.append(doctorsObject)

    def searchDoctorById(self):
        self.id = input("Enter the doctor id:\n")
        f = open("doctors.txt", "r")
        lines = f.readlines()
        for line in lines:
            inx = line.split("_")
            doctorsObject = Doctor(inx[0], inx[1], inx[2], inx[3], inx[4], inx[5])
            if self.id in inx:
                self.doctors_list.append(doctorsObject)
                break
        else:
            print("Can't find the doctor with the same ID on the system")

    def searchDoctorByName(self):
        self.name = input("Enter the doctor name:\n")
        f = open("doctors.txt", "r")
        lines = f.readlines()
        for line in lines:
            inx = line.split("_")
            doctorsObject = Doctor(inx[0], inx[1], inx[2], inx[3], inx[4], inx[5])
            if self.name in inx:
                self.doctors_list.append(doctorsObject)
                break
        else:
            print("Can't find the doctor with same name on the system")

    def displayDoctorInfo(self):
        for i in range(len(self.doctors_list)):
            print("Id   Name                   Speciality      Timing          Qualification   Room Number\n")
            print("{:<4} {:<22} {:<15} {:<15} {:<15} {:<15}".format(self.doctors_list[i].id, self.doctors_list[i].name,
                                                                    self.doctors_list[i].specialist,
                                                                    self.doctors_list[i].timing,
                                                                    self.doctors_list[i].qualification,
                                                                    self.doctors_list[i].roomNb))
        self.doctors_list.clear()

    def editDoctorInfo(self):
        self.id = input("Please enter the id of the doctor that you want to edit their information:\n")
        f = open("doctors.txt", "r")
        lines = f.readlines()
        for line in lines:
            inx = line.split("_")
            if self.id in inx:
                self.name = input("Enter new Name:\n")
                self.specialist = input("Enter new Specialist in:\n")
                self.timing = input("Enter new Timing:\n")
                self.qualification = input("Enter new Qualification:\n")
                self.roomNb = input("Enter new Room number\n")
                newdoctorsObject = line.replace(inx[1], self.name).replace(inx[2], self.specialist)\
                    .replace(inx[3], self.timing).replace(inx[4], self.qualification).replace(inx[5], self.roomNb)

    def displayDoctorsList(self):
        print("Id   Name                   Speciality      Timing          Qualification   Room Number\n")
        for i in range(1, len(self.doctors_list)):
            print("{:<4} {:<22} {:<15} {:<15} {:<15} {:<15}".format(self.doctors_list[i].id, self.doctors_list[i].name,
                                                                    self.doctors_list[i].specialist,
                                                                    self.doctors_list[i].timing,
                                                                    self.doctors_list[i].qualification,
                                                                    self.doctors_list[i].roomNb))
        self.doctors_list.clear()

    def writeListOfDoctorsToFile(self):
        f = open("doctors.txt", "w")
        for lines in self.doctors_list:
            f.write(lines)

    def addDrToFile(self):
        f = open("doctors.txt", "a")
        f.write("\n" + Doctor().enterDrInfo())
