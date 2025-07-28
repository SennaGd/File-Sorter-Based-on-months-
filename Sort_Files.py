import os,shutil
from os import listdir
from os.path import isfile, join

print("\n\n\n") # Better terminal outputs

#! DEBUGGING
#? create test files
# July = open("C://Users//senna//Documents//Python File Sorter//files" + r"\Testfile_2025_Juli", "w")
# August = open("C://Users//senna//Documents//Python File Sorter//files" + r"\Testfile_2025_Augustus.txt", "w")
# September = open("C://Users//senna//Documents//Python File Sorter//files" + r"\Testfile_2025_December", "w")

#! Variables
# Path for files
Path = "C://Users//senna//Documents//Python File Sorter//files"

#* "Files" = all files inside the folder (Type = list|arr)
Files = os.listdir(Path)

# All months
Months_List = [
    "Januari","Februari","Maart",
    "April", "Mei", "Juni",
    "Juli", "Augustus", "September",
    "Oktober", "November", "December"
               ]

Sets_Months = [
    [Months_List[0],Months_List[1],Months_List[2]],
    [Months_List[3],Months_List[4],Months_List[5]],
    [Months_List[6],Months_List[7],Months_List[8]],
    [Months_List[9],Months_List[10],Months_List[11]]
]
# Sets for months
Set_Names = ["Januari-Maart", 
             "April-Juni", 
             "Juli-September",
             "Oktober-December"]


#? Create Sets
for x in Set_Names:
    if not os.path.exists(Path + x):
        os.makedirs(Path + "/" + x, exist_ok=True)


#? Create set months inside sets
counter = 0
set_number = 0
for _ in Months_List:
    while counter < 3: # Set1
        Set = Path + "//" + Set_Names[set_number] + "//" + Months_List[counter]
        if not os.path.exists(Set):
            os.makedirs(Set, exist_ok=True)
        counter += 1
        
    set_number += 1
    
    while counter < 6: # Set2
        Set = Path + "//" + Set_Names[set_number] + "//" + Months_List[counter]
        if not os.path.exists(Set):
            os.makedirs(Set, exist_ok=True)
        counter += 1
    
    set_number += 1
 
    while counter < 9: # Set3
        Set = Path + "//" + Set_Names[set_number] + "//" + Months_List[counter]
        if not os.path.exists(Set):
            os.makedirs(Set, exist_ok=True)
        counter += 1
    
    set_number += 1
        
    while counter < 12: # Set4
        Set = Path + "//" + Set_Names[set_number] + "//" + Months_List[counter]
        if not os.path.exists(Set):
            os.makedirs(Set, exist_ok=True)
        counter += 1

 
#? Check all files | EXCLUDE FOLDERS
# Shows all files | In array
file_list = [f for f in listdir(Path) if isfile(join(Path, f))]

# find out what month the file is:
for file_name in file_list:
    
    # Sets location for files
    file_location = Path + "//" + file_name
    
    # Gets the month of each file
    for x in Months_List:        
        month_offset = (file_name.find(x))
        if month_offset != -1:
            month = file_name[month_offset:month_offset+len(x)]
            
    #! Set:0 = jan -> mar, Set:1 = apr -> Jun, Set:2 = jul -> sep, Set:3 = okt -> dec
    set_finder = 0 # counter for sets
    for x in Sets_Months:
        if month == x[0] or month == x[1] or month == x[2]:
            print("Current file location: " + file_location)
            print("Move Path: " + Path + "//" + Set_Names[set_finder] + "//" + month + "//" + file_name + "\n")
            file_destination = Path + "//" + Set_Names[set_finder] + "//" + month + "//" + file_name
            #! COPY FILE TO CORRESPONDING DESTINATION
            try:
                shutil.copy(file_location, file_destination)
            except:
                shutil.SameFileError
                
        set_finder += 1

print(":3\n\n\n")