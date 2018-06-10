import os

with open("output.txt", "w") as a:
    for path, subdirs, files in os.walk(r'/var/www/html/songs/'):
       for filename in files:
         f = os.path.join(path, filename)
         a.write(f.replace("/var/www/html/","https://beyonitysoftwares.ml/")+ os.linesep) 
