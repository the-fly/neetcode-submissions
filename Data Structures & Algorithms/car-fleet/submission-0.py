class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        if len(position) == 0:
            return cars

        for i in range(len(position)):
            carPosition = position[i]
            carSpeed = speed[i]
            carETA = (target - carPosition) / carSpeed
            cars.append((carPosition, carETA))
        
        cars.sort(reverse = True)

        currentFleetETA = -1
        numberOfFleets = 0

        for car in cars:
            if car[1] > currentFleetETA:
                currentFleetETA = car[1]
                numberOfFleets += 1

        return numberOfFleets






        