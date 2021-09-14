# You have a long flowerbed in which some of the plots are planted, and some are not.
# However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's,
# where 0 means empty and 1 means not empty, and an integer n,
# return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

def can_place_flowers(flowerbed: list[int], n: int) -> bool:
    k = n
    last_idx = len(flowerbed) - 1
    
    def in_bounds(i: int) -> bool:
        return i >= 0 and i <= last_idx
    
    def can_place(i: int) -> bool:
        curr = flowerbed[i]
        next_ = flowerbed[i+1] if i < last_idx else curr
        prev = flowerbed[i-1] if i > 0 else curr

        if not in_bounds(i): return False
        return curr == 0 and prev != 1 and next_ != 1
    
    for i,_ in enumerate(flowerbed):
        if k <= 0:
            break
        if can_place(i):
            flowerbed[i] = 1
            k -= 1
            
    return k == 0

    
if __name__ == "__main__":
    print(can_place_flowers([1,0,0,0,1], 1))  # true
    print(can_place_flowers([1,0,0,0,1], 2))  # false
    print(can_place_flowers([1,0,0,0,0,1], 2))  # false
    print(can_place_flowers([0,0,1,0,1], 1))  # true