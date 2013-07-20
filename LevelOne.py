from Utilities import check_user_input_staic

def start_level():
    """This will start the first level and will eventually give control back to the 
        driver so that they can either move on or save progress. This is a complete 
        command line/python interper game
    """

    #this make sure that the first problem is completed if failed it will start over

    while(!first_problem()):
        pass


def first_problem():
    """First problem will disscuss the importance of the user and do the first lesson dealing with
        proccedurces(math functions), boolean, and Strings
    """
    #This will be the opening dialog, explain the orgin storry and waht the overall goals of the game
    game_intro()
    