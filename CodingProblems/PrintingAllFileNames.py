import os, glob
os.chdir("I:\\pictures")

print("------printing all image file names having extension .jpg---------")
for file in glob.glob("*.jpg"):
    print(file)

print("------printing all the directory names present inside curr dir ----")
path = "."
files = os.listdir(path)
for name in files:
    print(name)

print("------printing file names having numeric name like 1.txt, 2.exe etc --")
for file in glob.glob('./[0-9].*'):
    print(file)

# print(glob.glob('./[0-9].*'))