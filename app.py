from users import users_data
from flask import Flask, jsonify, request

app = Flask(__name__)


@app .route('/user/<get_login>')
def getUserByLogin(get_login):
    found = [user for user in users_data if user['login'] == get_login]
    if (len(found) > 0):
        return jsonify({'user': found})
    return jsonify({'errMessage': ' User not found'})


@app .route('/users')
def getUsers():
    return jsonify(users_data)


@app.route('/login', methods=['POST'])
def login():
    data = {
        "login": request.json['login'],
        "password": request.json['password'],
        "token": request.json['token']
    }
    print(data)
    return jsonify({'login': 'ok'})


@app .route('/post-test', methods=['POST'])
def postTest():
    body = request.json
    print(str(body))
    #print(hash("Rafael Badal"))
    return jsonify({'post': 'ok'})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
