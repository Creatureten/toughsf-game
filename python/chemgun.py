def designGun(reaction):
    """
    method for the design of a chemical gun"""
    dH = reaction.dH()  # unit: kj/mol
    print(dH)
    adbT = reaction.adbT()
    print(adbT)