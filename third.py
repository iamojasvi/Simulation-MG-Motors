import random
import matplotlib.pyplot as plt

def flipcoins():
    flipa = random.randint(0, 1)
    flipb = random.randint(0, 1)
    return flipa, flipb

def playgame(initialmoney=10):
    playeramoney = initialmoney
    playerbmoney = initialmoney
    rounds = 0

    while playeramoney > 0 and playerbmoney > 0:
        flipa, flipb = flipcoins()

        if flipa == flipb:
            playeramoney += 1
            playerbmoney -= 1
        else:
            playeramoney -= 1
            playerbmoney += 1

        rounds += 1

    return rounds

def runsimulation(numexperiments=500, initialmoney=10):
    roundslist = []

    for _ in range(numexperiments):
        rounds = playgame(initialmoney)
        roundslist.append(rounds)

    return roundslist

def plotresults(roundslist, numexperiments):
    plt.figure(figsize=(10, 6))
    plt.hist(roundslist, bins=range(min(roundslist), max(roundslist) + 1, 1), edgecolor='black')
    plt.title(f"Distribution of Game Lengths ({numexperiments} Simulations)")
    plt.xlabel("Number of Rounds")
    plt.ylabel("Frequency")

    averagerounds = calculateaverage(roundslist)
    plt.axvline(averagerounds, color='red', linestyle='dashed', linewidth=1, label=f'Average = {averagerounds:.2f} rounds')
    plt.legend()

    plt.grid(True)
    plt.show()

def calculateaverage(roundslist):
    return sum(roundslist) / len(roundslist) if roundslist else 0.0

def printaverage(roundslist):
    averagerounds = calculateaverage(roundslist)
    print(f"Average Rounds: {averagerounds:.2f} ")

def simulate():
    numexperiments = 500
    roundslist = runsimulation(numexperiments)
    plotresults(roundslist, numexperiments)
    printaverage(roundslist)

simulate()
