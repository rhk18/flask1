from flask import Flask,request,json, jsonify

app = Flask(__name__)

@app.route("/v1/sanitized/input/",methods=["POST"])
def check_input():
    data=request.get_json()
    name=data['name']
    sql_injection_chars = ["'", ";", "--", "/"]
    json_string = json.dumps(name)
    for char in sql_injection_chars:
        if char in json_string:
            result=jsonify({"result":"unsanitised"})
            break
        else:
            result=jsonify({"result":"sanitised"})
    return result
    
if __name__=="__main__":
    app.run(debug=True,port=8000)
