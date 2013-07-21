import os
SAVE_FILES = ~chia

def checkSave():
    try:
        os.rmdir(SAVE_FILES)
    except OSError as ex:
        if ex.errno == errno.ENOTEMPTY:
            return os.listdir(SAVE_FILES)
    os.mkdir(SAVE_FILES)
    return []

def chooseSave(lst):
    print lst
    validID = false

    if not lst:
        newID = raw_input("Wake up, my boy! There's a world out there that needs saving. By what name will you make yourself known?")
        f = open(newID, w)
        return f

    else:
        while !validID:
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

