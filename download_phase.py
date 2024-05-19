import requests
import threading
import os


def download(url, filename):
    response = requests.get(url, stream=True)
    with open(filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:  # Filter out keep-alive new chunks
                file.write(chunk)
    print(f'File downloaded and saved as {filename}')


def download_files_from_links(file_path):
    threads = []

    with open(file_path, 'r') as f:
        for line in f.readlines():
            parts = line.split()
            if len(parts) >= 3:
                url = parts[2].strip()
                filename = f'Ghahve_Talkh/{parts[0]}{parts[1].strip(":")}.mkv'

                if not os.path.exists(filename):
                    print(f'{filename} is downloading..')
                    thread = threading.Thread(target=download, args=(url, filename))
                    threads.append(thread)
                    thread.start()
                else:
                    print(f'{filename} already exists, skipping download.')

    # Wait for all threads to complete
    for thread in threads:
        thread.join()


# Example usage
download_files_from_links('Ghahve_Talkh/links.txt')
