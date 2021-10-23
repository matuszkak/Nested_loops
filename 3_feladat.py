cars = [
    {
        "price": 1549,
        "passengerQty": 4,
        "currency": "EUR",
        "type": "Kia",
        "transmission": "manual",
        "passengers": ["Gabor", "Andras", "Timea", "Martin", "Miklos"]
    },
    {
        "price": 1954,
        "passengerQty": 5,
        "currency": "EUR",
        "type": "Suzuki",
        "transmission": "manual",
        "passengers": ["Gabor", "Andras", "Timea", "Martin", "Miklos"]
    },
    {
        "price": 2544,
        "passengerQty": 5,
        "currency": "USD",
        "type": "Opel",
        "transmission": "manual",
        "passengers": ["Gabor", "Andras", "Timea", "Martin", "Miklos"]
    },
    {
        "price": 2544,
        "passengerQty": 2,
        "currency": "USD",
        "type": "Opel",
        "transmission": "manual",
        "passengers": ["Gabor", "Timea", "Miklos"]
    },
    {
        "price": 9542,
        "passengerQty": 4,
        "currency": "USD",
        "type": "Ford",
        "transmission": "automatic",
        "passengers": ["Gabor", "Timea", "Miklos"]
    },
]

usd_eur = 0.86

for car in cars:
    if car["currency"] == "EUR":
        car["price"] = round(usd_eur * car["price"], 1)
        car["currency"] = "USD"
    print(
        f'a(z) {car["type"]} típusú autó ára {car["price"]} {car["currency"]}')
