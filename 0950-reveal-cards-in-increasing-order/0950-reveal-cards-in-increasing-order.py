class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        """
        Complexities:
        Time: O(n^2)
        Space: O(n)

        where n = len(deck)
        """
        # run through a sample deck, save ordering
        sample = [i for i in range(len(deck))]

        revealedCards = []
        while len(revealedCards) < len(deck):
            revealedCards.append(sample[0])
            sample.pop(0)
            
            if len(sample) == 0:
                break

            sample.append(sample[0])
            sample.pop(0)

        # sort deck
        deck.sort()

        # replace sample with deck values
        returnedArr = [-1] * len(deck)
        for i in range(len(revealedCards)):
            returnedArr[revealedCards[i]] = deck[i]

        return returnedArr