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


def getEmissions():
    with open('Data/EmissionLines.txt','r') as f:
        raw = f.readlines()

    emissionDict = {}
    sep = []
    for l in raw:
        if 'SPECTRA' in l:
            sep.append(raw.index(l))
    for i in range(len(sep)):
        start = sep[i]
        if i < len(sep)-1:
            end = sep[i+1]
        else:
            end = len(raw)
        newEm = raw[start:end]
        newEmStrip = [r.rstrip() for r in newEm]

        emissionDict.update({newEm[0].replace('SPECTRA ','').rstrip():newEmStrip})

    return emissionDict

    
