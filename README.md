# SharePCScreenshot
There is a way to use BOOX eReader as secondary display over WiFi, but is failing for me, so created a quick fix

On my Ubuntu PC I run a Flask python serevr. From the browser of my eReader I send an http GET request to it.
The Server grabs a screenshot of my PC and sends it back. In this way I am able to see the screen of my PC as an 
image to my eReader. Also I have created the HTML page such that when image is clicked it reloads the page. Thus to 
upate the screen shot of my PC, I just touch the image on my eReader once with the pen.
