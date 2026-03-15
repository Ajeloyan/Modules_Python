def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    filename1: str = "lost_archive.txt"
    try:
        print("\nCRISIS ALERT: Attempting access to 'lost_archive.txt'...")
        with open(filename1, "r") as file1:
            print(file1.read())
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    except Exception as e:
        print(f"RESPONSE: {e}")
    finally:
        print("STATUS: Crisis handled, system stable")
    print()

    filename2 = "classified_vault.txt"
    try:
        print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
        with open(filename2, "r") as file2:
            print(file2.read())
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    except Exception as e:
        print(f"RESPONSE: {e}")
    finally:
        print("STATUS: Crisis handled, security maintained")
    print()

    filename3 = "standard_archive.txt"
    try:
        print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
        with open(filename3, "r") as file3:
            print(f"SUCCESS: Archive recovered - \"{file3.read()}\"")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    except Exception as e:
        print(f"RESPONSE: {e}")
    finally:
        print("STATUS: Normal operations resumed")
    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
