import os 

old_file = os.path.join("new-projects", "drivers.txt")
new_file = os.path.join("new-projects", "driver-info.txt")
os.rename("old file", "new file")

with open(new_file) as d:
    info = d.read() 