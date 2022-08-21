from tracemalloc import start


class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """

        # APPROACH
        # greedy method - keep a priority queue with max fuel
        # while iterationg through the stations, if you run out of the fuel
        # just pull the fuel from the visited stations having max fuel, keep track of the 
        # stations and move ahead


        # net_fuel = target - startFuel
        # min_stations = len(stations)
        station_cnt = 0
        current_fuel = startFuel
        for station, fuel in stations:
            if station <= current_fuel:
                current_fuel += fuel
                station_cnt += 1
                if current_fuel >= target:
                    break
        

        

sol = Solution()
target = 100
startFuel = 1
stations = [[10,100]]
sol.minRefuelStops(target, startFuel, stations)