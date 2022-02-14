from flask import Flask,jsonify,request
from alphabetrecog import get_pred

app = Flask(__name__)

@app.route("/")
def main():
    return "my first api alphabet recognizer"

@app.route('/get-prediction',methods=["POST"])
def get_prediction():
    image = request.files.get('alphabet')
    prediction = get_pred(image)
    return jsonify({
        'prediction':prediction,
    },200)

if(__name__=='__main__'):
    app.run(debug=True)
