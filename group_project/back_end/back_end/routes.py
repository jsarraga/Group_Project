from flask import Flask, jsonify, request
from flask_cors import CORS
from users import User
from providers import Provider
from user_files import User_files
import util

app = Flask(__name__)
CORS(app)

@app.route("/api/user/create", methods=['POST'])
def create_user_account():
    api_key = util.random_api_key()
    data = request.get_json()
    user = User()
    user.username = data['username']
    password = data['password']
    hashed_pass = util.hash_password(password)
    user.password_hash = hashed_pass
    user.first_name = data['first_name']
    user.last_name = data['last_name']
    user.email = data['email']
    user.api_key = api_key
    user.save()
    return jsonify({"api_key": account.api_key})

@app.route("/api/provider/create", methods=['POST'])
def create_provider_account():
    api_key = util.random_api_key()
    data = request.get_json()
    provider = Provider()
    provider.username = data['username']
    password = data['password']
    hashed_pass = util.hash_password(password)
    provider.password_hash = hashed_pass
    provider.api_key = api_key
    provider.hospital = data['hospital']
    provider.department = data['department']
    provider.doctor_name = data['doctor_name']
    provider.email = data['email']
    provider.save()
    return jsonify({"api_key": account.api_key})

@app.route('/user/login', methods=['POST'])
def user_login():
    data = request.get_json()
    user = User.login(username=data['username'], password=data['password'])
    return jsonify({"api_key": user.api_key})

@app.route('/provider/login', methods=['POST'])
def provider_login():
    data = request.get_json()
    provider = Provider.login(username=data['username'], password=data['password'])
    return jsonify({"api_key": provider.api_key})

# might need to adjust to reflect file titles. Then render info when they click on a file to open it
@app.route("/<api_key>/userfiles", methods=['GET'])
def get_files(api_key):
    user = User.api_authenticate(api_key)
    files = user.get_files()
    file_list = []
    for file in files:
        data = {}
        data["Blood Type"] = file.blood_type
        data["Allergies"] = file.allergies
        data["Medications"] = file.medications
        file_list.append(data)
    return jsonify(file_list)

@app.route("/<api_key>/add_file", methods=['POST'])
def add_file(api_key):
    user = User.api_authenticate(api_key)
    data = request.get_json()
    user.add_file(blood_type=data["blood_type"], allergies=data["allergies"],
                medications=data['medications'], user_pk=user.pk)

# fix. how to get user_file_pk
@app.route("/<api_key>/user_file/remove_file", methods=['POST'])
def remove_file(api_key):
    user = User.api_authenticate(api_key)
    user_file = user.get_one_user_file()


if __name__ == "__main__":
    app.run(debug=True)