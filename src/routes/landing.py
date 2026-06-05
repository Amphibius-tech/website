from flask import Blueprint, render_template, request, jsonify, url_for

from src.database.provider.leads_info import LeadsInfoProvider
from src.util.log_adapter import logger

landing_bp = Blueprint("landing_bp", __name__, static_folder="static", template_folder="templates")


@landing_bp.route('/', methods=['GET'])
def index():
    try:
        return render_template('main.html')
    except Exception as e:
        logger.error(f"Error rending the main page: {str(e)}")

@landing_bp.route("/submit-enquiry", methods=["POST"])
def submit_enquiry():
    try:
        LeadsInfoProvider().add_web_leads_entry(request)

        return jsonify({
            "status": "success",
            "message": "Enquiry submitted successfully"
        }), 200
    except Exception as e:
        logger.error(f"Error submit_enquiry the main page: {str(e)}")
    
@landing_bp.route("/signin", methods=["GET"])
def signin():
    try:
        return render_template("signin.html")
    except Exception as e:
        logger.error(f"Error signin the main page: {str(e)}")

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
        logger.error(f"Error login the main page: {str(e)}")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
