import json
import os
<<<<<<< Updated upstream
import json
from Constants import __SAVE_FILES, __PROPERTIES_FILES
def check_save():
    try:
        os.rmdir(__SAVE_FILES)
    except OSError as ex:
        if ex.errno == ENOTEMPTY:
            return os.listdir(__SAVE_FILES)
    os.mkdir(__SAVE_FILES)
    return []
=======
from Constants import __SAVE_DIRECTORY_1, __CURRENT_USER, __SAVE_FILE, __set_current_user

def check_save():
    try:
        os.rmdir(__SAVE_DIRECTORY)
    except OSError:
        return true
        #return os.listdir(__SAVE_DIRECTORY)
    os.mkdir(__SAVE_DIRECTORY)
    return false
>>>>>>> Stashed changes

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

<<<<<<< Updated upstream
    else:
        while not validID:
            inputID = raw_input("Chosen one. You have returned! What was your name again...")
            try:
                f = open(inputID)
            except IOError:
                print "Don't lie to me, boy!"
                continue
            print "Oh, of course I knew that. Ready to save the world " + inputID + "?" 
            return f
         
#def readSave(f):
#    SaveData saveInfo = new SaveData(f)
#    f.seek(os.SEEK_CUR)


def makeSave(name):
    f = open(name, w)
    f.write("character_name = " + name)
    f.close

def open_prop_files():
    file_json = open(__SAVE_FILES + "/" + __PROPERTIES_FILES).read()
    return json.loads(file_json)
    
    
=======
    __set_current_user(inputID)
    print "Oh, of course I knew that. Ready to save the world " + inputID + "?" 

def make_save(name):
    data = [ { "name" : name, "items" : [], "progress" : [] } ]
    with open(os.getcwd() + SAVE_FILE + "/" + name + ".json", "wr") as outfile:
        json.dump(data, outfile)
    __set_current_user(name)
>>>>>>> Stashed changes
