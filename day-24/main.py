# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Solution
with open("Input/Names/invited_names.txt") as names_file:
	names = names_file.readlines()

with open("Input/Letters/starting_letter.txt") as letter_file:
	letter = letter_file.read()
	for name in names:
		new_letter = letter.replace("[name]", name.strip()) # strip() removes the new line character
		with open(f"Output/ReadyToSend/letter_for_{name.strip()}.txt", mode="w") as completed_letter:
			completed_letter.write(new_letter)


