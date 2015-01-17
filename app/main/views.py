from flask import render_template, current_app, flash, redirect, url_for
from . import main
from forms import ContactForm
from ..email import send_email

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/menu')
def menu():
    return render_template('menu.html')

@main.route('/hours-and-directions')
def hours():
    return render_template('hours-and-directions.html')

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        name = contact_form.name.data
        email = contact_form.email.data
        phone = contact_form.phone.data
        message = contact_form.message.data
        if current_app.config['APP_ADMIN']:
                send_email(current_app.config['APP_ADMIN'], 'Robata Grill Inquiry',
                           'mail/message', name=name, email=email, phone=phone, message=message)
        flash('Your message has been sent. We will be in contact with you shortly.')
        return redirect(url_for('main.contact'))
    return render_template('contact.html', contact_form = contact_form)

