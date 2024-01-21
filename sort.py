import os
import shutil
from concurrent.futures import ThreadPoolExecutor

def process_folder(folder_path):
    
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            move_file(file_path)

def move_file(file_path):
    
    _, extension = os.path.splitext(file_path)
    extension = extension[1:]  
    destination_folder = os.path.join("Хлам", extension)

    
    os.makedirs(destination_folder, exist_ok=True)

    
    shutil.move(file_path, os.path.join(destination_folder, os.path.basename(file_path)))

def main():
    input_folder = "Ваша_папка_хлам"
    output_folder = "Хлам"

    
    os.makedirs(output_folder, exist_ok=True)

    
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.submit(process_folder, input_folder)

if __name__ == "__main__":
    main()