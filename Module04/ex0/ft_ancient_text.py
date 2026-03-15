def main() -> None:
    filename: str = "ancient_fragment.txt"
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print(f"Accessing Storage Vault: {filename}")
    try:
        file = open(filename, "r")
        print("Connection established...")
        print()
        print("RECOVERED DATA:")
        content = file.read()
        print(content)
        print()
        print("Data recovery complete. Storage unit disconnected.")
        file.close()
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    except PermissionError as e:
        print(e)


if __name__ == "__main__":
    main()
