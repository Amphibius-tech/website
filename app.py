from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('main.html')

# @app.route('/form', methods=['POST'])
# def form():
#     name = request.form.get('name')
#     email = request.form.get('email')
#     service = request.form.get('service')
#     message = request.form.get('message')

#     if not all([name, email, service, message]):
#         flash("Please fill in all required fields.", "warning")
#         return redirect(url_for('index'))

#     try:
#         new_form = EnquiryForm(
#             name=name,
#             email=email,
#             service=service,
#             message=message
#         )
#         db.session.add(new_form)
#         db.session.commit()
#         flash("✅ Your enquiry has been submitted successfully!", "success")
#     except Exception as e:
#         db.session.rollback()
#         flash("❌ Something went wrong. Please try again later.", "danger")
#         print("Error:", e)
    
#     return redirect(url_for('index'))


if __name__ == "__main__":
    app.run()