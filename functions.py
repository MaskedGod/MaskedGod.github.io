FILE_PATH = r"D:\Anal Fuckery\Ardit\todo\web_todo\todos.txt"


def get_todos():
    """Read a text file and returns a list"""
    with open(FILE_PATH, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(data):
    """Write list of tasks into a text file"""
    with open(FILE_PATH, 'w') as file:
        file.writelines(data)

