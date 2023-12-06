class IntervalMerger:
    def merge_intervals(self, intervals):
        """
        Merges a list of intervals that may overlap.
        
        Args:
        - intervals (List[List[int]]): List of intervals in the form of lists [start, end].
        
        Returns:
        - List[List[int]]: Merged intervals.
        """
        if not intervals:
            return []

        # Sort intervals based on the start value
        intervals.sort(key=lambda x: x[0])
        merged_intervals = [intervals[0]]

        # Merge overlapping intervals
        for i in range(1, len(intervals)):
            if intervals[i][0] <= merged_intervals[-1][1]:
                # Merge if intervals overlap
                merged_intervals[-1][1] = max(merged_intervals[-1][1], intervals[i][1])
            else:
                # Add non-overlapping intervals
                merged_intervals.append(intervals[i])

        return merged_intervals


# Driver Code
if __name__ == '__main__':
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        num_intervals = int(input())
        interval_values = list(map(int, input().strip().split()))
        intervals = []
        index = 0
        # Create a list of intervals from input values
        for i in range(num_intervals):
            start = interval_values[index]
            index += 1
            end = interval_values[index]
            index += 1
            intervals.append([start, end])
        
        # Create IntervalMerger object
        merger = IntervalMerger()
        # Obtain merged intervals
        merged = merger.merge_intervals(intervals)
        # Print merged intervals
        for interval in merged:
            for val in interval:
                print(val, end=" ")
        print()
