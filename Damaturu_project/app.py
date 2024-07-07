from flask import Flask, jsonify, render_template, send_from_directory
import os
import requests
from config import API_KEY, OPENWEATHERMAP_API_KEY

app = Flask(__name__, static_url_path='/static')

# Replace CITY with the desired city name
CITY = "damaturu,yobe"
WEATHER_API_URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={OPENWEATHERMAP_API_KEY}&units=metric"

def fetch_weather_data():
    try:
        response = requests.get(WEATHER_API_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return {"error": "Could not fetch weather data"}

@app.route('/data', methods=['GET'])
def get_weather_data():
    weather_data = fetch_weather_data()
    return jsonify(weather_data)

@app.route('/index.html', methods=['GET'])
def serve_html():
    return render_template('index.html', api_key=API_KEY)

if __name__ == '__main__':
    app.run(debug=True)
