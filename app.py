# SOEN287 Web Programming Take-Home Final Exam
# Winter 2020

from flask import Flask, render_template

app = Flask(__name__)


# TODO: Question 2: Survey FlaskForm
# Write your survey FlaskForm starting on the next line

# end of your survey FlaskForm


@app.route('/')
def exam():
    return render_template('exam.html')


# TODO: Question 1: questions endpoints
# Routes for the 4 questions templates starting on the next line

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
