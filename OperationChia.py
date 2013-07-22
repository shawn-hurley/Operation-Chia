from Utilities import check_user_input_staic
from EasterEggs import surprise_1
<<<<<<< Updated upstream
from Constants import __MAIN_MENU_TEXT, __PROPERTIES_FILES, __CONTINUE_GAME_TEXT, __CONTINUE_CONFIG_OPTIONS, __NEW_GAME_TEXT, \
__OPTIONS_TEXT, __WHAT_CHANGE_OPTIONS, __CHANGE_TO_TEXT
from SaveUtil import check_save, open_prop_files
=======
from Constants import __PROPERTIES_FILES, __MAIN_MENU_TEXT, __CONTINUE_GAME_TEXT, __NEW_GAME_TEXT, __OPTIONS_TEXT, __FIRST_NEW_GAME_TEXT, __FIRST_OPTIONS_TEST, __CURRENT_USER, __FIRST_TIME, __SAVE_DIRECTORY, __SAVE_FILE
import SaveUtil

>>>>>>> Stashed changes
def main_menu():
    """This will be the main menu"""
    #ls_of_games = check_save()
    #print 
    #print out menu
    print(__MAIN_MENU_TEXT)
<<<<<<< Updated upstream
    print(__CONTINUE_GAME_TEXT)
    print(__NEW_GAME_TEXT)
    print(__OPTIONS_TEXT)
    user_input = check_user_input_staic(["1","2","3","4"], "Select your choice! ")
=======
    #check to see if completely new game
    if __FIRST_TIME:
        print(__FIRST_NEW_GAME_TEXT)
        user_input = check_user_input_staic(["1", "3"], "Select your choice! ")
    #full options menu
    else:
        print(__CONTINUE_GAME_TEXT)
        print(__NEW_GAME_TEXT)
        print(__OPTIONS_TEXT)
        user_input = check_user_input_staic(["1","2","3","4"], "Select your choice! ")

>>>>>>> Stashed changes
    if user_input == "1":
        newID = raw_input("Wake up, my boy! There's a world out there that needs saving. By what name will you make yourself known?")
        make_save(newID)
        print("And here we go...")
        #start the game here

    if user_input == "2":
        if __FIRST_TIME:
            newID = raw_input("Wake up, my boy! There's a world out there that needs saving. By what name will you make yourself known?")
            make_save(newID)
            print("And here we go...")
            #start the game here
        else:
            choose_save()        
            print("And here we go...")
            #start the game here


    if user_input == "3":
<<<<<<< Updated upstream
        configure_options()
=======
        pass
>>>>>>> Stashed changes

    if user_input == "4":
        surprise_1()
        main_menu()

def configure_options():
    json_props_file = open_prop_files()
    #print out the properties nicely
    list_of_choices = []
    for index, option in enumerate(json_props_file):
        print(str(index+1) + ".) " + option + ": " + json_props_file[option])
        list_of_choices.append(str(index+1))

    #figure out what they want to change
    user_what_to_change = check_user_input_staic(list_of_choices, __WHAT_CHANGE_OPTIONS)
    #figure out what they want to change it to.
    user_what_change_to = check_user_input_staic(["true", "false"], __CHANGE_TO_TEXT)
    #call to write changes
    user_what_to_do = check_user_input_staic(["yes", "no"], __CONTINUE_CONFIG_OPTIONS)    
    if user_what_to_do == "yes":
        configure_options()
    else:
        main_menu()


if __name__ == "__main__":
    main_menu()
