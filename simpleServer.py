from flask import Flask, request, render_template, json, jsonify

import os
from flask import send_file
import pyscreenshot as ImageGrab
import io
import numpy
from tempfile import NamedTemporaryFile
import time
import socket
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
   if False:
     im = im.rotate(90, expand=True)
     if False:
       im = im.crop(box=[1, 40, 1800, 1300])
     else:
       im = im.crop(box=[100, 550, 1100, 1800])
   else:
     if True:
         im = im.crop(box=[1375, 50, 3000, 2000])
     else:
         im = im.crop(box=[1570, 10, 3000, 2000])
   im.save(f, format='png')
   f.seek(0,0)
   #im.save("/home/aknirala/Pictures/screenshot"+time.ctime()+".jpg", "JPEG")
   return send_file(f, mimetype='image/gif')

if __name__ == "__main__":
    #Manually change the IP below to your PC current IP. I am sure there are ways to do it automatically.
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ipAddr = s.getsockname()[0]
    s.close()
    os.system("cp templates/render_Tmp.html templates/render.html")
    sedCommand = "sed -i \"s/PLACEHOLDER_01/"+ipAddr+"/g\" \"templates/render.html\""
    print(sedCommand)
    os.system(sedCommand)
    app.run(host=ipAddr, debug=True)
    #app.run(host='10.26.48.80', debug=True)
    #app.run(host='10.26.48.80', debug=True)
    #app.run(host='10.26.53.201', debug=True)
