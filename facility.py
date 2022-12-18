#####################################################
# Title: Alberta Hospital (AH) Management System    #
# Author:  Mark Pagarigan                           #
# Version: v1.2                                     #
# Project: Classes Group                            #
#####################################################

class Facility:

    list_facility = []
    def __init__(self, name=""):
        self.name = name 
        
# # Methods
    def addFacility(self):#Adds and writes the facility name to the file
        name = input("Enter Facility name: ")
        self.list_facility.append("\n"+name )
        self.writeListOffacilitiesToFile()
    

    def displayFacilities(self): #Displays the list of facilities
        self.list_facility.clear()
        file = open('facilities.txt', 'r')
        file_content = file.readlines()   
        for eachline in file_content:
            self.list_facility.append(eachline)
        print  ("".join(self.list_facility) + "\n")
        

    def writeListOffacilitiesToFile(self): #writes the facilities list to facilities.txt
        file = open('facilities.txt' , 'w')
        file.write("".join(self.list_facility))
        file.close()

#======================================================
    def facilityMenu(self):
        while True:
            facility_option = self.inputNumber("Facilities Menu:\n1 - Display Facilities list\n2 - Add Facility\n3 - Back to the Main Menu\n\nOption: ")
            if facility_option == 1:
                self.displayFacilities()
            elif facility_option == 2:
                self.addFacility()
            elif facility_option == 3:
                break
            else:
                print("Invalid Input Please choose option 1 - 3\n")
                input("Press any key to continue\n")

            print("\nBack to the prevoius Menu")

    def inputNumber(self,string):
        while True:
            inp = input(string)
            if inp.isnumeric(): 
                inp = int(inp)
                return inp
            else:
                print("\nInvalid input Please use number")
                input("Press any key to continue\n")  