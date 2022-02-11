fileName = input("Insert input File Name: ")
fileR = open(fileName, "r")
fileW = open(fileName[:-3]+"_4_lines.py", "w")
content = fileR.readlines()
fileR.close()
fileW.write("import os\nopen('output.py','w').write('")
for line in content:
    for char in line: 
        fileW.write(char.replace("'",'"').replace("\\","\\\\").replace("\n",""))
    fileW.write("\\n")
fileW.write("')\nos.system('python3 output.py')\nos.remove('output.py')")
fileW.close()