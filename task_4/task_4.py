# Decorator with error handler for command functions
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command."
        except KeyError:
            return "KeyError. Try using a valid key."
        except IndexError:
            return "Enter the argument for the command."
    return inner


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return f"The contact with the name '{name}' already exists!"
    else:
        contacts[name] = phone
        return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return f"The contact with the name '{name}' does NOT exist!"


@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts.get(name)


@input_error
def show_all(contacts):
    return_str = ""
    # max_name_len = len(max(contacts.keys(), key=len))
    for k, v in contacts.items():
        return_str += f"{k:>15}: {v:<15}\n"
    return return_str
    # return '\n'.join(map('\t'.join, contacts.items()))


def help_info():
    return """
        help                                    - to show this information
        hello                                   - to show the greeting
        add [ім'я] [номер телефону]             - to add contact
        change [ім'я] [новий номер телефону]    - to change contact phone number
        phone [ім'я]                            - to show contact phone number
        all                                     - to show list of all contacts
        close
        exit
        """


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        # > add [ім'я] [номер телефону]
        elif command == "add":
            print(add_contact(args, contacts))

        # > change [ім'я] [новий номер телефону]
        elif command == "change":
            print(change_contact(args, contacts))

        # > phone [ім'я]
        elif command == "phone":
            print(show_phone(args, contacts))

        # > all
        elif command == "all":
            print(show_all(contacts))

        # > help_info
        elif command == "help":
            print(help_info())

        else:
            print("Enter valid command!")
            print(help_info())


if __name__ == "__main__":
    main()
