import csv
import datetime

answer = 0
choice = 0
CurrentDate = datetime.date.today()


def Home():
    print("=================================== \n           HABIT TRACKER            \n=================================== \n" )
    print("1. Dashboard ")
    print("2. Habits ")
    print("3. Calendar")
    print("4. Statistics")
    print("5. Achievements")
    print("6. Exit\n")
    while True:
        try:
            answer = int(input("Choose a menu (1-6) : "))
            if answer<1 or answer>6:
                print("Invalid Number")
                choice = int(input("Choose a menu (1-6) : "))
            else:
                break
        except ValueError:
            print("Invalid Number")
    return answer

def Dashboard():
    print("=================================== \n             DASHBOARD              \n=================================== \n" )
    
    print(f"Today: {CurrentDate}")
    print("Quick Stats")
    
    print("1. Mark Habit Complete")
    print("O. Return\n")
    while True:
        try:
            choice = int(input("Choose a menu (0-1) : "))
            if choice<0 or choice>1:
                print("Invalid Number")
            else:
                break
        except ValueError:
            print("Invalid Number")
    
    return choice

def Habits():
    print("=================================== \n              HABITS                \n=================================== \n" )
    print("1. All Habits ")
    print("2. Add Habit")
    print("3. Delete Habit")
    print("4. Edit Habit")
    print("5. Categories")
    print("0. Return\n")
    while True:
        try:
            choice = int(input("Choose a menu (0-5) : "))
            if choice<0 or choice>6:
                print("Invalid Number")
                choice = int(input("Choose a menu (0-5) : "))
            else:
                break
        except ValueError:
            print("Invalid Number")
    return choice

def AllHabits():
    FileName = "Habits.csv"
    AccessMode = "r"
    Habits = []
    with open(FileName, AccessMode) as MyFile:
        reader = csv.DictReader(MyFile)
        for Habit in reader:
            if Habit['status'] == 'active':
                Habits.append(Habit)
                print(f"{Habit['id']}. {Habit['name']}({Habit['category']})")
    if not Habits:
        print("There are no habits currently")
    input("Press Enter to continue...")
    return

def AddHabit(): 
    FileName = "Habits.csv"
    AccessMode = "r"
    new_id = 1
    with open(FileName, AccessMode) as MyFile:
        reader = csv.DictReader(MyFile)
        Habits = []
        IDs = []
        for Habit in reader:
            Habits.append(Habit)
            IDs.append(int(Habit['id']))
    if IDs:
        new_id = max(IDs) + 1
    
        
    AccessMode = "a"
    MyFile = open(FileName,AccessMode)
    Habits = ["Study", "Fitness", "Health", "Work", "Personal"]
    Frequency = ["Daily", "Weekly"]
    Habit = input("Ener a new Habit : ")
    while True:
        try:
            if "," in Habit:
                print("Invalid Habit")
                Habit = input("Ener a new Habit (no commas) : ")
            else:
                break
        except:
            print("Invalid number")

    print('\nCategory:')
    for i in range(len(Habits)):
        print(f"{i}. {Habits[i]}")
    while True:
        try:
            Category = int(input("Choose a category(0-5) : "))
            if Category<0 or Category>5:
                print("Invalid number")
                Category = input("Choose a category(0-5) : ")
            else:
                break
        except:
            print("Invalid number")
    for i in range(len(Habits)):
        if Category == i:
            Category = Habits[i]
    print(f"{Category}")

    print('\nFrequency:')
    for i in range(len(Frequency)):
        print(f"{i}. {Frequency[i]}")
    while True:
        try:
            Freq = int(input("Choose a Frequency(0-1) : "))
            if Freq<0 or Freq>1:
                print("Invalid number")
                Freq = int(input("Choose a Frequency(0-1) : "))
            else:
                break
        except:
            print("Invalid number")

    for i in range(len(Frequency)):
        if Freq == i:
            Freq = Frequency[i]
    print(f"{Freq}\n")
    
    print("Habit added successfully")
    MyFile.write(f"{new_id},{Habit},{Category},{Freq},{CurrentDate},active\n")
    MyFile.close()

    return

def DeleteHabit():
    FileName = "Habits.csv"
    AccessMode = "r"
    Habits = []
    with open(FileName, AccessMode) as MyFile:
        reader = csv.DictReader(MyFile)
        Habits = []
        Active = []
        for Habit in reader:
            Habits.append(Habit)
            if Habit['status'] == 'active':
                print(f"{Habit['id']}. {Habit['name']}({Habit['category']})")
                Active.append(Habit)
    if not Active:
        print("There are no habits currently")
        input("Press Enter to continue...")
        return
    
    found = False
    while True:
        try:
            choice = int(input(f"Enter habit ID to delete : "))
            for Habit in Active:
                if int(Habit['id']) == choice:
                    found = True
                    break
            if not found:
                print("Invalid ID")
            if found:
                break
        except ValueError:
            print("Invalid ID")

    for Habit in Habits:
        if int(Habit['id']) == choice:
            Habit['status'] = 'inactive'
            break

    print("Habit deleted successfully!")

    AccessMode = "w"
    MyFile = open(FileName, AccessMode)
    MyFile.write("id,name,category,frequency,created_date,status\n")
    for Habit in Habits:
        MyFile.write(f"{Habit['id']},{Habit['name']},{Habit['category']},{Habit['frequency']},{Habit['created_date']},{Habit['status']}\n")
    MyFile.close()

    input("Press Enter to continue...")
    return

