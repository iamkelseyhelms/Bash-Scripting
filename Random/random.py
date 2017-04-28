#
# Author: Kelsey Helms
# Date Created: February 21, 2017
# Filename: random.py
#
# Overview: This program randomly generates 10 lowercase letters,
# prints them and adds them to files, randomly generates 2 numbers,
# prints them, multiplies them, and prints the product
#

from random import randint

###################################
#           Variables             #
###################################

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


###################################
#           Functions             #
###################################

# return letter from random index of alphabet array
def randomLetter():
    return alphabet[randint(0, 25)]


# create files with 10 lowercase letters
def createFiles(x):

    # holds all files for easy open access in for loop
    allFiles = []

    # for all files
    for i in range(0, x):

        # create file with correct number name
        allFiles.append('file' + str(i + 1) + '.txt')

        # open file and create file content string
        thisFile = open(allFiles[i], "w")
        fileContents = ""

        # for all 10 lowercase letters
        for j in range(10):

            # get random letter
            newLetter = randomLetter()

            # add it to file and file contents
            thisFile.write(newLetter)
            fileContents += newLetter

        # print file contents
        print("File " + str(i + 1) + " Contents: " + fileContents)

        # add newline to file and close file
        thisFile.write('\n')
        thisFile.close()


# generates 2 random integers and multiplies them
def randomProduct():

    # 2 ints in the range 1-42 inclusive
    x = randint(1, 42)
    y = randint(1, 42)

    # multiply 2 ints
    product = x * y

    # print 2 ints and product
    print(str(x) + '\n' + str(y) + '\n' + str(product))


###################################
#             Main                #
###################################

def main():

    # create 3 files
    createFiles(3)

    # generate random product of 2 ints
    randomProduct()


# run everything!
main()
