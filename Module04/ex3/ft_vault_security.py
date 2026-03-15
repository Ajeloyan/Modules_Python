def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    filename1: str = "classified_data.txt"
    filename2: str = "security_protocols.txt"
    try:
        print("Initiating secure vault access...")
        with open(filename1, "r") as file1:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            print(file1.read())
        print()
        with open(filename2, "w") as file2:
            print("SECURE PRESERVATION:")
            content = "[CLASSIFIED] New security protocols archived"
            file2.write(content)
            print(content)
        print("Vault automatically sealed upon completion")
    except (PermissionError, FileNotFoundError) as e:
        print(e)
        return
    print()
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
