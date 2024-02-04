from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Each member represented as an object with 'name' and 'content' properties
members_data = [{"name": "member1", "content": "Member 1 content"},
                {"name": "member2", "content": "Member 2 content"},
                {"name": "member3", "content": "Member 3 content"}]

@app.route('/members')
def get_members():
    return jsonify({"members": members_data})

@app.route('/lists')
def get_lists_route():
    return jsonify({"members": members_data})

@app.route('/add-member', methods=['POST'])
def add_member():
    new_member = {"name": "new_member", "content": "New Member content"}
    members_data.append(new_member)
    return jsonify({"members": members_data})

@app.route('/delete-member', methods=['POST'])
def delete_member():
    member_to_delete = {"name": "new_member", "content": "New Member content"}
    if member_to_delete in members_data:
        members_data.remove(member_to_delete)
    return jsonify({"members": members_data})

@app.route('/update-member', methods=['PUT'])
def update_member():
    updated_member_data = request.get_json()

    old_member = updated_member_data.get("old_member", "")
    new_member = updated_member_data.get("new_member", "")

    # Assuming members_data is a list of objects with 'name' property
    for member in members_data:
        if member['name'] == old_member:
            member['content'] = new_member

    return jsonify({"members": members_data})

if __name__ == "__main__":
    app.run(debug=True)
