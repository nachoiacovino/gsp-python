# Python Gender Model

Install the requirements inside the project with

### pip install -r requirements.txt

This project is a gender prediction tool, there is an input CSV and the when you run the file with

### py **init**.py

you get everything from the input.csv, pass it for the gender_model and get a level of confidence for man/woman, we store this in a prediction column and the higher one in a confidence column in another file called results.csv

Lastly, there's a function that calculates how many predictions were accurate, because we know beforehand if they are male/female, we can know how many predictions were corrected and the percentage is printed on the console.

Note: The model will output a slightly different value each time you run a prediction.
