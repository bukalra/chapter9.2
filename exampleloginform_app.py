from locale import currency
import os
import csv
from flask import Flask, render_template, request
from api import get_rates, export_file_to_csv

app = Flask(__name__)
@app.route("/calculator/", methods=["GET", "POST"])
def form_view():
    if request.method == "POST":
        data = request.form
        amount = data.get('amount')
        currency = data.get('currency')
        for item in items:
            if item['code'] == currency:
                result =  str(round(item['ask'] * float(amount),2))
                return render_template("result.html", entity=result)
    else:
        return render_template("index.html", items=items)

if __name__ == '__main__':
    items = get_rates()
    data = get_rates()
    export_file_to_csv(data)
    app.run(debug=True)