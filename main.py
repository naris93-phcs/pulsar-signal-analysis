from src.pipeline import (
    run_real_data_analysis,
    run_simulation_analysis,
)


def print_menu():
    """
    Display the main application menu.
    """
    print()
    print("=" * 58)
    print("                 PULSAR SIGNAL ANALYSIS")
    print("=" * 58)
    print("       Signal Processing for Pulsar Observations")
    print()
    print("Choose analysis mode:")
    print()
    print("  1. Synthetic Pulsar Simulation")
    print("  2. Real Pulsar Profile (PSR B0329+54)")
    print()
    print("  0. Exit")
    print()
    print("=" * 58)


def main():
    """
    Run the pulsar analysis application.
    """
    while True:
        print_menu()

        choice = input("Enter choice (0, 1 or 2): ").strip()

        print()

        if choice == "0":
            print("=" * 58)
            print("Thank you for using Pulsar Signal Analysis.")
            print("Goodbye!")
            print("=" * 58)
            break

        try:
            if choice == "1":
                print("Running synthetic pulsar simulation...")
                print()

                run_simulation_analysis()

            elif choice == "2":
                print("Loading real pulsar observation...")
                print("Pulsar: PSR B0329+54")
                print("Observation frequency: 10.55 GHz")
                print("Source: European Pulsar Network Database")
                print()

                run_real_data_analysis()

            else:
                print("Invalid choice.")
                print("Please enter 0, 1 or 2.")

        except FileNotFoundError as error:
            print("Required data file was not found.")
            print(f"Details: {error}")

        except ValueError as error:
            print("The analysis could not be completed.")
            print(f"Details: {error}")

        except KeyboardInterrupt:
            print()
            print("Analysis interrupted by the user.")

        except Exception as error:
            print("An unexpected error occurred.")
            print(f"Details: {error}")

        input("\nPress Enter to return to the main menu...")


if __name__ == "__main__":
    main()