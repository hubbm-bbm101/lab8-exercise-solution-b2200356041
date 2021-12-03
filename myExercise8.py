import sys
info_dict = {}

file = open(sys.argv[1],"r")
for item in file:
    name = item.split(":")[0]
    info_dict[name] = (item.split(":")[1].split(","))
try:
    for x in sys.argv[2].split(","):
        uni = info_dict[x][0]
        dep = info_dict[x][1]
        print("name:", x ,",University:", uni ,",Department:",dep)
except KeyError:
    print("no name called" ,x, "found in students list!!")









