import argparse
import sys
import pathlib
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "folder",
        metavar="FOLDER",
        nargs="?",
        default="./test",
    )
    parser.add_argument(
        "search",
        metavar="search",
        nargs="?",
        default="old",
    )
    parser.add_argument(
        "replace",
        metavar="replace",
        nargs="?",
        default="new",
    )
    args = parser.parse_args()
    folder = pathlib.Path(args.folder)
    search = args.search
    replace = args.replace
    if not folder.is_dir():
        print("The specified folder doesn't exist")
        sys.exit()
    renamer = Renamer(folder, search, replace)
    renamer.renameFiles()



class Renamer():
    def __init__(self, folder, search, replace):
        self._folder = folder
        self._search = search
        self._replace = replace

    def renameFiles(self):
        print(self._folder)
        print(self._search)
        print(self._replace)

        for filename in os.listdir(self._folder):
            if self._search in filename:
                new_filename = filename.replace(self._search, self._replace)
                old_path = os.path.join(self._folder, filename)
                new_path = os.path.join(self._folder, new_filename)
                os.rename(old_path, new_path)
