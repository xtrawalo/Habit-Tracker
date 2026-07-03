import csv
answer = 0
choice = 0

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
            answer = int(input("Choose a menu (1-6)"))
            if answer<1 or answer>6:
                print("Invalid Number")
                choice = int(input("Choose a menu (1-6)"))
            else:
                break
        except ValueError:
            print("Invalid Number")
    return answer

def Dashboard():
    print("=================================== \n             DASHBOARD              \n=================================== \n" )
    print("1. Today's Progress")
    print("2. Habits Due Today")
    print("3. Current Streak")
    print("4. Quick Stats")
    print("5. Recent Activity")
    print("O. Return\n")
    while True:
        try:
            choice = int(input("Choose a menu (0-5)"))
            if choice<0 or choice>5:
                print("Invalid Number")
                choice = int(input("Choose a menu (0-5)"))
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
    print("6. Completed Today")
    print("0. Return\n")
    while True:
        try:
            choice = int(input("Choose a menu (0-6)"))
            if choice<0 or choice>6:
                print("Invalid Number")
                choice = int(input("Choose a menu (0-6)"))
            else:
                break
        except ValueError:
            print("Invalid Number")
    return choice

def Calendar():
    print("=================================== \n             CALENDAR               \n=================================== \n" )
    print("1. Daily View ")
    print("2. Monthly View ")
    print("3. Heatmap")
    print("4. History")
    print("0. Return\n")
    while True:
        try:
            choice = int(input("Choose a menu (0-4)"))
            if choice<0 or choice>4:
                print("Invalid Number")
                choice = int(input("Choose a menu (0-4)"))
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
            choice = int(input("Choose a menu (0-5)"))
            if choice<0 or choice>5:
                print("Invalid Number")
                choice = int(input("Choose a menu (0-5)"))
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
            choice = int(input("Choose a menu (0-5)"))
            if choice<0 or choice>5:
                print("Invalid Number")
                choice = int(input("Choose a menu (0-5)"))
            else:
                break
        except ValueError:
            print("Invalid Number")
    return choice

answer = Home()
print(answer)
while True:
    if answer == 1:
        choice == Dashboard()
        if choice == 0:
            Home()
    if answer == 2:
        choice == Habits ()
        if choice == 0:
            Home()
    if answer == 3:
        choice == Calendar()
        if choice == 0:
            Home()
    if answer == 4:
        choice == Statistics()
        if choice == 0:
            Home()
    if answer == 5:
        choice == Achievements()
        if choice == 0:
            Home()
    if answer == 6:
        break


