with open("input.txt", "r") as file:
    shuffle = file.read().split("\n")

def read_instruction(line, deck, length):
    line = line.split(" ")
    if line[0] == "cut":
        N = int(line[1])
        return deck[N:] + deck[:N]
    if line[0] == "deal":
        if line[-1] == "stack":
            deck.reverse()
            return deck
        else:
            inc = int(line[-1])
            new_deck = range(length)
            for index, elem in enumerate(deck):
                new_deck[index*inc%length] = elem
            return new_deck

deck = range(10007)
for instruction in shuffle:
    deck = read_instruction(instruction, deck, len(deck))
print(deck.index(2019))
