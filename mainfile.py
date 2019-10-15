from flask import Flask, render_template, redirect, request
from forms import SignUpForm
app=Flask(__name__)
app.config['SECRET_KEY']='wasteaf'


@app.route('/')
def screen1():
    return render_template('openscreen.html')


@app.route('/adminlogin')
def screen2():
    return render_template('adminlogin.html')


@app.route('/stafflogin')
def screen3():
    return render_template('stafflogin.html')


if __name__ == '__main__':
    app.run(debug=True)
