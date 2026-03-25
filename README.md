# SummarAIze - YouTube Video Summarizer

## Overview

summarAIze is an AI-powered application that generates concise summaries of YouTube videos. It extracts transcripts from videos and uses a transformer-based model to produce meaningful summaries, helping users quickly understand long video content.

## Features

* Extracts transcripts from YouTube videos
* Generates concise summaries using a pre-trained NLP model
* Simple API endpoint for integration
* Chrome extension interface for easy usage

## Tech Stack

* Backend: Python, Flask
* NLP Model: Hugging Face Transformers (DistilBART)
* Frontend: HTML, JavaScript (Chrome Extension)
* API: YouTube Transcript API

## Project Structure

```
summarAIze/
│
├── app.py                 # Flask backend
├── popup.html            # Chrome extension UI
├── popup.js              # Extension logic
├── hf_cache/             # Model cache directory
└── README.md
```

## Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/summarAIze.git
cd summarAIze
```

### 2. Install dependencies

```
pip install flask youtube-transcript-api transformers
```

### 3. Run the backend server

```
python app.py
```

The server will start at:

```
http://127.0.0.1:5000
```

## Usage

### API Endpoint

```
GET /summary?url=YOUTUBE_VIDEO_URL
```

### Example

```
http://127.0.0.1:5000/summary?url=https://www.youtube.com/watch?v=VIDEO_ID
```

### Response

```
{
  "summary": "Generated summary text..."
}
```

## Chrome Extension Setup

1. Open Chrome and go to `chrome://extensions/`
2. Enable Developer Mode
3. Click "Load unpacked"
4. Select the project folder
5. Open any YouTube video and click the extension button
6. Click "Summarise" to generate the summary

## How It Works

1. Extracts video ID from the YouTube URL
2. Fetches transcript using YouTube Transcript API
3. Splits transcript into chunks
4. Processes each chunk using a summarization model
5. Combines results into a final summary

## Limitations

* Works only for videos with available transcripts
* Long videos may take more time to process
* Summary quality depends on transcript accuracy

## Future Improvements

* Support for multiple languages
* Improved summarization accuracy
* UI enhancements
* Deployment on cloud for public access
* Text to Speech to read out the summary


