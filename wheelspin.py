import random


# Collect user input

item_list = []


add_item = input("Please enter the items to include in the tournament (seperate by commas): ")

new_item = [item.strip() for item in add_item.split(',')]

item_list.extend(new_item)


# Show what was added 

print("You have added: ", [i.title() for i in item_list])


# Primary round: Spin to eliminate one item

winners = []

remaining = item_list.copy()


while len(remaining) > 1:

	winner = random.choice(remaining)

	winners.append(winner)

	remaining.remove(winner)


# The last selected item is the loser of the primary item

loser = remaining[0]

print(f"☠️ {loser.title()} lost the primary round and will be eliminated")

print(f"Winners moving to next bracket: {[w.title() for w in winners]}")



# Run each bracket 

def bracket_round(contenders):

	next_round = []

	random.shuffle(contenders)

	for i in range(0, len(contenders),2):

		if i + 1 < len(contenders):

			# Pair items and pick random winner

			a = contenders[i]

			b = contenders[i+1]

			winner = random.choice([a,b])

			print(f"{a.title()} vs {b.title()} -> Winner: {winner.title()}")

			next_round.append(winner)

		else:

			# If odd number, last item advances automatically

			print(f"{contenders[i].title()} gets a free pass to the next round")

			next_round.append(contenders[i])

	return next_round


# Run the tournament until one winner remains

bracket = winners

round_num = 1

while len(bracket) > 1:

	print(f"\n--- Round {round_num} ({len(bracket)} contenders) ---")

	bracket = bracket_round(bracket)

	round_num += 1


# Display final winner

print(f"\n🏆 THE WINNER IS: **{bracket[0].title()}**")
