from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, desc
from sqlalchemy.orm import aliased
from dotenv import load_dotenv
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from operator import itemgetter
from functools import reduce
from datetime import datetime
from icecream import ic
from collections import defaultdict
import os


load_dotenv()

db = SQLAlchemy()

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
        db.init_app(app)

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
    
# Form Create new activity
class Aktivitas_LahanForm(FlaskForm):
    lahan_idForm = db.Column(db.Integer, db.ForeignKey('Lahan.id'))
    pengeluaran_idForm = db.Column(db.Integer, db.ForeignKey('Pengeluaran.id'))
    statusForm = db.Column(db.String(255))
    id_panenForm = db.Column(db.Integer, db.ForeignKey('Hasil_Panen.id'))
    
# Form Create new pengeluaran
class PengeluaranForm(FlaskForm):
    tanggalForm = db.Column(db.Date, nullable=False)
    jenis_aktivitasForm = db.Column(db.String(255))
    total_pengeluaranForm = db.Column(db.DECIMAL(10, 2))
    keteranganForm = db.Column(db.TEXT)


# Deklarasi entity User
class User(db.Model, UserMixin):
    # Nama tabel dalam database
    __tablename__ = 'User'
    
    # Definisi kolom-kolom dalam tabel User
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), unique=True, nullable=False)
    Nama_Lengkap = db.Column(db.String(80))
    Nama_Penggilan = db.Column(db.String(30))
    Nomor_Telepon = db.Column(db.String(20))
    Password = db.Column(db.String(255), nullable=False)
    Bio = db.Column(db.TEXT)             
    
# Deklarasi entity Lahan
class Lahan(db.Model, UserMixin):
    # Nama tabel dalam database
    __tablename__ = 'Lahan'

    # Definisi kolom-kolom dalam tabel Lahan
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(255))
    lokasi = db.Column(db.String(255))
    deskripsi = db.Column(db.TEXT)
    luas = db.Column(db.Integer)
    jenis_tanaman = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    user = db.relationship('User', backref=db.backref('lahans', lazy=True))
    
# Deklarasi Entity Pendapatan
class Pendapatan(db.Model, UserMixin):
    __tablename__ = 'Pendapatan'
    id = db.Column(db.Integer, primary_key=True)
    tanggal = db.Column(db.Date)
    nama_barang = db.Column(db.String(255))
    harga_barang = db.Column(db.DECIMAL(10, 2))
    jumlah = db.Column(db.Integer)
    keterangan = db.Column(db.TEXT)
    hasil_panen_id = db.Column(db.Integer, db.ForeignKey('Hasil_Panen.id'))
    
# Deklarasi Entity Hasil Panen
class Hasil_Panen(db.Model, UserMixin):
    __tablename__ = 'Hasil_Panen'
    id = db.Column(db.Integer, primary_key=True)
    lahan_id = db.Column(db.Integer, db.ForeignKey('Lahan.id'))
    jenis_tanaman = db.Column(db.String(255))
    jumlah_hasil_panen = db.Column(db.Integer)
    waktu_mulai = db.Column(db.DateTime)
    waktu_panen = db.Column(db.DateTime)
    judul_panen = db.Column(db.String(255))

# Deklarasi Entity Pengeluaran
class Pengeluaran(db.Model, UserMixin):
    # Nama tabel dalam database
    __tablename__ = 'Pengeluaran'

    # Definisi kolom-kolom dalam tabel Pengeluaran
    id = db.Column(db.Integer, primary_key=True)
    tanggal = db.Column(db.Date, nullable=False)
    jenis_aktivitas = db.Column(db.String(255))
    total_pengeluaran = db.Column(db.DECIMAL(10, 2))
    keterangan = db.Column(db.TEXT)

# Deklarasi Entity Aktivitas Lahan
class Aktivitas_Lahan(db.Model, UserMixin):
    # Nama tabel dalam database
    __tablename__ = 'Aktivitas_Lahan'

    # Definisi kolom-kolom dalam tabel Aktivitas_Lahan
    id = db.Column(db.Integer, primary_key=True)
    lahan_id = db.Column(db.Integer, db.ForeignKey('Lahan.id'))
    pengeluaran_id = db.Column(db.Integer, db.ForeignKey('Pengeluaran.id'))
    status = db.Column(db.String(255))
    id_panen = db.Column(db.Integer, db.ForeignKey('Hasil_Panen.id'))

