#####################################################
# Title: Alberta Hospital (AH) Management System    #
# Author: Mark Pagarigan                            #
# Version: v1.2                                     #
# Project: Classes Group                            #
#####################################################

import doctor
import facility
import laboratory
import patient


class Management:
    #only access number
    def inputNum(self,string):
        while True:
            inp = input(string)
            if inp.isnumeric(): 
                inp = int(inp)
                return inp
            else:
                print("\nInvalid input Please use number")
                input("Press any key to continue\n")


    def DisplayMenu (self):
        while True:
            menu_option = self.inputNum('''\nWelcome to Alberta Hospital (AH) Managment system 
Select from the following options, or select 0 to stop: 
1 - 	Doctors
2 - 	Facilities
3 - 	Laboratories
4 - 	Patients 

Option: ''')
            
            if menu_option == 1:
                doctor.Doctor().docMainMenu()
            elif menu_option == 2:
                facility.Facility().facilityMenu()
            elif menu_option == 3:
                laboratory.Lab().labMenu()
            elif menu_option == 4:
                patient.Patient().patientMenu()
            elif menu_option == 0:
                break
            else:
                print("Invalid Input Please choose option 1 - 4 or 0 to exit\n")
                input("Press any key to continue\n")

    #----------------------------------
  
obj_mgmt = Management()
obj_mgmt.DisplayMenu()

 




