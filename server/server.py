from flask import Flask, request, jsonify

app = Flask(__name__)

members_data = ["member1", "member2", "member3"]

@app.route('/members')
def get_members():
    return jsonify({"members": members_data})

@app.route('/add-member', methods=['POST'])
def add_member():
    new_member = "new_member"
    members_data.append(new_member)
    return jsonify({"members": members_data})

if __name__ == "__main__":
    app.run(debug=True)
