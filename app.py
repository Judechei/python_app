from flask import Flask, jsonify

app = Flask(__name__)s
@app.route('/')
def home():
    return jsonify({"message": "Welcome to api!"}), 200

@app.route('/about')
def about():
    return jsonify({"author": "Jjude!"}), 200

if __name__ == '__main__':
    app.run()