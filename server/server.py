from flask import Flask, request, jsonify

app = Flask(__name__)

members_data = ["member1", "member2", "member3"]

@app.route('/members')
def get_members():
    return jsonify({"members": members_data})

@app.route('/add-member', methods=['POST'])
def add_member():
    new_member = "new_member"  # Replace this with the logic to get the new member data
    members_data.append(new_member)
    return jsonify({"members": members_data})

@app.route('/delete-member', methods=['POST'])
def delete_member():
    member_to_delete = "new_member"  # Replace this with the logic to get the member to delete
    if member_to_delete in members_data:
        members_data.remove(member_to_delete)
    return jsonify({"members": members_data})

@app.route('/update-member', methods=['PUT'])
def update_member():
    # Replace this with the logic to get the updated member data from the request
    updated_member_data = request.get_json()

    old_member = updated_member_data.get("old_member", "")
    new_member = updated_member_data.get("new_member", "")

    if old_member and old_member in members_data:
        index = members_data.index(old_member)
        members_data[index] = new_member

    return jsonify({"members": members_data})

if __name__ == "__main__":
    app.run(debug=True)
