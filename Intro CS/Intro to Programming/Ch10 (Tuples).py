# sort by the hour this time 


fname = input("Enter file name: ")
fhand = open(fname)
counts = dict()
times = list()
for line in fhand:
    email= line.split()
    if len(email) < 6 :
        continue
    email=email[5].split(':')
    if line.startswith("From"):
        counts[email[0]] = counts.get(email[0],0)+1
for key,val in counts.items():
    newtup=(key,val)
    times.append(newtup)
times=sorted(times)
for key,val in times:
    print(key,val)



