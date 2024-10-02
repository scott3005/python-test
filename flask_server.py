from flask import Flask 


app=Flask(__name__)

@app.route("/")
def main():
    return "hello world" 



@app.route("/live")
def live():
    return "live and ready"
if __name__=="__main__":
    app.run()