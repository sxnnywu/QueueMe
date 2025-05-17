from flask import Flask, request, jsonify
from database import init_db, get_db, close_db

app = Flask(__name__)
app.teardown_appcontext(close_db)

@app.route('/queues', methods=['POST'])
def create_queue():
    data = request.json
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO queues (name, description, location, time_per_person) VALUES (?, ?, ?, ?)",
        (data['name'], data.get('description', ''), data.get('location', ''), data.get('timePerPerson', 5))
    )
    db.commit()
    queue_id = cursor.lastrowid
    return jsonify({'id': queue_id}), 201

@app.route('/queues', methods=['GET'])
def list_queues():
    db = get_db()
    queues = db.execute("SELECT * FROM queues").fetchall()
    return jsonify([dict(q) for q in queues])

@app.route('/queues/<int:queue_id>/join', methods=['POST'])
def join_queue(queue_id):
    data = request.json
    db = get_db()
    db.execute(
        "INSERT INTO queue_members (queue_id, name) VALUES (?, ?)",
        (queue_id, data['name'])
    )
    db.commit()
    return jsonify({'message': 'Joined queue'}), 201

@app.route('/queues/<int:queue_id>/members', methods=['GET'])
def get_members(queue_id):
    db = get_db()
    members = db.execute(
        "SELECT name FROM queue_members WHERE queue_id = ?", (queue_id,)
    ).fetchall()
    return jsonify([m['name'] for m in members])

if __name__ == '__main__':
    init_db()
    app.run(debug=True)