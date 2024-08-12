from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


@app.route('/')
def index():
    return "Players Data"


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"


def player_to_dict(player):
    return {
        'name': player.name,
        'description': player.description,
        'id': player.id
    }


@app.route('/players')
def get_players():
    players_data = Player.query.all()

    output = [player_to_dict(player) for player in players_data]

    return jsonify({"Players": output})


@app.route('/players/<id>')
def get_player(id):
    player = Player.query.get_or_404(id)
    return {"name": player.name, "description": player.description}


@app.route('/players', methods=['POST'])
def add_player():
    player = Player(name=request.json['name'], description=request.json['description'])
    db.session.add(player)
    db.session.commit()
    return {'id': player.id}


@app.route('/players/<id>', methods=['DELETE'])
def delete_player(id):
    player = Player.query.get(id)
    if player is None:
        return jsonify({'error': 'Player not found'}), 404
    db.session.delete(player)
    db.session.commit()
    return jsonify({'message': 'Player deleted successfully'}), 200


@app.route('/players/<int:player_id>', methods=['PUT'])
def update_player(player_id):
    player = Player.query.get(player_id)
    if player:
        data = request.get_json()
        player.name = data.get('name', player.name)
        player.description = data.get('description', player.description)
        db.session.commit()
        return jsonify({'message': 'Player updated successfully'}), 200
    else:
        return jsonify({'error': 'Player not found'}), 404
