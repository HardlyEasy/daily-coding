import random
from typing import List


class Solution:
    @staticmethod
    def roll_all(dice_command: str):
        dice_amt, sides = Solution.convert_command(dice_command)
        my_sum = 0
        if 1 <= dice_amt <= 100:
            for i in range(1, dice_amt+1):
                my_sum += Solution.roll_once(sides)
            return my_sum
        else:
            raise Exception("roll_all(): incorrect number of dice")

    @staticmethod
    def roll_once(sides: int):
        if 2 <= sides <= 100:
            return random.randint(1, sides)  # (inc, inc)
        else:
            raise Exception("roll_once(): incorrect number of sides")

    @staticmethod
    def convert_command(dice_command: str) -> List[int]:
        return list(map(int, dice_command.split("d")))


class Test:
    challenge_input = ['5d12', '6d4', '1d2', '1d8', '3d6', '4d20', '100d100']

    @staticmethod
    def test():
        for i in range(0, len(Test.challenge_input)):
            print(Solution.roll_all(Test.challenge_input[i]))

Test.test()