from flask import Flask, jsonify, request

app = Flask(__name__)

# A simple in-memory "database" (list of dictionaries)
books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 2, "title": "1984", "author": "George Orwell"},
]


# 1. GET Endpoint: Retrieve all books
@app.route("/books", methods=["GET"])
def get_books():
  # Returns 200 OK with the full list of books
  return jsonify({"books": books}), 200


# 2. GET Endpoint: Retrieve a single book by its ID
@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
  for book in books:
    if book["id"] == book_id:
      return jsonify(book), 200  # 200 OK

  # If the book doesn't exist, return 404 Not Found
  return jsonify({"error": "Book not found!"}), 404


# 3. POST Endpoint: Add a new book to the library
@app.route("/books", methods=["POST"])
def add_book():
  data = request.get_json()

  # Validate that the client sent both title and author
  if not data or "title" not in data or "author" not in data:
    return (
        jsonify({"error": "Bad Request: 'title' and 'author' are required."}),
        400,
    )  # 400 Bad Request

  # Create the new book object
  new_book = {
      "id": len(books) + 1,
      "title": data["title"],
      "author": data["author"],
  }
  books.append(new_book)

  # Return 201 Created with the new book details
  return (
      jsonify({"message": "Book added successfully!", "book": new_book}),
      201,
  )


if __name__ == "__main__":
  app.run(debug=True)