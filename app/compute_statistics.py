class ComputeStatistics:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.read_file()

    def read_file(self):
        data = []
        try:
            with open(self.file_path, "r") as file:
                for line in file:
                    stripped = line.strip()
                    if stripped:
                        data.append(int(stripped))
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
        except ValueError as e:
            print(f"Invalid number in file: {e}")
        except IOError as e:
            print(f"I/O error: {e}")
        return data

    def count_numbers(self):
        return len(self.data)

    def summation(self):
        return sum(self.data)

    def average(self):
        return self.summation() / self.count_numbers() if self.data else 0

    def minimum_number(self):
        return min(self.data) if self.data else None

    def maximum_number(self):
        return max(self.data) if self.data else None

    def print_statistics(self):
        if not self.data:
            print("No valid data to process.")
            return

        print(f"Total = {self.count_numbers()}")
        print(f"Summation = {self.summation()}")
        print(f"Average = {round(self.average())}")
        print(f"Minimum = {self.minimum_number()}")
        print(f"Maximum = {self.maximum_number()}")

