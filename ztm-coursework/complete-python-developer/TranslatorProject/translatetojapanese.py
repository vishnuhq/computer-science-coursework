# Note that I named this file the same as traslate.py so it gave me an import error. (Circular Import)
from translate import Translator
translator = Translator(to_lang="ja")
try:
    with open("./test.txt", mode = "r") as test_file:
        lines = test_file.readlines()
        for line in lines:
            print(f'English: {line}')
            print(f'Japanese: {translator.translate(line)}\n')
except FileNotFoundError:
    print("The given file is not found.")