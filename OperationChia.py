import os
from Utilities import check_user_input_staic
from EasterEggs import surprise_1
from GameControler import GameControler
from SaveUtil import open_prop_files, choose_save, make_save, save_item_to_file, write_dict_to_file, open_save_file
from Constants import __PROPERTIES_FILES, __MAIN_MENU_TEXT, __WHAT_CHANGE_OPTIONS, __CONTINUE_CONFIG_OPTIONS, __CHANGE_TO_TEXT,  __CONTINUE_GAME_TEXT, __NEW_GAME_TEXT, \
__OPTIONS_TEXT, __FIRST_TIME, __SAVE_DIRECTORY

game_controller = GameControler()
def main_menu():
    """This will be the main menu"""
    #ls_of_games = check_save()
    #print 
    #print out menu
    #check to see if completely new game
    if __FIRST_TIME:
        print(__MAIN_MENU_TEXT)
        print(__NEW_GAME_TEXT)
        print(__OPTIONS_TEXT)
        user_input = check_user_input_staic(["1", "3"], "Select your choice! ")
    #full options menu
    else:
        print(__MAIN_MENU_TEXT)
        print(__NEW_GAME_TEXT)
        print(__CONTINUE_GAME_TEXT)
        print(__OPTIONS_TEXT)
        user_input = check_user_input_staic(["1","2","3","4"], "Select your choice! ")

    if user_input == "1":
        newID = raw_input("Wake up, my boy! There's a world out there that needs saving. By what name will you make yourself known?")
        make_save(newID)
        prop_dict = open_prop_files()
        save_dict = open_save_file()
        game_controller.set_game_controler(prop_dict, save_dict)
        

    if user_input == "2":
        if __FIRST_TIME:
            newID = raw_input("Wake up, my boy! There's a world out there that needs saving. By what name will you make yourself known?")
            make_save(newID)
        else:
            choose_save() 
        
        prop_dict = open_prop_files()
        save_dict = open_save_file()
        game_controller.set_game_controler(prop_dict, save_dict)     

    if user_input == "3":
        configure_options()
        pass

    if user_input == "4":
        surprise_1()
        main_menu()

    ready = "no"
    while ready != "yes":
	ready =  raw_input("Ready to save the world? (yes/no)")

    print("And so we go...")
    game_controller.get_next_level()


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
    json_props_file = save_item_to_file(json_props_file, user_what_change_to, json_props_file.keys()[int(user_what_to_change)-1])
    #Actually write to file.
    write_dict_to_file(__PROPERTIES_FILES, json_props_file)
    print json_props_file
    user_what_to_do = check_user_input_staic(["yes", "no"], __CONTINUE_CONFIG_OPTIONS)    
    if user_what_to_do == "yes":
        configure_options()
    else:
        main_menu()


if __name__ == "__main__":
    main_menu()
