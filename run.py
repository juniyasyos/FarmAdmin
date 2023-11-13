from flask import Flask, render_template

app = Flask(__name__,template_folder='template')

@app.route('/')
def home():
    return 'Selamat datang di halaman utama!'

@app.route('/about')
def about():
    return 'Ini adalah halaman about kami.'

@app.route('/Dashboard')
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
