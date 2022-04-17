from flask import render_template, request, jsonify


def bad_request(message):
    response = jsonify({'error': 'bad request', 'message': message,'code':400})
    response.status_code = 400
    return response


def unauthorized(message):
    response = jsonify({'error': 'unauthorized', 'message': message,'code':401})
    response.status_code = 401
    return response


def forbidden(message):
    response = jsonify({'error': 'forbidden', 'message': message,'code':403})
    response.status_code = 403
    return response

def servererror(message):
    response = jsonify({'error': 'servererror', 'message': message, 'code':500})
    response.status_code = 500
    return response

