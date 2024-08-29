import sys
from platform import system, architecture
from extract_addons import main as extract_addons
from extract_archives import main as extract_archives

version = "v2.1.0"


def display_menu():
    print(
        f"Vermeil's Addon Extractor {version}, {system()} ({architecture()[0]})\n"
        "\nSelect an option:\n"
        "1. Extract addons (GMA)\n"
        "2. Extract archives (ZIP, RAR, 7Z, TAR)\n"
        "3. Exit"
    )


def handle_choice(choice):
    options = {"1": extract_addons, "2": extract_archives, "3": sys.exit}

    if choice in options:
        options[choice]()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")


def main():
    try:
        while True:
            display_menu()
            choice = input("Enter your choice (1-3): ").strip()
            handle_choice(choice)
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)


if __name__ == "__main__":
    main()
