import json
import os
import json
from Constants import __PROPERTIES_FILES, __SAVE_DIRECTORY, __set_current_user, __set_save_file


def choose_save():
    validID = False
    inputID = ""
    print("Chosen one. You have returned! What was your name again...\nLet's consult my journal. I write everything down!")
    for file_name in os.listdir(__SAVE_DIRECTORY):
            if ".json" in file_name:
                print(file_name[:5])

    while not validID:

        
        inputID = raw_input("Now which one here were you?")
        try:
            f = open(__SAVE_DIRECTORY + inputID + ".json")
        except IOError:
            print "Don't lie to me, boy!"
            continue
        validID = True
    __set_current_user(inputID)
    __set_save_file(inputID)
    print("Oh, of course I knew that.") 

def open_prop_files():
    with open(__PROPERTIES_FILES) as props:
        file_json = props.read()
    return json.loads(file_json)

    

def make_save(name):
    data = [ { "name" : name, "items" : [], "progress" : [] } ]
    with open(__SAVE_DIRECTORY + name + ".json", "wr") as outfile:
        json.dump(data, outfile)
    __set_current_user(name)
    __set_save_file(name)


def save_item_to_file(file_dict, thing_to_save, spot_to_save):
    """will return the file_dict, which should be saved later, on exit, except for the properties
       Tha should saved immediatly after
    """
    file_dict[spot_to_save] = thing_to_save
    return file_dict

def write_dict_to_file(file_name, dict_to_save):
    """takes the file name, and will overwrite the entire file with the correct dict."""
    with open(file_name, "w") as outfile:
        json.dump(dict_to_save, outfile)
    