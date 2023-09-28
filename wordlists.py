# Prompt the user for the input filename
input_filename = input("Enter the name of the input text file (e.g., names.txt): ")

# Initialize an empty list to store usernames
wordlist = []

try:
    # Open the user-provided input file for reading
    with open(input_filename, "r") as input_file:
        # Read each line from the input file
        for line in input_file:
            # Split the line into first and last names
            parts = line.strip().split()
            if len(parts) == 2:
                firstname = parts[0].lower()
                lastname = parts[1].lower()
                # Generate username variations
                username = firstname + lastname
                username_dot = firstname + "." + lastname
                username_last_first = lastname + firstname
                username_last_first_dot = lastname + "." + firstname
                # Add the generated usernames to the wordlist
                wordlist.extend([username, username_dot, firstname, lastname, username_last_first, username_last_first_dot])

    # Prompt the user for the output filename
    output_filename = input("Enter the name of the output text file (e.g., custom_wordlist.txt): ")

    # Write the generated wordlist to a file
    with open(output_filename, "w") as output_file:
        for word in wordlist:
            output_file.write(word + "\n")

    print(f"Wordlist has been successfully generated and saved to {output_filename}")

except FileNotFoundError:
    print(f"Error: The file '{input_filename}' was not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
