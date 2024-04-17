place_holder = "[name]"

with open("C:/Users/sesay/OneDrive/Desktop/Python-Projects/Mail Merge Project Start/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("C:/Users/sesay/OneDrive/Desktop/Python-Projects/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(place_holder,stripped_name)
        with open(f"C:/Users/sesay/OneDrive/desktop/Python-Projects/Mail Merge Project Start/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode = "w") as completed_letter:
            completed_letter.write(new_letter)
