# YouTube Shorts Automation Tool

An end-to-end Python automation tool that converts raw video files into **YouTube Shorts–ready clips** by automating trimming, formatting, and export for vertical video platforms.

---

## 🚀 Features

- Automatically processes raw videos into **YouTube Shorts format (9:16)**
- Supports **video trimming and resizing**
- Generates platform-ready output clips
- Reduces repetitive manual video editing work
- Simple and reusable Python-based workflow

---

## 🛠 Tech Stack

- Python  
- Video Processing Libraries (e.g., MoviePy)  
- OS File Handling  

---

## 📂 Project Structure

youtube-shots-automation/
│
├── input_videos/ # Raw input videos
├── output_shorts/ # Generated YouTube Shorts
├── main.py # Core automation script
├── requirements.txt # Project dependencies
└── README.md

---

## ⚙️ How It Works

1. Place raw video files inside the `input_videos/` folder  
2. Run the automation script  
3. The script:
   - Trims the video (if configured)
   - Converts it to vertical format
   - Exports Shorts-ready clips to `output_shorts/`
4. Upload the generated clips directly to YouTube Shorts

---

## ▶️ Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/srujangowda756/youtube-shots-automation.git
cd youtube-shots-automation
pip install -r requirements.txt
python main.py
