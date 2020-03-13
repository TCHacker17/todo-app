from flask import Flask
from flask import render_template
# from templates import task_list

app = Flask(__name__)


@app.route('/login')
def index():
	return render_template("login.html")

@app.route('/')
def home():
	return render_template("task_list.html")

@app.route('/task')
def task():
	return render_template("task_list2.html")