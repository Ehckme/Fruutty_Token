from flask import Flask
from flask import flash
from flask import Blueprint
from flask import request, render_template, redirect, url_for
from fruuty_token.create_token import Token

import json
import json


import io
import base64
from PIL import Image


fruuty_token_bp = Blueprint('fruuty_token', __name__,
                            template_folder='templates',
                            static_folder='static',
                            static_url_path='/static/fruuty_token',
                            )


@fruuty_token_bp.route('/index', methods=['GET', 'POST'])
def index():

    return render_template('index.html')

@fruuty_token_bp.route('/', methods=['GET', 'POST'])
def fruuty():

    return render_template('fruuty.html')

@fruuty_token_bp.route('/generate', methods=['GET', 'POST'])
def generate():
    fruuty_toke_amount = request.form.get('fruuty_token', False)
    if request.method == 'POST':
        token = Token()
        fruuty_token = token.fruuty_token(fruuty_toke_amount)
        print(fruuty_token)

        # What image do we open here
        qr_image = Image.open('esizable_token.png')
        data = io.BytesIO()
        qr_image.save(data, 'PNG')
        encoded_qr_image = base64.b64encode(data.getvalue())

        return render_template('generate.html', token=encoded_qr_image.decode('utf-8'))

    return render_template('generate.html')



@fruuty_token_bp.route('/scanner', methods=['GET', 'POST'])
def scanner():

    if request.method == 'POST':
        data = str(request.form.get('token_results', False))
        global json_response
        try:
            json_response = json.loads(data)
            print('json loads = ', json_response)
            print(json_response['token_id'])
            flash('token', data)
            return render_template('scanner_results.html',
                                   # store_name=json_response['store_name'],
                                   user=json_response['user_id'],
                                   token_id=json_response['token_id'],
                                   token_amount=json_response['token_amount'],
                                   city=json_response['city'],
                                   user_countryr=json_response['user_country'],
                                   trade_country=json_response['trade_country'],
                                   date=json_response['date'],
                                   # Processor=json_response['Processor'],

                                   )
        except json.decoder.JSONDecodeError as e:
            flash('OOPS! There seems to be an error, looks like you tried to create a token without scanning.')
            return render_template('error.html', )

    return render_template('scanner.html',)

@fruuty_token_bp.route('/fruuty-market', methods=['GET', 'POST'] )
def fruuty_market():
    return render_template('fruuty_market.html')

@fruuty_token_bp.route('/scanner-results', methods=['GET', 'POST'])
def scanner_results():
    return render_template('scanner_results.html')


@fruuty_token_bp.route('/new-scann', methods=['GET', 'POST'])
def new_scann():
    return render_template('new_scann.html')