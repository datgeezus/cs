class ArrayQuery:
    def __init__(self, nums: list[int]):
        total = 0
        self.__prefix = []
        for n in nums:
            total += n
            self.__prefix.append(total)

    def range_sum(self, left, right):
        pre_right = self.__prefix[right]
        pre_left = self.__prefix[left - 1] if left > 0 else 0
        return pre_right - pre_left


if __name__ == "__main__":
    array = ArrayQuery([2, -1, 3, -3, 4])
    assert array.range_sum(2, 3) == 0
