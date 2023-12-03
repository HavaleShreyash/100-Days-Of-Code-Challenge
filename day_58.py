from typing import List

def earliest_full_bloom(planting_times: List[int], growing_times: List[int]) -> int:
    """
    Calculates the earliest possible day when all seeds are blooming.

    Args:
        planting_times: A list of planting times for each flower seed.
        growing_times: A list of growing times for each flower seed.

    Returns:
        The earliest day when all seeds are blooming.
    """

    number_of_seeds = len(planting_times)
    sorted_indices = sorted(range(number_of_seeds), key=lambda x: -growing_times[x])
    total_planting_time = 0
    maximum_bloom_time = 0

    for index in sorted_indices:
        bloom_time = total_planting_time + planting_times[index] + growing_times[index]
        maximum_bloom_time = max(maximum_bloom_time, bloom_time)
        total_planting_time += planting_times[index]

    return maximum_bloom_time


if __name__ == "__main__":
    planting_times = [1, 4, 3]
    growing_times = [2, 3, 1]
    earliest_bloom_day = earliest_full_bloom(planting_times, growing_times)
    print(earliest_bloom_day)
