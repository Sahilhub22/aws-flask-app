from flask import Flask, request
import pymysql

app = Flask(__name__)

db = pymysql.connect(
    host="flask-db.cbummsam8br0.us-east-2.rds.amazonaws.com",
    user="admin",
    password="Sahilpoiu",
    database="mydb"
)

@app.route('/')
def home():
    return '''
    <form action="/save" method="post">
        <input name="username">
        <button type="submit">Save</button>
    </form>
    '''

@app.route('/save', methods=['POST'])
def save():
    username = request.form['username']

    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO users(name) VALUES(%s)",
        (username,)
    )

    db.commit()

    return "Saved Successfully"

app.run(host='0.0.0.0', port=5000)
