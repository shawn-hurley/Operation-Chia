import os
from SaveUtil import __check_save

__PROPERTIES_FILES = "properties.prop"
__MAIN_MENU_TEXT = "\n\n\n\t\tOperation Chia \n\tMake your choice of what to do next."
__CONTINUE_GAME_TEXT = "Choose 1 to continue your game"
__NEW_GAME_TEXT = "Choose 2 to start a new game"
__OPTIONS_TEXT = "Choose 3 to configure your options"
__SAVE_FILES = "gameData"
__WHAT_CHANGE_OPTIONS = "What would you like to change? "
__CHANGE_TO_TEXT = "What would you like to change it to? pick either true or false. "
__CONTINUE_CONFIG_OPTIONS = "Would you like to continue editing the options?(yes or no) "
__MAIN_MENU_TEXT = "\t\tOperation Chia \n\tMake your choice of what to do next."
__FIRST_TIME = __set_first_time()
__FIRST_NEW_GAME_TEXT = "Choose 1 to start a new game"
__FIRST_OPTIONS_TEST = "Choose 3 to configure your options"
__NEW_GAME_TEXT = "Choose 1 to start a new game"
__CONTINUE_GAME_TEXT = "Choose 2 to continue your game"
__OPTIONS_TEXT = "Choose 3 to configure your options"
__SAVE_DIRECTORY_1 = os.getcwd + "/gameData/"
__CURRENT_USER = __set_current_user("Chi4M4sT3R")
__SAVE_FILE = __SAVE_DIRECTORY + __CURRENT_USER + ".json"



def __set_current_user(name):
    __CURRENT_USER = name
    __SAVE_FILE = __SAVE_DIRECTORY + __CURRENT_USER + ".json"


def __set_first_time():
    if check_save:
        __FIRST_TIME = false
    else:
        __FIRST_TIME = true
