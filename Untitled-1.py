def new_person(first_name,last_name):
    person = f"{first_name} {last_name}"
    return person 
active = True
while active:
    print("\nPlease tell me your name")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name:")
    if f_name == 'q':
        break

    l_name = input("Last name:")
    if l_name == 'q':
        break
    
    formatted_name = new_person(f_name, l_name)
    print(formatted_name)
