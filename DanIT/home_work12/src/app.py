from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)
CSV_FILE = "students.csv"

# Инициализация CSV файла

def init_csv_file():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "name", "surname", "age"])

def read_users():
    init_csv_file()
    with open(CSV_FILE, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))

def write_users(users):
    init_csv_file()
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["id", "name", "surname", "age"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(users)

def generate_new_id(users):
    return str(max((int(user["id"]) for user in users), default=0) + 1)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(read_users())

@app.route("/users/<id>", methods=["GET"])
def get_user(id):
    user = next((u for u in read_users() if u["id"] == id), None)
    return (jsonify(user), 200) if user else (jsonify({"error": "User not found"}), 404)

@app.route("/users", methods=["POST"])
def create_user():
    users = read_users()
    data = request.json
    
    if not all(k in data for k in ["name", "surname", "age"]):
        return jsonify({"error": "Missing name, surname, or age"}), 400
    
    new_user = {"id": generate_new_id(users), **data}
    users.append(new_user)
    write_users(users)
    return jsonify(new_user), 201

@app.route("/users/<id>", methods=["PUT"])
def update_user(id):
    users = read_users()
    data = request.json
    
    for user in users:
        if user["id"] == id:
            user.update(data)
            write_users(users)
            return jsonify(user)
    
    return jsonify({"error": "User not found"}), 404

@app.route("/users/<id>", methods=["PATCH"])
def patch_user(id):
    users = read_users()
    data = request.json
    
    for user in users:
        if user["id"] == id:
            for key, value in data.items():
                if value is not None:
                    user[key] = value
            write_users(users)
            return jsonify(user)
    
    return jsonify({"error": "User not found"}), 404

@app.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    users = read_users()
    filtered_users = [u for u in users if u["id"] != id]
    
    if len(users) == len(filtered_users):
        return jsonify({"error": "User not found"}), 404
    
    write_users(filtered_users)
    return jsonify({"message": "User deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)
