import csv
import datetime

answer = 0
choice = 0
CurrentDate = datetime.date.today()


def Home():
    print("=================================== \n           HABIT TRACKER            \n=================================== \n" )
    print("1. Dashboard ")
    print("2. Habits ")
    print("3. Exit\n")
    while True:
        try:
            answer = int(input("Choose a menu (1-3) : "))
            if answer<1 or answer>3:
                print("Invalid Number")
            else:
                break
        except ValueError:
            print("Invalid Number")
    return answer

def Dashboard():
    FileName = "Habits.csv"
    AccessMode = "r"
    ActiveHabits = []
    with open(FileName, AccessMode) as MyFile:
        reader = csv.DictReader(MyFile)
        for Habit in reader:
            if Habit['status'] == 'active':
                ActiveHabits.append(Habit)

    FileName = "History.csv"
    AccessMode = "r"
    CompletedByDate = {}
    with open(FileName, AccessMode) as MyFile:
        reader = csv.DictReader(MyFile)
        for Entry in reader:
            if Entry['status'] == 'completed':
                CompletedByDate.setdefault(Entry['date'], set()).add(Entry['habit_id'])
    
    Today = str(CurrentDate)
    TotalHabits = len(ActiveHabits)
    CompletedToday = 0
    DueToday = []
    for Habit in ActiveHabits:
        if Habit['id'] in CompletedByDate.get(Today, set()):
            CompletedToday += 1
        else:
            DueToday.append(Habit)
    
    Percentage = int((CompletedToday / TotalHabits) * 100) if TotalHabits > 0 else 0

    ActiveIDs = {Habit['id'] for Habit in ActiveHabits}
    Streak = 0
    Day = CurrentDate
    while True:
        DayStr = str(Day)
        DoneThatDay = CompletedByDate.get(DayStr, set())
        if ActiveIDs and ActiveIDs.issubset(DoneThatDay):
            Streak += 1
            Day = Day - datetime.timedelta(days=1)
        else:
            break

    print("=================================== \n             DASHBOARD              \n=================================== \n" )
    print(f"Today: {CurrentDate}")
    print(f"Progress: {CompletedToday}/{TotalHabits} ({Percentage}%)")
    print(f"Streak : 🔥 {Streak} days\n")
    print("---------")
    if DueToday:
        for Habit in DueToday:
            print(f"□ {Habit['name']}")
    else:
        print("All Habits Completed !")
    
    print("1. Mark Habit Complete")
    print("0. Return\n")

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

def Complete():
    FileName = "Habits.csv"
    AccessMode = "r"
    Active = []
    with open (FileName, AccessMode) as MyFile:
        reader = csv.DictReader(MyFile)
        for Habit in reader:
            if Habit['status'] == 'active':
                Active.append(Habit)
                print(f"{Habit['id']}. {Habit['name']} ({Habit['category']})")
    if not Active:
        print("There are no habits currently")
        input("Press Enter to continue...")
        return
    
    found  = False
    while True:
        try:
            choice = int(input("Enter habit ID to mark complete : "))
            for Habit in Active:
                if int(Habit['id']) == choice:
                    found = True
                    break
            if not found:
                print("Invalid ID")
            else:
                break
        except ValueError:
            print("Invalid ID")
    
    already_done = False
    FileName = "History.csv"
    AccessMode = "r"
    with open(FileName, AccessMode) as MyFile:
        reader = csv.DictReader(MyFile)
        for Entry in reader:
            if Entry['habit_id'] == str(choice) and Entry['date'] == str(CurrentDate) and Entry['status'] == 'completed':
                already_done = True
                break

    if already_done:
        print("Habit already marked complete today!")
        input("Press Enter to continue...")
        return
    
    AccessMode = "a"
    MyFile = open(FileName, AccessMode)
    MyFile.write(f"{choice},{CurrentDate},completed\n")
    MyFile.close()

    print("Habit marked complete!")
    input("Press Enter to continue...")
    return

def History():
    FileName = 'Habits.csv'
    AccessMode = 'r'
    HabitsDates = {}
    with open(FileName, AccessMode) as MyFile:
        FileData = csv.DictReader(MyFile)
        for Habit in FileData:
            HabitsDates[Habit['id']] = Habit['created_date']

    FileName = 'History.csv'
    AccessMode = 'r'
    CompletedHabits = {}
    with open(FileName, AccessMode) as MyFile:
        FileData = csv.DictReader(MyFile)
        for Habit in FileData:
            if Habit['status'] == "completed":
                CompletedHabits.setdefault(Habit['habit_id'], set()).add(Habit['date'])

    History = []
    for habit_id, created_date in HabitsDates.items():
        created = datetime.datetime.strptime(created_date, "%Y-%m-%d").date()
        days_since_created = (CurrentDate - created).days

        for offset in range(days_since_created + 1):
            day = created + datetime.timedelta(days=offset)
            day_str = day.strftime("%Y-%m-%d")

            if habit_id in CompletedHabits and day_str in CompletedHabits[habit_id]:
                status = "completed"
            else:
                status = "missing"

            History.append({
                "habit_id": habit_id,
                "date": day_str,
                "status": status
            })

    return History

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
            if choice<0 or choice>5:
                print("Invalid Number")
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
            Category = int(input("Choose a category(0-4) : "))
            if Category<0 or Category>4:
                print("Invalid number")
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

answer = Home()
while True:
    if answer == 1:
        choice = Dashboard()
        if choice == 0:
            answer = Home()
        elif choice == 1:
            Complete()
    elif answer == 2:
        choice = Habits ()
        if choice == 0:
            answer = Home()
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
    elif answer == 3:
        break
