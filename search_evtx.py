import os
import evtx


def search_events(folder_path, keyword):
    found_events = []

    for root, _, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".evtx"):
                file_path = os.path.join(root, filename)
                with evtx.Evtx(file_path) as log:
                    for record in log.records():
                        if keyword in record.xml():
                            found_events.append((filename, record.record_num))

    return found_events


def generate_statistics(found_events):
    event_count = len(found_events)
    event_files = set()
    for event in found_events:
        event_files.add(event[0])

    file_count = len(event_files)
    print("Statistics:")
    print(f"Total Events Found: {event_count}")
    print(f"Total Unique Files with Events: {file_count}")


def main():
    folder_path = input("Enter the folder path containing the .evtx files: ")
    keyword = input("Enter the keyword to search for: ")

    found_events = search_events(folder_path, keyword)

    if found_events:
        print("Found Events:")
        for event in found_events:
            print(f"File: {event[0]}, Event ID: {event[1]}")

        generate_statistics(found_events)
    else:
        print("No events found matching the keyword.")


if __name__ == "__main__":
    main()