# Class Functional Programming Operation 
class Operation:
    def __init__(self) -> None:
        pass
    
    # Pure Function filtered lahan by id
    def _filter_lahan(self, user, lahan_data):
        return lahan_data.query.filter_by(user_id=user.id)

    def get_total_lahan(self, user):
        return self._filter_lahan(user, Lahan).count()

    def get_total_hasil_panen(self, user):
        return Hasil_Panen.query.join(Lahan).filter(Lahan.user_id == user.id).count()

    def get_total_pendapatan(self, user):
        return db.session.query(func.sum(Pendapatan.harga_barang * Pendapatan.jumlah)).join(Hasil_Panen).join(Lahan).filter(Hasil_Panen.lahan_id == Lahan.id).filter(Lahan.user_id == user.id).scalar() or 0

    def get_total_pengeluaran(self, user):
        return db.session.query(func.sum(Pengeluaran.total_pengeluaran)).join(Aktivitas_Lahan, Aktivitas_Lahan.pengeluaran_id == Pengeluaran.id).join(Lahan).filter(Lahan.user_id == user.id).scalar() or 0

    def get_list_lahan(self, user):
        customColors = ["#98a6ad", "#41b3f9", "#f4c63d", "#d17905", "#453d3f", "#453d3f"]
        data_lahan = [str(lahan.nama) for lahan in self._filter_lahan(user, Lahan).all()]
        return list(map(lambda x,y: [x,y], data_lahan, customColors))
    
    # Fungsi untuk mendapatkan semua lahan milik pengguna tertentu
    def get_all_lahan(self, user):
        return list(filter(lambda lahan: lahan.user_id == user.id, lahan_data.query.all()))

    # Fungsi untuk menghitung total pengeluaran lahan per bulan
    def Pengeluaran_lahan_perbulan(self, user):
        result = (
            db.session.query(
                Lahan.id.label('lahan_id'),
                func.month(Pengeluaran.tanggal).label('bulan'),
                func.sum(Pengeluaran.total_pengeluaran).label('total_pengeluaran')
            )
            .select_from(Lahan)
            .join(Aktivitas_Lahan, Lahan.id == Aktivitas_Lahan.lahan_id)
            .join(Pengeluaran, Aktivitas_Lahan.pengeluaran_id == Pengeluaran.id)
            .filter(Lahan.user_id == user.id)
            .group_by(Lahan.id, func.month(Pengeluaran.tanggal))
            .all()
        )

        data_per_lahan = {}

        for row in result:
            lahan_id = row.lahan_id
            bulan = row.bulan
            total_pengeluaran = row.total_pengeluaran

            if lahan_id not in data_per_lahan:
                data_per_lahan[lahan_id] = {}

            data_per_lahan[lahan_id][bulan] = total_pengeluaran

        return list(map(lambda lahan_id: list(map(lambda bulan: data_per_lahan[lahan_id].get(bulan, 0), range(1, 13))), data_per_lahan.keys()))

    # Fungsi untuk mendapatkan semua data yang dimiliki lahan
    def get_data_lahan(self, lahan_id):
        return (
            db.session.query()
            .select_from(Lahan, Lahan.id == lahan_id)
            .join(Aktivitas_Lahan, Aktivitas_Lahan.pengeluaran_id == Pengeluaran.id)
            .filter(Lahan.user_id == user.id)
            .all()
        )

     # Fungsi untuk mendapatkan semua data pendapatan berdasarkan user
    
    # FUngsi untuk mendapatkan semua Pendapatan user
    def get_all_pendapatan(self, user):
        return (
            db.session.query(Hasil_Panen, Pendapatan)
            .join(Hasil_Panen, Hasil_Panen.id == Pendapatan.hasil_panen_id)
            .join(Lahan, Lahan.user_id == user.id)
            .order_by(desc(Pendapatan.tanggal))
            .all()
        )
    
    # Fungsi untuk mendapatkan semua pengeluaran berdasarkan user
    def get_all_pengeluaran(self, user):
        query_result = (
            db.session.query(Lahan, Aktivitas_Lahan, Pengeluaran)
            .join(Aktivitas_Lahan, Aktivitas_Lahan.lahan_id == Lahan.id)
            .join(Pengeluaran, Aktivitas_Lahan.pengeluaran_id == Pengeluaran.id)
            .filter(Lahan.user_id == user.id)
            .all()
        )

        # Mengurutkan hasil query berdasarkan tanggal dengan urutan descending
        sorted_result = sorted(filter(lambda item: item[0].user_id == user.id, query_result), key=lambda item: item[2].tanggal, reverse=True)

        return list(sorted_result)
    
    # Fungsi untuk mendapatkan semua aktivitas lahan berdasarkan user
    def get_all_activity(self, user):
        return list(map(
            lambda x: db.session.query(Pengeluaran, Lahan, Aktivitas_Lahan)
            .join(Aktivitas_Lahan, Lahan.id == Aktivitas_Lahan.lahan_id)
            .join(Pengeluaran, Aktivitas_Lahan.pengeluaran_id == Pengeluaran.id)
            .filter(Lahan.user_id == user.id)
            .order_by(desc(Pengeluaran.tanggal))
            .all(), [None]))[0]

    @staticmethod
    def aktivitas_perlahan(id_lahan, current_user):
        query_result = (
            db.session.query(Lahan, Aktivitas_Lahan, Pengeluaran)
            .join(Aktivitas_Lahan, Aktivitas_Lahan.lahan_id == Lahan.id)
            .join(Pengeluaran, Aktivitas_Lahan.pengeluaran_id == Pengeluaran.id)
            .filter(Lahan.user_id == current_user.id)
            .filter(Lahan.id == id_lahan)
            .all()
        )

        # Mengurutkan hasil query berdasarkan tanggal dengan urutan descending
        sorted_result = sorted(filter(lambda item: item[0].user_id == current_user.id, query_result), key=lambda item: item[2].tanggal, reverse=True)

        return list(sorted_result)
    