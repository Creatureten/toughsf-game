import math


def designGun(
    reaction,
    cal,
    chamberLength,
    shot,
):
    """
    method for the design of a chemical gun
    reaction: self explanatory
    cal: caliber, gun tube inner diameter meter
    chamberLength: assuming a straight gun tube, how much length does the chamber take up? meter
    shot: shot mass, kg.

    """
    if len(reaction.Reactants) == 1 and reaction.Reactants[0].MeltingPoint_K > 273.15:
        theta = 0
        """
            θ = 0: perforated grain
            θ = 1: cylindrical grain
        """
        l = chamberLength
        """   chamber      barrel
            lllllllllllxxxxxxxxxxxxx
        """
        rho = reaction.Reactants[0].Density_kg__m3
        A = (cal / 2) ** 2 * math.pi  # chamber base area, m^2
        c = (A * l) * rho
        w = shot
        Rl = (1 + c / (2 * w)) / (1 + c / (3 * w))  # lagrange ratio

        if theta == 0:

            def f(x, lbda, M):
                """
                calculates the fraction of propellant burned at any given x
                """
                return 1 - math.log(x / l + 1) / M

            def pb(x, lbda, M):
                return lbda * c * Rl / V(x) * (1 - f(x)) * math.exp(-M * (1 - f(x)))

        else:

            def f(x, lbda, M):
                return ((1 + theta) * (x / l + 1) ** (-theta / M) - 1) / theta

            def pb(x, lbda, M):
                return (
                    lbda
                    * c
                    * Rl
                    / V(x)
                    * (1 - f(x))
                    * (1 + theta * f(x))
                    * ((1 - theta * f(x)) / (1 - theta)) ** (M / theta)
                )

        def V(x):
            return (x + l) * A

        def f_web(D):
            """
            D: see iniWeb
            """
            lbda, beta = solidPropellantSpecs(reaction, D)
            M = (A * D) ** 2 / (
                w * c * lbda * beta ** 2
            )  # central ballistics parameter, dim less

            # xm: location of max pressure
            # xc: location of burnout

            if theta == 0:
                xm = (math.e - 1) * l
                xc = (math.exp(M) - 1) * l

            else:
                xm = (((M + 2 * theta) / (M + theta)) ** (M / theta) - 1) * l
                xc = ((1 + theta) ** (M / theta) - 1) * l

    else:
        pass


def solidPropellantSpecs(reaction, iniWeb):
    """
    Function for calculating the relevant parameters of a conventional gun.
    iniWeb: initial web diameter, smallest thickness of the initial propell
            ant grain, for cylindrical grain, equals initial diameter, for
            perforated cylindrical grain, equals the radius.
    """
    adbT = reaction.adbT()
    spR = reaction.spGasR()
    spF = spR * adbT  # known as propellant force in reference, unit J/kg, symbol: λ
    rho = reaction.Reactants[0].Density_kg__m3
    beta = 350 * iniWeb / (adbT * spF * rho)  # burn rate coefficient, symbol: β
    return spF, beta
