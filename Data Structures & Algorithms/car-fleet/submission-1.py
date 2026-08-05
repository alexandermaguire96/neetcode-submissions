class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #data processing
        better_fleet = [(position[i], speed[i]) for i in range(len(position))]
        #has to be reverse sorted because we need to know the fastest end first
        sorted_fleet = sorted(better_fleet, reverse = True)
        print(sorted_fleet)

        def numFleets():
            stack = []
            
            for pos, speed in sorted_fleet:
                #turn calc
                turns = (target - pos) / speed
                while not stack or (turns > stack[-1]):
                
                    stack.append(turns)

            number_fleets = len(stack)
            return number_fleets
        return numFleets()