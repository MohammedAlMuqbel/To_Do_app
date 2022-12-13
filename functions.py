def get_to_do(filepath="Data.txt"):
    """ Read a text file and
    return the list of to_do items"""
    with open(filepath, 'r') as file_local:
        to_do = file_local.readlines()
    return to_do


def write_to_do(y,filepath="Data.txt" ):
    """ Write the to_do items list
    in the text file"""
    with open(filepath, 'w') as file_1:
        file_1.writelines(y)


if __name__=="main":
    print(get_to_do())