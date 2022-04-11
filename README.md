# Southern Linc Coding Challenge

## Brief Overview
Using Ruby, Python, or server-side JavaScript, write a simple command line program that:
• accesses a webpage,
• searches for occurrences of a particular word in the source of the downloaded page, printing the number of occurrences to the user,
• and then writes the webpage to disk with all occurrences of that word in the webpage source replaced with a second specified word.
Your program should take three command line arguments:
• URL of a webpage
• Word 1
• Word 2
As an example, we’ll expect to run your program like this:
$ ruby file_downloader.rb google.com apples bananas
Once this is executed, we might expect to see something like:
Downloading source of google.com… Parsing…
Found 24 occurrences of “apples”
Replaced all occurrences of “apples” with “bananas”
Saved new file as google.com.html


# The Program
## Specifications
The program was written with the above specifications using Python. 
It takes in 3 parameters as arguments. The first of which is the website.
The website is pulled using a GET request made by urllib3 and is then decoded with UTF-8 format for string parsing.


## Regex
For string parsing, I used the re import with the finditer method. This allows to pass in compiled regex strings for pattern matching.
You can pass in either a simple string or a regex pattern that can find matching.

## Character Index
Once the patterns have been matched, the character start and end position of the patterns are returned using a tuple.
Once the tuple is stored, we being replacing the patterns using a reverse for loop.

## Reverse Loop
The reverse loop is using in order to preserve character index as the string changes size. 
If the words are replaced from the end to the start, it won't matter if we continue to operate on an adjusted string.
The loop is quasi-recursive as it performs the looped operation on the data that is already being operated on.

## File Saving
The file is stored using the simple python methods of storing data.
The file is stored using the working directory (although it would be simple enough to pass in a 4th argument for directory)
The files full location is returned as not to confuse to user on where the file is stored.

## Error Handling
All aspects of the program have error handling using try-excepts. 
The Program will use a sys.exit when it encounters an error and in some places return the exception.




# USING THE PROGRAM
## Executing
Once you are in the working directory with your favorite command prompt, you can execute the program as below.

C:\Users\user\directory>py SoutherLincChallenge.py starfishstudios.org (?i)starfish(\s)studios REGEX

Note the second argument's regex pattern. You must pass in arguments as they relate to the import re patterns. 
Syntax for these expressions can be found here: https://docs.python.org/3/library/re.html

## Return
Your return should look something like this:
Sending Get Request to starfishstudios.org...
Decoding the page in UTF-8 Format.
Decoding Successful. Page Ready for Modification.
Searching page for '(?i)starfish(\s)studios'.
Found 6 occurrences of '(?i)starfish(\s)studios'.
All 6 occurrences of '(?i)starfish(\s)studios' were replaced.
Saving Modified Site to file...
Saved file to C:\Users\Austin Woods\Desktop\SoutherLinc\SoutherLincChallenge\SoutherLincChallenge\starfishstudios.org.html
Replacement Complete.










