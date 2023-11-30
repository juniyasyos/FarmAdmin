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
        # Initialize Flask application
        self.app = Flask(__name__, template_folder='template')
        self.models = Models(self.app)
        self.operation = None

        # Set secret key from environment variables
        self.app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')

         # Initialize LoginManager for user authentication
        self.login_manager = LoginManager(self.app)
        self.login_manager.login_view = 'dashboard'
        
         # Setup user loader function for LoginManager
        self.setup_user_loader()
        
         # Setup routes for different endpoints
        self.setup_routes()
        
        
    # Define a user loader function for LoginManager
    def setup_user_loader(self):
        self.operation = None
        
        @self.login_manager.user_loader
        def load_user(user_id):
            return User.query.get(int(user_id))

    # Function in Function Functional Programming
    def setup_routes(self):
        # Login route for user authentication
        user = current_user
        @self.app.route('/login', methods=['GET', 'POST'])
        def login():
            # Handle user login
            if request.method == 'POST':
                email, password = request.form.get('email'), request.form.get('password')
                user = User.query.filter_by(email=email).first()
                if user and check_password_hash(user.Password, password):
                    login_user(user)
                    return redirect(url_for('dashboard'))
                else:
                    flash('Invalid email or password', 'error')
            return render_template('public/html/loginCoba.html', error=None)

        # Registration route for creating a new user account
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
                DB.session.add(new_user)
                DB.session.commit()
                flash('Your account has been created! You can now log in.', 'success')
                return redirect(url_for('login'))
            return render_template('public/html/registerEx.html', form=form)


        # Dashboard route to display user's dashboard
        @self.app.route('/Dashboard', methods=["GET", "POST"])
        @login_required
        def dashboard(): 
            self.operation = Operation()

            data = {
                'profil_user' : user,
                'total_lahan': self.operation.get_total_lahan(user, Lahan),
                'total_hasil_panen': self.operation.get_total_hasil_panen(user, Hasil_Panen, Lahan),
                'total_pendapatan': int(self.operation.get_total_pendapatan(user, Pendapatan, Hasil_Panen, Lahan)),
                'total_pengeluaran': int(self.operation.get_total_pengeluaran(user, Pengeluaran, Aktivitas_Lahan, Lahan)),
                'list_lahan' : self.operation.get_list_lahan(user, Lahan),
                'chart_labels' : ["jan", "feb", "mar", "apr","mei","jun","jul","agus","sep","okt","nov","des"],
                'chart_series' : self.operation.Pengeluaran_lahan_perbulan(user, Pengeluaran, Lahan, Aktivitas_Lahan),
                'list_aktifitas' : self.operation.get_all_activity(user, Pengeluaran, Lahan, Aktivitas_Lahan)[0:10],
                'list_pengeluaran' : self.operation.get_all_pengeluaran(user, Lahan, Aktivitas_Lahan, Pengeluaran)[0:10],
                'list_pendapatan' : self.operation.get_all_pendapatan(user, Hasil_Panen, Pendapatan, Lahan)[0:10]
                }
            return render_template('public/html/Dashboard.html', **data)


        # Route to update the status of an activity
        @self.app.route('/update_statusActivity', methods=["POST", "GET"])
        @login_required
        def update_statusActivity():
            data = request.get_json()
            activity_id = data['aktivitas_id']
            new_status = data['new_status']
            
            aktivitas_lahan = Aktivitas_Lahan.query.get(activity_id)
            if request.method == "POST":
                aktivitas_lahan.status = new_status
                DB.session.commit()
                return jsonify({'new_status': aktivitas_lahan.status})
            return jsonify({'error': 'Aktivitas_Lahan tidak ditemukan'}), 404

                        
        # Profile route to display user's profile information
        @self.app.route("/profile")
        @login_required
        def profile():
            data = {
                'profil_user' : user,
                }
            return render_template('public/html/profile.html', **data)


        @self.app.route("/update_profile", methods=["POST"])
        @login_required
        def update_profile():
            if request.method == "POST":
                data = request.get_json()

                try:
                    current_user.email = data['email']
                    current_user.Nama_Lengkap = data['nama_lengkap']
                    current_user.Nama_Penggilan = data['nama_panggilan']
                    current_user.Nomor_Telepon = data['nomor_telepon']
                    current_user.Bio = data['bio']

                    DB.session.commit()

                    return jsonify({'success': 'Update profil berhasil'})
                except Exception as e:
                    print(f"Error: {e}")
                    return jsonify({'error': f'Gagal mengubah profil: {e}'}), 404
        
        

        # Manajemen route for managing user's land
        @self.app.route("/manajemen", methods=["GET", "POST"])
        @login_required
        def manajemen():
            self.operation = Operation()
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
                DB.session.add(new_lahan)
                DB.session.commit()
            
            data = {
                'profil_user': user,
                'lahan_data': self.operation.get_all_lahan(user, Lahan),
                'form':form
                }
            return render_template('public/html/base_manajemen.html', **data)

        
        # Update route to update land information
        @self.app.route("/update_lahan", methods=["POST"])
        @login_required
        def update_lahan():
            data = request.json
            lahan_id = data['id_lahan']
            ic(lahan_id)
            ic(data)
            
            data_lahan = Lahan.query.get(lahan_id)
            ic(data_lahan)
            if data_lahan.user_id == current_user.id:
                data_lahan.nama = data['nama_lahan']
                data_lahan.luas = data['luas_lahan']
                data_lahan.jenis_tanaman = data['jenis_tanaman']
                data_lahan.lokasi = data['lokasi_lahan']
                data_lahan.deskripsi = data['deskripsi_lahan']
                
                DB.session.commit()
                
                return jsonify({'message': 'Data tanah berhasil diperbarui'})
            
            return jsonify({'error': 'Gagal edit data'}), 404

        # Manajemen Lahan route to manage activities on a specific land        
        @self.app.route("/manajemen_lahan/<id_lahan>", methods=["GET", "POST"])
        @login_required
        def manajemen_lahan(id_lahan):
            self.operation = Operation()
            form_aktivitas = Aktivitas_LahanForm()
            form_pengeluaran = PengeluaranForm()
            
            # Debug New Data
            # ic(form_aktivitas.statusForm.data)
            
            # ic(
            #     form_pengeluaran.tanggalForm.data,
            #     form_pengeluaran.jenis_aktivitasForm.data,
            #     form_pengeluaran.total_pengeluaranForm.data,
            #     form_pengeluaran.keteranganForm.data
            #     )
            

            if request.method == "POST":
                new_pengeluaran = Pengeluaran(
                    tanggal=form_pengeluaran.tanggalForm.data,
                    jenis_aktivitas=form_pengeluaran.jenis_aktivitasForm.data,
                    total_pengeluaran=str(int(form_pengeluaran.total_pengeluaranForm.data)/1000_000),
                    keterangan=form_pengeluaran.keteranganForm.data
                )

                DB.session.add(new_pengeluaran)
                DB.session.flush()  # ID pengeluaran dapat digunakan saat membuat aktivitas lahan baru

                new_akctivity = Aktivitas_Lahan(
                    lahan_id=id_lahan,
                    pengeluaran_id=new_pengeluaran.id,
                    status=form_aktivitas.statusForm.data
                )

                DB.session.add(new_akctivity)
                DB.session.commit()

            activity_type_choices = [
                ('pembibitan', 'Pembibitan'),
                ('penanaman', 'Penanaman'),
                ('pemeliharaan', 'Pemeliharaan Tanaman'),
                ('pengendalian', 'Pengendalian Hama dan Penyakit'),
                ('panen', 'Panen'),
                ('pascapanen', 'Pascapanen'),
                ('pengolahan-tanah', 'Pengolahan Tanah'),
                ('pertanian-organik', 'Pertanian Organik'),
                ('peternakan', 'Peternakan'),
                ('perikanan', 'Perikanan'),
                ('agroforestri', 'Agroforestri'),
                ('irigasi', 'Irigasi'),
                ('teknologi-pertanian', 'Penggunaan Teknologi Pertanian'),
                ('pengolahan-hasil', 'Pengolahan Hasil Pertanian'),
                ('pengembangan-varietas', 'Pengembangan Varietas Unggul'),
                ('pasar-pertanian', 'Pasar Pertanian'),
                ('penelitian-pengembangan', 'Penelitian dan Pengembangan'),
                ('pengelolaan-sumber-daya', 'Pengelolaan Sumber Daya Alam'),
                ('pendidikan-pertanian', 'Pendidikan Pertanian'),
                ('pengelolaan-limbah', 'Pengelolaan Limbah Pertanian'),
            ]
            data = {
                'profil_user': user,
                'nama_lahan': Lahan.query.filter_by(id=id_lahan, user_id=current_user.id).first().nama,
                'data_aktivitas': self.operation.aktivitas_perlahan(id_lahan=id_lahan, current_user=current_user),
                'form_activity': form_aktivitas,
                'form_pengeluaran': form_pengeluaran,
                'id_lahan': id_lahan,
                'activity_type_choices': activity_type_choices
            }

            return render_template('public/html/manajemen_activity.html', **data)
        
        
        # Manajemen Lahan route to manage activities on a specific land        
        @self.app.route("/update_activity", methods=["POST"])
        @login_required
        def update_activity():
            # var data = {
            #         'id_pengeluaran': id_pengeluaran,
            #         'id_aktivitas': id_aktivitas,
            #         'tanggal': tanggal,
            #         'jenis_aktivitas': jenis_aktivitas,
            #         'status_aktivitas': status_aktivitas,
            #         'total_pengeluaran': total_pengeluaran,
            #         'keterangan': keterangan
            #     };
            data = request.json
            activity_id = data['id_aktivitas']
            pengeluaran_id = data['id_pengeluaran']
            
            data_pengeluaran = Pengeluaran.query.get(pengeluaran_id)
            data_aktivitas = Aktivitas_Lahan.query.get(activity_id)
            
            if data_pengeluaran and data_aktivitas:
                data_pengeluaran.tanggal = data['tanggal']
                data_pengeluaran.jenis_aktivitas = data['jenis_aktivitas']
                data_pengeluaran.total_pengeluaran = str(int(data['total_pengeluaran'])/1000000)
                data_pengeluaran.keterangan = data['keterangan']
                data_aktivitas.status = data['status_aktivitas']
                
                DB.session.commit()
                return jsonify({'message': 'Data tanah berhasil diperbarui'})
            
            return jsonify({'error': 'Gagal edit data'}), 404
        
        
        # Homepage route
        @self.app.route('/')
        def homepage():
            return render_template('public/html/Homepage.html')
        

        # Error handling for 404 Not Found
        @self.app.errorhandler(404)
        def page_not_found(error):
            return render_template(f'public/html/404.html')

    def run(self):
         # Run the Flask application
        self.app.run(debug=True)

# Instantiate the Controller_Application class
if __name__ == '__main__':
    my_app = Controller_Application()
    my_app.run()
