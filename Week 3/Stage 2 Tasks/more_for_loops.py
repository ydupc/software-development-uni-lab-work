def odd_range(start, stop):
    start = start if start % 2 == 1 else start + 1
    return list(range(start, stop + 1, 2))
def even_range_desc(start, stop_exclusive):
    start = start if start % 2 == 0 else start - 1
    return list(range(start, stop_exclusive, -2))
if __name__ == "__main__":
    print(", ".join(map(str, odd_range(9, 49))) + ",")
    print()
    print(", ".join(map(str, even_range_desc(100, 50))) + ",")
