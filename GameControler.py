from Constants import *

class GameControler(Object):
    """This class is a singleton. it will use a static string to declare itself. This should be
       generated, should be checked at begining of game. We will have to make a mechinism for a new
       or continued game to reset this. This should contain the user's save game file as a dict and open
       it should also have the properties file dict open and ready.
     """
     unique_id  = random_string()

    def set_game_controler(self, properties_dict, user_save_dict):
        """Should set the game controler up for use"""
        self.__properties_dict = properties_dict
        self.__user_save_dict = user_save_dict

    def get_property(property):
        return self.__properties_dict[property]

    def get_item(item):
        if item in self.__user_save_dict["item"]:
            return self.__user_save_dict["item"][item]
        else:
            return False

    def get_next_level():
        module =__import__(__get_next_level())
        func = getattr(module, "start")
        func()
        #This is so that control flow should come back here(can implement a true false here)
        get_next_level_or_quit()

    def __get_next_level():
        number = self.__user_save_dict["progress"][7:]
        number += 1
        return "Chapter" + str(number)


    def get_next_level_or_quit():
        pass