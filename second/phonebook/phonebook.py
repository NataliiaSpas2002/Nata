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
        "city": "Kuiv",
        "address": "Ushakova Mukolu 6"
    },
    "+380996636752": {
        "name": "Spasenko Mikhailo",
        "city": "Kuiv",
        "address": "Ushakova Mukolu 6"
    },
    "+380996638762": {
        "name": "Spasenko Anna",
        "city": "Kuiv",
        "address": "Ushakova 16A"
    }
}

datafile_path = os.path.join(current_dir, "data", (args.data_path + ".json"))

if not os.path.exists(datafile_path):

    with open(datafile_path, "a") as file:
        json.dump(PHONEBOOK, file, indent=4)

else:
    with open(datafile_path, "r") as file:
        PHONEBOOK = json.load(file)
        print(PHONEBOOK)

def new_data():
    phonenumber = input("Please enter your number: ")
    name = input("Please enter your name: ")
    city = input("Please enter your city: ")
    address = input("Please enter your address: ")
    PHONEBOOK[phonenumber] = {"name": name, "city": city, "address": address}

new_data()

with open(datafile_path, "w") as file:
    json.dump(PHONEBOOK, file, indent=4)
    print(PHONEBOOK)

# def delete_entry()
#     pass


def search_by_name():
    result = [name for name in PHONEBOOK]


def update():
    pass












