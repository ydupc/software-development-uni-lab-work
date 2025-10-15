def print_range(start=1, stop=10, step=1):
    nums = list(range(start, stop + (1 if step>0 else -1), step))
    print(", ".join(str(n) for n in nums) + ",")
if __name__ == "__main__":
    print_range()
