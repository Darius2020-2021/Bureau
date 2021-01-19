import os
import shutil
source ="Bureau\java\mali.txt"
target= "Image\mali.txt"
shutil.copy(source, target)
os.remove(source)

