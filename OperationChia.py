from Utilities import check_user_input_staic
from EasterEggs import surprise_1

def main_menu():
    """This will be the main menu"""
    try:
        prop_file = open(PROP_FILE_PATH, "a")
    except Exception, e:
        raise e
    #print out menu
    print()
    user_input = check_user_input_staic(["1","2","3","4"], "Select you choice!")
    if user_input == "1":
        pass
    if user_input == "2":
        pass
    if user_input == "3":
        pass
    if user_input == "4":
        surprise_1()
        main_menu()

if __name__ == "__main__":
    main_menu()