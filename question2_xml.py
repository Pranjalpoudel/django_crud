# Submitted by: Pranjal Poudel
import xml.etree.ElementTree as ET

"""
Question 2:
How do you parse XML data in Python using xml.etree.ElementTree? Write a Python program
to parse an XML string containing book information with nested elements, access attributes and
element text, extract array-like elements (genres), modify the XML (add new elements), and
convert back to XML string.
"""

# XML parsing: use ET.fromstring() for strings or ET.parse() for files.

# 1. Parse XML string
xml_data = """
<book id="101">
    <title>Learning Python</title>
    <author>John Doe</author>
    <year>2023</year>
    <genres>
        <genre>Technology</genre>
        <genre>Education</genre>
    </genres>
</book>
"""

root = ET.fromstring(xml_data)

# 2. Access attributes and element text
print("Book ID (Attribute):", root.attrib["id"])
print("Title:", root.find("title").text)
print("Author:", root.find("author").text)
print("Year:", root.find("year").text)

# 3. Extract array-like elements (genres)
genres_list = [genre.text for genre in root.find("genres").findall("genre")]
print("Genres:", ", ".join(genres_list))

# 4. Modify XML: Add new elements
rating_element = ET.SubElement(root, "rating")
rating_element.text = "4.5"

# Add a new genre
genres_node = root.find("genres")
new_genre = ET.SubElement(genres_node, "genre")
new_genre.text = "Coding"

# 5. Convert back to XML string
updated_xml = ET.tostring(root, encoding="unicode")
print("\nUpdated XML String:")
print(updated_xml)

print("Submitted by: Pranjal Poudel")
