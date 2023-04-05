# Nicole Zhou, Marc Jiang
# M & N
# SoftDev
# Nov 21 2022


from flask import Flask  # facilitate flask webserving
from flask import render_template  # facilitate jinja templating
import requests

app = Flask(__name__)  # create Flask object




@app.route("/", methods=['GET', 'POST'])
def display_img():
    key = open("key_nasa.txt").read()
    r = requests.get(f"https://api.nasa.gov/planetary/apod?api_key=B1EO3QsuyDdnHPatdgaTVSbqEBLlgbxLdVDNmlr9")
    dict = r.json()
    url = dict['url']
    explanation = dict['explanation']
    return render_template("main.html",img = url, info = explanation)


if __name__ == "__main__":  # false if this file imported as module
    # enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
