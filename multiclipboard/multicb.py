import sys
import clipboard
import json


SAVED_DATA = "clipboard.json"


def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


# save_items("test.json", {"key": "value"})
def load_data(file_path):
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
            return data

    except:

        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)
    if command.lower() == "save":
        key = input("enter the key :")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
    elif command.lower() == "load":
        key = input("enter the key :")
        if key in data:
            clipboard.copy(data[key])
            print("data copied to clip board")
        else:
            print("key is not exist")
    elif command.lower() == "list":
        print(data)
    else:
        print("that's non of our options")
else:
    print('please add exactly one command')
