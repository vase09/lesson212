from flask import request
from app import models, db

from flask import current_app as app, jsonify, abort


@app.route('/users', methods=['GET'])
def get_users():
    """ Возвращает список пользователей """
    users = db.session.query(models.User).all()

    return jsonify([user.serialize() for user in users])


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """ Возвращает список пользователей по ID """
    user = db.session.query(models.User).filter(models.User.id == user_id).first()

    if user is None:
        abort(404)

    return jsonify(user.serialize())


@app.route('/orders', methods=['GET'])
def get_orders():
    """ Возвращает список заказов """
    orders = db.session.query(models.Order).all()

    return jsonify([order.serialize() for order in orders])


@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """ Возвращает список заказов по ID"""
    order = db.session.query(models.Order).filter(models.Order.id == order_id).first()

    if order is None:
        abort(404)

    return jsonify(order.serialize())


@app.route('/offers', methods=['GET'])
def get_offers():
    """ Возвращает список предложений """
    offers = db.session.query(models.Offer).all()

    return jsonify([offer.serialize() for offer in offers])


@app.route('/offers/<int:order_id>', methods=['GET'])
def get_offer(order_id):
    """ Возвращает предложения по ID """
    offer = db.session.query(models.Offer).filter(models.Offer.id == order_id).first()

    if offer is None:
        abort(404)

    return jsonify(offer.serialize())


@app.route('/users', methods=['POST'])
def create_user():
    data = request.json

    db.session.add(models.User(**data))

    db.session.commit()

    return {}

@app.route('/users/<int:user_id>', methods=['PUT'])
def edit_user(user_id):
    data = request.json

    user = db.session.query(models.User).filter(models.User == user_id).first()
    if user is None:
        abort(404)

    db.session.query(models.User).filter(models.User.id == user_id).update(**data)
    db.session.commit()

    return {}


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):

    result = db.session.query(models.User).filter(models.User.id == user_id).delete()

    if result == 0:
        abort(404)

    db.session.commit()

    return {}