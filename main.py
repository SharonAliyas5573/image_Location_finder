from flask import Flask, render_template, request
import piexif
import folium
import re   

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the uploaded image
        image_file = request.files["dropzone-file"]
        exif_dict = piexif.load(image_file.read())

        # Extract the geo location from the EXIF data
        latitude = exif_dict["GPS"][piexif.GPSIFD.GPSLatitude]
        longitude = exif_dict["GPS"][piexif.GPSIFD.GPSLongitude]

        # Convert the geo location to decimal degrees
        latitude = (latitude[0][0] / latitude[0][1] +latitude[1][0] / latitude[1][1] / 60 +latitude[2][0] / latitude[2][1] / 3600)
        longitude = (longitude[0][0] / longitude[0][1] +longitude[1][0] / longitude[1][1] / 60 +longitude[2][0] / longitude[2][1] / 3600)

        # Plot the geo location on a map
        map_location = folium.Map(location=[latitude, longitude], zoom_start=13)
        folium.Marker(location=[latitude, longitude]).add_to(map_location)
        map_html = map_location.get_root().render()
       

        return render_template("index.html", map_html=map_html)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
