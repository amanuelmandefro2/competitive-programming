class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        min_len = float('inf')
        sub_cards = {}
       
        for i in range(len(cards)):
            if cards[i] in sub_cards:
                min_len = min(min_len, i-sub_cards[cards[i]]+1) 
            sub_cards[cards[i]] = i    
            

        return -1 if min_len == float('inf') else min_len