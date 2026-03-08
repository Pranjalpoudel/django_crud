import json
import xml.etree.ElementTree as ET
import os
import re

def print_header(text):
    print("\n" + "="*60)
    print(f" OUTPUT FOR: {text}")
    print("="*60)

def demo_q1():
    print_header("Question 1 (JSON Parsing)")
    book_json = '{"id": 101, "title": "Python Programming", "author": "Guido", "year": 1991, "genres": ["Tech"]}'
    data = json.loads(book_json)
    print(f"Parsed ID: {data['id']}, Title: {data['title']}")
    data["rating"] = 4.8
    data["genres"].append("Educational")
    print("Modified Data and converted back to JSON:")
    print(json.dumps(data, indent=4))

def demo_q2():
    print_header("Question 2 (XML Parsing)")
    xml_data = '<book id="101"><title>Python</title><genres><genre>Tech</genre></genres></book>'
    root = ET.fromstring(xml_data)
    print(f"Parsed Book ID: {root.attrib['id']}, Title: {root.find('title').text}")
    new_gen = ET.SubElement(root.find('genres'), 'genre')
    new_gen.text = "Education"
    print("Modified XML Output:")
    print(ET.tostring(root, encoding='unicode'))

def demo_validations():
    print_header("API Validation Logic (Q3 - Q9)")
    
    # Q3: Mobile Validation
    def validate_mobile(m):
        return bool(re.match(r'^(98|97|96)\d{8}$', m))
    
    print(f"Q3: Validating '9841234567': {validate_mobile('9841234567')}")
    print(f"Q3: Validating '12345': {validate_mobile('12345')}")

    # Q4: Username Validation
    def validate_username(u):
        return bool(re.match(r'^[a-zA-Z]+\d+$', u))
    
    print(f"Q4: Validating 'user123': {validate_username('user123')}")
    print(f"Q4: Validating '123user': {validate_username('123user')}")

    # Q8: Password Match and Strength
    def validate_pw(p, cp):
        if p != cp: return "Passwords do not match"
        if len(p) < 8: return "Too short"
        if not re.search(r'[A-Z]', p): return "No uppercase"
        return "Valid"

    print(f"Q8: Testing 'pass' vs 'pass': {validate_pw('pass', 'pass')}")
    print(f"Q8: Testing 'Pass123!' vs 'Pass123!': {validate_pw('Pass123!', 'Pass123!')}")

if __name__ == "__main__":
    demo_q1()
    demo_q2()
    demo_validations()
    print("\n" + "="*60)
    print(" ALL DEMOS COMPLETED ")
    print("="*60)
