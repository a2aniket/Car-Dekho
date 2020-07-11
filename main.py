from flask import Flask, render_template, request
import sys
import pickle
app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))

@app.route("/", methods=["GET", "POST"])
def home():
    prediction =""
    fuel_type_diesel = 0
    owner_two = 0
    if request.method == "POST":
        car_name = request.form.get("carName")
        year = int(request.form.get("year"))
        year = 2020-year
        price = int(float(request.form.get("price")))
        km_driven = int(request.form.get("kmDriven"))
        fuel_type_petrol = request.form.get("fuelType")
        if fuel_type_petrol == "Petrol":
            fuel_type_petrol = 1
            fuel_type_diesel = 0
        else:
            fuel_type_petrol = 0
            fuel_type_diesel = 1
        seller_type_dealer = request.form.get("sellerType")
        if seller_type_dealer == "Dealer":
            seller_type_dealer = 1
        else:
            seller_type_dealer = 0
        transmission_manual = request.form.get("transmission")
        if transmission_manual == "Manual":
            transmission_manual = 1
        else:
            transmission_manual = 0

        owner_one = int(request.form.get("owner"))
        if owner_one == 1:
            owner_one = 1
            owner_two = 0
        else:
            owner_one = 0
            owner_two = 1

        car_details = [5, year, price, km_driven, fuel_type_diesel, fuel_type_petrol, seller_type_dealer, transmission_manual, owner_one, owner_two]
        prediction = model.predict([car_details])
        prediction = round(prediction[0], 2)
    return render_template("Home.html", prediction=prediction)


app.run(debug=True)
sys.exit()
