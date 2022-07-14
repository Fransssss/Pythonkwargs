# **kwargs = stands for 'key word arguments'

def hello(**kwargs):
    print("\nHello " + kwargs['first'] + kwargs['middle'] + kwargs['last'])

def the_age(**kwargs):
    print("\nThis year, You are " + kwargs['first'] + " y/o.\nLast year, You were " + kwargs['middle'] + " y/o.\nNext year, You will be " + kwargs['last'] + " y/o.")

def the_city(**kwargs):
    print("\nYou are from " + kwargs['first'])

def the_prof(**kwargs):
    print("\nNow, Your profession is " + kwargs['first'] + ".\nPreviously, Your profession was " + kwargs['last'])

def capitalize_first_letter(word):
    if word.islower():
        word = word.capitalize()
    return word


print("\n== Short Introduction ==")
print("1. Name")
print("2. Age")
print("3.City")
print("4. Profession")
print("E. Exit")
choice = input("choice: ")

while choice != 'E' and choice != 'e':
    if choice == '1':
        print("\n- Name")
        name = input("Input a name: ")
        if len(name) == 0:
            print("\n[Invalid name / No input]")
        else:
            name = capitalize_first_letter(name)
            hello(last=name, first="Ms", middle="/mr ")

    elif choice == '2':
        print("\n- Age")
        age_now = input("Input an age: ")
        if age_now.isdigit():
            age_a_year_later = int(age_now) + 1
            if age_now != '0':
                age_a_year_before = int(age_now) - 1
            the_age(last=str(age_a_year_later),middle=str(age_a_year_before),first=str(age_now))
        else:
            print("\n[Input should be a digit]")

    elif choice == '3':
        city = input("\nWhat city are you from: ")
        if len(city) <= 3:
            print("\n[Invalid city]")
        else:
            city = capitalize_first_letter(city)
            the_city(first=city)

    elif choice == '4':
        profession_now = input("\nWhat is your profession: ")
        if len(profession_now) <= 3:
            print("\n[Invalid profession]")
        else:
            profession_before = input("What was your profession: ")
            profession_now = capitalize_first_letter(profession_now)
            profession_before = capitalize_first_letter(profession_before)
            the_prof(last=profession_before, first=profession_now)

    else:
        print("\n[Invalid choice]")

    print("\n== Short Introduction ==")
    print("1. Name")
    print("2. Age")
    print("3.City")
    print("4. Profession")
    print("E. Exit")
    choice = input("choice: ")
