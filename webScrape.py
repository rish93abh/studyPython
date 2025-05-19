import urllib.request, urllib.parse, urllib.error

link = 'https://www.dr-chuck.com/page1.htm' # any URL link

fhand = urllib.request.urlopen(link)

for lines in fhand:
    print(lines.decode().strip())
