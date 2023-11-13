from flask import Flask, render_template

app = Flask(__name__,template_folder='')

@app.route('/')
def home():
    return 'Selamat datang di halaman utama!'

@app.route('/about')
def about():
    return 'Ini adalah halaman about kami.'

@app.route('/Homepage')
def Homepage():
    return render_template('public/html/Homepage.html')

# Handler untuk rute 404 (rute yang tidak ada dalam opsi kode)
@app.errorhandler(404)
def page_not_found(error):
    return render_template('public/html/nangendi.html')

if __name__ == '__main__':
    app.run(debug=True)
