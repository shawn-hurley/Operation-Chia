import json
import os
import json
from Constants import __SAVE_DIRECTORY, __CURRENT_USER, __SAVE_FILE, __set_current_user

def check_save():
    try:
        os.rmdir(__SAVE_DIRECTORY)
    except OSError:
        return true
        #return os.listdir(__SAVE_DIRECTORY)
    os.mkdir(__SAVE_DIRECTORY)
    return false

def choose_save(lst):
    validID = false
    inputID = ""

    while not validID:
        print("Chosen one. You have returned! What was your name again...")
        "Let's consult my journal. I write everything down!"
        print(__SAVE_DIRECTORY)
        inputID = raw_input("Now which one here were you?")
        try:
            f = open(__SAVE_DIRECTORY + inputID + ".json")
        except IOError:
            print "Don't lie to me, boy!"
            continue
        validID = true
    __set_current_user(inputID)
    print "Oh, of course I knew that. Ready to save the world " + inputID + "?" 


def open_prop_files():
    file_json = open(__SAVE_FILES + "/" + __PROPERTIES_FILES).read()
    return json.loads(file_json)
    

def make_save(name):
    data = [ { "name" : name, "items" : [], "progress" : [] } ]
    with open(os.getcwd() + SAVE_FILE + "/" + name + ".json", "wr") as outfile:
        json.dump(data, outfile)
    __set_current_user(name)
