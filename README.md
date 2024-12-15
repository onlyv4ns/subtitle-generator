# subtitle-generator

A Python-based tool for extracting audio from videos, transcribing the audio using OpenAI's Whisper model, and generating subtitles in the desired language. Optionally, the subtitles can be translated to a target language using Google Translate API. Ideal for generating subtitles quickly for various video content.

Features:

- Extracts audio from video files.
- Transcribes audio to text using Whisper.
- Generates .srt subtitle files.
- Supports optional translation of subtitles to a target language (e.g., Indonesian, English, etc.).

# Requirements

Make sure to install the following dependencies:

1. Clone the repository :

```bash
git clone https://github.com/onlyv4ns/subtitle-generator.git
cd video-subtitle-generator
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Install FFmpeg (required by moviepy):

```bash
sudo apt install ffmpeg
```

# Usage

Run the script as follows to generate subtitles from a video:

```bash
python sub.py -i path/to/video.mp4 -o path/to/output.srt --translate --lang en
```

Option :

-i: Path to input video.
-o: Path to output subtitle (.srt) file.
--translate: Optional flag to translate subtitles.
--lang: Target language for translation (default: id for Indonesian).
