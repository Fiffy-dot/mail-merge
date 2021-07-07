# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# get the names of the invitees
with open("input/names/invited_names.txt") as names:
    people = names.readlines()
    invitees = []
    for person in people:  # we need to strip the names in the list to a format we can use
        new_person = person.strip("\n")
        invitees.append(new_person)

# replace the placeholder with the list of invitees we have
with open("input/letters/starting_letter.txt") as letter:
    content = letter.read()
    for invitee in invitees:
        new_letter = content.replace("[name]",invitee)
        ready_letter = open(f"Output/ReadyToSend/letter_for_{invitee}.txt", "w")
        ready_letter.write(new_letter)
        ready_letter.close()







