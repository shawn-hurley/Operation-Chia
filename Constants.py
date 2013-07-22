import os


__SAVE_DIRECTORY = "gameData/"

#Constant to see if the player has played before

def __set_first_time():
    try:
        os.mkdir(__SAVE_DIRECTORY)
    except OSError:
        if any(".json" in file_name for file_name in os.listdir(__SAVE_DIRECTORY)):
            return False
    return True

__PROPERTIES_FILES = "properties.prop"
__MAIN_MENU_TEXT = "\n\n\n\t\tOperation Chia \n\tMake your choice of what to do next."
__WHAT_CHANGE_OPTIONS = "What would you like to change? "
__CHANGE_TO_TEXT = "What would you like to change it to? pick either true or false. "
__CONTINUE_CONFIG_OPTIONS = "Would you like to continue editing the options?(yes or no) "
__FIRST_TIME = __set_first_time()
__NEW_GAME_TEXT = "Choose 1 to start a new game"
__CONTINUE_GAME_TEXT = "Choose 2 to continue your game"
__OPTIONS_TEXT = "Choose 3 to configure your options"
__CURRENT_USER = "Chi4M4sT3R"
__SAVE_FILE = __SAVE_DIRECTORY + __CURRENT_USER + ".json"

#Setters for current game info
def __set_current_user(name):
    __CURRENT_USER = name


def __set_save_file(name):
    __SAVE_FILE = __SAVE_DIRECTORY + __CURRENT_USER + ".json"

