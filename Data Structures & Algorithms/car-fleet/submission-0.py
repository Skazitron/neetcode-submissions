class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        cars = sorted(zip(position, speed), reverse=True)

        for car in cars:
            pos, speed = car
            curtime = (target - pos)/speed
            if not time or curtime > time[-1]:
                time.append(curtime)
        
        return len(time)