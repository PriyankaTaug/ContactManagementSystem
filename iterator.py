from flask  import Flask,jsonify, request


app = Flask(__name__)

contacts = []


def contact_add(name,phone,email):
    contact = {
        "name":name,
        "phone":phone,
        "email":email,
    }
    contacts.append(contact)
    return f"Successfully added"


@app.route('/add_contact',methods = ['POST'])
def add_contact():
    # Get json data from request
    data = request.get_json()
    #validate data
    if not data:
        return jsonify({"error":"the data is empty"})
    
    name = data['name']
    phone= data['phone']
    email = data['email']
    
    message = contact_add(name,phone,email)
    return jsonify({"message": message, "contacts": contacts}), 201


def view_contacts(contacts):
    if not contacts:
        print("No contact available")
        return 
    for idx,contact in enumerate(contacts):
        print(f"{idx+1}.Name:{contact['name']},Phone number : {contact['phone']},Email:{contact['email']}")

if __name__ == '__main__':
    app.run(debug=True)