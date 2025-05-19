
def fileWrite(fname):
    file_w = open(fname,'w')
    txt = input('Enter your text here: ')
    print('You have entered: ',txt)
    file_w.write(txt)
    print('File updated')
        
def fileRead(fname):
    file_r = open(fname)
    print(file_r.read())
    

try:
    filename = input('Enter file name: ')
    open(filename)
    #   demo.txt        where.data       mbox.txt   tracks.csv  dracula.txt

except:
    print('File not found. Please try again.')
    quit()


menu = input('File found.\nType 1 for read file. Type 2 for write file\n>')

if menu == '1':
    fileRead(filename)
elif menu == '2':  
    fileWrite(filename)
else:
    print('Invalid input.') 

