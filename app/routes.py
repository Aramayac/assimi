from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import User

crud_bp = Blueprint("crud", __name__)

@crud_bp.route("/")
def home():
    page = request.args.get('page', 1, type=int)
    users = User.query.paginate(page=page, per_page=5)
    return render_template("index.html", users=users)

@crud_bp.route("/dashboard")
def dashboard():
    users_count = User.query.count()
    return render_template("dashboard.html", users_count=users_count)

@crud_bp.route("/add", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        new_user = User(
            nom=request.form["nom"],
            prenom=request.form["prenom"],
            age=int(request.form["age"]),
            nationalite=request.form["nationalite"]
        )
        db.session.add(new_user)
        db.session.commit()
        flash("Utilisateur ajouté ✅", "success")
        return redirect(url_for("crud.home"))
    return render_template("add.html")

@crud_bp.route("/update/<int:id>", methods=["GET", "POST"])
def update_user(id):
    user = User.query.get_or_404(id)
    if request.method == "POST":
        user.nom = request.form["nom"]
        user.prenom = request.form["prenom"]
        user.age = int(request.form["age"])
        user.nationalite = request.form["nationalite"]
        db.session.commit()
        flash("Utilisateur modifié ✏️", "success")
        return redirect(url_for("crud.home"))
    return render_template("update.html", user=user)

@crud_bp.route("/delete/<int:id>")
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash("Utilisateur supprimé ❌", "danger")
    return redirect(url_for("crud.home"))
