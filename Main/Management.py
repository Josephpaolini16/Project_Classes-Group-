# Group 13
# Jean Pascua
# Justine Barredo
# Joe Paolini
# This Alberta Health Management System demonstrate the system inside a particular Hospital.
# With the help of this system, the management can see the Doctor's information along with their availability.
# It allows the management to add, edit, and search Doctors, Facilities, Laboratory, and Patients.
# The system has the ability to calculate the cost of your medical expenses.
# Only the management or authorized personnels can utilize the system because of its features.

# Classes
from Doctor import Doctor
from Facilities import facilities 
from Labs import labs   
from Patient import Patient

#  Display the categories, you can choose and access any of these categories by calling their respective classes and methods
class Management:

    def DisplayMenu(self):
        while True:
            menu_input = input("Welcome to Alberta Hospital (AH) Management system\n"
                         "Select from the following options, or select 0 to stop:\n"
                         "1 - 	Doctors\n"
                         "2 - 	Facilities\n"
                         "3 - 	Laboratories\n"
                         "4 - 	Patients\n>")
# Class named "Doctor" will be call on this condition
            if menu_input == "1":
                while True:
                    doc_input = input("Doctors Menu: \n"
                                "1 - Display Doctors list\n"
                                "2 - Search for doctor by ID\n"
                                "3 - Search for doctor by name\n"
                                "4 - Add doctor\n"
                                "5 - Edit doctor info\n"
                                "6 - Back to the Main Menu\n>")
                    if doc_input == "1":
                        Doctor().readDoctorsFile()
                        Doctor().displayDoctorsList()
                        print("\nBack to the previous Menu\n")
                    elif doc_input == "2":
                        Doctor().searchDoctorById()
                        Doctor().displayDoctorInfo()
                        print("\nBack to the previous Menu\n")
                    elif doc_input == "3":
                        Doctor().searchDoctorByName()
                        Doctor().displayDoctorInfo()
                        print("\nBack to the previous Menu\n")
                    elif doc_input == "4":
                        Doctor().addDrToFile()
                        print("\nBack to the previous Menu\n")
                    elif doc_input == "5":
                        Doctor().editDoctorInfo()
                        print("\nBack to the previous Menu\n")
                    else:
                        Management().DisplayMenu()
# Class named "Facility" will be call on this condition
            elif menu_input == "2":
                while True:
                    fac = facilities("pat")
                    fac_input = input("Facilities Menu: \n"
                                "1 - Display Facilities list\n"
                                "2 - Add Facility\n"
                                "3 - Back to Main Menu\n>")
                    if fac_input == "1":
                        fac.displayFacilities()
                        print("\nBack to the previous Menu\n")
                    elif fac_input == "2":
                        fac.addFacility()
                        fac.writeListOffacilitiesToFile()
                        print("\nBack to the previous Menu\n")
                    else:
                        Management().DisplayMenu()
#  Class named "Lab" will be call on this condition
            elif menu_input == "3":
                while True:
                    lab = labs(1, 1)
                    lab_input = input("Laboratories Menu\n"
                                "1 - Display laboratories list\n"
                                "2 - Add laboratory\n"
                                "3 - Back to the Main Menu\n>")
                    if lab_input == "1":
                        lab.readLabFile()
                        lab.displayLabs()
                        print("\nBack to the previous Menu\n")
                    elif lab_input == "2":
                        lab.enterLabInfo()
                        lab.formatLabInfo()
                        lab.addLabToFile()
                        print("\nBack to the previous Menu\n")
                    else:
                        Management().DisplayMenu()
#  Class named "Patient" will be call on this condition
            elif menu_input == "4":
                while True:
                    pat_input = input("Patients Menu:\n"
                                "1 - Display patients list\n"
                                "2 - Search for patient by ID\n"
                                "3 - Add patient\n"
                                "4 - Edit patient info\n"
                                "5 - Back to the Main Menu\n>")
                    if pat_input == "1":
                        Patient().readPatientFile()
                        Patient().displayPatientList()
                        print("\nBack to the previous Menu\n")
                    elif pat_input == "2":
                        Patient().searchPatientById()
                        Patient().displayPatientInfo()
                        print("\nBack to the previous Menu\n")
                    elif pat_input == "3":
                        Patient().addPatientToFile()
                        print("\nBack to the previous Menu\n")
                    elif pat_input == "4":
                        Patient().editPatientInfo()
                        print("\nBack to the previous Menu\n")
                    else:
                        Management().DisplayMenu()
            elif menu_input == "0":
                exit()


Management().DisplayMenu()