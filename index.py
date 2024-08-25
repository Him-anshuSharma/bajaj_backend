from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/bfhl', methods=['GET', 'POST'])
def bfhl():
    if request.method == 'GET':
        return jsonify({
            "operation_code": 1
        }), 200

    if request.method == 'POST':
        data = request.json.get('data', [])
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        lowercase_alphabets = [item for item in alphabets if item.islower()]
        highest_lowercase = max(lowercase_alphabets, default='', key=lambda x: x) if lowercase_alphabets else None

        response = {
            "is_success": True,
            "user_id": "Himanshu_Sharma_01032003",  # Replace with your details
            "email": "sharmanshu0103@gmail.com",  # Replace with your college email
            "roll_number": "21BCI0253",  # Replace with your roll number
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else []
        }
        return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
