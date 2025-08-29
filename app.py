from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def bfhl():
    try:
        print("Request received!")
        data = request.get_json()
        print("Request data:", data)

        if not data or "data" not in data:
            return jsonify({
                "is_success": False,
                "message": "Invalid JSON or missing 'data' key"
            }), 400

        data_array = data.get("data", [])

        full_name = "john_doe"
        dob = "17091999"
        email = "john@xyz.com"
        roll_number = "ABCD123"
        user_id = f"{full_name}_{dob}"

        even_numbers = []
        odd_numbers = []
        alphabets = []
        special_characters = []
        sum_of_numbers = 0
        alpha_concat = ""

        for item in data_array:
            if isinstance(item, str) and item.isdigit():
                num = int(item)
                sum_of_numbers += num
                if num % 2 == 0:
                    even_numbers.append(item)
                else:
                    odd_numbers.append(item)
            elif isinstance(item, str) and item.isalpha():
                alphabets.append(item.upper())
                alpha_concat += item
            else:
                special_characters.append(item)

        reversed_alpha = alpha_concat[::-1]
        concat_string = ""
        for i, ch in enumerate(reversed_alpha):
            concat_string += ch.upper() if i % 2 == 0 else ch.lower()

        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(sum_of_numbers),
            "concat_string": concat_string
        }

        print("Response:", response)
        return jsonify(response), 200

    except Exception as e:
        print("Exception occurred:", e)
        return jsonify({
            "is_success": False,
            "message": str(e)
        }), 400

@app.route('/', methods=['GET'])
def home():
    return "Server is running! Use POST /bfhl endpoint.", 200

if __name__ == '__main__':
    app.run(debug=True)
