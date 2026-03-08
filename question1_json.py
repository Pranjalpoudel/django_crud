# Submitted by: Pranjal Poudel
import json

"""
Question 1:
How do you parse JSON data in Python using the json module? How do you convert Python
dictionary back to JSON string? Write a Python program to parse a JSON string containing book
information (id, title, author, year, genres array), access and print each field, modify the data (add
rating, append to genres), and convert back to JSON.
"""

# JSON parsing: use json.loads() for strings or json.load() for files.
# Dictionary to JSON: use json.dumps() for strings or json.dump() for files.

# 1. Parse JSON string
book_json = """
{
    "id": 101,
    "title": "Python Programming",
    "author": "Guido van Rossum",
    "year": 1991,
    "genres": ["Educational", "Technology"]
}
"""

data = json.loads(book_json)

# 2. Access and print each field
print("ID:", data["id"])
print("Title:", data['title'])
print("Author:", data["author"])
print("Year:", data["year"])
print("Genres:", ", ".join(data["genres"]))

# 3. Modify the data
data["rating"] = 4.8  # Add rating
data["genres"].append("Programming")  # Append to genres

# 4. Convert back to JSON string
updated_json = json.dumps(data, indent=4)
print("\nUpdated JSON String:")
print(updated_json)

print("Submitted by: Pranjal Poudel")
