from app.compute_statistics import ComputeStatistics

if __name__ == "__main__":
    stats = ComputeStatistics("numbers.txt")
    stats.print_statistics()
