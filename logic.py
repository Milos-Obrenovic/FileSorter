from json import load
import os

def sort_files_by_extension():
    # Get the user's home directory and the Downloads folder path
    home = os.path.expanduser("~")
    downloads = os.path.join(home, "Downloads")

    # Load the configuration from the JSON file
    with open("config.json", "r") as f:
        temp_config = load(f)

    config = {}
    for category, extensions in temp_config.items():
        for ext in extensions:
            config[ext] = category

    # Read the Downloads folder and sort
    for filename in os.listdir(downloads):
        ext = os.path.splitext(filename)[1].lower()
        if ext in config:
            target_folder = os.path.join(home, config[ext])
            os.makedirs(target_folder, exist_ok=True)

            source = os.path.join(downloads, filename)
            target = os.path.join(target_folder, filename)
            os.rename(source, target)
        else:
            print(f"Extension '{ext}' not found in config, skipping '{filename}'.")


if __name__ == "__main__":
    sort_files_by_extension()
