from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length
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

class Lahan(db.Model, UserMixin):
    __tablename__ = 'Lahan'
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(255))
    lokasi = db.Column(db.String(255))
    deskripsi = db.Column(db.TEXT)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    user = db.relationship('User', backref=db.backref('lahans', lazy=True))

class Pendapatan(db.Model, UserMixin):
    __tablename__ = 'Pendapatan'
    id = db.Column(db.Integer, primary_key=True)
    tanggal = db.Column(db.Date)
    nama_barang = db.Column(db.String(255))
    harga_barang = db.Column(db.DECIMAL(10, 2))
    jumlah = db.Column(db.Integer)
    keterangan = db.Column(db.TEXT)
    lahan_id = db.Column(db.Integer, db.ForeignKey('Lahan.id'))
    hasil_panen_id = db.Column(db.Integer, db.ForeignKey('Hasil_Panen.id'))

class Hasil_Panen(db.Model, UserMixin):
    __tablename__ = 'Hasil_Panen'
    id = db.Column(db.Integer, primary_key=True)
    lahan_id = db.Column(db.Integer, db.ForeignKey('Lahan.id'))
    jenis_tanaman = db.Column(db.String(255))
    jumlah_hasil_panen = db.Column(db.Integer)
    waktu_mulai = db.Column(db.DateTime)
    waktu_panen = db.Column(db.DateTime)

class Pengeluaran(db.Model, UserMixin):
    __tablename__ = 'Pengeluaran'
    id = db.Column(db.Integer, primary_key=True)
    jenis_aktivitas = db.Column(db.String(255))
    total_pengeluaran = db.Column(db.DECIMAL(10, 2))
    keterangan = db.Column(db.TEXT)

class Aktivitas_Lahan(db.Model, UserMixin):
    __tablename__ = 'Aktivitas_Lahan'
    id = db.Column(db.Integer, primary_key=True)
    lahan_id = db.Column(db.Integer, db.ForeignKey('Lahan.id'))
    pengeluaran_id = db.Column(db.Integer, db.ForeignKey('Pengeluaran.id'))
    status = db.Column(db.String(255))
    id_panen = db.Column(db.Integer, db.ForeignKey('Hasil_Panen.id'))
