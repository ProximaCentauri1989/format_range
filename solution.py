MIN_ALLOWED_RANGE_LENGTH = 2

class Range:
    def __init__(self, sequence):
        self.__range = sequence
    def to_string(self):
        if len(self.__range) != 1:
            return f'{self.__range[0]}-{self.__range[len(self.__range)-1]}'
        return f'{self.__range[0]}'

class RangeBuilder:
    def __init__(self, sequence):
        self.__sequence = sequence
        self.__current = 0

    def is_last(self):
        return self.__current >= len(self.__sequence)

    """"""
    def __next(self):
        if self.is_last():
            raise IndexError('out_of_range')

        left_bound = self.__current
        right_bound = self.__current
        while(right_bound + 1 < len(self.__sequence) and self.__sequence[right_bound + 1] - self.__sequence[right_bound] == 1):
            right_bound+=1
        self.__current = right_bound + 1 if right_bound - left_bound >= MIN_ALLOWED_RANGE_LENGTH else left_bound + 1

        if right_bound - left_bound >= MIN_ALLOWED_RANGE_LENGTH:
            return Range(self.__sequence[left_bound:right_bound+1])
        else:
            return Range(self.__sequence[left_bound:left_bound+1])

    def reset(self):
        self.__current = 0

    def get_sequence(self):
        return self.__sequence

    def __validate(self):
        if not isinstance(self.__sequence, list):
            raise Exception('No list instance provided')
        for elem in self.__sequence:
            if not isinstance(elem, int):
                raise Exception('No list of integers provided')

    def solution(self):
        self.__validate()
        solution = ""
        while(not self.is_last()):
            range = self.__next()
            solution += range.to_string() + ',' if not self.is_last() else range.to_string()
        return solution


def main():
    try:
        ordered_list = [-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]
        builder = RangeBuilder(ordered_list)
        result = builder.solution()
    except Exception as err:
        print(err)
    else:
        print("Solved") if result == '-6,-3-1,3-5,7-11,14,15,17-20' else print("Failed")

if __name__ == "__main__":
    main()
