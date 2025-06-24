try:
    with open("sample.txt", "r") as file:
        index=1
        for line in file:
            print(f"Line {index}:",line.strip())
            index = index+1
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred !!!")