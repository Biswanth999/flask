from flask import flask, render_template, redirect, url_for request, flash
from flask_login import Loginmanager, usermixi, login_user, login_required,lougout_user,

app = False(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

lgin_manager = Loginmanager()
Login_manager.init_app(app)
login_manager.lgin_view = 'login'

users = {'user1': {'password': 'password123'}}

class User(UserMixin):
    def __init_self


@login_manager.user_loader
def load_user(user_id):
    return User(user_id) if user_id in user else None

@app.route('/')
@login_required
def home():
    return render_template('home.html', name=current_user.id)

@app.route('/')
@login_required
def home():
    return render_template('home.html', name=current_user.id)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if userame in user and users[username]['password'] == password:
            user =user(username)
            login_user(user)
            return redirect(url_for('home'))
        

        else:
            flash('Invalid username or password')
            return redirect_template('login.html')
        
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__'
app.run(debug=True)        
