# SOEN287 Web Programming Take-Home Final Exam
# Winter 2020

from flask import Flask, render_template

app = Flask(__name__)


# TODO: Question 2: Survey FlaskForm
# Write your survey FlaskForm starting on the next line

# end of your survey FlaskForm



@app.route('/')
def exam():
    return render_template('exam.html', prev_link="", next_link="/q1")


# TODO: Question 1: questions endpoints
# Routes for the 4 questions templates starting on the next line
@app.route('/q1')
def q1():
    return render_template('q1.html', prev_link="/", next_link="/q2")

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

# end of your survey endpoint


# TODO: Question 3: Survey Results Endpoint
# Write your survey results endpoint starting on the next line

# end of your survey results endpoint


# TODO: Question 4: JavaScript and regular expressions
# Write your postal codes endpoint starting on the next line

# end of your postal codes endpoint


if __name__ == '__main__':
    app.run()
