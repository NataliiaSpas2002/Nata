import os
import json
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("data_path", help="Phonebook file path")
args = parser.parse_args()


current_dir = os.path.dirname(os.path.realpath(__file__))

PHONEBOOK = {}

datafile_path = os.path.join(current_dir, f"{args.data_path}.json")

if not os.path.exists(datafile_path):
    print(datafile_path)

    with open(datafile_path, "w") as file:
        json.dump(PHONEBOOK, file, indent=4)


try:
     with open(datafile_path, "r") as file:
        PHONEBOOK = json.load(file)
        print(PHONEBOOK)
except json.JSONDecodeError:
    print("Error decoding JSON. Resetting thr data file.")
    PHONEBOOK = {}


def new_data(phonenumber, name, city, address):
    if not phonenumber.startswith("+"):
        print("Invalid phone number format.")
        return

    PHONEBOOK[phonenumber] = {"name": name, "city": city, "address": address}
    with open(datafile_path, "w") as file:
        json.dump(PHONEBOOK, file, indent=4)
        print(PHONEBOOK)

def search_by_name(search_name):
    result = [number for number, entry in PHONEBOOK.items() if entry["name"] == search_name]
    return result


def update(phone_number, name, city, address):
    if phone_number in PHONEBOOK:
        print(f"Updating information for phone number: {phone_number}")
        PHONEBOOK[phone_number] = {"name": name, "city": city, "address": address}
        with open(datafile_path, "w") as file:
            json.dump(PHONEBOOK, file, indent=4)
            print(PHONEBOOK)
        print("Update successful!")
    else:
        print(f"Phone number {phone_number} not found in the phonebook.")


def delete(phone_number):
    if phone_number in PHONEBOOK:
        del PHONEBOOK[phone_number]
        with open(datafile_path, "w") as file:
            json.dump(PHONEBOOK, file, indent=4)
            print(PHONEBOOK)
        print(f"Record for phone number {phone_number} deleted successfully.")
    else:
        print(f"Phone number {phone_number} not found in the phonebook.")

if __name__ == '__main__':
    our_process = True

    while our_process:
        print("What the step do you want?",
              "1 - new_data",
              "2 - search_by_name",
              "3 - update",
              "4 - delete", sep='/n' )
        user_input = input()
        if user_input == '1':
            phonenumber = input("Please enter your number: ")
            name = input("Please enter your name: ")
            city = input("Please enter your city: ")
            address = input("Please enter your address: ")
            new_data(phonenumber, name, city, address)
        if user_input == '2':
            search_name = input("Enter a name to search: ")
            search_result = search_by_name(search_name)
            print(f"Search result for '{search_name}': {search_result}")
        if user_input == '3':
            phonenumber = input("Please enter your number: ")
            name = input("Please enter the update name: ")
            city = input("Please enter the update city: ")
            address = input("Please enter the update address: ")
            update(phonenumber, name, city, address)
        if user_input == '4':
            phone_to_delete = input("Enter a phone number to delete: ")
            delete(phone_to_delete)

    print("Update Phonebook: ")
    print(PHONEBOOK)


