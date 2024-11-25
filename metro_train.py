import multiprocessing
import time

class Train(multiprocessing.Process):
    def __init__(self, train_id, stations, travel_time):
        super().__init__()
        self.train_id = train_id
        self.stations = stations
        self.travel_time = travel_time
        self.current_station = 0

    def run(self):
        while True:
            # Simulate travel time
            time.sleep(self.travel_time)
            
            # Move to the next station
            self.current_station = (self.current_station + 1) % len(self.stations)
            print(f"Train {self.train_id} arrived at station {self.stations[self.current_station]}")

            # Simulate passenger boarding and alighting (you can implement more complex logic here)
            print(f"Passengers boarding and alighting at station {self.stations[self.current_station]}")

if __name__ == "__main__":
    stations = ["Station A", "Station B", "Station C", "Station D"]
    travel_time = 5  # seconds

    num_trains = 2
    trains = []
    for i in range(num_trains):
        train = Train(i+1, stations, travel_time)
        trains.append(train)
        train.start()

    # Keep the main process running to avoid early termination
    while True:
        time.sleep(1)