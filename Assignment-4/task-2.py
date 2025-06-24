with open("output.txt", "w") as file:
    user_input = input("Enter text to write to file: ")
    file.write(user_input + "\n")
    print("Data successfully written to output.txt. \n")
with open("output.txt", "a") as file:
    additional_input = input("Enter additional text to append: ")
    file.write(additional_input + "\n")
    print("Data successfully appended.")
with open("output.txt", "r") as file:
    print("\nFinal content of output.txt:")
    print(file.read())