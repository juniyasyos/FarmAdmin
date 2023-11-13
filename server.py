from flask import Flask, render_template
# from Experimen import DatabaseHelper


# class Models:
#     def __init__(self) -> None:
#         self.DB = DatabaseHelper()
#         self.aktivitas_lahan = ""
#         self.Jadwal_aktivitas = ""
#         self.list_total_pendapatan = ""
#         self.list_total_pengeluaran = ""
    
#     def get_all_pendapatan(self):
#         query = """
#                 SELECT 
#                 hp.tanggal_panen AS Tanggal,
#                 l.nama_lahan AS Nama,
#                 hp.jumlah_panen AS Jumlah
#                 FROM hasil_panen hp
#                 JOIN lahan l ON hp.lahan_id = l.id;
#                 """
#         return self.DB.execute_query(query)
        
#     def get_all_pengeluaran(self):
#         query = """SELECT
#                     p.tanggal AS Tanggal,
#                     l.nama_lahan AS Nama_Lahan,
#                     p.biaya AS Biaya,
#                     p.keterangan AS Keterangan
#                 FROM pengeluaran p
#                 JOIN lahan l ON p.lahan_id = l.id"""
#         return self.DB.execute_query(query)
        
        


# models = Models()
# pengeluaran = models.get_all_pengeluaran()
# pendapatan = models.get_all_pendapatan()
# models.DB.close_connection()

# for i in pendapatan:
#     print(i)

# for i in pengeluaran:
#     print(i)

app = Flask(__name__,template_folder='template')

@app.route('/')
def Dashboard():
    return render_template('public/html/Dashboard.html')
        
@app.route('/Homepage')
def Homepage():
    return render_template('public/html/Homepage.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('public/html/404.html')

if __name__ == '__main__':
    app.run(debug=True)
