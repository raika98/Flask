from flask import Flask, render_template, request

import pandas
from sklearn.tree import DecisionTreeClassifier

data = pandas.read_csv ("Categories.csv")

x = data.drop(columns=["Price"])
y = data["Price"]

model = DecisionTreeClassifier()

model.fit(x, y)

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
    
def home():
    name = "Amazing"

    if request.method == "POST":
        Age = request.form['Age']
        Sex = request.form['Sex']

        predicted_value = model.predict([[Age, Sex]])

        return render_template("index.html", predicted_Price=predicted_value[0])
    return render_template("index.html", predicted_Price=name)

if __name__ == '__main__':
    app.run(debug=True)
