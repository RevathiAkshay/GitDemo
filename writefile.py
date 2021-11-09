## to open the file and assign to object in read mode

with open('C:/Users/Public/test/test1.txt', 'r') as ofile1:

    ## to read into an object in the list
    line1 = ofile1.readlines()

    # to open the file again in write mode
    with open('C:/Users/Public/test/test1.txt', 'w') as ofile2:

        # write the file in reversed mode into the file
        for l1 in reversed(line1):
            ofile2.write(l1)

    # Open the file in read mode and print the file content
    with open('C:/Users/Public/test/test1.txt', 'r') as ofile2:
        line2 = ofile2.readlines()
        for l2 in (line2):
            print(l2)

