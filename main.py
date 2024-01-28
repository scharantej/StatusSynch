
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///status_benefits.sqlite'
db = SQLAlchemy(app)

class Partner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    status = db.Column(db.String(80), nullable=False)
    benefits = db.Column(db.String(255), nullable=False)

class Mapping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    partner1 = db.Column(db.String(80), nullable=False)
    status1 = db.Column(db.String(80), nullable=False)
    partner2 = db.Column(db.String(80), nullable=False)
    status2 = db.Column(db.String(80), nullable=False)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/status-benefits')
def status_benefits():
    partners = Partner.query.all()
    return render_template('status_benefits.html', partners=partners)

@app.route('/mapping')
def mapping():
    mappings = Mapping.query.all()
    return render_template('mapping.html', mappings=mappings)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        flash('Your message has been sent!')
        return redirect(url_for('contact'))
    return render_template('contact.html')

@app.errorhandler(404)
def error_404(error):
    return render_template('error.html'), 404

@app.errorhandler(500)
def error_500(error):
    return render_template('error.html'), 500

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
