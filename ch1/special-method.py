from collections import namedtuple, Counter
from random import choice, shuffle

Card = namedtuple('Card', ['rank', 'suit'])

class Deck:

    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __call__(self):

        shuffle(self._cards)

if __name__ == "__main__":

    a = 1
    a[1]
    a()


with open("read.txt", "rb") as f:

    데이터셋 = f.read()
    ///

with open("read.csv", "w") as f:

    f.write(데이터셋)