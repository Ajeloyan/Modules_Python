def main() -> None:
    filename: str = "new_discovery.txt"
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print(f"Initializing new storage unit: {filename}")
    try:
        file = open(filename, "w")
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        file.write("[ENTRY 001] New quantum algorithm discovered\n"
                   "[ENTRY 002] Efficiency increased by 347%\n"
                   "[ENTRY 003] Archived by Data Archivist trainee")
        file.close()
        file = open(filename, "r")
        content = file.read()
        print(content)
        print()
        print("Data inscription complete. Storage unit sealed.")
        print(f"Archive '{filename}' ready for long-term preservation.")
    except PermissionError as e:
        print(e)
    finally:
        file.close()


if __name__ == "__main__":
    main()
