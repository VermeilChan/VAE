import sys
from extract_addons import main as extract_addons
from extract_archives import main as extract_archives


def main():
    options = {
        "1": extract_addons,
        "2": extract_archives,
        "3": lambda: sys.exit(0),
    }

    try:
        while True:
            print(
                "Select an option:\n1. Extract addons (GMA)\n2. Extract archives (ZIP, RAR, 7Z, TAR)\n3. Exit"
            )
            choice = input("Enter your choice (1/2/3): ").strip()

            if choice in options:
                options[choice]()
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)


if __name__ == "__main__":
    main()
