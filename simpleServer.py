from flask import Flask, request, render_template, json, jsonify

import os
from flask import send_file
import pyscreenshot as ImageGrab
import io
import numpy
from tempfile import NamedTemporaryFile


ASSETS_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
 

@app.route("/")
def hello():
    return "Server hears you!!"

@app.route('/<string:page_name>/')
def render_static(page_name):
    return render_template('%s.html' % page_name)

#Copied with pride from: https://stackoverflow.com/questions/7877282/how-to-send-image-generated-by-pil-to-browser
def serve_pil_image(pil_img):
    img_io = numpy.genfromtxt(io.BytesIO(pil_img.encode()))
    img_io.seek(0)
    return send_file(img_io , mimetype='image/jpeg')

@app.route("/<int:param>/")
def go_to(param):
    return getImage()

@app.route('/getImage', methods=['GET'])
def getImage():
   im=ImageGrab.grab()
   f = NamedTemporaryFile(delete=False)
   im = im.rotate(90, expand=True)
   im.save(f, format='png')
   f.seek(0,0)
   return send_file(f, mimetype='image/gif')

if __name__ == "__main__":
    #Manually change the IP below to your PC current IP. I am sure there are ways to do it automatically.
    app.run(host='10.36.56.27', debug=True)
