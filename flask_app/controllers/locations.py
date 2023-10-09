from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.location import Location
from flask_app.models.user import User

@app.route('/location/<int:id>')
def view(id):
    if 'id' not in session:
        return redirect('/logout')
    # id = session['id']
    print("ID in session:", session['id'])
    print("Printing out the id passed from /location/id: ", id)
    location = Location.get_one(id)
    user = User.get_one(session['id'])
    print("Results returned to route for location:", location)
    print("Results returned to route for user:", user)
    return render_template("view_location.html", user=user, location=location)

@app.route('/add_location', methods=["GET", "POST"])
def create_location():
    if 'id' not in session:
        return redirect('/logout')
    id = session['id']
    print("ID in session:", id)
    if request.method == "GET":
        return render_template("add_location.html", user_id=id)
    print(request.form)
    if not Location.validate_location(request.form):
        return redirect('/add_location')
    print("in create route")
    print(request.form)
    location_id = Location.save(request.form)
    print("location_id created: ", location_id)
    return redirect("/dashboard")

@app.route('/location/edit/<int:id>', methods=["GET", "POST"])
def edit_location(id):
    if 'id' not in session:
        return redirect('/logout')
    # id = session['id']
    # print("ID in session:", id)
    if request.method == "GET":
        location = Location.get_one(id)
        # date_time = recipe["date_made"].strftime("%Y-%m-%d")
        # print("date and time:",date_time)
        return render_template("edit_location.html", location=location)
    if not Location.validate_location(request.form):
        print("in edit route")
        print(request.form)
        return redirect(f"/location/edit/{id}")
    print("in edit route")
    print(request.form)
    Location.edit(request.form)
    return redirect("/dashboard")

@app.route('/location/delete/<int:id>')
def delete_location(id):
    print("Deleting location - ", id)
    Location.delete(id)
    return redirect("/dashboard")

@app.route('/companies')
def tree_companies():
    if 'id' not in session:
        return redirect('/logout')
    return render_template("tree_companies.html")

@app.route('/tree_search')
def tree_search():
    if 'id' not in session:
        return redirect('/logout')
    return render_template("tree_search.html")

@app.route('/tree_survey')
def tree_survey():
    if 'id' not in session:
        return redirect('/logout')
    return render_template("tree_survey.html")