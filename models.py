from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, desc
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

class Models:
    def __init__(self, app=None, db_config=None):
        if app:
            self.init_app(app, db_config)

    def init_app(self, app, db_config=None):
        if db_config is None:
            db_config = self.load_db_config()

        app.config['SQLALCHEMY_DATABASE_URI'] = self.get_database_uri(db_config)
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(app)

    def load_db_config(self):
        return {
            'DB_HOST': os.getenv('DB_HOST'),
            'DB_PORT': os.getenv('DB_PORT'),
            'DB_USER': os.getenv('DB_USER'),
            'DB_PASSWORD': os.getenv('DB_PASSWORD'),
            'DB_NAME': os.getenv('DB_NAME'),
        }

    def get_database_uri(self, db_config):
        return (
            f"mysql+mysqlconnector://{db_config['DB_USER']}:{db_config['DB_PASSWORD']}@"
            f"{db_config['DB_HOST']}:{db_config['DB_PORT']}/{db_config['DB_NAME']}"
        )

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=30)])
    full_name = StringField('Full Name', validators=[Length(max=80)])
    nickname = StringField('Nickname', validators=[Length(max=30)])
    phone_number = StringField('Phone Number', validators=[Length(max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    bio = StringField('Bio')
    submit = SubmitField('Register')

# Entity Database
class User(db.Model, UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), unique=True, nullable=False)
    Nama_Lengkap = db.Column(db.String(80))
    Nama_Penggilan = db.Column(db.String(30))
    Nomor_Telepon = db.Column(db.String(20))
    Password = db.Column(db.String(255), nullable=False)
    Bio = db.Column(db.TEXT)

    def get_total_lahan(self):
        return Lahan.query.filter_by(user_id=self.id).count()

    def get_total_hasil_panen(self):
        return Hasil_Panen.query.join(Lahan).filter(Lahan.user_id == self.id).count()

    def get_total_pendapatan(self):
        return db.session.query(func.sum(Pendapatan.harga_barang * Pendapatan.jumlah)).\
            join(Hasil_Panen).join(Lahan).\
            filter(Hasil_Panen.lahan_id == Lahan.id).filter(Lahan.user_id == self.id).\
            scalar() or 0

    def get_total_pengeluaran(self):
        return db.session.query(func.sum(Pengeluaran.total_pengeluaran)).\
            join(Aktivitas_Lahan, Aktivitas_Lahan.pengeluaran_id == Pengeluaran.id).\
            join(Lahan).filter(Lahan.user_id == self.id).scalar() or 0
    
    def get_list_lahan(self, get_all=False):
        result = list(map(lambda x:str(x)[1:-1], ic(Lahan.query.filter_by(user_id=self.id).all())))
        if get_all and len(result) >= 5:
            return result
        return result[0:5]
            

class Lahan(db.Model, UserMixin):
    __tablename__ = 'Lahan'
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(255))
    lokasi = db.Column(db.String(255))
    deskripsi = db.Column(db.TEXT)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    user = db.relationship('User', backref=db.backref('lahans', lazy=True))

    def Pengeluaran_lahan_perbulan(current_user):
            result = (
                db.session.query(
                    Lahan.id.label('lahan_id'),
                    func.month(Pengeluaran.tanggal).label('bulan'),
                    func.sum(Pengeluaran.total_pengeluaran).label('total_pengeluaran')
                )
                .select_from(Lahan)
                .join(Aktivitas_Lahan, Lahan.id == Aktivitas_Lahan.lahan_id)
                .join(Pengeluaran, Aktivitas_Lahan.pengeluaran_id == Pengeluaran.id)
                .filter(Lahan.user_id == current_user.id)
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

            return [[data_per_lahan[lahan_id].get(bulan, 0)/1000 for bulan in range(1, 13)] for lahan_id in data_per_lahan.keys()]

class Pendapatan(db.Model, UserMixin):
    __tablename__ = 'Pendapatan'
    id = db.Column(db.Integer, primary_key=True)
    tanggal = db.Column(db.Date)
    nama_barang = db.Column(db.String(255))
    harga_barang = db.Column(db.DECIMAL(10, 2))
    jumlah = db.Column(db.Integer)
    keterangan = db.Column(db.TEXT)
    hasil_panen_id = db.Column(db.Integer, db.ForeignKey('Hasil_Panen.id'))
    
    def get_all(current_user):
        return (
            db.session.query(Hasil_Panen,Pendapatan)
            .join(Hasil_Panen, Hasil_Panen.id == Pendapatan.hasil_panen_id)
            .join(Lahan,Lahan.user_id == current_user.id)
            .order_by(desc(Pendapatan.tanggal))
            .all()
        )

class Hasil_Panen(db.Model, UserMixin):
    __tablename__ = 'Hasil_Panen'
    id = db.Column(db.Integer, primary_key=True)
    lahan_id = db.Column(db.Integer, db.ForeignKey('Lahan.id'))
    jenis_tanaman = db.Column(db.String(255))
    jumlah_hasil_panen = db.Column(db.Integer)
    waktu_mulai = db.Column(db.DateTime)
    waktu_panen = db.Column(db.DateTime)
    judul_panen = db.Column(db.String(255))
    

class Pengeluaran(db.Model, UserMixin):
    __tablename__ = 'Pengeluaran'
    id = db.Column(db.Integer, primary_key=True)
    tanggal = db.Column(db.Date, nullable=False)
    jenis_aktivitas = db.Column(db.String(255))
    total_pengeluaran = db.Column(db.DECIMAL(10, 2))
    keterangan = db.Column(db.TEXT)
    
    def get_all(current_user):
        return (
            db.session.query(Lahan,Pengeluaran)
            .join(Aktivitas_Lahan, Aktivitas_Lahan.id == Pengeluaran.id)
            .join(Lahan)
            .filter(Lahan.user_id == current_user.id)
            .order_by(desc(Pengeluaran.tanggal))
            .all()
        )
    
class Aktivitas_Lahan(db.Model, UserMixin):
    __tablename__ = 'Aktivitas_Lahan'
    id = db.Column(db.Integer, primary_key=True)
    lahan_id = db.Column(db.Integer, db.ForeignKey('Lahan.id'))
    pengeluaran_id = db.Column(db.Integer, db.ForeignKey('Pengeluaran.id'))
    status = db.Column(db.String(255))
    id_panen = db.Column(db.Integer, db.ForeignKey('Hasil_Panen.id'))
    
    def get_all(current_user):
        return (
            db.session.query(Pengeluaran, Lahan, Aktivitas_Lahan)
            .join(Aktivitas_Lahan, Lahan.id == Aktivitas_Lahan.lahan_id)
            .join(Pengeluaran, Aktivitas_Lahan.pengeluaran_id == Pengeluaran.id)
            .filter(Lahan.user_id == current_user.id)
            .order_by(desc(Pengeluaran.tanggal))
            .all()
        )
