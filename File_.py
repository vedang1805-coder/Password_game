import os

def create_file(filename):
    try:
        with open(filename,"x") as file:
            print(f"File name {filename} Created successfully ")
    except FileExistsError:
        print(f"File name {filename} already exist")
    except Exception as e:
        print("An error occured")

def viwe_file():
    files = os.listdir()
    if not files:
        print("No file Found!")
    else:
        print("File in directory!")
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been removed from your system successfully!!!!!!")
    except FileNotFoundError:
        print("file not found")
    except Exception as e:
        print("An error occured!!!!!")       


def read_File(filename):
    try:
        with open(filename,"r") as file:
            content = file.read()
            print(f"Contant of {filename} :\n {content}")
    except FileNotFoundError:
        print(f"{filename}doesn't exist")

    except Exception as e:
        print("An an Error occured !")
def edit_file(filename):
    try:
        with open("sim.txt","a") as file:
            content = input("Enter data to add =  ")
            file.write(content + "\n")
            print(f"Contant added to {filename} Successfully :)")
    except FileNotFoundError:
        print(f"{filename} DOESN'T exist!")
    except Exception as e:
        print("An error occurred!")
def main():
    while True:
        print("File managment App :))")
        print("Press 1.. to create File")
        print("Press 2.. to View all Files")
        print("Press 3.. to Delete any  File")
        print("Press 4.. to Read any  File")
        print("Press 5.. to Edit any  File")
        print("Press 6.. Exit")
        
        choice = (input("Enter Your Choice :)"))
        if choice == "1":
            filename = input("Enter file name to Create File = ")
            create_file(filename)
        elif choice == "2":
            viwe_file()
        elif choice == "3":
            filename = input("Enter a filename to delete a file = ")
            delete_file(filename)
        elif choice == "4":
            filename = input("Enter a file name to read file = ")
            read_File(filename)
        elif choice == "5":
            filename = input("Enter a file name to edit_a file = ")
            edit_file(filename)
        elif choice == "6":
            print("Closing the file")
            break
        else:
            print("Please enter a range between a given range :)")


main()