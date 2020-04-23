# SOEN287 Web Programming Take-Home Final Exam
# Winter 2020
import csv

from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, RadioField, SubmitField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Email
from wtforms.widgets import ListWidget, CheckboxInput
from wtforms_components import ColorField


app = Flask(__name__)
app.secret_key = 'allo'

# TODO: Question 2: Survey FlaskForm
# Write your survey FlaskForm starting on the next line

class MultiCheckboxField(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()

class SurveyForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired(), Email()])
    checkbox = BooleanField('Show e-mail?', default=False)
    color = ColorField('Favorite Color',
                           validators=[InputRequired()])
    radio_group = RadioField('What is your favorite letter?',
                             validators=[InputRequired()],
                             choices=[('a', 'a'),
                                      ('b', 'b'),
                                      ('c', 'c'),
                                      ('d', 'd')],
                             render_kw={'required': True})
    submit = SubmitField('Submit')
# end of your survey FlaskForm



@app.route('/')
def exam():
    return render_template('exam.html')


# TODO: Question 1: questions endpoints
# Routes for the 4 questions templates starting on the next line
@app.route('/q1')
def q1():
    return render_template('q1.html', next_link="/q2")

@app.route('/q2')
def q2():
    return render_template('q2.html', prev_link="/q1", next_link="/q3")

@app.route('/q3')
def q3():
    return render_template('q3.html', prev_link="/q2", next_link="/q4")

@app.route('/q4')
def q4():
    return render_template('q4.html', prev_link="/q3", next_link="")
# End of the 4 questions templates


# TODO: Question 2: Survey Endpoint
# Write your survey endpoint starting on the next line
@app.route('/survey', methods=['GET', 'POST'])
def survey():
    form = SurveyForm()
    if form.validate_on_submit():
        with open('data/info.csv', 'w') as f:
            writer = csv.writer(f)
            try:
                n = request.form['checkbox']
                writer.writerow([request.form['email'],
                                 request.form['color'],
                                 request.form['radio_group']])
            except:
                writer.writerow([request.form['color'],
                                 request.form['radio_group']])

        return redirect('/survey/results')
    return render_template('survey.html', form=form)
# end of your survey endpoint


# TODO: Question 3: Survey Results Endpoint
# Write your survey results endpoint starting on the next line

# end of your survey results endpoint


# TODO: Question 4: JavaScript and regular expressions
# Write your postal codes endpoint starting on the next line

# end of your postal codes endpoint


if __name__ == '__main__':
    app.run()
