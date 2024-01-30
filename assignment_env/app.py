from flask import Flask, render_template,request

app = Flask(__name__)  

@app.route('/')
def home():  
    return render_template('home.html')  

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/user/<username>')
def user(username):  
    return f'Hello,{username}'
@app.route('/submit', methods=['GET', 'POST'])


@app.route('/submit', methods=['GET','POST'])
def submit():  
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return f'Thank you, {name}! We received you.'
    return render_template('form.html')


@app.route('/hello', methods=['GET','POST'])
def index():
    if request.method =='POST':
        return 'This is a request'
    return render_template('home.html')