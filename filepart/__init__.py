import sys, getopt
from .__main__ import __version__

from .utils import Help
from .wizard import Wizard
from .split import Splitter
from .build import Builder

def main(argv=None):
    if argv == None:
        argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, "hvsbp:o:", ["help", "version", "split", "build", "parts=", "output="])
    except getopt.GetoptError:
        print(Help.SHORT)
        sys.exit(2)

    print(opts)
    print(args)

    if len(opts) > 0:
        mode = ""
        file = args[0] if len(args) > 0 else ""
        parts = ""
        output = ""

        for opt, arg in opts:
            if opt in ("-h", "--help"):
                print(Help.LONG)
                sys.exit(0)
            
            elif opt in ("-v", "--version"):
                print(__version__)
                sys.exit(0)
            
            elif opt in ("-s", "--split"):
                mode = "split"

            elif opt in ("-b", "--build"):
                mode = "build"
            
        if not file:
            print(Help.SHORT)
            print(f"\n\n{__name__}: error: You must provide a file.")
            sys.exit(2)

        for opt, arg in opts:
                if opt in ("-p", "--parts"):
                    parts = arg
                
                elif opt in ("-o", "--output"):
                    output = arg

        if mode == "split":
            if not parts:
                print(Help.SHORT)
                print(f"\n\n{__name__}: error: You must provide the parts.")
                sys.exit(2)
        
        if not output:
            output = "./"

        if mode == "split":
            splitter = Splitter(
                file=file,
                parts=parts,
                output=output
            )
            splitter.split()
        
        elif mode == "build":
            builder = Builder(
                file=file,
                output=output
            )
            builder.build()

    else:
        wizard = Wizard()
        mode = wizard.options["mode"]
        file = wizard.options["file"]
        if mode == "split":
            parts = wizard.options["parts"]
        output = wizard.options["output"]

        if mode == "split":
            splitter = Splitter(
                file=file,
                parts=parts,
                output=output
            )
            splitter.split()
        
        elif mode == "build":
            builder = Builder(
                file=file,
                output=output
            )
            builder.build()