
class PackageManager():#handles the array that contains the data and returning data
    def __init__(self): 
         self.totalnum = 0
         self.pkglist = []
         self.sorted = False
    

    #insertion sort, time complexity O(n^2)
    def sort(self): 
        for i in range(1, len(self.pkglist)):
            key = self.pkglist[i]
            s = i - 1
            while s>=0 and self.pkglist[s].urg < key.urg:
                self.pkglist[s+1] = self.pkglist[s]
                s-=1
            self.pkglist[s+1] = key
        self.sorted = True
    #for any operations that required searching for a data entry, a linear search is used.
    #In order to implement a binary search, the array would need to be sorted by id but the insertion sort sorts by urgency
    #Because multiple entries can have the same urgency, a binary search would not accurately return data in the way it would require here.
    def printinfo(self, id):
         for Package in self.pkglist:
            if Package.packageID == id:
                Package.print()
         
    def print(self):
        for Package in self.pkglist:
            Package.print()

    def printdeliv(self):
        for Package in self.pkglist:
            if Package.status == 2:
                Package.print()
    
    def printtransit(self):
         for Package in self.pkglist:
              if Package.status == 1:
                   Package.print()

    def updatestat(self, id):
         for Package in self.pkglist:
              if Package.packageID == id:
                   Package.status = 2
                   return
    
    def delete(self, id):
         for Package in self.pkglist:
              if Package.packageID == id:
                   self.pkglist.remove(Package)

             
    #def search(self,)

class Package(): #handles indevidual entries
    totalNum = 0
    def __init__(self, weight, desZip, urg):
          self.packageID = Package.totalNum
          self.weight = weight
          self.desZip = desZip
          self.urg = int(urg)
          self.status = 1
          Package.totalNum +=1
        
    def print(self):
        urgent = Package.urgdic[str(self.urg)]
        stat = Package.statdic[str(self.status)]
        print(f"Package ID: {self.packageID}, Weight: {self.weight}g, Destination Zip: {self.desZip}, Status: {stat}, {urgent}")
    
    def update(self, weight, desZip, urg):
         self.weight = weight
         self.desZip = desZip
         self.urg = urg

    #to simplify sorting and updating, dictionaries are used as references
    # instead of storing the urgencies and statuses as strings.
    urgdic = {
          "1":"Low urgency",
          "2":"Slight urgency",
          "3":"Moderate urgency",
          "4":"High urgency",
          "5":"Critical urgency"
    }
    
    statdic = {
         "1":"In Transit",
         "2":"Delivered"
    }

    
        
class Menu(): #handles printing of menus and logic of submenu for editing
     def drawHome(self):
          print("--------------------------------------------------------")
          print("Welcome to Evan's package manager!\n")
          print("What would you like to do?\n")
          print("1. View package list")
          print("2. View delivered packages")
          print("3. View packages in transit")
          print("4. Update package delivery status")
          print("5. Modify package details")
          print("6. Create new package")
          print("7. Delete package")
          print("8. Sort package list")
          print("9. Search by ID")
     def editmenu(self):
          print("1: Update wight")
          print("2: Update Zip code")
          print("3: Update Urgency")
          print("4: Cancel")
    
     def editcase(self, id, case, Manager):
        menu = True
        while menu:
            if case == 1:
                for Package in Manager.pkglist:
                    if Package.packageID == id:
                        weight = float(input("Please enter new weight"))
                        Package.update(weight, Package.desZip, Package.urg)  
                        menu = False     
            if case == 2:
                for Package in self.pkglist:
                    if Package.packageID == id:
                        Zip = int(input("Please enter new Zipcode"))
                        Package.update(Package.weight, Zip, Package.urg)
                        menu = False
            if case == 3:
                for Package in self.pkglist:
                    if Package.packageID == id:
                        Urg = int(input("Please enter new urgency 1-5. 1 is low, 5 is high."))
                        Package.update(Package.weight, Package.desZip, Urg)
                        menu = False
            #else:
               # print("Please make a valid selection")
          
                   
          

menu = Menu()
pkgmanager = PackageManager()

#placeholder data
Package1 = Package(12.7, 47648, 1)
Package2 = Package(24.2, 42420, 2)
Package3 = Package(22.7, 47712, 3)
Package4 = Package(12.1, 47680, 4)
Package5 = Package(18.5, 47715, 5)


pkgmanager.pkglist.append(Package1)
pkgmanager.pkglist.append(Package2)
pkgmanager.pkglist.append(Package3)
pkgmanager.pkglist.append(Package4)
pkgmanager.pkglist.append(Package5)

#menu logic, requests integer input for navigation

while True: 
    menu.drawHome()
    case = input()
    if case == "1":
          print("")
          pkgmanager.print()
          pause = input("\nPress enter to continue")
    if case == "2":
         print("")
         pkgmanager.printdeliv()
         pause = input("\nPress enter to continue")
    if case == "3":
         print("")
         pkgmanager.printtransit()
         pause = input("\nPress enter to continue")
    if case == "4":
         print("")
         update = int(input("What is the ID of the package you'd like to update?"))
         pkgmanager.updatestat(update)
         pause = input("\nPress enter to continue")
    if case == "5":
         print("")
         id = int(input("Please enter the ID of the package you wish to edit"))
         menu.editmenu()
         case2 = int(input(""))
         menu.editcase(id, case2,pkgmanager)
         pause = input("\nPress enter to continue")
    if case == "6":
         print("")
         weight = float(input("Please enter your package weight."))
         zip = int(input("Please enter your package's destination zip code."))
         urg = int(input("Please enter your package's urgency 1-5. 1 is low, 5 is high."))
         newpack = Package(weight, zip, urg)
         pkgmanager.pkglist.append(newpack)
         pkgmanager.sorted = False
         print("New package created successfully.")
         pause = input("\nPress enter to continue")
    if case == "7":
         print()
         id = int(input("Please enter the ID of the package you wish to delete"))
         pkgmanager.delete(id)
         pause = input("\nPress enter to continue")
    if case == "8":
         print()
         pkgmanager.sort()
         pkgmanager.sorted = True
         print("Sort completed successfully!")
         pause = input("\nPress enter to continue")
    if case == "9":
         print()
         id = int(input("Please enter the ID of the package you wish to search for."))
         pkgmanager.printinfo(id)
         pause = input("\nPress enter to continue")

         