from flask import Flask, render_template, request, jsonify

from src.database.provider.leads_info import LeadsInfoProvider

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('main.html')

@app.route("/submit-enquiry", methods=["POST"])
def submit_enquiry():

    LeadsInfoProvider().add_leads_entry(request)

    return jsonify({
        "status": "success",
        "message": "Enquiry submitted successfully"
    }), 200


if __name__ == "__main__":
    app.run()