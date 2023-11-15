import os
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_required, login_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from models import Models, User, db
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from icecream import ic


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=30)])
    full_name = StringField('Full Name', validators=[Length(max=80)])
    nickname = StringField('Nickname', validators=[Length(max=30)])
    phone_number = StringField('Phone Number', validators=[Length(max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    bio = StringField('Bio')
    submit = SubmitField('Register')

class MyApp:
    def __init__(self):
        self.app = Flask(__name__, template_folder='template')
        self.models = Models(self.app)

        # Set secret key from environment variables
        self.app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')

        self.login_manager = LoginManager(self.app)
        self.login_manager.login_view = 'dashboard'

        @self.login_manager.user_loader
        def load_user(user_id):
            return User.query.get(int(user_id))

        @self.app.route('/login', methods=['GET', 'POST'])
        def login():
            if request.method == 'POST':
                email = request.form.get('email')
                password = request.form.get('password')

                user = User.query.filter_by(email=email).first()
                if user and check_password_hash(user.Password, password):
                    login_user(user)    
                    return redirect(url_for('dashboard'))
                else:
                    flash('Invalid email or password', 'error')

            return render_template('public/html/loginCoba.html', error=None)


        @self.app.route('/register', methods=['GET', 'POST'])
        def register():
            form = RegistrationForm()

            if form.validate_on_submit():
                hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha1')

                new_user = User(
                    email=form.email.data,
                    Nama_Lengkap=form.full_name.data,
                    Nama_Penggilan=form.nickname.data,
                    Nomor_Telepon=form.phone_number.data,
                    Password=hashed_password,
                    Bio=form.bio.data
                )
                db.session.add(new_user)
                db.session.commit()

                flash('Your account has been created! You can now log in.', 'success')
                return redirect(url_for('login'))

            return render_template('public/html/registerEx.html', form=form)

        @self.app.route('/Dashboard', methods=["GET", "POST"])
        @login_required
        def dashboard():
            return render_template('public/html/Dashboard.html')

        @self.app.route('/homepage')
        def homepage():
            return render_template('public/html/Homepage.html')

        @self.app.errorhandler(404)
        def page_not_found(error):
            return render_template('public/html/404.html')

    def run(self):
        self.app.run(debug=True)

if __name__ == '__main__':
    my_app = MyApp()
    my_app.run()
