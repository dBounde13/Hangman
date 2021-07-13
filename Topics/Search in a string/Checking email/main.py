def check_email(string):
    if "@" in string and " " not in string and "." in string and string.rfind('.') > string.find('@') + 1:
        return True
    else:
        return False
