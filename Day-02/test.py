# Conditional Handling (if,else,elif)

import sys

type = sys.argv[1]

if type == "t2.micro" :
    print ("this is the right instance type")
elif type == "t3.micro":
    print ("you will be charged two dollar a day")
elif type == "t3.medium":
    print ("you will be charged four dollar a day")
elif type == "t3.xlarge":
    print ("you will be charged eight dollar a day")

else :
    print ("this is an incorrect instance type")
