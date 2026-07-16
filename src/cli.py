from src.config import (
    MONTE_CARLO_CONFIG,
    SIMULATION_CONFIG,
)
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


def get_positive_float(prompt, default):
    """
    Request a positive floating-point value from the user.

    Pressing Enter returns the supplied default value.
    """
    while True:
        user_input = input(
            f"{prompt} [{default}]: "
        ).strip()

        if user_input == "":
            return default

        try:
            value = float(user_input)

            if value <= 0:
                print("Please enter a value greater than zero.")
                continue

            return value

        except ValueError:
            print(
                "Invalid input. "
                "Please enter a numerical value."
            )


def get_positive_integer(prompt, default):
    """
    Request a positive integer value from the user.

    Pressing Enter returns the supplied default value.
    """
    while True:
        user_input = input(
            f"{prompt} [{default}]: "
        ).strip()

        if user_input == "":
            return default

        try:
            value = int(user_input)

            if value <= 0:
                print(
                    "Please enter an integer "
                    "greater than zero."
                )
                continue

            return value

        except ValueError:
            print(
                "Invalid input. "
                "Please enter a whole number."
            )


def configure_simulation():
    """
    Create temporary simulation settings from user input.

    The default dictionaries in config.py are not modified.
    """
    simulation_config = SIMULATION_CONFIG.copy()

    print()
    print("=" * 58)
    print("              SYNTHETIC SIMULATION SETTINGS")
    print("=" * 58)
    print()
    print("Press Enter to keep each default value.")
    print()

    simulation_config["duration"] = get_positive_float(
        "Observation duration (s)",
        SIMULATION_CONFIG["duration"],
    )

    simulation_config["sampling_rate"] = get_positive_integer(
        "Sampling rate (Hz)",
        SIMULATION_CONFIG["sampling_rate"],
    )

    simulation_config["period"] = get_positive_float(
        "Pulsar period (s)",
        SIMULATION_CONFIG["period"],
    )

    simulation_config["pulse_width"] = get_positive_float(
        "Pulse width (phase)",
        SIMULATION_CONFIG["pulse_width"],
    )

    simulation_config["pulse_amplitude"] = get_positive_float(
        "Pulse amplitude",
        SIMULATION_CONFIG["pulse_amplitude"],
    )

    simulation_config["noise_level"] = get_positive_float(
        "Noise level",
        SIMULATION_CONFIG["noise_level"],
    )

    n_simulations = get_positive_integer(
        "Monte Carlo runs",
        MONTE_CARLO_CONFIG["n_simulations"],
    )

    print()
    print("Selected simulation parameters")
    print("------------------------------")
    print(
        f"Duration: "
        f"{simulation_config['duration']} s"
    )
    print(
        f"Sampling rate: "
        f"{simulation_config['sampling_rate']} Hz"
    )
    print(
        f"Period: "
        f"{simulation_config['period']} s"
    )
    print(
        f"Pulse width: "
        f"{simulation_config['pulse_width']} phase"
    )
    print(
        f"Pulse amplitude: "
        f"{simulation_config['pulse_amplitude']}"
    )
    print(
        f"Noise level: "
        f"{simulation_config['noise_level']}"
    )
    print(f"Monte Carlo runs: {n_simulations}")
    print()

    return simulation_config, n_simulations


def run_application():
    """
    Run the interactive command-line application.
    """
    while True:
        print_menu()

        choice = input(
            "Enter choice (0, 1 or 2): "
        ).strip()

        print()

        if choice == "0":
            print("=" * 58)
            print(
                "Thank you for using "
                "Pulsar Signal Analysis."
            )
            print("Goodbye!")
            print("=" * 58)
            break

        try:
            if choice == "1":
                simulation_config, n_simulations = (
                    configure_simulation()
                )

                print(
                    "Running synthetic "
                    "pulsar simulation..."
                )
                print()

                run_simulation_analysis(
                    simulation_config=simulation_config,
                    n_simulations=n_simulations,
                )

            elif choice == "2":
                print(
                    "Loading real pulsar "
                    "observation..."
                )
                print("Pulsar: PSR B0329+54")
                print(
                    "Observation frequency: "
                    "10.55 GHz"
                )
                print(
                    "Source: European Pulsar "
                    "Network Database"
                )
                print()

                run_real_data_analysis()

            else:
                print("Invalid choice.")
                print("Please enter 0, 1 or 2.")

        except FileNotFoundError as error:
            print("Required data file was not found.")
            print(f"Details: {error}")

        except ValueError as error:
            print(
                "The analysis could not "
                "be completed."
            )
            print(f"Details: {error}")

        except KeyboardInterrupt:
            print()
            print("Analysis interrupted by the user.")

        except Exception as error:
            print("An unexpected error occurred.")
            print(f"Details: {error}")

        input(
            "\nPress Enter to return "
            "to the main menu..."
        )