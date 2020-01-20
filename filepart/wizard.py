from .utils import parse_size
from .utils import exceptions
from .utils import parts_exist
import os
from os import _exit
from os.path import exists, isfile


class Wizard:
    options = {}

    def __init__(self):
        self.cls()
        self.ask_loop()

    def cls(self):
        print("\n" * 100)

    def ask_loop(self):
        while 1:
            try:
                file_name = input("The name of the file: ")
            except KeyboardInterrupt:
                print()
                os._exit(0)
            self.cls()
            
            if file_name:
                if exists(file_name) and isfile(file_name):
                    self.options["mode"] = "split"
                else:
                    if parts_exist(file_name):
                        self.options["mode"] = "build"
                    else:
                        print(file_name + " does not exits.\n")
                        continue
                
                self.options["file"] = file_name                
                break
            else:
                print("You must give a file.\n")

        if self.options["mode"] == "split":
            while 1:
                print("File name: " + self.options["file"])
                try:
                    parts = input("Number of parts or size of parts: ")
                except KeyboardInterrupt:
                    self.cls()
                    self.ask_loop()
                    return
                self.cls()
                try:
                    parts = parse_size(parts)
                except exceptions.ValueError:
                    print("You must give a value.\n")
                    continue
                except exceptions.UnitError:
                    print("You must give a valid unit.\n")
                    continue
                except exceptions.SizeError:
                    print("You must give a bigger value.\n")
                    continue
                except exceptions.InvalidValue:
                    print("You must give a valid value.\n")
                    continue
                except Exception as error:
                    print(f"{__name__}: error: " + error)
                    os._exit(0)

                print("File name:  " + self.options["file"])
                print("File parts: " + parts["formatted"])
                self.options["parts"] = parts
                break
        else:
            print("File name: " + self.options["file"])

        while 1:
            try:
                out = input("Output folder (optional): ")
            except KeyboardInterrupt:
                self.cls()
                self.ask_loop()
                return
            self.cls()
            print("File name:  " + self.options["file"])
            if self.options["mode"] == "split":
                print("File parts: " + self.options["parts"]["formatted"])
            
            if out:
                if exists(out) and not isfile(out):
                    self.options["output"] = out
                    break
                else:
                    print(out + " does not exist.\n")
                    continue
            else:
                self.options["output"] = "./"
                break

        self.cls()
        print("File name:     " + self.options["file"])
        if self.options["mode"] == "split":
            print("File parts:    " + self.options["parts"]["formatted"])
        print("Output folder: " + self.options["output"])