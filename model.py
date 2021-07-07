from flask import render_template, request

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle


def linear_regression_model():
    
    df = pd.read_csv('manhattan.csv')

    X = df[['bedrooms', 'bathrooms', 'size_sqft']]
    y = df.rent

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=6)

    model = LinearRegression()
    model.fit(X_train, y_train)

    file_name = 'linear_regression.pickle'
    pickle.dump(model, open(file_name, 'wb'))

    if request.method == 'POST':

        # This is one way to do it!
        # bedrooms = request.form['bedrooms_input']
        # bathrooms = request.form['bedrooms_input']
        # size_sqft = request.form['size_sqft_input']

        # Shortening the code above with list comprehension
        features = [int(x) for x in request.form.values()]
        final_features = [np.array(features)]

        # predicted_rent = model.predict(np.array([[bedrooms, bathrooms, size_sqft]]))

        loaded_model = pickle.load(open(file_name, 'rb'))

        predicted_rent = loaded_model.predict(final_features)

        predicted_rent = '\U0001F449 The predicted rent is ${}\U0001F448'.format(round(predicted_rent[0]))
        context = {'predicted_rent': predicted_rent}

        return render_template("predict.html", predicted_rent=context['predicted_rent'])

    else:
        return render_template("predict.html")