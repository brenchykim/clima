from flask import Flask, render_template
import requests

app = Flask (__name__)

def get_weather_data(city):
    API_KEY = '775912caa55ed46659e49ad990c41053'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ city }&units=metric&lang=es&appid={API_KEY}'
    r = requests.get(url).json()
    return r

@app.route("/")
def index():
    print(get_weather_data('Guayaquil'))
    return render_template('index.html',context='BRENCHY')

if __name__ == "__main__":
    app.run(debug=True)
 