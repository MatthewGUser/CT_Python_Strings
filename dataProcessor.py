# [ Task 1 ]

def verify(name):
    # Split the input into parts
    name_parts = name.split()

    # Wrong amount of input
    if len(name_parts) != 2:
        print("Error: Need first and last name only.")
    else:
        first_name = name_parts[0]
        last_name = name_parts[1]

        # Check if first or last name is too short
        if len(first_name) < 2 or len(last_name) < 2:
            print("Error: First or last name too short")
        else:
            print(f"First Name: {first_name}")
            print(f"Last Name: {last_name}")

name = input("Please enter first and last name: ")
verify(name)