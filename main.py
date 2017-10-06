from flask import Flask, render_template, request
from apiRequests import build_weather_api_call, build_weather_data

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods = ['POST', 'GET'])
def weather_api_call():
    if request.method == 'POST':
        try:
            city_name = request.form["city_name"]
            city_data = build_weather_data(city_name)
            return render_template('index.html', city_data=city_data)  
        except (TypeError):
            return render_template('index.html', error="Please enter a valid city!")

    return render_template('index.html')



app.run()