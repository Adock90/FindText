import os
import sys
import re

if len(sys.argv) < 3 or sys.argv[1] == "--h":
    print("findText.py: HELP\npython3 findText.py <Text> <FileType> <logging>:\n\t<Type>: Specifies either 1 file '--file' or a whole directory '--dir'.\n\t<Text>: Phrase to look for.\n\t<logging>: Optional but if set --verbose prints errors.")
    sys.exit(1)

FindText = sys.argv[1]
Where = sys.argv[2]
Type = sys.argv[3]
Error = ""

try:
    Error = sys.argv[4]
except:
    pass

def ParseDirs(Where=Where, FindText=FindText, Error=Error):
    for root, dirs, files in os.walk(Where):
        for filename in files:
            filepath = os.path.join(root, filename)
            try:
                if Error == "--very-verbose":
                    print(f"Opening {filepath}")
                with open(filepath, "r") as ReadFile:
                    content = ReadFile.read().splitlines()
                    i = 0
                    for line in content:
                        i+=1
                        if re.search(FindText, line):
                            print(filepath+": "+str(i)+" "+line)
            except UnicodeDecodeError:
                pass
            except:
                if Error == "--verbose" or Error == "--very-verbose":
                    print(f"Failed to open {filepath}")
            
        for dirname in dirs:
            ParseDirs(Where=dirname)


if Type == "--file":
    if os.path.exists(Where):
        try:
            if Error == "--very-verbose":
                    print(f"Opening {Where}")
            with open(Where, "r") as ReadFile:
                content = ReadFile.read().splitlines()
                i = 0
                for line in content:
                    i+=1
                    if re.search(FindText, line):
                        print(str(i)+" "+line)
        except:
            if Error == "--verbose" or Error == "--very-verbose":
                print(f"Failed to open {Where}")
    else:
        if Error == "--verbose" or Error == "--very-verbose":
            print(f"{Where} doesn't exist")
elif Type == "--dir":
    ParseDirs(Where=Where)
else:
    print("findText.py: HELP\npython3 findText.py <Text> <FileType> <logging>:\n\t<Type>: Specifies either 1 file '--file' or a whole directory '--dir'.\n\t<Text>: Phrase to look for.\n\t<logging>: Optional but if set --verbose prints errors.")
    sys.exit(1)