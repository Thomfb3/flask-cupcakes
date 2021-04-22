"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template

from models import db, connect_db, Cupcake

from seed import run_seed

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "keep-this-a-secret"

connect_db(app)


@app.route('/')
def home_page():
    """homepage"""
    cupcakes = Cupcake.query.all()
    return render_template('index.html', cupcakes=cupcakes)


@app.route('/api/cupcakes')
def get_all_cupcakes():
    """Show all cupcakes"""
    cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)



@app.route('/api/cupcakes/<int:id>')
def get_cupcakes(id):
    """Get a cupcake by ID"""
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())


#Edit form
@app.route('/api/cupcakes/<int:id>/edit')
def edit_cupcakes(id):
    """Get a cupcake by ID"""
    cupcake = Cupcake.query.get_or_404(id)

    return render_template("edit_cupcake.html", cupcake=cupcake)



@app.route('/api/cupcakes', methods=["POST"])
def create_cupcakes():
    """Create new cupcake"""
    #Collect Cupcake form data
    new_cupcake = Cupcake(flavor=request.json["flavor"], size=request.json["size"], rating=request.json["rating"], image=request.json["image"])

    #Commit new to DB
    db.session.add(new_cupcake)
    db.session.commit()
    response_json = jsonify(cupcake=new_cupcake.serialize())
    return (response_json, 201)



@app.route('/api/cupcakes/<int:id>', methods=["PATCH"])
def update_cupcakes(id):
    """Update a cupcake"""
    #Set cupcake update data with form data
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)
    #Commit Update to DB
    db.session.commit()

    return jsonify(cupcake=cupcake.serialize())



@app.route('/api/cupcakes/<int:id>', methods=["DELETE"])
def delete_cupcakes(id):
    """Delete a cupcake"""
    cupcake = Cupcake.query.get_or_404(id)
    #Commit delete to DB
    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(messeage="Cupcake Deleted!")

