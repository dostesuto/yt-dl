
# YouTube Video Downloader

This is a simple Python-based tool that allows you to download YouTube videos directly from the command line. It uses the `yt-dlp` library for downloading and `ffmpeg` for merging video and audio files.

## Features

- Download videos from YouTube.
- Automatically merge video and audio files using `ffmpeg`.
- Choose the best video and audio quality available.
- Customizable output file naming.
- Simple command-line interface (CUI).

## Requirements

- Python 3.6 or higher
- `yt-dlp` (installed via `pip`)
- `ffmpeg` (required for merging video and audio files)

## Installation

### Step 1: Install Python

Ensure you have Python 3.6 or higher installed on your machine. You can download it from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/).

### Step 2: Install Dependencies

Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/yt-video-downloader.git
cd yt-video-downloader
```

Then, install the necessary Python libraries using `pip`:

```bash
pip install -r requirements.txt
```

Alternatively, you can manually install `yt-dlp` and `ffmpeg` using the following commands:

```bash
pip install yt-dlp
```

**For `ffmpeg`**:

- On Windows, download and install from [ffmpeg.org](https://ffmpeg.org/download.html).
- On macOS, use Homebrew: `brew install ffmpeg`.
- On Linux (Ubuntu/Debian), use: `sudo apt install ffmpeg`.

Make sure that `ffmpeg` is accessible in your system's `PATH`.

### Download the Python script

[Download Python script.](https://github.com/DQNEO/memo/blob/master/AboutMe.md)
### Step 3: Run the Script

Once everything is installed, you can run the downloader script:

```bash
python app.py
```

You will be prompted to enter a YouTube video URL:

```arduino
YouTubeのURLを入力してください: https://www.youtube.com/watch?v=kagoEGKHZvU
```

The script will download the video and automatically merge the best video and audio formats.

## Customization

You can modify the `app.py` file to customize the download behavior, such as changing the file output format or selecting a different quality.

For example, to download only the best audio, you can change the `ydl_opts` to:

```python
ydl_opts = {
    'format': 'bestaudio',
    'outtmpl': '%(title)s.%(ext)s',
}
```

## Troubleshooting

### Error: `ffmpeg is not installed`

Make sure you have `ffmpeg` installed and that it is in your system's `PATH`. For detailed installation instructions, see the section above.

### Error: `ERROR: You have requested merging of multiple formats but ffmpeg is not installed`

If you encounter this error, it's because `yt-dlp` requires `ffmpeg` to merge separate video and audio files. Installing `ffmpeg` will resolve the issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
