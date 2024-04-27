from flask import Flask, render_template,request,redirect,url_for,session
from flask_mysqldb import MySQL
from flask_session import Session

app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='admin12345'
app.config['MYSQL_DB']='logindata'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
   return render_template('login.html')

@app.route('/start', methods=['POST'])
def start():
    return render_template('index.html')

@app.route('/logout')
def logout():
    session.clear()
    return render_template('home.html')

@app.route('/login', methods=['POST','GET']) 
def verify_login():
    session["username"] = request.form.get("username")
    passcode = request.form['password']

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM logindata WHERE Username = %s AND Passcode = %s", (session["username"], passcode))
    user = cur.fetchone()
    mysql.connection.commit()
    cur.close()

    if user:
        # Redirect to the quiz difficulty choosing page
        return render_template('index.html')
    else:
        #flash('Invalid credentials. Please try again.')
        return render_template('login.html',error='Invalid credentials, Please try again or click on Register')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        passcode = request.form['password']
        email = request.form['email']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM logindata WHERE EmailID = %s", (email,))
        existing_user = cur.fetchone()
        mysql.connection.commit()
        cur.close()

        if existing_user:
            return render_template('register.html', error='Email ID already exists. Please use a different email ID.')

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO logindata(Username,Passcode,EmailID) values(%s,%s,%s)",(username, passcode, email))
        mysql.connection.commit()
        cur.close()
        # Redirect to the login page after successful registration
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/german')
def german():
    return render_template('german-shepard.html')

@app.route('/dober')
def dober():
    return render_template('Doberman.html')

@app.route('/lab')
def lab():
    return render_template('Labrador.html')

@app.route('/pit')
def pit():
    return render_template('Pit Bull.html')

@app.route('/bull')
def bull():
    return render_template('Bull Dog.html')

@app.route('/rot')
def rot():
    return render_template('Rottweiler.html')

@app.route('/dashshund')
def dashshund():
    return render_template('Dachshund.html')

@app.route('/greatdane')
def greatdane():
    return render_template('Great Dane.html')

@app.route('/haski')
def haski():
    return render_template('haski.html')

@app.route('/golden')
def golden():
    return render_template('Golden Retriever.html')

@app.route('/pomaranian')
def pomaranian():
    return render_template('pomaranian.html')

@app.route('/beagle')
def beagle():
    return render_template('Beagle.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)