print(' This is Anagrams project')


p = input("Enter 1st word: ")
q = input("Enter 2nd word: ")

s1 = p.lower()
s2 = q.lower()

# taste
# state


for x in s1:
    if s1.count(x) != s2.count(x):
        print(p,'and',q,'are not Anagrams.')
        break
    
else:
    print(p,'and',q,'are Anagrams.')
