import os
os.environ["HF_HOME"] = "./hf_cache"

from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline

import urllib.parse

def extract_video_id(url):
    parsed_url = urllib.parse.urlparse(url)
    query = urllib.parse.parse_qs(parsed_url.query)
    return query.get("v", [""])[0]

app = Flask(__name__)

summariser = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)

@app.get('/summary')
def summary_api():
    url = request.args.get('url', '')

    if not url:
        return jsonify({"error": "Missing URL"}), 400

    video_id = extract_video_id(url)

    if not video_id:
        return jsonify({"error": "Invalid YouTube URL"}), 400

    transcript = get_transcript(video_id)

    if transcript.startswith("Error"):
        return jsonify({"error": transcript}), 500

    summary = get_summary(transcript)

    return jsonify({
        "summary": summary
    }), 200


def get_transcript(video_id):
    try:
        api = YouTubeTranscriptApi()
        transcript_list = api.fetch(video_id)
        transcript = ' '.join([d.text for d in transcript_list])
        return transcript
    except Exception as e:
        return f"Error: {str(e)}"

def get_summary(transcript):
    summary = ''

    for i in range(0, (len(transcript)//1000)+1):
        chunk = transcript[i*1000:(i+1)*1000]

        if chunk.strip() == "":
            continue

        result = summariser(
            chunk,
            max_length=120,
            min_length=30,
            do_sample=False
        )

        summary += result[0]['summary_text'] + ' '

    return summary
    

if __name__ == '__main__':
    app.run()