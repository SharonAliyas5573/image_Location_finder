# image_Location_finderGEOSNAP

GEOSNAP is a web application that plots the geo-location of an image on a map. The application is built using Flask, a popular Python web framework, and uses the Folium library to create the map and the Piexif library to extract the geo-location information from the image's EXIF data.
Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
Prerequisites

The following libraries must be installed in order to run the GEOSNAP application:

    Flask
    Folium
    Piexif

You can install the libraries by running the following command in your terminal:

pip install flask folium piexif

Running the Application

To run the GEOSNAP application, simply run the following command in your terminal:

python app.py

This will start the Flask development server and you can access the application at http://127.0.0.1:5000/ in your web browser.

Built With

    Flask - The web framework used
    Folium - The library used to create the map
    Piexif - The library used to extract the geo-location information from the image's EXIF data



This project is licensed under the MIT License - see the LICENSE file for details.