import argparse

COMMANDS = {
    'toolbox-info': 'Show available toolbox commands'
}

def main():
    parser = argparse.ArgumentParser(description='Toolbox command overview')
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Show command descriptions'
    )

    args = parser.parse_args()

    if args.verbose:
        print("Commands and descriptions:")
        for key, description in COMMANDS.items():
            print(f"  {key}: {description}")
    else:
        print("Commands:")
        for key in COMMANDS:
            print(f"  {key}")

if __name__ == "__main__":
    main()
