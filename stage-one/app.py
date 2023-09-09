"""A simple app that displays a json response"""
from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

app.route('/api/')
def json_response():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    curr_datetime = datetime.utcnow()
    day = curr_datetime.strftime('%A')
    date_time = curr_datetime.strftime('%Y%m%dT%H%M%SZ')
    
    if slack_name is not None and track is not None:
        data = {
            "slack_name": "TJames28",
            "current_day": day,
            "utc_time": date_time,
            "track": "backend",
            "github_file_url": "",
            "github_repo_url":,
            "status_code":,
        }
        
    return jsonify(data)


if __name__ == "__main__":
    app.run()
        