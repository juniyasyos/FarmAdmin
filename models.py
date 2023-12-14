from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import aliased
from sqlalchemy import func, desc
from dotenv import load_dotenv
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from operator import itemgetter
from functools import reduce
from datetime import datetime
# from icecream import ic
from collections import defaultdict
import os


load_dotenv()

# Asumsikan DB sebagai Immutable
DB = SQLAlchemy()

# Deklarasi class Models
class Models:
    # Fungsi inisialisasi class
    def __init__(self, app=None, db_config=None):
        # Memanggil fungsi init_app jika app telah diberikan
        if app:
            self.init_app(app, db_config)

    # Fungsi inisialisasi app dan database
    def init_app(self, app, db_config=None):
        # Menggunakan db_config default jika tidak diberikan
        if db_config is None:
            db_config = self.load_db_config()

        # Konfigurasi URI database dan track modifications
        app.config['SQLALCHEMY_DATABASE_URI'] = self.get_database_uri(db_config)
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        DB.init_app(app)

    # Fungsi untuk memuat konfigurasi database
    def load_db_config(self):
        return {
            'DB_HOST': os.getenv('DB_HOST'),
            'DB_PORT': os.getenv('DB_PORT'),
            'DB_USER': os.getenv('DB_USER'),
            'DB_PASSWORD': os.getenv('DB_PASSWORD'),
            'DB_NAME': os.getenv('DB_NAME'),
        }

    # Fungsi untuk mendapatkan URI database
    def get_database_uri(self, db_config):
        return (
            f"mysql+mysqlconnector://{db_config['DB_USER']}:{db_config['DB_PASSWORD']}@"
            f"{db_config['DB_HOST']}:{db_config['DB_PORT']}/{db_config['DB_NAME']}"
        )

