import requests
from flask import Flask , render_template , request

data = [{"table":"C","no":"133/C/NBP/2022","tradingDate":"2022-07-11","effectiveDate":"2022-07-12","rates":
[
 {"currency":"dolar amerykański","code":"USD","bid":4.7167,"ask":4.8119},
 {"currency":"dolar australijski","code":"AUD","bid":3.1745,"ask":3.2387},
 {"currency":"dolar kanadyjski","code":"CAD","bid":3.6222,"ask":3.6954},
 {"currency":"euro","code":"EUR","bid":4.7496,"ask":4.8456},
 {"currency":"forint (Węgry)","code":"HUF","bid":0.011561,"ask":0.011795},
 {"currency":"frank szwajcarski","code":"CHF","bid":4.8034,"ask":4.9004},
 {"currency":"funt szterling","code":"GBP","bid":5.6129,"ask":5.7263},
 {"currency":"jen (Japonia)","code":"JPY","bid":0.034319,"ask":0.035013},
 {"currency":"korona czeska","code":"CZK","bid":0.1930,"ask":0.1970},
 {"currency":"korona duńska","code":"DKK","bid":0.6383,"ask":0.6511},
 {"currency":"korona norweska","code":"NOK","bid":0.4616,"ask":0.4710},
 {"currency":"korona szwedzka","code":"SEK","bid":0.4436,"ask":0.4526},
 {"currency":"SDR (MFW)","code":"XDR","bid":6.1549,"ask":6.2793}
 ]
 }]

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()

with open("rates.csv", "w") as plik:
        
    for rate in data[0]["rates"]:
        plik.write(rate.get("currency"))
        plik.write(";")
        plik.write(rate.get("code"))
        plik.write(";")
        plik.write(str(rate.get("bid")))
        plik.write(";")
        plik.write(str(rate.get("ask")))
        plik.write("\n")


        
        print(f"{rate['currency']}, {rate['code']}")
        print(rate["bid"]) 
        print(rate["ask"])
        print("----------------")



app = Flask(__name__)
rates=[
 {"currency":"dolar amerykański","code":"USD","bid":4.7167,"ask":4.8119},
 {"currency":"dolar australijski","code":"AUD","bid":3.1745,"ask":3.2387},
 {"currency":"dolar kanadyjski","code":"CAD","bid":3.6222,"ask":3.6954},
 {"currency":"euro","code":"EUR","bid":4.7496,"ask":4.8456},
 {"currency":"forint (Węgry)","code":"HUF","bid":0.011561,"ask":0.011795},
 {"currency":"frank szwajcarski","code":"CHF","bid":4.8034,"ask":4.9004},
 {"currency":"funt szterling","code":"GBP","bid":5.6129,"ask":5.7263},
 {"currency":"jen (Japonia)","code":"JPY","bid":0.034319,"ask":0.035013},
 {"currency":"korona czeska","code":"CZK","bid":0.1930,"ask":0.1970},
 {"currency":"korona duńska","code":"DKK","bid":0.6383,"ask":0.6511},
 {"currency":"korona norweska","code":"NOK","bid":0.4616,"ask":0.4710},
 {"currency":"korona szwedzka","code":"SEK","bid":0.4436,"ask":0.4526},
 {"currency":"SDR (MFW)","code":"XDR","bid":6.1549,"ask":6.2793}
]

codes = ["USD", "AUD", "CAD", "EUR", "HUF", "CHF", "GBP", "JPY", "CZK", "DKK", "NOK" , "SEK", "XDR"]

@app.route("/" , methods=["GET", "POST"])
def kantor():
    if request.method == ["GET"]:
        print("We recived POST")
        amount = request.form["amount"]
        for rate in rates:
            if rate["code"] == request.form["codes"]:
                kwota = round((float((rate["ask"]) * float(amount))), 2)

    return render_template("base.html", date=date , codes=codes, result=kwota)
