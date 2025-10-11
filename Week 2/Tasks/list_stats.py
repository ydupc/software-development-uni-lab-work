def main():
    raw = input("Enter numbers separated by spaces: ").strip()
    try:
        nums = [float(t) for t in raw.split()]
    except ValueError:
        print("Please enter only numbers.")
        return
    if not nums:
        print("No numbers entered.")
        return
    print(f"Count: {len(nums)}")
    print(f"Min:   {min(nums)}")
    print(f"Max:   {max(nums)}")
    print(f"Mean:  {sum(nums)/len(nums):.4f}")

if __name__ == "__main__":
    main()
