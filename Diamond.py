contact = "Email fieldalex08@gmail.com "8385393" "
website = "Not supported yet"
print("Version 1.0 beta")
while True:
    # take input from the user
    choice = input("Enter choice: check in or tutorials? ")

    # check if choice is one of the options
    if choice in ('check in','tutorials'):
        try:
            Choice = float(input("Answer: ")
        except ValueError:
            print("Invalid input. Please enter a answer.")
            continue

        if choice == 'check in':
            print(contact)
        if choice == 'tutorial':
            print(Website)
