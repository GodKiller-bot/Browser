import os
import requests
import sys

# write your code here
args = sys.argv
directory = args[1]
if not os.path.exists(directory):
    os.mkdir(directory)
#This is for specifying the directory in which the web pages will be stored
#You can comment the above part cause it won't run if it's not commented
stack = []
file_stack = dict()
a = 0
while a != 1:
    url = input()
    if ".com" in url:
        url_copy = url.rstrip(".com")
    else:
        url_copy = url.rstrip(".org")
    if url == "exit":
        a += 1

    elif url == "back":
        print(stack[-2])

    elif url == url_copy:
        for i in file_stack:
            if i == url:
                with open(file_stack[url], "r") as file1:
                    for line in file1:
                        print(line)

    elif (".com" in url) or (".org" in url):
        r = requests.get("https://" + url)
        if r:
            b = r.text
            print(b)
            url = os.path.join(directory, url_copy + ".txt")
            with open(url, "w") as file1:
                file1.write(b)
            stack.append(b)
            file_stack[url_copy] = url

        else:
            print("Error: Incorrect URL")
