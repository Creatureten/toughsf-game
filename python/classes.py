from misc import shortHand, cocatenate, getEmissions
from constants import R as R


class Material:
    """
    a class intended to capture and represent
    material properties
    """

    directory = {}

    def __init__(self, name=None):
        self.Name = name
        Material.directory.update({repr(self): self})

    def __repr__(self):
        return self.Name

    def __str__(self):
        return self.Name

    def molW(self):
        molM = 0
        for e, ec in zip(self.Elements, self.ElementCount):
            molM += e.MolarMass_g__mol * ec
        return molM

    def show(self):
        """
        debugging function to prettyprint
        all the material properties
        """
        propDict = vars(self)
        print("{}".format(self.Name))
        for k, v in zip(propDict.keys(), propDict.values()):
            if k == "Name":
                pass
            elif isinstance(v, list):
                print("|\{:}".format(k))
                vstr = ""
                for i in v:
                    vstr += "{:^10}".format(shortHand(i, 9))
                print("| \{:}".format(vstr))
            else:
                print("|\{:_<40}{:_>20}".format(k, v))

        print("\n")

    def buildReference():
        for m in Material.directory.values():
            m._housekeep()

    def _housekeep(self):
        """
        housekeeping function that must be performed once the
        ingestion of data is complete to not break later code

        transcribes element makeup information from string form
        into actual element references
        """
        propDict = vars(self)
        vals = ["Elements", "ElementCount"]
        for (k, v) in zip(vals, [propDict[i] for i in vals]):
            if isinstance(v, str):
                # we are dealing with a element symbol here
                if v in Element.periodic.keys():
                    setattr(self, k, [Element.periodic[v]])
            elif isinstance(v, float):
                # we are handling ElementCount here.
                setattr(self, k, [v])
            elif isinstance(v, list):
                nl = []
                for m in v:
                    if m in Element.periodic.keys():
                        nl.append(Element.periodic[m])
                    else:
                        nl.append(m)
                setattr(self, k, nl)


class Reaction:
    """
    a class intended to capture and represent
    reactions
    """

    directory = {}

    def updateReference():
        for r in Reaction.directory.values():
            r._housekeep()

    def __init__(self, name=None):
        self.Name = name
        Reaction.directory.update({repr(self): self})

    def __repr__(self):
        return self.Name

    def _housekeep(self):
        """
        housekeeping function that must be performed once the
        ingestion of data is complete to not break later code

        transcribes material in string form into actual references
        """
        propDict = vars(self)
        vals = ["Reactants", "ReactantCounts", "Products", "ProductCounts"]
        for (k, v) in zip(vals, [propDict[i] for i in vals]):
            if isinstance(v, str):
                # the reaction only involves one Reactants
                if v in Material.directory.keys():
                    setattr(self, k, [Material.directory[v]])
            elif isinstance(v, float):
                # we are handling either ReactantCounts or the ProductCounts
                setattr(self, k, [v])
            elif isinstance(v, list):
                nl = []
                for m in v:
                    if m in Material.directory.keys():
                        nl.append(Material.directory[m])
                    else:
                        nl.append(m)
                setattr(self, k, nl)

    def dH(self):
        # by convention, the kj/mol here denotes one unit of reaction,
        # and does not equate a single mole of reactant!!!
        h0 = 0
        for (r, rn) in zip(self.Reactants, self.ReactantCounts):
            # default to 0: element （单质）doesn't have EoF
            # eg, metals, graphite, etc.,
            h0 += getattr(r, "EnthalpyOfFormation_kJ__mol", 0) * rn
        h1 = 0
        for (p, pn) in zip(self.Products, self.ProductCounts):
            h1 += getattr(p, "EnthalpyOfFormation_kJ__mol", 0) * pn
        return h1 - h0

    def adbT(self):
        # calculates the specfic heat of all the products
        specHeat = 0  # j/k
        for (p, pn) in zip(self.Products, self.ProductCounts):
            specHeat += p.molW() * pn / 1000 * p.SpecificHeat_J__kg_K

        # by convention, a negative enthalpy change equals
        # an exothermic reaction.

        return -1 * self.dH() * 1000 / specHeat

    def spGasR(self):
        """calculates the specific gas constant of the reactants"""
        sigmaM = 0
        sigmaN = 0
        for p, pn in zip(self.Products, self.ProductCounts):
            sigmaM += p.molW() * pn / 1000
            sigmaN += pn

        return R / (sigmaM / sigmaN)

    def show(self):
        """
        debugging function to prettyprint
        all the chemical reactions
        """

        dH = self.dH()

        propDict = vars(self)

        print("{}".format(self.Name))

        reactants = propDict["Reactants"]
        reactantCount = propDict["ReactantCounts"]
        products = propDict["Products"]
        productCount = propDict["ProductCounts"]

        print("|\\", end="")

        rea = ""
        for (r, rn) in zip(reactants, reactantCount):
            rea += "+ {:.0f} {} ".format(rn, str(r))
        pro = ""
        for (p, pn) in zip(products, productCount):
            pro += "+ {:.0f} {} ".format(pn, str(p))

        print("{}--->{}".format(rea[1:], pro[1:]))
        try:
            print(
                "|\ΔH={:.2f} kJ/mol,Ea={:.2f} kJ/mol".format(
                    dH, propDict["ActivationEnergy_kJ__mol"]
                )
            )
        except KeyError:
            print("|\ΔH={:.2f} kJ/mol".format(dH))
        try:
            print("|\Autoignition={}K".format(propDict["AutoignitionTemperature_K"]))
        except KeyError:
            pass
        try:
            print(
                "|\Characteristics Length={}m".format(
                    propDict["CharacteristicLength_m"]
                )
            )
        except KeyError:
            pass
        print("\n")


class Element:
    """
    a class intended to capture and represent
    reactions
    """

    directory = {}
    periodic = {}

    def __init__(self, name=None):
        self.Name = name
        Element.directory.update({repr(self): self})

    def __repr__(self):
        return self.Name

    def show(self):
        """
        debugging function to prettyprint
        all the elemental properties
        """
        propDict = vars(self)
        print("{}".format(self.Name))
        for k, v in zip(propDict.keys(), propDict.values()):
            if k == "Name":
                pass
            elif isinstance(v, list):
                print("|\{:}".format(k))
                vstr = ""
                for i in v:
                    vstr += "{:^10}".format(shortHand(i, 9))
                print("| \{:}".format(vstr))
            else:
                print("|\{:_<40}{:_>20}".format(cocatenate(k), v))

        print("\n")

    def buildPeriodic():
        emLines = getEmissions()
        for e in Element.directory.values():
            Element.periodic.update({e.Symbol: e})
            """
                try to incorporate emission data into elements"""
            try:
                setattr(e, "Emission", emLines[e.Emission])
            except AttributeError:
                # print("element {} does not have emission data".format(e))
                pass
