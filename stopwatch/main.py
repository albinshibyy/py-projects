import time
import threading

class Stopwatch:
    def __init__(self):
        self.start_time = 0
        self.elapsed_time = 0
        self.running = False
        self.lap_times = []
        self.lap_number = 1

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            self.display_time()

    def stop(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.running = False

    def reset(self):
        self.start_time = 0
        self.elapsed_time = 0
        self.running = False
        self.lap_times = []
        self.lap_number = 1

    def lap(self):
        if self.running:
            lap_time = time.time() - self.start_time
            self.lap_times.append(lap_time)
            print(f"\nLap {self.lap_number}: {self.format_time(lap_time)}")
            self.lap_number += 1

    def display_time(self):
        if self.running:
            elapsed_time = time.time() - self.start_time
            print(f"\rTime: {self.format_time(elapsed_time)}", end="")
            threading.Timer(0.1, self.display_time).start()

    def format_time(self, seconds):
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        seconds = int(seconds % 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def main():
    stopwatch = Stopwatch()
    print("Stopwatch Menu:")
    print("  s - Start")
    print("  p - Pause")
    print("  r - Reset")
    print("  l - Lap")
    print("  q - Quit")
    while True:
        command = input("\nEnter command: ")
        if command == "s":
            stopwatch.start()
        elif command == "p":
            stopwatch.stop()
        elif command == "r":
            stopwatch.reset()
        elif command == "l":
            stopwatch.lap()
        elif command == "q":
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
