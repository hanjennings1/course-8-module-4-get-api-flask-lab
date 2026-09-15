from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

# TODO: Implement homepage route that returns a welcome message

@app.route("/")
def home():
    # Return a welcome message
    return jsonify({"message": "Welcome to the Product Catalog API!"}), 200


#Implement GET /products route that returns all products or filters by category
@app.route("/products")
def get_products():
    # Return all products or filter by ?category=
    category = request.args.get("category")
    if category:
        # Filter products by category (case-insensitive match)
        filtered = [p for p in products if p["category"].lower() == category.lower()]
        return jsonify(filtered)
    # No filter provided — return all products
    return jsonify(products), 200


# Implement GET /products/<id> route that returns a specific product by ID or 404
@app.route("/products/<int:product_id>")
def get_product_by_id(product_id):
    # Find the first product matching the given id, else None
    product = next((p for p in products if p["id"] == product_id), None)

    if product:
        return jsonify(product), 200

    # No match found — return 404 with an error message
    return jsonify({"error": "Product not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
