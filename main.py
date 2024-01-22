from flask import Flask, render_template, request, redirect, url_for, g, jsonify, json
from geopy import distance
import os
import math, numpy as np


# def get_direction(latlng1,latlng2):
#     lon1 = latlng1[1]
#     lat1 = latlng1[0]
#     lon2 = latlng2[1]
#     lat2 = latlng2[0]
#     dLon = lon2 - lon1;
#     y = math.sin(dLon) * math.cos(lat2);
#     x = math.cos(lat1)*math.sin(lat2) - math.sin(lat1)*math.cos(lat2)*math.cos(dLon);
#     brng = np.rad2deg(math.atan2(y, x));
#     if brng >= 315 or brng <= 45:
#         direction = 'north'
#     elif brng > 45 and brng <= 135:
#         direction = 'east'
#     elif brng > 135 and brng <= 225:
#         direction = 'south'
#     else:
#         direction = 'west'
#     return direction

urls = {1: 'https://i.ibb.co/PtFTSRy/output-01.jpg',
    2: 'https://i.ibb.co/sgBRjVv/output-02.jpg',
    3: 'https://i.ibb.co/FbrBQ3H/output-03.jpg',
    4: 'https://i.ibb.co/zJNXLNf/output-04.jpg',
    5: 'https://i.ibb.co/Y0PDZdJ/output-05.jpg',
    6: 'https://i.ibb.co/cLJd61X/output-06.jpg',
    7: 'https://i.ibb.co/CPR6qJZ/output-07.jpg',
    8: 'https://i.ibb.co/zmS1r6v/output-08.jpg',
    9: 'https://i.ibb.co/PrtpV50/output-09.jpg',
    10: 'https://i.ibb.co/yddVKs4/output-10.jpg',
    11: 'https://i.ibb.co/NSfcpyF/output-11.jpg',
    12: 'https://i.ibb.co/k8VS1CV/output-12.jpg',
    13: 'https://i.ibb.co/1mKC857/output-13.jpg',
    14: 'https://i.ibb.co/YfYhxcV/output-14.jpg',
    15: 'https://i.ibb.co/RvhxwFz/output-15.jpg',
    16: 'https://i.ibb.co/LPhW6Gt/output-16.jpg',
    17: 'https://i.ibb.co/pyCZLT6/output-17.jpg',
    18: 'https://i.ibb.co/BjJTkQn/output-18.jpg',
    19: 'https://i.ibb.co/g72dWNt/output-19.jpg',
    20: 'https://i.ibb.co/r446xP7/output-20.jpg',
    21: 'https://i.ibb.co/kJBW6BQ/output-21.jpg'}

locations = {1:[35.447623115956944, 139.646890697955],
2:[35.445450447446596, 139.65093725461762],
3:[35.44516616336661, 139.64982127391968],
4:[35.4501462210642, 139.639305673953],
5:[35.44913271480336, 139.6368393470723],
6:[35.4473776722891, 139.64156299746497],
7:[35.44752867100016, 139.64314849631197],
8:[35.45000109733972, 139.6362910895489],
9:[35.45177999708371, 139.63342026390674],
10:[35.446281932601444, 139.63000125734217],
11:[35.446778869100754, 139.6311812611813],
12:[35.44606165602915, 139.6287907904504],
13:[35.44438745545561, 139.63549024015703],
14:[35.44479720092408, 139.63331563763015],
15:[35.44532999001117, 139.63401537299026],
16:[35.44102051111175, 139.62810703502046],
17:[35.440692477603015, 139.6282870428625],
18:[35.44244283907018, 139.6471656043005],
19:[35.443735857907924, 139.64732378647741],
20:[35.44413746984906, 139.64373123469588],
21:[35.443946331806536, 139.64779957085614]}


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', urls = urls)

@app.route('/linkstreetview', methods=['GET', 'POST'])
def linkstreetview():
    data = request.get_json()
    key = data[1].split("-")[1].split(".")[0]
    markerlatlng = [data[0]["lat"],data[0]["lng"]]
    selfielatlng = locations[int(key)]
    distance_feet = distance.distance(selfielatlng, markerlatlng).feet
    # direction = get_direction(selfielatlng, markerlatlng)
    if distance_feet < 500:
        text = f"The Kasuga Sniffer barks excitedly! The selfie was taken less than 500 feet away."
    elif distance_feet < 1000:
        text = "The Kasuga Sniffer seems to smell something. The selfie was taken within 1000 feet."
    else:
        text = "The Kasuga Sniffer does not react."
    map_url = f'http://maps.google.com/maps?q=&layer=c&cbll={markerlatlng[0]},{markerlatlng[1]}&cbp=11,0,0,0,0'
    #html = f'<a href=\"{map_url}\">View this location in Google Street View</a>'
    return jsonify(result=text, map_url=map_url)
    
if __name__ == "__main__":
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host="127.0.0.1", port=8080, debug=True)






    




