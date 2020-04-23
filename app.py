# SOEN287 Web Programming Take-Home Final Exam
# Winter 2020

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, RadioField, SubmitField
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
    checkbox_group = MultiCheckboxField('Checkbox', choices=[('c1', 'Checkbox 1')])
    fav_color = ColorField('Favorite Color',
                           validators=[InputRequired()])
    radio_group = RadioField('Radio button group',
                             validators=[InputRequired()],
                             choices=[('r1', 'Radio button 1'),
                                      ('r2', 'Radio button 2'),
                                      ('r3', 'Radio button 3'),
                                      ('r4', 'Radio button 4')],
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
        
        return render_template('survey.html', form=request.form,
                               checkboxes=request.form.getlist('checkbox_group'))
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
