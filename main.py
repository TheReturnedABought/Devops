import argparse
import sort

sorted_numbers = []

def main():
    parser = argparse.ArgumentParser(description="Choose a sorting algorithm.")
    parser.add_argument("algorithm", choices=["bubble", "quick", "merge"], help="The sorting algorithm to use.")
    parser.add_argument("numbers", nargs='+', type=int, help="A list of integers to sort.")

    args = parser.parse_args()

    if args.algorithm == "bubble":
        sorted_numbers = sort.bubble_sort(args.numbers)
    elif args.algorithm == "quick":
        sorted_numbers = sort.quick_sort(args.numbers)
    elif args.algorithm == "merge":
        sorted_numbers = sort.merge_sort(args.numbers)

    print("Sorted numbers:", sorted_numbers)

if __name__ == "__main__":
    main()
