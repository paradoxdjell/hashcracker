print "\n\nHello!";
print "\nThis is a simple hashcracker I wrote in Python.";
print "\nYou can find this on http://github.com/paradoxdjell/hashcracker"
print "\nFeel free to use your own wordlist. Just replace words.txt with your own file and ensure it is named words.txt.";

inp = raw_input("\nEnter the md5 sum: ")
print "\nYou entered ", inp

class A:
    def assignment(self):
        line = fh.readline()

a = A()

import hashlib

fh = open("words.txt", "r")

flag = 0;

for line in fh:
    a.assignment
    s = hashlib.md5(line.encode())
    if inp == s.hexdigest():
        print "\nMatch found! - ", line
        flag = 1;
        break

if flag == 0:
    print "\nNo match found."

fh.close();
