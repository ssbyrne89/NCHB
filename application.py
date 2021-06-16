# NCHB/application.py

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

@application.route("/wtmm_sell_Ad_space_on_a_poster")
def wtmm_sell_Ad_space_on_a_poster():
    return render_template("wtmm_sell_Ad_space_on_a_poster.html")

@application.route("/wtmm_start_a_youtube_channel")
def wtmm_start_a_youtube_channel():
    return render_template("wtmm_start_a_youtube_channel.html")

@application.route("/wtmm_social_media_marketing")
def wtmm_social_media_marketing():
    return render_template("wtmm_social_media_marketing.html")
    
@application.route("/wtmm_cryptocurrency_interest_paying_accounts")
def wtmm_cryptocurrency_interest_paying_accounts():
    return render_template("wtmm_cryptocurrency_interest_paying_accounts.html")

@application.route("/wtmm_designing_tshirts")
def wtmm_designing_tshirts():
    return render_template("wtmm_designing_tshirts.html")

@application.route("/wtmm_bank_CD_accounts")
def wtmm_bank_CD_accounts():
    return render_template("wtmm_bank_CD_accounts.html")

@application.route("/wtmm_running_a_node")
def wtmm_running_a_node():
    return render_template("wtmm_running_a_node.html")

@application.route("/wtmm_browsing_the_internet")
def wtmm_browsing_the_internet():
    return render_template("wtmm_browsing_the_internet.html")

@application.route("/wtmm_driving")
def wtmm_driving():
    return render_template("wtmm_driving.html")
