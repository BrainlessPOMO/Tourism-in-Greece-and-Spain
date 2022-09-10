from os.path import exists as file_exists
from os import remove


def main():
    file_path = 'webpageInfo.db'
    if file_exists(file_path) == False:
        return 0

    remove(file_path)
    return 1


main()
