import qrcode
import json
import datetime



class Token:
        def __init__(self):
                return

        def fruuty_token(self, amount,):
                self.amount = amount
                fruuty_qr_token = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=100,
                    border=1,
                )
                self.data = {'token_id': '8493405',
                             'user_id': '987033',
                             'store_name': 'jimusi',
                             'city': 'New York',
                             'user_country': 'South Africa',
                             'trade_country': 'USA',
                             'token_amount': f'{self.amount}',
                             'date': f'{datetime.datetime.today()}',
                             'processor': 'fruuty',
                             }

                self.jsonify_data = json.dumps(self.data)
                fruuty_qr_token.add_data(self.jsonify_data)
                fruuty_qr_token.make(fit=True)
                fruuty_token_image = fruuty_qr_token.make_image(fill_color='black', back_color='white')
                # token_image = qrcode.make(f'{self.jsonify_data}')
                # image = token_image.save('new_fruuty_token.jpeg')

                return fruuty_token_image.save('fruutty_token.png')

        def fruuty_product_token(self):
            return

token = Token()
amount = token.fruuty_token(7777777)





# fruuty_token = [0.5, 1, 2, 2.5, 5, 10, 15, 20, 25, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 1000, 1500, 5000]
