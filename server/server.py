import os
from flask import Flask, request, jsonify
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv
from flask_cors import CORS

# SENDGRID_API_KEY=SG.9chAMWduRDCMe2aCL9LnWA.
# D3YNJPXOvSXs2f9BMYdD9mt7eRDKIXABcN_YUbGvu_4

load_dotenv()

app = Flask(__name__)
CORS(app)

SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
PORT = int(os.getenv('PORT', 5000))

@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        data = request.json
        name = data.get('Name')
        email = data.get('Email')
        message = data.get('Message')

        msg = Mail(
            from_email='remyshema20@gmail.com',
            to_emails='shemaremy2003@gmail.com',
            subject='New Form Submission',
            html_content=f"""
                <p><strong>Name:</strong> {name}</p>
                <p><strong>Email:</strong> {email}</p>
                <p><strong>Message:</strong> {message}</p>
            """
        )


        sg = SendGridAPIClient(SENDGRID_API_KEY)
        sg.send(msg)

        return jsonify({"message": "Message has been sent successfully."}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"message": "Server error. Please try again later."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
