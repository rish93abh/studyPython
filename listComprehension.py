print ("This is List Comprehension")

a = [x for x in range(1,6)]
print(a)

b = [x for x in '8421847']
print(b)

c = [int(x) for x in '8421847']
print(c)

d = [x.lower() for x in 'hElLo WorLD']
print(d)

e = [x for x in 'S@up4!er6*man&Ba7%t$46m#a@2n0' if x.isalpha()]    # x.isalpha()
print(e)