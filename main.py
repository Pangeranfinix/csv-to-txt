import csv,string

path = input("> Masukan file path : ")
o = open(path)
data = csv.reader(o)
s = string.ascii_uppercase
a = input("Masukan Kolom (A / B / C) : ")
i = s.find(a.upper())
with open(path.replace(".csv",".txt"),"w") as f:
 for x in data:
  print(">> Write "+x[i])
  f.write(x[i]+"\n")
print("")
