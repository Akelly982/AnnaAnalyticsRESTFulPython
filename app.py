from flask import Flask, jsonify, request
from flask_cors import CORS





app = Flask(__name__)
CORS(app)




@app.route('/')
def hello():
    return 'Hello World! I am currently running'



@app.route('/activeParentBtn', methods=['POST'])
def active():

    if request.method == "POST":
        return jsonify({
            'isSuccessfull': True, 
            'errorMsg': '',
            'DataSet': [{'parentId': 1, 'parentName':"Simple Math", 'childData': 
                            [{'childId': '1A', "childName": "addition"},
                            {'childId': '1B', "childName": "subtraction"},
                            {'childId': '1C', "childName": "multiply"}]},

                    {'parentId': 2, 'parentName':"CP1017", 'childData': 
                            [{'childId': '2A', "childName": "predictX"},
                            {'childId': '2B', "childName": "predictY"}]},

                    {'parentId': 3, 'parentName':"ADST506", 'childData': 
                            [{'childId': '3A', "childName": "predictZ"},
                            {'childId': '3B', "childName": "predictR"}]}
                    ]
        })

    