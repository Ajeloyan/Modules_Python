import os
import site
import sys


def main() -> None:

    venv_path = os.environ.get('VIRTUAL_ENV')
    if venv_path:
        print()
        print("MATRIX STATUS: Welcome to the construct")
        print()
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(venv_path)}")
        print()
        print(f"Environment Path: {venv_path}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting\nthe global system.")
        print()

        print(f"Package installation path: \n{site.getsitepackages()[0]}")
    else:
        print()
        print("MATRIX STATUS: You're still plugged in")
        print()
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()
        print("To enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate   # On Windows")
        print()
        print("Then run this program again.")


if __name__ == "__main__":
    main()
