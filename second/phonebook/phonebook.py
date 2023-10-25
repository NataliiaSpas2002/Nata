# Topic 11
# Task 2

import os
import json
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("data_path", help="Phonebook file path")
args = parser.parse_args()


current_dir = os.path.dirname(os.path.realpath(__file__))

PHONEBOOK = {
    "+380936752692": {
        "name": "Spasenko Mikhailo",
        "city": "Kyiv",
        "address": "Ushakova Mukolu 6"
    },
    "+380996636752": {
        "name": "Spasenko Mikhailo",
        "city": "Kyiv",
        "address": "Ushakova Mukolu 6"
    },
    "+380996638762": {
        "name": "Spasenko Anna",
        "city": "Kyiv",
        "address": "Ushakova 16A"
    }
}

datafile_path = os.path.join(current_dir, "data", f"{args.data_path}.json")

if not os.path.exists(datafile_path):

    with open(datafile_path, "w") as file:
        json.dump(PHONEBOOK, file, indent=4)

try:
     with open(datafile_path, "r") as file:
        PHONEBOOK = json.load(file)
        print(PHONEBOOK)
except json.JSONDecodeError:
    print("Error decoding JSON. Resetting thr data file.")
    PHONEBOOK = {}


def new_data():
    phonenumber = input("Please enter your number: ")
    if not phonenumber.startswith("+"):
        print("Invalid phone number format.")
        return

    name = input("Please enter your name: ")
    city = input("Please enter your city: ")
    address = input("Please enter your address: ")

    PHONEBOOK[phonenumber] = {"name": name, "city": city, "address": address}


def search_by_name(search_name):
    result = [number for number, entry in PHONEBOOK.items() if entry["name"] == search_name]
    return result


search_name = input("Enter a name to search: ")
search_result = search_by_name(search_name)
print(f"Search result for '{search_name}': {search_result}")


def update(phone_number):
    if phone_number in PHONEBOOK:
        print(f"Updating information for phone number: {phone_number}")
        name = input("Please enter the update name: ")
        city = input("Please enter the update city: ")
        address = input("Please enter the update address: ")

        PHONEBOOK[phone_number] = {"name": name, "city": city, "address": address}
        print("Update successful!")
    else:
        print(f"Phone number {phone_number} not found in the phonebook.")


def delete(phone_number):
    if phone_number in PHONEBOOK:
        del PHONEBOOK[phone_number]
        print(f"Record for phone number {phone_number} deleted successfully.")
    else:
        print(f"Phone number {phone_number} not found in the phonebook.")


new_data()
phone_to_delete = input("Enter a phone number to delete: ")
delete(phone_to_delete)

print("Update Phonebook: ")
print(PHONEBOOK)

with open(datafile_path, "w") as file:
    json.dump(PHONEBOOK, file, indent=4)
    print(PHONEBOOK)











