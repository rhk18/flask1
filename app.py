from flask import Flask,request,json, jsonify
import re

app = Flask(__name__)

@app.route("/v1/sanitized/input/",methods=["POST"])
def check_input():
    data=request.get_json()
    name=data['name']
    pattern =r"[^a-zA-Z0-9]"
    if re.search(pattern,name):
        return jsonify({"result":"unsanitised"})
    else:
        return jsonify({"result":"sanitised"})
    
if __name__=="__main__":
    app.run(debug=True,port=8000)
