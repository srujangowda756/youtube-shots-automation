import os
import numpy as np
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.VideoClip import VideoClip

BASE_DIR = "shorts_output"

WIDTH = 1080
HEIGHT = 1920
FPS = 24


def make_animated_background(t):
    """
    Generates a smooth animated gradient frame (AI-style visuals)
    """
    x = np.linspace(0, 1, WIDTH)
    y = np.linspace(0, 1, HEIGHT)
    xv, yv = np.meshgrid(x, y)

    r = 0.5 + 0.5 * np.sin(2 * np.pi * (xv + t * 0.15))
    g = 0.5 + 0.5 * np.sin(2 * np.pi * (yv + t * 0.12))
    b = 0.5 + 0.5 * np.sin(2 * np.pi * (xv + yv + t * 0.10))

    frame = np.stack([r, g, b], axis=2)
    return (frame * 255).astype(np.uint8)


def generate_video(short_path):
    voice_path = os.path.join(short_path, "voice.mp3")
    output_path = os.path.join(short_path, "video.mp4")

    audio = AudioFileClip(voice_path)
    duration = audio.duration

    video = VideoClip(
        make_animated_background,
        duration=duration
    ).with_audio(audio)   # ✅ MoviePy 2.x method

    video.write_videofile(
        output_path,
        fps=FPS,
        codec="libx264",
        audio_codec="aac"
    )

    audio.close()
    video.close()


def process_all_shorts():
    for date_folder in os.listdir(BASE_DIR):
        date_path = os.path.join(BASE_DIR, date_folder)
        if not os.path.isdir(date_path):
            continue

        for short_folder in os.listdir(date_path):
            short_path = os.path.join(date_path, short_folder)
            video_path = os.path.join(short_path, "video.mp4")

            if os.path.exists(os.path.join(short_path, "voice.mp3")) and not os.path.exists(video_path):
                print(f"Generating AI-style animated video for {short_path}")
                generate_video(short_path)

    print("AI-style video generation complete.")


if __name__ == "__main__":
    process_all_shorts()
