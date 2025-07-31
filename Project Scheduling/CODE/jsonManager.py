import json
import os

file_path = 'DATA\data.json'

def update(name, email):
    if name == "" or email == "":
        return "Incorrect entry"
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
    else:
        data = {}
    if name not in data:
        return "Name not in data"
    data[name] = email

    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

    return f" {name}'s new email is {email}"

def create(name, email):
    if name == "" or email == "":
        return "Incorrect entry"
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
    else:
        data = {}

    if name in data:
        return
    data[name] = email

    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

    return f"Added {name} with email {email}"

def delete(name):
    if not os.path.exists(file_path):
        print("File does not exist.")
        return

    with open(file_path, 'r') as f:
        data = json.load(f)

    if name in data:
        del data[name]
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        return (f"Deleted: {name}")
    else:
        return (f"{name} not found in the data.")

def updateName(old_name, new_name):
    with open(file_path , 'r') as f:
        data = json.load(f)

    if old_name in data:
        data[new_name] = data.pop(old_name)
        with open(file_path , 'w') as f:
            json.dump(data, f, indent=4)
        return (f"Updated name from '{old_name}' to '{new_name}'")
    else:
        return (f"Name '{old_name}' not found in data.")
