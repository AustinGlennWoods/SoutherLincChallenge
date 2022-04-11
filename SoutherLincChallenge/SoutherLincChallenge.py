import os
import re
import sys
import urllib3


def findAndReplaceData(data, positions, newWord):
    #Replaces string of characters based on their start and end positions
    #Doing it by index allows for greater control over replacement
    newData = data[:positions[0]] + newWord + data[positions[1]:]
    #Uncomment to see each replacement of each occurrence
    #print("Replaced characters at " + str(positions[0]) + " from " + data[positions[0]:positions[1]] + " to " + newData[positions[0]:positions[0]+len(newWord)])
    return newData






# Creating a PoolManager instance for sending requests.
http = urllib3.PoolManager()


# Sending a GET request and getting back response as HTTPResponse object using parm 1
try:
    print("Sending Get Request to " + sys.argv[1] + "...")
    resp = http.request("GET", sys.argv[1])
except:
    sys.exit("Failed to get page from " + sys.argv[1])


# Storing the Data locally
try:
    print("Decoding the page in UTF-8 Format.")
    webData = resp.data.decode("UTF-8")
    print("Decoding Successful. Page Ready for Modification.")
except:
    sys.exit("Failed to decode the page.")


#Finds all Occurrences of the particular word using finditer to allow regex to be passed in
matches = []
try:
    print("Searching page for '" + sys.argv[2] + "'.")
    regexInput = re.compile(sys.argv[2])
    for match in re.finditer(regexInput, webData):
        matches.append((match.start(), match.end()))
    print("Found " + str(len(matches)) + " occurrences of '" + sys.argv[2] +"'.")
except:
    sys.exit("Error. Failed to find occurrences.")


#Replaces words in reversed order
#This is done in reversed order as to safely maintain character positions
try:
    if (len(matches) > 0):
        for pos in reversed(matches):
            webData = findAndReplaceData(webData, pos, sys.argv[3])
        print("All " + str(len(matches)) + " occurrences of '" + sys.argv[2] + "' were replaced.")
    else:
        print("No occurrences were replaced since none were found.")
except Exception as e:
    print("There was an error replacing the values. See the following for more information.")
    sys.exit(e)


#Write the modified data to a file 
try:
    print("Saving Modified Site to file...")
    file = open(sys.argv[1]+".html", "w")
    file.write(webData)
    print("Saved file to " + os.getcwd() + "\\" + sys.argv[1] + ".html")
    file.close()
except Exception as e:
    print("There was an error writing data to file. See below for more information.")
    sys.exit(e)


print("Replacement Complete.")