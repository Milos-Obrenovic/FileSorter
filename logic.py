import json
import os
import shutil

def sort_files_by_extension():
    # ~/Downloads
    home = os.path.expanduser("~")
    downloads = os.path.join(home, "Downloads")
    config_path = os.path.join(os.path.dirname(__file__), "config.json")

    # Load config
    with open(config_path, "r") as f:
        temp_config = json.load(f)

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
            
            if os.path.exists(target):
                base, ext = os.path.splitext(filename)
                counter = 1
                while os.path.exists(target):
                    target = os.path.join(target_folder, f"{base}_{counter}{ext}")
                    counter += 1
            
            shutil.move(source, target)
        else:
            print(f"Extension '{ext}' not found in config, skipping '{filename}'.")


if __name__ == "__main__":
    sort_files_by_extension()
