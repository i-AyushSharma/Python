import shutil

shutil.copy("EgFile.txt", "main.py")
f = open("EgFile.txt", "w")
f.write("This file named 'main.py' is made by runnung the program file named 'ShutilModule' and will be deleted in next 30 seconds.")
f.close()

import os
import time

time.sleep(30)
os.remove("main.py")