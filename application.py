from flask import Flask, render_template

application = Flask(__name__)

@application.route("/")
def index():
    return render_template("index.html")

@application.route("/about")
def about():
    return render_template("about.html")

@application.route("/wtmm")
def wtmm():
    return render_template("wtmm.html")

@application.route("/real_estate_resources")
def REresources():
    return render_template("REresources.html")

@application.route("/personal_finance_and_savings_resources")
def PFSresources():
    return render_template("PFSresources.html")