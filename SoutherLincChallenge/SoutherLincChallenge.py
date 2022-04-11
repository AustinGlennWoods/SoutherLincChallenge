import re
import sys
import urllib3


def findAndReplaceData(data, positions, newWord):
    #Replaces string of characters based on their start and end positions
    #Doing it be index allows for greater control over replacement
    newData = data[:positions[0]] + newWord + data[positions[1]:]
    print("Replaced characters at " + str(positions[0]) + " from " + data[positions[0]:positions[1]] + " to " + newData[positions[0]:positions[0]+len(newWord)])
    return newData


# Creating a PoolManager instance for sending requests.
http = urllib3.PoolManager()
print("Sending Get Request to " + sys.argv[1] + "...")
# Sending a GET request and getting back response as HTTPResponse object using parm 1
resp = http.request("GET", sys.argv[1])
# Storing the Data locally
webData = resp.data.decode("UTF-8")


#Finds all Occurences of the particular word 
#also uses finditer to allow regex to be passed in
matches = []
for match in re.finditer(sys.argv[2], webData):
    matches.append((match.start(), match.end()))


#Replaces words in reveresed order
#This is done in reversed as to safely maintain character position
for pos in reversed(matches):
    webData = findAndReplaceData(webData, pos, sys.argv[3])


#Write the modified data to a file 
print("Saving Modified Site to file...")
file = open(sys.argv[1]+".html", "w")
file.write(webData)
file.close()
