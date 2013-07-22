import json
import os
import json
from Constants import __SAVE_DIRECTORY, __set_current_user, __set_save_file


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
    file_json = open(__SAVE_DIRECTORY + __PROPERTIES_FILES).read()
    return json.loads(file_json)
    

def make_save(name):
    data = [ { "name" : name, "items" : [], "progress" : [] } ]
    with open(__SAVE_DIRECTORY + name + ".json", "wr") as outfile:
        json.dump(data, outfile)
    __set_current_user(name)
    __set_save_file(name)

