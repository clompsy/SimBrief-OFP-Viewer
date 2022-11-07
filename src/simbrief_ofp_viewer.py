from flask import Flask, render_template, request, jsonify
import requests
import xmltodict

app = Flask(__name__)

@app.route('/')
def index():
    if request.args.get("id") is not None:
        url = "https://www.simbrief.com/api/xml.fetcher.php?userid=" + request.args.get("id")
    elif request.args.get("name") is not None:
        url = "https://www.simbrief.com/api/xml.fetcher.php?username=" + request.args.get("name")
    else:
        return "Open the URL by providing either a simbrief id as 'id' parameter or simbrief username as 'name' parameter."
    
    response = requests.get(url)
    data = xmltodict.parse(response.content)
    
    if response.status_code == 400:
        return data['OFP']['fetch']['status']
    else:
        return render_template('index.html', data=data)

@app.route('/metar', methods= ['GET'])
def metar():
    url = "https://metar.vatsim.net/metar.php?id=" + request.args.get("station")
    response = requests.get(url)
    return jsonify(metar=response.text)

if __name__ == '__main__':
   app.run(host="0.0.0.0")