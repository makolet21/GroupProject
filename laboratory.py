#####################################################
# Title: Alberta Hospital (AH) Management System    #
# Author: Kevin Waje                                #
# Modified by: Mark Pagarigan                       #
# Version: v1.2                                     #
# Project: Classes Group                            #
#####################################################


class Lab:

    lab_list = []
    new_lab_list = []
    #constructor
    def __init__(item, facility_name = "" , cost=0):
        item.facility_name = facility_name
        item.cost = cost

    #getters
    def get_facility_name(item):
        return item.facility_name

    def get_cost(item):
        return item.cost

    #setters
    def set_facility_name(item, facility_name):
        item.facility_name = facility_name

    def set_cost(item, cost):
        item.cost = cost

  #================================================  
   #Adds and writes the lab name to the file in the format of the data that is in the file
    def addtolabFile(item):
        item.new_lab_list.append(item.enterLaboratoryInfo() )
        item.writeListOfLabsToFile()
        
    # Writes the list of labs into the file laboratories.txt
    def writeListOfLabsToFile(item):
        myfile = open("laboratories.txt", 'w')
        for index in range(len(item.new_lab_list)):
            myfile.write(item.formatLabInfo(item.new_lab_list[index]))
        myfile.close()

    #Displays the list of laboratories
    def displayLabsList(item):
        for index in range(len(item.new_lab_list)):
            print(f' {item.new_lab_list[index].facility_name} \t\t {item.new_lab_list[index].cost}')

    #Formats the Laboratory object similar to the laboratories.txt file
    def formatLabInfo(item,obj):
        return (" ".join(str(obj).split()).replace(" ","_")+"\n")

    #Asks the user to enter lab name and cost and forms a Laboratory object
    def enterLaboratoryInfo(item):
        facility_name = input("Enter Facility Name: ")
        cost = float(input("Enter Facility Cost: "))
        lab_obj = Lab(facility_name, cost)
        return lab_obj

    #Reads the laboratories.txt file and fills its contents in a list of Laboratory objects
    def readLaboratoriesFile(item):
        myfile = open("laboratories.txt", 'r')
        file_content = myfile.readlines()

        for eachline in file_content:
            item.lab_list = eachline.rstrip().split("_")
            lab = Lab(item.lab_list[0],item.lab_list[1])

            # add new list to prevent item.lab_list = eachline.rstrip().split("_") reseting the data
            item.new_lab_list.append(lab) 
        

    def __str__(item):
        return ("{:<15}  {:<0} ".format(item.facility_name, item.cost ))

    def labMenu(item):
        while True:
            item.readLaboratoriesFile()
            lab_options = item.inputNumber("Laboratories Menu:\n1 - Display laboratories list \n2 - Add laboratory \n3 - Back to the Main Menu\nOption :")
            if lab_options == 1:
                item.displayLabsList()
            elif lab_options == 2:
                item.addtolabFile()
            elif lab_options == 3:
                break
            else:
                print("Invalid Input Please choose option 1 - 3\n")
                input("Press any key to continue\n")

            print("\nBack to previous Menu")
            item.new_lab_list.clear()

    def inputNumber(self,string):
        while True:
            inp = input(string)
            if inp.isnumeric(): 
                inp = int(inp)
                return inp
            else:
                print("\nInvalid input Please use number")
                input("Press any key to continue\n")