def EditHabit():
    FileName = "Habits.csv"
    AccessMode = "r"
    Habits = []
    Categorys = ["Study", "Fitness", "Health", "Work", "Personal"]
    Frequency = ["Daily", "Weekly"]
    with open(FileName, AccessMode) as MyFile:
        reader = csv.DictReader(MyFile)
        Habits = []
        for Habit in reader:
            Habits.append(Habit)
            print(f"{Habit['id']}. {Habit['name']} ({Habit['category']}) /{Habit['status']}")
    found = False
    while True:
        try:
            choice = int(input(f"Enter habit ID to edit : "))
            found = False
            for Habit in Habits:
                if int(Habit['id']) == choice:
                    found = True
                    break
            if not found:
                print("Invalid ID")
            if found:
                break
        except ValueError:
            print("Invalid ID")

    for Habit in Habits:
        if int(Habit['id']) == choice:
            name = input("Change habit name (Enter X to skip) : ")
            while True:
                try:
                    if "," in name:
                        print("Invalid name")
                        name = input("Ener a new Habit (no commas) : ")
                    else:
                        break
                except ValueError:
                    print("Invalid name")
            if name.upper() != "X":
                Habit['name'] = name
            
            print('\nCategory:')
            for i in range(len(Categorys)):
                print(f"{i}. {Categorys[i]}")
            skip = False
            while True:
                Category = input("Change habit category (0-4) (Enter X to skip) : ")
                if Category.upper() == "X":
                    skip = True
                    break
                try:
                    Category = int(Category)
                    if Category<0 or Category>4:
                        print("Invalid number")
                    else:
                        break
                except ValueError:
                    print("Invalid number")    
            if not skip:
                Habit['category'] = Categorys[Category]           
                print(f"{Category}")
        
            print('\nFrequency:')
            for i in range(len(Frequency)):
                print(f"{i}. {Frequency[i]}")
            skip = False
            while True:
                Freq = input("Change habit Frequency (0-1) (Enter X to skip) : ")
                if Freq.upper() == "X":
                    skip = True
                    break
                try:
                    Freq = int(Freq)
                    if Freq<0 or Freq>1:
                        print("Invalid number")
                    else:
                        break
                except ValueError:
                    print("Invalid number")
            if not skip:
                Habit['frequency'] = Frequency[Freq]           
                print(f"{Freq}")
    
            break


    AccessMode = "w"
    MyFile = open(FileName, AccessMode)
    MyFile.write("id,name,category,frequency,created_date,status\n")
    for Habit in Habits:
        MyFile.write(f"{Habit['id']},{Habit['name']},{Habit['category']},{Habit['frequency']},{Habit['created_date']},{Habit['status']}\n")
    MyFile.close()

    input("Press Enter to continue...")
    return

def Categorys():
    FileName = 'Habits.csv'
    AccessMode = 'r'
    Categories = {
        'Study' : [],
        'Fitness' : [],
        'Health' : [],
        'Work' : [],
        'Personal' : []}

    with open(FileName, AccessMode) as MyFile:
        reader = csv.DictReader(MyFile)
        for Habit in reader:
            if Habit['status'] == 'active':
                Categories[Habit['category']].append(Habit["name"])
    if not any(Categories.values()):
        print("There are no habits currently")
        input("Press Enter to continue...")
        return
    
    for category, habits in Categories.items():
        if habits:
            print(f"{category}: {','.join(habits)}")
    input("Press Enter to continue...")
    return

def Calendar():
    print("=================================== \n             CALENDAR               \n=================================== \n" )
    print("1. Daily View ")
    print("2. Monthly View ")
    print("3. Heatmap")
    print("4. History")
    print("0. Return\n")
    while True:
        try:
            choice = int(input("Choose a menu (0-4) : "))
            if choice<0 or choice>4:
                print("Invalid Number")
            else:
                break
        except ValueError:
            print("Invalid Number")
    return choice

def Statistics():
    print("=================================== \n            Statistics              \n=================================== \n" )
    print("1. Completion Rate ")
    print("2. Weekly Progress ")
    print("3. Monthly Progress")
    print("4. Streak History")
    print("5. Best Habits")
    print("0. Return\n")
    while True:
        try:
            choice = int(input("Choose a menu (0-5) : "))
            if choice<0 or choice>5:
                print("Invalid Number")
                choice = int(input("Choose a menu (0-5) : "))
            else:
                break
        except ValueError:
            print("Invalid Number")
    return choice

def Achievements():
    print("=================================== \n            Achievements           \n=================================== \n" )
    print("1. Badges ")
    print("2. Milestones ")
    print("3. Longest Streak")
    print("4. Total Completed Habits")
    print("5. Level")
    print("0. Return\n")    
    while True:
        try:
            choice = int(input("Choose a menu (0-5) : "))
            if choice<0 or choice>5:
                print("Invalid Number")
                choice = int(input("Choose a menu (0-5) : "))
            else:
                break
        except ValueError:
            print("Invalid Number")
    return choice

answer = Home()
print(answer)
while True:
    if answer == 1:
        choice = Dashboard()
        if choice == 0:
            Home()
    if answer == 2:
        choice = Habits ()
        if choice == 0:
            Home()
        elif choice == 1:
            AllHabits()
        elif choice == 2:
            AddHabit()
        elif choice == 3:
            DeleteHabit()
        elif choice == 4:
            EditHabit()
        elif choice == 5:
            Categorys()
    if answer == 3:
        choice = Calendar()
        if choice == 0:
            Home()
    if answer == 4:
        choice = Statistics()
        if choice == 0:
            Home()
    if answer == 5:
        choice = Achievements()
        if choice == 0:
            Home()
    if answer == 6:
        break
