from flask import Flask, render_template, request
from src.db_provider.db_service import db, EnquiryForm

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config['SECRET_KEY'] = "SecREtKeY"

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        service = request.form['service']
        message = request.form['message']
        
        form = EnquiryForm(
            name=name,
            email=email,
            service=service,
            message=message
        )
        
        db.session.add(form)
        db.session.commit()
        print('enquiry form updated')
        
        render_template('main.html', message="Thanks for the enquiry, we will get back to you soon!")
        
    return render_template('main.html')



if __name__ == "__main__":
    app.run()