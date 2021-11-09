## To open an existing file through Python
ofile = open('C:/Users/Public/test/test1.txt')

#read contents 1 by 1
fso = ofile.readline()
while fso != "":
    print(fso)
    fso = ofile.readline()


ofile.close()