# Form create new user
class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=30)])
    full_name = StringField('Full Name', validators=[Length(max=80)])
    nickname = StringField('Nickname', validators=[Length(max=30)])
    phone_number = StringField('Phone Number', validators=[Length(max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    bio = StringField('Bio')
    submit = SubmitField('Register')

# Form Create new Lahan
class LahanForm(FlaskForm):
    nama_lahan = StringField('Nama Lahan', validators=[DataRequired()])
    lokasi_lahan = StringField('Lokasi Lahan', validators=[DataRequired()])
    deskripsi_lahan = StringField('Deskripsi Lahan', validators=[DataRequired()])
    luas_lahan = StringField('Luas Lahan', validators=[DataRequired()])
    jenis_tanaman = StringField('Jenis Tanaman', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
class Aktivitas_LahanForm(FlaskForm):    
    # Buat pilihan status aktivitas
    # FP immutable
    status_activity_choices = (
        ('Belum Selesai', 'Belum Selesai'),
        ('Progres', 'Progres'),
        ('Selesai', 'Selesai'),
    )

    # Buat field Select untuk status aktivitas dan StringField untuk id_panen
    statusForm = SelectField('Status Aktivitas', choices=status_activity_choices, validators=[DataRequired()])
    
# Form Create new pengeluaran
class PengeluaranForm(FlaskForm):
    # Immutable Data 
    activity_type_choices = (
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
    )
    

    tanggalForm = DateField('Tanggal', validators=[DataRequired()])
    jenis_aktivitasForm = SelectField('Jenis Aktivitas', choices=activity_type_choices)
    total_pengeluaranForm = StringField('Total Pengeluaran', validators=[DataRequired()])
    keteranganForm = StringField('Keterangan', validators=[DataRequired()])
    submit = SubmitField('Submit')


# Deklarasi entity User
class User(DB.Model, UserMixin):
    # Nama tabel dalam database
    __tablename__ = 'User'
    
    # Definisi kolom-kolom dalam tabel User
    id = DB.Column(DB.Integer, primary_key=True)
    email = DB.Column(DB.String(30), unique=True, nullable=False)
    Nama_Lengkap = DB.Column(DB.String(80))
    Nama_Penggilan = DB.Column(DB.String(30))
    Nomor_Telepon = DB.Column(DB.String(20))
    Password = DB.Column(DB.String(255), nullable=False)
    Bio = DB.Column(DB.TEXT)             
    
# Deklarasi entity Lahan
class Lahan(DB.Model, UserMixin):
    # Nama tabel dalam database
    __tablename__ = 'Lahan'

    # Definisi kolom-kolom dalam tabel Lahan
    id = DB.Column(DB.Integer, primary_key=True)
    nama = DB.Column(DB.String(255))
    lokasi = DB.Column(DB.String(255))
    deskripsi = DB.Column(DB.TEXT)
    luas = DB.Column(DB.Integer)
    jenis_tanaman = DB.Column(DB.String(255))
    user_id = DB.Column(DB.Integer, DB.ForeignKey('User.id'))
    user = DB.relationship('User', backref=DB.backref('lahans', lazy=True))
    
# Deklarasi Entity Pendapatan
class Pendapatan(DB.Model, UserMixin):
    __tablename__ = 'Pendapatan'
    id = DB.Column(DB.Integer, primary_key=True)
    tanggal = DB.Column(DB.Date)
    nama_barang = DB.Column(DB.String(255))
    harga_barang = DB.Column(DB.DECIMAL(10, 2))
    jumlah = DB.Column(DB.Integer)
    keterangan = DB.Column(DB.TEXT)
    hasil_panen_id = DB.Column(DB.Integer, DB.ForeignKey('Hasil_Panen.id'))
    
# Deklarasi Entity Hasil Panen
class Hasil_Panen(DB.Model, UserMixin):
    __tablename__ = 'Hasil_Panen'
    id = DB.Column(DB.Integer, primary_key=True)
    lahan_id = DB.Column(DB.Integer, DB.ForeignKey('Lahan.id'))
    jenis_tanaman = DB.Column(DB.String(255))
    jumlah_hasil_panen = DB.Column(DB.Integer)
    waktu_mulai = DB.Column(DB.DateTime)
    waktu_panen = DB.Column(DB.DateTime)
    judul_panen = DB.Column(DB.String(255))

# Deklarasi Entity Pengeluaran
class Pengeluaran(DB.Model, UserMixin):
    # Nama tabel dalam database
    __tablename__ = 'Pengeluaran'

    # Definisi kolom-kolom dalam tabel Pengeluaran
    id = DB.Column(DB.Integer, primary_key=True)
    tanggal = DB.Column(DB.Date, nullable=False)
    jenis_aktivitas = DB.Column(DB.String(255))
    total_pengeluaran = DB.Column(DB.DECIMAL(10, 2))
    keterangan = DB.Column(DB.TEXT)

# Deklarasi Entity Aktivitas Lahan
class Aktivitas_Lahan(DB.Model, UserMixin):
    # Nama tabel dalam database
    __tablename__ = 'Aktivitas_Lahan'

    # Definisi kolom-kolom dalam tabel Aktivitas_Lahan
    id = DB.Column(DB.Integer, primary_key=True)
    lahan_id = DB.Column(DB.Integer, DB.ForeignKey('Lahan.id'))
    pengeluaran_id = DB.Column(DB.Integer, DB.ForeignKey('Pengeluaran.id'))
    status = DB.Column(DB.String(255))
    id_panen = DB.Column(DB.Integer, DB.ForeignKey('Hasil_Panen.id'))
    
    
# Class Functional Programming Operation 
class Operation:
    def __init__(self) -> None:
        pass
    
    # (Pure Function and First-Class dan Higher-Order Functions) filtered lahan by id
    def _filter_lahan(self, user, lahan_data):
        return lahan_data.query.filter_by(user_id=user.id)

    # (Pure Function and First-Class dan Higher-Order Functions) count all lahan
    def get_total_lahan(self, user, lahan_data):
        return self._filter_lahan(user, lahan_data).count()

    # (Pure Function and First-Class dan Higher-Order Functions) count panen
    def get_total_hasil_panen(self, user, data_hasil_panen, data_lahan):
        return data_hasil_panen.query.join(data_lahan).filter(data_lahan.user_id == user.id).count()

    # (Pure Function and First-Class dan Higher-Order Functions) count pendapatan
    def get_total_pendapatan(self, user, data_pendapatan, data_hasil_panen, data_lahan, ):
        return DB.session.query(func.sum(data_pendapatan.harga_barang * data_pendapatan.jumlah)).join(data_hasil_panen).join(data_lahan).filter(data_hasil_panen.lahan_id == data_lahan.id).filter(data_lahan.user_id == user.id).scalar() or 0

    # (Pure Function and First-Class dan Higher-Order Functions) count pengeluaran
    def get_total_pengeluaran(self, user, data_pengeluaran, data_aktivitas_lahan, data_lahan):
        return DB.session.query(func.sum(data_pengeluaran.total_pengeluaran)).join(data_aktivitas_lahan, data_aktivitas_lahan.pengeluaran_id == data_pengeluaran.id).join(data_lahan).filter(data_lahan.user_id == user.id).scalar() or 0

    # (Pure Function and First-Class dan Higher-Order Functions) get list lahan user
    def get_list_lahan(self, user, data_lahan):
        customColors = ["#98a6ad", "#41b3f9", "#f4c63d", "#d17905", "#453d3f", "#453d3f"]
        data_lahan = [str(lahan.nama) for lahan in self._filter_lahan(user, data_lahan).all()]
        return list(map(lambda x,y: [x,y], data_lahan, customColors))
    
    # (Pure function and First-Class dan Higher-Order Functions) get lahan user
    def get_all_lahan(self, user, lahan_data):
        return list(filter(lambda lahan: lahan.user_id == user.id, lahan_data.query.all()))

    # (First-Class dan Higher-Order Functions) Get Pengeluaran per Bulan 
    def Pengeluaran_lahan_perbulan(self, user, data_pengeluaran, data_lahan, data_aktivitas_lahan):
        # Query ke database untuk mendapatkan data pengeluaran per bulan per lahan
        result = (
            DB.session.query(
                data_lahan.id.label('lahan_id'),  # Menggunakan label untuk memberi nama pada hasil query
                func.month(data_pengeluaran.tanggal).label('bulan'),  # Mengambil bulan dari tanggal pengeluaran
                func.sum(data_pengeluaran.total_pengeluaran).label('total_pengeluaran')  # Mengambil total pengeluaran
            )
            .select_from(data_lahan)
            .join(data_aktivitas_lahan, data_lahan.id == data_aktivitas_lahan.lahan_id)
            .join(data_pengeluaran, data_aktivitas_lahan.pengeluaran_id == data_pengeluaran.id)
            .filter(data_lahan.user_id == user.id)
            .group_by(data_lahan.id, func.month(data_pengeluaran.tanggal))  # Mengelompokkan hasil query berdasarkan bulan dan lahan
            .all()
        )

        data_per_lahan = {}

        # Mengorganisir hasil query ke dalam struktur data yang diinginkan
        for row in result:
            lahan_id = row.lahan_id
            bulan = row.bulan
            total_pengeluaran = row.total_pengeluaran

            if lahan_id not in data_per_lahan:
                data_per_lahan[lahan_id] = {}

            data_per_lahan[lahan_id][bulan] = total_pengeluaran

        # Mengubah struktur data menjadi list untuk setiap lahan dan bulan
        return list(map(lambda lahan_id: list(map(lambda bulan: data_per_lahan[lahan_id].get(bulan, 0), range(1, 13))), data_per_lahan.keys()))

    # Fungsi untuk mendapatkan semua data yang dimiliki lahan
    def get_data_lahan(self, lahan_id, data_lahan, data_aktivitas_lahan, data_pengeluaran):
        return (
            DB.session.query()
            .select_from(data_lahan, data_lahan.id == lahan_id)
            .join(data_aktivitas_lahan, data_aktivitas_lahan.pengeluaran_id == data_pengeluaran.id)
            .filter(data_lahan.user_id == user.id)
            .all()
        )

    # (First-Class dan Higher-Order Functions) Get all pendapatan
    def get_all_pendapatan(self, user, data_hasil_panen, data_pendapatan, data_lahan):
        return (
            DB.session.query(data_hasil_panen, data_pendapatan)
            .join(data_hasil_panen, data_hasil_panen.id == data_pendapatan.hasil_panen_id)
            .join(data_lahan, data_lahan.user_id == user.id)
            .order_by(desc(data_pendapatan.tanggal))
            .all()
        )
    
    # (First-Class dan Higher-Order Functions) Get all pengeluaran
    def get_all_pengeluaran(self, user, data_lahan, data_aktivitas_lahan, data_pengeluaran):
        query_result = (
            DB.session.query(data_lahan, data_aktivitas_lahan, data_pengeluaran)
            .join(data_aktivitas_lahan, data_aktivitas_lahan.lahan_id == data_lahan.id)
            .join(Pengeluaran, data_aktivitas_lahan.pengeluaran_id == Pengeluaran.id)
            .filter(data_lahan.user_id == user.id)
            .all()
        )

        # Mengurutkan hasil query berdasarkan tanggal dengan urutan descending
        sorted_result = sorted(filter(lambda item: item[0].user_id == user.id, query_result), key=lambda item: item[2].tanggal, reverse=True)

        return list(sorted_result)
    
    # (First-Class dan Higher-Order Functions) Get all activity
    def get_all_activity(self, user, data_pengeluaran, data_lahan, data_aktivitas_lahan):
        return list(map(
            lambda x: DB.session.query(data_pengeluaran, data_lahan, Aktivitas_Lahan)
            .join(Aktivitas_Lahan, data_lahan.id == data_aktivitas_lahan.lahan_id)
            .join(data_pengeluaran, data_aktivitas_lahan.pengeluaran_id == data_pengeluaran.id)
            .filter(data_lahan.user_id == user.id)
            .order_by(desc(data_pengeluaran.tanggal))
            .all(), [None]))[0]


    # (First-Class dan Higher-Order Functions) Get all activity per lahan
    def aktivitas_perlahan(self, id_lahan, current_user):
        query_result = (
            DB.session.query(Lahan, Aktivitas_Lahan, Pengeluaran)
            .join(Aktivitas_Lahan, Aktivitas_Lahan.lahan_id == Lahan.id)
            .join(Pengeluaran, Aktivitas_Lahan.pengeluaran_id == Pengeluaran.id)
            .filter(Lahan.user_id == current_user.id)
            .filter(Lahan.id == id_lahan)
            .all()
        )

        # Mengurutkan hasil query berdasarkan tanggal dengan urutan descending
        sorted_result = sorted(filter(lambda item: item[0].user_id == current_user.id, query_result), key=lambda item: item[2].tanggal, reverse=True)

        return list(sorted_result)
