class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck_order = deque()
        deck.sort()
        deck_order.append(deck[-1])
        for i in range(len(deck)-2, -1, -1):
            old = deck_order.pop()
            deck_order.appendleft(old)
            deck_order.appendleft(deck[i])
        
        return list(deck_order)
        