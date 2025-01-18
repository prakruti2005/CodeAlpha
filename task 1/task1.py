import os
import shutil

def organize_files(directory):
    """Organize files in the specified directory into subfolders based on file extensions."""
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return

    # Define categories and their corresponding file extensions
    categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.flv'],
        'Music': ['.mp3', '.wav', '.aac', '.flac'],
        'Archives': ['.zip', '.rar', '.tar', '.gz'],
        'Scripts': ['.py', '.js', '.html', '.css'],
        'Others': []  # Catch-all category
    }

    # Create subfolders for each category
    for category in categories:
        category_path = os.path.join(directory, category)
        os.makedirs(category_path, exist_ok=True)

    # Move files into the appropriate subfolder
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        file_extension = os.path.splitext(file_name)[1].lower()
        destination_folder = 'Others'

        for category, extensions in categories.items():
            if file_extension in extensions:
                destination_folder = category
                break

        destination_path = os.path.join(directory, destination_folder, file_name)
        shutil.move(file_path, destination_path)
        print(f"Moved: {file_name} -> {destination_folder}")

    print("File organization complete!")

if __name__ == "__main__":
    target_directory = input("Enter the directory to organize: ").strip()
    organize_files(target_directory)
