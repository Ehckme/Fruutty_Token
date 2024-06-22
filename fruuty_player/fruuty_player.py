from flask import Flask
from flask import flash
from flask import Blueprint
from flask import request, render_template, redirect, url_for


import json

import io
import base64
from PIL import Image

fruuty_player_bp = Blueprint('fruuty_player', __name__,
                            template_folder='templates',
                            static_folder='static',
                            static_url_path='/static/fruuty_player',
                            )

@fruuty_player_bp.route('/fruuty-player', methods=['GET', 'POST'])
def fruuty_player():

    return render_template('fruuty_player.html')