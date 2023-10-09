from flask_app import app
from flask import render_template, redirect, request, session, flash, Flask
from flask_app.models.user import User
from flask_app.models.location import Location
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)     # we are creating an object called bcrypt, which is made by invoking the function Bcrypt with our app as an argument

#app = Flask(__name__)  Still having this line in was causing the Not Found page to load
@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/register', methods=["POST"])
def register():
    print("REQUEST FORM: ", request.form)
    if not User.validate_register(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password" : pw_hash
    }
    id = User.save(data)
    # store user id into session
    session['id'] = id
    print("ID in session:", session['id'])
    return redirect("/dashboard")

@app.route('/dashboard')
def dashboard():
    if 'id' not in session:
        return redirect('/logout')
    id = session['id']
    print("ID in session:", id)
    user = User.get_one(id)
    locations = Location.get_locations_for_user(id)
    date_time = locations[0]["created_at"].strftime("%Y-%m-%d") #.strftime("%B %d %Y")
    print("date and time:",date_time)
    return render_template("dashboard.html", user=user, locations=locations)

@app.route('/login', methods=['POST'])
def login():
    # see if the username provided exists in the database
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password", "login")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password", "login")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['id'] = user_in_db.id
    print("The ID returned from the DB", user_in_db.id)
    print(f"/login/{user_in_db.id}")
    # never render on a post!!!
    return redirect("/dashboard")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


# @app.route('/user/edit/<int:id>', methods=["GET", "POST"])
# def edit_user(id):
#     #print(id)
#     if request.method == "GET":
#         user = User.get_one(id)
#         return render_template("edit_user.html", user=user)
#     data = {
#         "id": [id],
#         "first_name": request.form["first_name"],
#         "last_name": request.form["last_name"],
#         "email": request.form["email"]
#     }
#     User.edit_user(data)
#     return redirect("/dashboard")

# @app.route('/user/delete/<int:id>')
# def delete_user(id):
#     User.delete_user(id)
#     return redirect("/dashboard")