# Monthly Rent Prediction (Using Linear Regression)

## Project Overview
This particular Machine Learning project was built using the Flask framework, and the purpose of the ML model that runs behind the scenes, is to predict the monthly rent in the borough of Manhattan, located in the city that never sleeps - New York.

## How Will The ML Model Be Triggered?
To keep things simple, the user will pass several values (number of bedrooms, bathrooms, and the square footage of the house) to the HTML form's input boxes. These values will then be fed to the Linear Regression algorithm, which in turn helps predict the rent of the house.

## Demo
If you would like to a feel for how the web application actually works, it has been deployed to Heroku.  
The URL is active, so feel free to take a look at it! 👉 https://monthly-rent-prediction.herokuapp.com/ 
  
If the website is taking too long to load, it's one of two possible reasons.  
1. The application might be too heavy.
2. Since I'm using the free version of Heroku, it's probably slow.

## Procfile
Do not even bother paying attention to the Procfile cause it's ONLY for Heroku deployment purposes.

## Technologies Used
* Python
* Flask
* HTML & CSS

## Cloning
Want to get the copy of the files used in this project onto your own device?  
Simply clone it or download the Zip folder!  

As far as the Python libraries/modules are concerned, I have shared the requirements.txt  
which you can use to install the same versions used in this project.
  
To download all the libs/mods in one go:  
1. cd to the directory where requirements.txt is located
2. run the command --> pip install -r requirements.txt

main.py is the file that must be run on your machine to fire up the local server.
