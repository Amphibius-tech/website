from flask import Blueprint, render_template, request, jsonify, url_for

from src.database.provider.leads_info import LeadsInfoProvider

landing_bp = Blueprint("landing_bp", __name__, static_folder="static", template_folder="templates")


@landing_bp.route('/', methods=['GET'])
def index():
    return render_template('main.html')

@landing_bp.route("/submit-enquiry", methods=["POST"])
def submit_enquiry():

    LeadsInfoProvider().add_leads_entry(request)

    return jsonify({
        "status": "success",
        "message": "Enquiry submitted successfully"
    }), 200
    
@landing_bp.route("/signin", methods=["GET"])
def signin():
    return render_template("signin.html")

@landing_bp.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
        if data:
            email = data.get("email")
            password = data.get("password")
            
            if email == "techamphibius@gmail.com" and password == "password123":   
                return jsonify({
                    "status": "success",
                    "message": "Login successful",
                    "redirect_url": url_for('leads_management_bp.lead')
                }), 200
            else:
                return jsonify({
                    "status": "error",
                    "message": "Invalid email or password"
                }), 401
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
