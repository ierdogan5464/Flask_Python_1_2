from flask import Flask 
app = Flask(__name__)

@app.route("/")
def head ():
    return "hello world clarusway 17"

@app.route("/second")
def head2 ():
    return "Second page"

@app.route("/third")
def head3 ():
    return "third page"




if __name__ == '__main__':

    #  app.run(debug=True, port=30000)
    app.run(host= '34.201.46.238', port=8081)