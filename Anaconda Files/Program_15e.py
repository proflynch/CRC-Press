# Program_15e: Monte Carlo Simulation. European roulette.
# A gambler keeps betting on the ball landing on a red pocket.
import random
import matplotlib.pyplot as plt
def spin():
   pocket = random.randint(1,37)
   return pocket
def roulette(bankroll, wager, spins):
    Num_Spins = []
    balance = []
# The first spin.
    num_spins = 1
# Set maximum number of spins.
    while num_spins < spins:
        # Payout if ball lands on red.
        if (spin() % 2) == 0:
            # Add money to bankroll.
            bankroll = bankroll + wager
            # Increase number of spins.
            Num_Spins.append(num_spins)
            # Append the balance.
            balance.append(bankroll)
        # Gambler loses if ball lands in a black or green pocket. 
        else:
            # Subtract the money from the bankroll.
            bankroll = bankroll - wager 
            # Increase the number of spins.
            Num_Spins.append(num_spins)
            # Append the balance.
            balance.append(bankroll)          
        num_spins = num_spins + 1      
    plt.plot(Num_Spins , balance)
    final_balances.append(balance[-1])
    return(final_balances) 
simulations = 1
#Create a list for calculating final funds.
final_balances = []
while simulations <= 100:
    end_balance = roulette(10000 , 100 , 3700)
    simulations = simulations + 1
plt.rcParams["font.size"] = "20"    
plt.xlabel('Number of Spins of Roulette Wheel')
plt.ylabel('Bankroll (Euros)')
plt.show()
print("The player starts the game with 10,000 euros and ends with " + \
      str(sum(end_balance)/len(end_balance)), "euros")