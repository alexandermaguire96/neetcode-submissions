class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        
        
        for i in range(len(numbers)-1):

            pair = target - numbers[i]
            print(numbers[i], i)

            for j in range(i+1, len(numbers)):

                print(numbers[j])

                if numbers[j] == pair:
                    return [(i + 1),(j + 1)]

                