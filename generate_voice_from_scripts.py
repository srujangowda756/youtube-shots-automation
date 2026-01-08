import os
import pyttsx3

BASE_DIR = "shorts_output"


def generate_voice(script_path, output_path):
    spoken_lines = []

    # Read and clean script
    with open(script_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if line.startswith("HOOK:"):
                spoken_lines.append(line.replace("HOOK:", "").strip())
            elif line.startswith("INSIGHT:"):
                spoken_lines.append(line.replace("INSIGHT:", "").strip())
            elif line.startswith("CTA:"):
                spoken_lines.append(line.replace("CTA:", "").strip())

    if not spoken_lines:
        print(f"Skipped empty script: {script_path}")
        return

    final_text = " ".join(spoken_lines)

    # 🔑 FIX: Create a NEW engine per file
    engine = pyttsx3.init()
    engine.setProperty("rate", 165)

    engine.save_to_file(final_text, output_path)
    engine.runAndWait()

    # Explicit cleanup (important on Windows)
    del engine


def process_all_scripts():
    for date_folder in os.listdir(BASE_DIR):
        date_path = os.path.join(BASE_DIR, date_folder)
        if not os.path.isdir(date_path):
            continue

        for short_folder in os.listdir(date_path):
            short_path = os.path.join(date_path, short_folder)
            script_path = os.path.join(short_path, "script.txt")
            voice_path = os.path.join(short_path, "voice.mp3")

            if os.path.exists(script_path) and not os.path.exists(voice_path):
                print(f"Generating voice for {script_path}")
                generate_voice(script_path, voice_path)

    print("Voice generation complete.")


if __name__ == "__main__":
    process_all_scripts()
