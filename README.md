# Module Lab: Building RESTful GET APIs with Flask
**Completed Sept 15, 2026**

## Overview

This is a Read-Only RESTful API built with Flask that serves a mock product catalog. It supports fetching all products, filtering by category, and retrieving a single product by ID. All responses are returned as JSON with appropriate HTTP status codes.

## Learning Goals

- Implement RESTful API endpoints using Flask
- Handle HTTP GET methods to serve resource data
- Support query parameters and dynamic route segments
- Return consistent JSON responses using `jsonify()`
- Follow RESTful conventions in route structure and response formatting

## Project Structure

```
.
├── app.py          # Flask app and route definitions
├── data.py         # Mock product data
├── test_app.py     # Pytest test suite
├── Pipfile
├── Pipfile.lock
└── README.md
```

## Setup Instructions

### Clone the Repository

```bash
git clone https://github.com/hanjennings1/course-8-module-4-get-api-flask-lab.git
cd course-8-module-4-get-api-flask-lab
```

### Install Dependencies

```bash
pipenv install
pipenv shell
```

### Run the Server

```bash
python app.py
```

The API runs at `http://localhost:5000` by default.

## API Endpoints

### `GET /`

Returns a welcome message.

**Example response (200):**
```json
{
  "message": "Welcome to the Product Catalog API!"
}
```

### `GET /products`

Returns all products. Optionally filter by category using the `category` query parameter (case-insensitive).

**Example:** `GET /products?category=books`

**Example response (200):**
```json
[
  {
    "id": 2,
    "name": "Book",
    "price": 14.99,
    "category": "books"
  }
]
```

With no query parameter, all products are returned. An unmatched category returns an empty list.

### `GET /products/<id>`

Returns a single product by its integer ID.

**Example:** `GET /products/1`

**Example response (200):**
```json
{
  "id": 1,
  "name": "Laptop",
  "price": 899.99,
  "category": "electronics"
}
```

**If the ID doesn't exist (404):**
```json
{
  "error": "Product not found"
}
```

## Testing

The project includes a pytest suite covering all three routes.

```bash
pytest
```

All tests pass, covering:
- Homepage returns a 200 with a welcome message
- `/products` returns a list of all products
- Category filtering behaves as expected
- `/products/<id>` returns the correct product or a 404 for an invalid ID

## Implementation Notes

- Mock data lives in `data.py` and is imported into `app.py`, keeping data separate from route logic.
- All responses use `jsonify()` to ensure consistent JSON formatting and the correct `Content-Type` header.
- Category filtering normalizes both the query parameter and stored data with `.lower()` to avoid case-sensitivity mismatches.
- The `/products/<int:product_id>` route uses Flask's `int` converter, so non-numeric IDs are automatically rejected by Flask's routing before reaching the view function.
- HTTP status codes are explicit where it matters: `200` for successful lookups, `404` when a product ID isn't found.

## Conclusion

This lab covers the foundation of building read-only RESTful routes in Flask: serving collections, filtering with query strings, retrieving single resources by dynamic route segments, and returning well-structured JSON with correct status codes. This sets up the foundation for full CRUD APIs in the next module.