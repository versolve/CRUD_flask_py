from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev_secret')

# Config database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/flask_auth'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Upload folder config
UPLOAD_FOLDER = os.path.join('static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # max 16MB

db = SQLAlchemy(app)

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(255), nullable=True)  # nama file gambar

    def __repr__(self):
        return f'<Product {self.name}>'

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product_preview(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('preview_produk.html', product=product)

@app.route('/dashboard')
def dashboard():
    products = Product.query.all()
    return render_template('dashboard.html', products=products)

@app.route('/tambah', methods=['GET', 'POST'])
def tambah_produk():
    if request.method == 'POST':
        # Ambil file gambar dari form
        file = request.files.get('image')
        filename = None
        if file and file.filename != '':
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        p = Product(
            name=request.form['name'],
            description=request.form['description'],
            price=int(request.form['price']),
            stock=int(request.form['stock']),
            image=filename  # simpan nama file saja
        )
        db.session.add(p)
        db.session.commit()
        flash('Produk berhasil ditambahkan!', 'success')
        return redirect(url_for('dashboard'))

    return render_template('tambah_produk.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_produk(id):
    p = Product.query.get_or_404(id)
    if request.method == 'POST':
        file = request.files.get('image')
        if file and file.filename != '':
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            p.image = filename

        p.name = request.form['name']
        p.description = request.form['description']
        p.price = int(request.form['price'])
        p.stock = int(request.form['stock'])

        db.session.commit()
        flash('Produk berhasil diperbarui!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('edit_produk.html', product=p)

@app.route('/hapus/<int:id>', methods=['POST'])
def hapus_produk(id):
    p = Product.query.get_or_404(id)
    db.session.delete(p)
    db.session.commit()
    flash('Produk berhasil dihapus!', 'success')
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
