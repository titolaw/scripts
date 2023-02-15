# Downloads youtube videos as mp3 and saves to ~/Music

import sys
import subprocess
import os

# Get YouTube URL from command line argument
if len(sys.argv) < 2:
    print("Error: Please provide a YouTube URL.")
    sys.exit(1)
url = sys.argv[1]

# Create the Music directory if it doesn't exist
music_dir = os.path.expanduser('~/Music')
if not os.path.exists(music_dir):
    os.makedirs(music_dir)

# Download the audio as an mp3 file to the Music directory
try:
    subprocess.call(['youtube-dl', '-x', '--audio-format', 'mp3', '-o', f'{music_dir}/%(title)s.%(ext)s', url])
    print("Download complete!")
except:
    print("Error: Could not download audio.")
    sys.exit(1)

