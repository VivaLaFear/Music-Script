import yt_dlp
import os

def download_album(url):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'ffmpeg_location': current_dir, 
        'outtmpl': os.path.join(current_dir, 'Downloads', '%(album)s', '%(playlist_index)s - %(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }, {
            'key': 'EmbedThumbnail',
        }, {
            'key': 'FFmpegMetadata',
            'add_metadata': True,
        }],
        'writethumbnail': True,
        'quiet': False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\n[SUCCESS] Album downloaded to the 'Downloads' folder.")
    except Exception as e:
        print(f"\n[ERROR] Could not download this link: {e}")

def main():
    while True:
        print("\n--- Python Album Downloader ---")
        print("1. Download an Album/Playlist")
        print("2. Exit")
        
        choice = input("\nSelect an option (1 or 2): ").strip()

        if choice == '1':
            link = input("Paste the URL: ").strip()
            if link:
                download_album(link)
            else:
                print("Invalid URL. Please try again.")
        elif choice == '2':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid selection. Please enter 1 or 2.")

if __name__ == "__main__":
    main()