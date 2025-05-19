print(' This is Data Cleaning')

# Removing unwanted symbols from text

txt = 'These@programs#are being$done.on<python>in@Visual$Studio'
clean = ''

for x in txt:
    if x.isalpha() or x.isspace():
        clean = clean + x

    else:
        clean = clean + ' '


print(clean)