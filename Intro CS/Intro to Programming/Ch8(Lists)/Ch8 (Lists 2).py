

#
fname = input("Enter file name: ")
fhand = open(fname)
count = 0
for line in fhand:
    line.strip()
    cut= line.split()
    if len(cut) < 2 :
        continue
    if line.startswith("From"):
        print(cut[1])
        count += 1
print("There were", count, "lines in the file with From as the first word")
