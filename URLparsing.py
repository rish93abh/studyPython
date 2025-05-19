print(' This is URL parsing.')

url = input("Enter the URL: ")


protocol = url[ :url.find(':')]
# find method within slicing of string
print('Protocol: ',' '*(20 - len(protocol) - 8),protocol)



dot1 = url.find('.')
dot2 = url.find('.',dot1 + 1)
# find method for second dot
domain = url[dot1+1:dot2]
print('Domain: ',' '*(20 - len(domain) - 6),domain)



slashp = url.find('/',dot2)
slashl = url.find('/',slashp + 1)
webpage = url[slashp:slashl]
print ('Webpage: ',' '*(20 - len(webpage) - 7),webpage)



# https://www.udemy.com/course/
input()