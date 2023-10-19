
# Alex
    import json
    import os
    import time

    # Task 1
    FILE_NAME = "my_file.txt"
    WRITE_STR = "Hello file world!"

    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), FILE_NAME)

    def write(text: str):
        """
        :param text:
        :return:
        """
        with open(file_path, "w", encoding="utf-8") as obj:
            obj.write(text)
        print("successful")

    def read():
        """
        :return:
        """
        try:
            with open(file_path, "r", encoding="utf-8") as obj:
                print(obj.read())
        except FileNotFoundError:
            print("file empty")

    write(WRITE_STR)
    read()

    # Task 2

    class PhoneBook:
        """
        work with json file
        """
        json_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "phonebook.json"
        )
        delimiter = "-" * 100
        text = {
            "wrong_data": "Perhaps your answer has mistakes",
            "no_such": "I did’t find such a contact",
            "add": "Successful add date, check: {}",
            "update": "Successful update date, check: {}",
            "delete": "Successful delete phone {} from phonebook",
        }
        query_type = None

        @property
        def phone_book(self) -> dict:
            """
            read json
            :return: dict
            """
            try:
                with open(self.json_path, "r", encoding='utf-8') as obj:
                    return json.load(obj)
            except FileNotFoundError:
                return {}

        def add_new_entry(self, data: str):
            """
            add new entry into json
            :param data:
            :return:
            """
            data = data.replace(" ", "").split(",")
            if len(data) == 4 and data[2].replace("+", "").isdigit():
                new_entry = {
                    "first_name": data[0],
                    "last_name": data[1],
                    "telephone_number": data[2],
                    "city": data[3],
                }
                phone_book = self.phone_book
                phone_book.update({data[2]: new_entry})
                with open(self.json_path, "w", encoding='utf-8') as obj:
                    json.dump(phone_book, obj, indent=4)
                added_data = list((f"{key}: {value}, " for key, value in new_entry.items()))
                print(self.text.get("add").format(("".join(added_data), self.delimiter)))
            else:
                print(self.text.get("wrong_data"))

        def update_entry(self, new_value: str):
            """
            update entry for telephone number
            :param new_value:
            :return:
            """
            data = new_value.replace(" ", "").split(",")
            if len(data) == 4 and data[0].replace("+", "").isdigit():
                if data[0] in self.phone_book:
                    update_value = {
                        "first_name": data[1],
                        "last_name": data[2],
                        "telephone_number": data[0],
                        "city": data[3],
                    }
                    phone_book = self.phone_book
                    phone_book[data[0]] = update_value
                    with open(self.json_path, "w", encoding='utf-8') as obj:
                        json.dump(phone_book, obj, indent=4)
                    added_data = list(
                        (f"{key}: {value}, " for key, value in update_value.items())
                    )
                    print(
                        self.text.get("update").format(
                            ("".join(added_data) + self.delimiter)
                        )
                    )
                else:
                    print(self.text.get("no_such"))

        def delete_entry(self, phone_number: str):
            """
            :param phone_number:
            :return:
            """
            phone_book = self.phone_book
            if phone_number in phone_book:
                del phone_book[phone_number]
                with open(self.json_path, "w", encoding='utf-8') as obj:
                    json.dump(phone_book, obj, indent=4)
                print(self.text.get("delete").format(phone_number))
            else:
                print(self.text.get("no_such"))

        def search(self, query: str):
            """
            search entry for first name, last name, full name, number or city.
            :param query:
            :return:
            """
            results = {}
            query_types = {
                2: "name",
                3: "name",
                4: "name",
                5: "telephone_number",
                6: "city_or_state",
            }

            query_type = query_types.get(self.query_type)

            if query_type == "telephone_number":
                results = self.phone_book.get(query)
            else:
                for entry in self.phone_book.values():
                    if query_type == "city_or_state":
                        if query.lower() in entry["city"].lower():
                            results.update(entry)
                    elif query_type == "name":
                        first_name = entry["first_name"]
                        last_name = entry["last_name"]
                        full_name = first_name + " " + last_name
                        if query.lower() in (
                                full_name.lower(),
                                first_name.lower(),
                                last_name.lower(),
                        ):
                            results.update(entry)

            if results:
                answer = list((f"{key}: {value}, " for key, value in results.items()))
                print(f'Info by query: {"".join(answer)}', self.delimiter)
            else:
                print(self.text.get("no_such"))

    class User:
        """
        switch on program for interaction with user
        """
        start_text = (
            "\t1. Add new entries \n"
            "\t2. Search by first name \n"
            "\t3. Search by last name \n"
            "\t4. Search by full name\n"
            "\t5. Search by telephone number\n"
            "\t6. Search by city or state\n"
            "\t7. Delete a record for a given telephone number\n"
            "\t8. Update a record for a given telephone number\n"
            "\t9. An option to exit the program\n"
            "You choose : "
        )
        delimiter = "-" * 100

        def __init__(self):
            self.phone_book = PhoneBook()
            self.answer_dict = {
                1: {
                    "prompt": (
                        f"{self.delimiter}\nWrite info about entries in one line. "
                        f'IMPORTANT use ","(coma) for divide values\n'
                        "Hint: first name, last name, telephone number, "
                        "city or state\nPlease write: "
                    ),
                    "function": self.phone_book.add_new_entry,
                },
                2: {
                    "prompt": "Write first name for search: ",
                    "function": self.phone_book.search,
                },
                3: {
                    "prompt": "Write last name for search: ",
                    "function": self.phone_book.search,
                },
                4: {
                    "prompt": "Write full name for search: ",
                    "function": self.phone_book.search,
                },
                5: {
                    "prompt": "Write telephone number for search: ",
                    "function": self.phone_book.search,
                },
                6: {
                    "prompt": "Write city or state for search: ",
                    "function": self.phone_book.search,
                },
                7: {
                    "prompt": "Write telephone number for delete: ",
                    "function": self.phone_book.delete_entry,
                },
                8: {
                    "prompt": (
                        "Write telephone for update and new value. "
                        "Hint: first name, last name, telephone number, city or state: "
                    ),
                    "function": self.phone_book.update_entry,
                },
                9: "Goodbye",
            }

        def start(self):
            """
            :return:
            """
            answer = input("Choose actions:\n" + self.start_text)
            second_step = None
            first_step = None
            try:
                first_step = int(answer)
                if first_step == 9:
                    print(self.answer_dict.get(9, "Opps"))
                elif 0 < first_step < 9:
                    second_step = input(self.answer_dict.get(first_step)["prompt"])
                else:
                    raise ValueError
            except ValueError:
                print("Wrong query, try again")
                self.start()
            if second_step and first_step:
                try:
                    self.phone_book.query_type = first_step
                    self.answer_dict.get(first_step)["function"](second_step)
                    time.sleep(3)
                except ValueError:
                    print("Wrong query, try again")
                self.start()

    start = User()
    start.start()
