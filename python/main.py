from tabulate import tabulate
from classes import Material,Reaction,Element
            
def readCDE(filepath):
    """
    reads a file written in the format
    typical of Children of a Dead Earth
    """
    with open(filepath,'r') as f:
        raw = f.readlines()

    splitRaw = []
    for i in raw:
        if "\t" in i:
            a = i.split('\t')
            if '' in a:
                nl=[v for v in a if v != '']
            else:
                nl=a
        elif " " in i:
            nl=i.split(" ")
        elif i != '\n':
            nl = [i]
        else:
            pass
        nl = [h.rstrip() for h in nl]
        splitRaw.append(nl)

    return splitRaw


def parseCDE(filepath,identifier,itemclass):
    
    raw = readCDE(filepath)
    stuff = []
    for i in raw:
        if identifier in i:
            currIndex = raw.index(i)
            nextIndex = len(raw)-1
            
            for h in raw[currIndex+1:]:
                if identifier in h:
                    nextIndex = raw.index(h)
                    break
                
            stuff.append(raw[currIndex:nextIndex])
    ns = []
    
    for mat in stuff:
        nameStr = ''
        for i in mat[0][1:]:
            nameStr += i + ' '
        nameStr = nameStr[:-1]
        n = itemclass(nameStr)
        for matProp in mat[1:]:
            if len(matProp)==2:
                try:
                    setattr(n,matProp[0],float(matProp[1]))
                except ValueError:
                    setattr(n,matProp[0],matProp[1])
            else:
                proplist=[]
                for j in matProp[1:]:
                    try:
                        proplist.append(float(j))
                    except ValueError:
                        proplist.append(j)

                setattr(n,matProp[0],proplist)
        ns.append(n)

    return ns

alloy = parseCDE('Data/Materials/Alloys.txt','Material',Material)
ceramic = parseCDE('Data/Materials/Ceramics.txt','Material',Material)
combustable = parseCDE('Data/Materials/Combustables.txt','Material',Material)
compound = parseCDE('Data/Materials/Compounds.txt','Material',Material)
coolant = parseCDE('Data/Materials/Coolants.txt','Material',Material)
crystal = parseCDE('Data/Materials/Crystals.txt','Material',Material)
fiber = parseCDE('Data/Materials/Fibers.txt','Material',Material)
fissile = parseCDE('Data/Materials/Fissiles.txt','Material',Material)
fluid = parseCDE('Data/Materials/Fluids.txt','Material',Material)
fusile = parseCDE('Data/Materials/Fusiles.txt','Material',Material)
ion = parseCDE('Data/Materials/Ions.txt','Material',Material)
metal = parseCDE('Data/Materials/Metals.txt','Material',Material)
mineral = parseCDE('Data/Materials/Minerals.txt','Material',Material)
nbgas = parseCDE('Data/Materials/Noble Gases.txt','Material',Material)
nmetal = parseCDE('Data/Materials/Nonmetals.txt','Material',Material)
organic = parseCDE('Data/Materials/Organic Compounds.txt','Material',Material)
radionuclide = parseCDE('Data/Materials/Radionuclides.txt','Material',Material)

reactions = parseCDE('Data/ChemicalReactions.txt','ChemicalReaction',Reaction)
elements = parseCDE('Data/Elements.txt','Element',Element)

Element.buildPeriodic()
Material.buildReference()
Reaction.updateReference()


"""examples"""
print(Element.periodic['S'].AtomicMass)
print(Material.directory['Vanadium Chromium Steel'].Density_kg__m3)

