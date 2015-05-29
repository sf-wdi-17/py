from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  doc ="<html><body><h1>Hello World</h1></body></html>"
  return doc

@app.route("/test")
def idk():
  return "charlie murphy"

@app.route("/hello/<username>")
def show_user_profil(username):
  return "User %s" % username

if __name__ == "__main__":
  app.run()
