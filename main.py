from flask import *

app=Flask(__name__)

@app.route("/")
def sample():
    return render_template('homep.html')

@app.route("/register")
def sample1():
    return render_template('register.html')


@app.route("/login")
def sample2():
    return render_template('login.html')

@app.route("/FAQ")
def sample3():
    return render_template('FAQ.html')



if __name__=="__main__":
    app.run(debug=True)