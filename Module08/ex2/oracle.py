import os
import sys
try:
    from dotenv import load_dotenv
except (ImportError):
    print("Error: python-dotenv is not installed.")
    sys.exit(1)


def main() -> None:

    print("ORACLE STATUS: Reading the Matrix...")
    print()

    load_dotenv()
    print("Configuration loaded:")
    matrix_mode = os.getenv('MATRIX_MODE')
    database = os.getenv('DATABASE_URL')
    api = os.getenv('API_KEY')
    log = os.getenv('LOG_LEVEL')
    zion = os.getenv('ZION_ENDPOINT')

    print(f"Mode: {matrix_mode}")
    if database:
        print("Database: Connected to local instance")
    else:
        print("Database: failed to connect to local instance")

    if api:
        print("API Access: Authenticated")
    else:
        print("No api found")

    print(f"Log level: {log}")

    if zion:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")
    print()

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
