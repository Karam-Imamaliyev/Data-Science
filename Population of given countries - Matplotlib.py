    import math
    import numpy as np
    import matplotlib.pyplot as plt
     
    age = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
    population_france = np.array([100, 160, 310, 420, 490, 700, 675, 340, 80])
    population_usa = np.array([140, 180, 350, 598, 780, 981, 1351, 780, 157])
    countries = np.array(['USA', 'France'])
     
    plt.plot(age, population_usa)
    plt.fill_between(age, population_usa)
     
    plt.plot(age, population_france)
    plt.xlabel("Age")
    plt.ylabel("Population")
    plt.title("Population of Countries")
    plt.fill_between(age, population_france)
     
    plt.legend(countries)
    plt.show()