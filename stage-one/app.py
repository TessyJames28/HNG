"""A simple app that displays a json response"""
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

@app.route('/api', strict_slashes=False)
def json_response():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    curr_datetime = datetime.utcnow()
    day = curr_datetime.strftime('%A')
    date_time = curr_datetime.strftime('%Y-%m-%dT%H:%M:%SZ')
    data = {}
    
    if slack_name is not None and track is not None:
        data = {
            "slack_name": "TJames28",
            "current_day": day,
            "utc_time": date_time,
            "track": "backend",
            "github_file_url": "https://github.com/TessyJames28/HNG/blob/main/stage-one/app.py",
            "github_repo_url": "https://github.com/TessyJames28/HNG",
            "status_code": 200,
        }
        
    return jsonify(data)


if __name__ == "__main__":
    app.run()