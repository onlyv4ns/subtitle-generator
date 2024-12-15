import whisper
from moviepy.editor import *
from googletrans import Translator
import datetime
import argparse
import os
from tqdm import tqdm

def extract_audio_from_video(video_path, audio_output_path):
    video_clip = VideoFileClip(video_path)
    video_clip.audio.write_audiofile(audio_output_path)

def transcribe_audio(audio_path):
    model = whisper.load_model("base")
    print("Transcribing audio, this may take a while...")
    result = model.transcribe(audio_path)
    return result['segments']

def translate_text(text, dest_lang='id'):
    translator = Translator()
    translated = translator.translate(text, dest=dest_lang)
    return translated.text

def generate_srt(transcriptions, translate=False, dest_lang='id'):
    srt_output = ""
    print("Generating subtitles...")
    for i, segment in enumerate(tqdm(transcriptions, desc="Subtitles")):
        start_time = str(datetime.timedelta(seconds=int(segment['start'])))
        end_time = str(datetime.timedelta(seconds=int(segment['end'])))
        text = segment['text']
        
        if translate:
            text = translate_text(text, dest_lang)
        
        srt_output += f"{i + 1}\n{start_time},000 --> {end_time},000\n{text}\n\n"
    
    return srt_output

def save_srt(srt_content, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(srt_content)

def main(video_path, srt_output_path, audio_output_path="audio.wav", translate=False, dest_lang="id"):
    if not os.path.exists(video_path):
        print(f"Error: The video file {video_path} does not exist.")
        return

    print(f"Extracting audio from {video_path}...")
    extract_audio_from_video(video_path, audio_output_path)

    transcriptions = transcribe_audio(audio_output_path)

    srt_content = generate_srt(transcriptions, translate=translate, dest_lang=dest_lang)

    print(f"Saving subtitles to {srt_output_path}...")
    save_srt(srt_content, srt_output_path)
    print(f"Subtitles saved successfully to {srt_output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate subtitles for a video.")
    parser.add_argument("-i", "--input", required=True, help="Input video file")
    parser.add_argument("-o", "--output", required=True, help="Output .srt file")
    parser.add_argument("--translate", action="store_true", help="Translate subtitles (default: False)")
    parser.add_argument("--lang", default="id", help="Destination language for translation (default: 'id')")
    
    args = parser.parse_args()

    video_path = args.input
    srt_output_path = args.output
    translate = args.translate
    dest_lang = args.lang

    main(video_path, srt_output_path, translate=translate, dest_lang=dest_lang)
