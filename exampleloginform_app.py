from locale import currency
import os
import csv
from flask import Flask, render_template, request
from api import forwarder

items = forwarder()

app = Flask(__name__)
@app.route("/calculator/", methods=["GET", "POST"])
def form_view():
    if request.method == "POST":
        data = request.form
        amount = data.get('amount')
        currency = data.get('currency')
        for item in items:
            print(item['code'], currency)
            if item['code'] == currency:
                result =  str(round(item['ask'] * float(amount),2))
                entity = result
                return render_template("result.html", entity=entity)
    else:
        return render_template("index.html", items=items)

if __name__ == '__main__':
    app.run(debug=True)