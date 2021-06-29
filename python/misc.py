def shortHand(string,length,shorthand='...'):
    string = str(string)
    if length<len(shorthand):
        raise Exception("string '{}' is too long\
for specified length: {}".format(string,length))
    if len(string)>length:
        return '{}{}'.format(string[:length-len(shorthand)],shorthand)
    else:
        return '{0:^{1}}'.format(string,length)


def cocatenate(string):
    return string.replace('Microscopic','μ').replace('Gamma','γ')

with open('Data/EmissionLines.txt','r') as f:
    raw = f.readlines()
    sep = []
    for l in raw:
        if 'SPECTRA' in l:
            sep.append(raw.index(l))

    print(sep)
            
