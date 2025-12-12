from flask import Flask, request, send_from_directory  # type: ignore

app = Flask(__name__)
# print("app:", app) # <Flask 'app'>

stores = [{"name": "My Store", "items": [{"name": "Chair", "price": 15.99}]}]


# Serve the favicon.svg from the 'static' folder
@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        app.static_folder, "favicon.svg", mimetype="image/svg+xml"
    )


@app.get("/store")
def get_stores():
    return {"stores": stores}


@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201


@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "Store not found"}, 404


@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "Store not found"}, 404


@app.get("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message": "Store not found"}, 404
