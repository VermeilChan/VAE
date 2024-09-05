import sys
from platform import system, architecture
from extract_addons import main as extract_addons
from extract_archives import main as extract_archives

version = "v2.2.1"


def display_menu():
    print(
        f"\n{'=' * 50}\n"
        f"Vermeil's Addon Extractor {version}, {system()} ({architecture()[0]})\n"
        f"{'=' * 50}\n"
        "Select an option:\n"
        "1. Extract addons (GMA, BIN)\n"
        "2. Extract archives (ZIP, RAR, 7Z, TAR)\n"
        "3. Help\n"
        "4. Exit\n"
    )


def display_help():
    print(
        "\nHelp:\n"
        "1. Extract addons - Extracts GMA and BIN addon files.\n"
        "2. Extract archives - Extracts various archive formats (ZIP, RAR, 7Z, TAR).\n"
        "3. Exit - Closes the application.\n"
    )


def handle_choice(choice):
    options = {
        "1": extract_addons,
        "2": extract_archives,
        "3": display_help,
        "4": sys.exit
    }

    if choice in options:
        options[choice]()
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")


def main():
    try:
        while True:
            display_menu()
            choice = input("Enter your choice (1-4): ").strip()
            handle_choice(choice)
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)


if __name__ == "__main__":
    main()
