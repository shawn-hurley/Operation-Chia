from Utilities import check_user_input_staic
from EasterEggs import surprise_1
from Constants import __PROPERTIES_FILES, __MAIN_MENU_TEXT, __CONTINUE_GAME_TEXT, __NEW_GAME_TEXT, __OPTIONS_TEXT 

def main_menu():
    """This will be the main menu"""
    try:
        prop_file = open(__PROPERTIES_FILES, "a")
    except Exception, e:
        raise e
    #print out menu
    print(__MAIN_MENU_TEXT)
    print(__CONTINUE_GAME_TEXT)
    print(__NEW_GAME_TEXT)
    print(__OPTIONS_TEXT)
    user_input = check_user_input_staic(["1","2","3","4"], "Select you choice! ")
    if user_input == "1":
        print("this will continue game")
    if user_input == "2":
        print("This will start a new game")
    if user_input == "3":
        pass
    if user_input == "4":
        surprise_1()
        main_menu()

if __name__ == "__main__":
    main_menu()
