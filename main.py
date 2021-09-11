from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap
import smtplib

OWN_EMAIL = "chicksrated@yahoo.com"
OWN_PASSWORD = "zrrzbygwdwukuuiy"

app = Flask(__name__)
Bootstrap(app)
app.secret_key = "kjsdbvnsndkivndksnvkdsmvdlkmvkds"


class login_form(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    messages = StringField('Messages', validators=[DataRequired()])


@app.route("/", methods=['GET', 'POST'])
def home():
    form = login_form()
    if form.validate_on_submit():
        print("True")
        send_email(form.name.data, form.email.data, form.messages.data)
        redirect('www.google.com')
    return render_template('index.html', form=form)


def send_email(name, email, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nMessage:{message}"
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)
        connection.login(user=OWN_EMAIL, password=OWN_PASSWORD)
        connection.sendmail(from_addr=OWN_EMAIL, to_addrs="jatinv85276@gmail.com",
                            msg=f"Subject:Portfolio Messages\n\n {email_message}")


@app.route("/portfolio-details")
def interior_portfolio():
    return render_template('interior-portfolio.html')

@app.route('/movies-portfolio')
def movies_portfolio():
    return render_template('movie-portfolio.html')

@app.route("/blog-portfolio")
def blog_portfolio():
    return render_template("blog-portfolio.html")

@app.route("/omnifood-portfolio")
def omnifood_portfolio():
    return render_template("omnifood-portfolio.html")

if __name__ == "__main__":
    app.run(debug=True)
