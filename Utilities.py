def check_user_input_staic(answers, question):
    """This function will be used for checking the user input against the answer
        It is expected to ask the question as well as check the anser
        It will return either true or false depending on what you want.
    """
    user_input = raw_input(question)
    if user_input in answers:
        return True
    else
        return False
