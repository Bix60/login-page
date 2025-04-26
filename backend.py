from flask import Flask, request, jsonify

app = Flask(__name__)

USER_DB = {
    "user@example.com": "password123"
}

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if email in USER_DB and USER_DB[email] == password:
        return jsonify({"message": "Login successful!"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(debug=True)
