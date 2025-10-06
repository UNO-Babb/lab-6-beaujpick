#DiceRoll.py
#Name: Beau Pick
#Date:10/5/25
#Assignment:
import random

def roll_dice():
    """Simulate rolling two six-sided dice and return their total."""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2

def simulate_rolls(num_rolls=10000):
    """Simulate rolling two dice multiple times and count the totals."""
    results = {total: 0 for total in range(2, 13)} 

    for _ in range(num_rolls):
        total = roll_dice()
        results[total] += 1

    return results

def display_results(results, num_rolls):
    """Display counts and percentages of each dice total."""
    print(f"{'Total--'}{'Count--'}{'Percentage'}")
  
    for total in range(2, 13):
        count = results[total]
        percentage = (count / num_rolls) * 100
        print(f"{total:<6}{count:<10}{percentage:>6.2f}%")

def main():
    num_rolls = 10000
    results = simulate_rolls(num_rolls)
    display_results(results, num_rolls)

if __name__ == "__main__":
    main()
