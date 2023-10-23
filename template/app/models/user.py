import hashlib
from DatabaseHelper import DatabaseHelper

class User:
    def __init__(self, password="", name="", email=""):
        self.user_id = None
        self.name = name
        self.password = password
        self.email = email
    
def get_user(obj, type, db=None):
    """
    Dapatkan pengguna dengan nama atau alamat email yang diberikan.

    Args:
        name_or_email: Nama atau alamat email pengguna.

    Returns:
        Objek pengguna, atau None jika pengguna tidak ada.
    """
    db = DatabaseHelper()

    # Eksekusi kueri untuk mendapatkan pengguna.
    query = "SELECT * FROM pengguna WHERE {0} = '{1}'".format(type, obj)
    result = db.get_one(query)
    print("result = ",result)

    # Jika pengguna tidak ada, kembalikan None.
    if result is None:
        return None

    # Buat objek pengguna baru dan kembalikan.
    user = User()
    user.user_id = result[0]
    user.name = result[1]
    user.email = result[2]
    user.password = result[3]
    return user


def login(checking, password_entered):
    """
    Login pengguna dengan nama atau email dan kata sandi yang diberikan.

    Args:
        name_or_email: Nama atau alamat email pengguna.
        password_entered: Kata sandi yang dimasukkan pengguna.

    Returns:
        True jika login berhasil, False jika tidak.
    """
    
    # Dapatkan objek database helper.
    db = DatabaseHelper()

    # Dapatkan pengguna dengan nama atau alamat email yang diberikan.
    user = User.get_user(checking, "email" if "@" not in checking else "name", db=db)

    # Jika pengguna tidak ada, kembalikan False.
    if user is None:
        return False,"username atau email"

    # Hash kata sandi yang dimasukkan.
    # hashed_password = hashlib.sha256(password_entered.encode()).hexdigest()

    # Bandingkan kata sandi hash dengan kata sandi pengguna yang disimpan.
    # if hashed_password == user.password:
    if password_entered == user.password:
        return True
    else:
        return False, "password"

# get_user(type="nama_pengguna",obj="Ahmad Ilyas")