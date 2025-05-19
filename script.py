from time import sleep
import subprocess
import os

# ============ Output ===============
downloadPath = "D:\Youtube"
# ===================================

print("YouTube Downloader")
print("Ctrl+C to Interrupt\n")

format = input("Choose Format:\n1. Audio\n2. Video\n( Type 1 or 2 )\n\n")

try:
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        if format == "1":
            print("Youtube to Audio Downloader\n\n")
        if format == "2":
            print("Youtube to Video Downloader\n\n")
        url = input("Input Youtube URL: ")
        if not url:
            print("URL not valid. Please try again.\n")
            continue
        output_template = os.path.join(downloadPath, '%(title)s.%(ext)s')
        try:
            if format == "1":
                result = subprocess.run(['yt-dlp', '-x', '--audio-format', 'mp3', '-o', output_template, url], capture_output=True, text=True, check=True)
            if format == "2":
                result = subprocess.run(['yt-dlp', '-f', 'mp4', '-o', output_template, url], capture_output=True, text=True, check=True)
            print("\n\n\n🌐 Downloading...\n\n\n")
            sleep(5)
            print("✅ Success...")
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
            print(f"Output: {e.output}")

except KeyboardInterrupt:
    print("\n\nProgram Stopped. Thank you")
