import os
from flask import Flask, render_template, redirect, url_for, request, flash, jsonify
from flask_login import LoginManager, login_required, login_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from models import *
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from sqlalchemy import func, cast, Integer
from icecream import ic

class Controller_Application:
    def __init__(self):
        self.app = Flask(__name__, template_folder='template')
        self.models = Models(self.app)

        # Set secret key from environment variables
        self.app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')

        self.login_manager = LoginManager(self.app)
        self.login_manager.login_view = 'dashboard'
        self.setup_user_loader()
        self.setup_routes()
        

    def setup_user_loader(self):
        @self.login_manager.user_loader
        def load_user(user_id):
            return User.query.get(int(user_id))

    def setup_routes(self):
        user = current_user
        @self.app.route('/login', methods=['GET', 'POST'])
        def login():
            if request.method == 'POST':
                email, password = request.form.get('email'), request.form.get('password')
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
            customColors = ["#98a6ad", "#41b3f9", "#f4c63d", "#d17905", "#453d3f", "#453d3f"];
            list_lahan = list(map(lambda x,y: [x,y], user.get_list_lahan(), customColors))
            
            data = {
                'profil_user' : user,
                'total_lahan': user.get_total_lahan(),
                'total_hasil_panen': user.get_total_hasil_panen(),
                'total_pendapatan': int(user.get_total_pendapatan()),
                'total_pengeluaran': int(user.get_total_pengeluaran()),
                'list_lahan' : list_lahan,
                'chart_labels' : ["jan", "feb", "mar", "apr","mei","jun","jul","agus","sep","okt","nov","des"],
                'chart_series' : Lahan.Pengeluaran_lahan_perbulan(current_user=user),
                'list_aktifitas' : Aktivitas_Lahan.get_all(current_user=user)[0:10],
                'list_pengeluaran' : Pengeluaran.get_all(current_user=user)[0:10],
                'list_pendapatan' : Pendapatan.get_all(current_user=user)[0:10]
                }
            return render_template('public/html/Dashboard.html', **data)

        
        @self.app.route('/update_statusActivity', methods=["POST", "GET"])
        @login_required
        def update_statusActivity():
            data = request.get_json()
            activity_id = data['aktivitas_id']
            new_status = data['new_status']
            
            aktivitas_lahan = Aktivitas_Lahan.query.get(activity_id)
            if aktivitas_lahan:
                aktivitas_lahan.status = new_status
                db.session.commit()
                return jsonify({'new_status': aktivitas_lahan.status})
            return jsonify({'error': 'Aktivitas_Lahan tidak ditemukan'}), 404
                        

        @self.app.route("/profile")
        @login_required
        def profile():
            data = {
                'profil_user' : user,
                }
            return render_template('public/html/profile.html', **data)


        @self.app.route("/manajemen", methods=["GET", "POST"])
        @login_required
        def manajemen():
            form = LahanForm()
            new_lahan = Lahan(
                nama=form.nama_lahan.data,
                lokasi=form.lokasi_lahan.data,
                deskripsi=form.deskripsi_lahan.data,
                luas=form.luas_lahan.data,
                jenis_tanaman=form.jenis_tanaman.data,
                user_id=current_user.id
            );
            if new_lahan.nama != None:
                db.session.add(new_lahan)
                db.session.commit()
            
            data = {
                'profil_user': user,
                'lahan_data': Lahan.get_all(current_user=user),
                'form':form
                }
            return render_template('public/html/manajemen.html', **data)

        
        @self.app.route("/update_lahan", methods=["POST"])
        @login_required
        def update_lahan():
            data = request.json
            lahan_id = data['id_lahan']
            
            data_lahan = Lahan.query.get(lahan_id)
            
            if data_lahan and data_lahan.user_id == current_user.id:
                data_lahan.nama = data['nama_lahan']
                data_lahan.luas = data['luas_lahan']
                data_lahan.jenis_tanaman = data['jenis_tanaman']
                data_lahan.lokasi = data['lokasi_lahan']
                data_lahan.deskripsi = data['deskripsi_lahan']
                
                db.session.commit()
                
                return jsonify({'message': 'Data tanah berhasil diperbarui'})
            
            return jsonify({'error': 'Gagal edit data'}), 404
        
        
        @self.app.route('/')
        def homepage():
            return render_template('public/html/Homepage.html')

        import random
        @self.app.errorhandler(404)
        def page_not_found(error):
            return render_template(f'public/html/404.html')

    def run(self):
        self.app.run(debug=True)

if __name__ == '__main__':
    my_app = Controller_Application()
    my_app.run()
