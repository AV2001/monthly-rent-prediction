from flask import Flask, render_template
from model import linear_regression_model


app = Flask(__name__)

# Renders the index.html file and displays it whenever a user visits the home page
@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=["GET", "POST"])
def prediction():

    # Returning this function from the models.py file
    return linear_regression_model()


if __name__ == '__main__':
    app.run(debug=False)
