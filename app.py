from flask import Flask, jsonify, request
from flask_cors import CORS





app = Flask(__name__)
CORS(app)




@app.route('/')
def hello():    # def function this can be called anything
    return 'Hello World! I am currently running'



#-------Navigation ---------------------------
#---------------------------------------------

@app.route('/navBtn', methods=['POST','GET'])
def navFunc():
    if request.method == "POST" or request.method == "GET":
        return jsonify({
            'isSuccessfull': True,
            'errorMsg' : 'none', 
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
        



#------- Input -------------------------------
#---------------------------------------------


def getInputData(childId):
    switcher = {
        '1A' : input1A
    }
    func = switcher.get(childId, inputDefault)
    return func()


def input1A():
    return jsonify({
        'isSuccessfull' : True,
        'whoAmI' : 'Input1A',
        'errorMsg' : 'none',
        'dataArr' : [{'inputId' : 'labelNumeric' , 'inputItemData': [{'labelName': 'myFirstLabel', 'labelHint': "integer"}]},
                    {'inputId' : 'labelNumeric' , 'inputItemData': [{'labelName': 'mySecondLabel', 'labelHint': "2nd integer"}]}
        ],
    })

def inputDefault():
    return jsonify({
        'isSuccessfull' : False,
        'whoAmI' : 'Input Default',
        'errorMsg' : 'The Function you are looking for does not exist please try again or talk to a supervisor of this software..'
    })




# None is null for python
# here we use the FLASK request object to get our POST methods
@app.route('/itemInput', methods=['POST'])
def itemInput():
    if request.method == "POST":
        if(request.form["parentId"] !=  None and request.form["childId"] != None):         
            # relay received data back to user 
            parentId = request.form["parentId"];
            childId = request.form["childId"];

            # using switcher stmt  (an improv switch stmt)
            # return the resulting function result
            funcResult = getInputData(childId)
            return funcResult;




        else:
            return jsonify({
                'isSuccessfull' : False,
                'errorMsg' : 'request data missing for itemRequestWithData'
            })











#------- Output -------------------------------
#----------------------------------------------







@app.route('/itemInput', methods=['POST','GET'])
def itemOutput():
    if request.method == "POST" or request.method == "GET":
        return jsonify({
            'isSuccessfull': True,
            'errorMsg' : 'none',
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

    





#----- TESTING -----------------------------------------------------------------------
#-------------------------------------------------------------------------------------


#Testing data transfer and receving with method POST
# None is Null for pythong
# https://flask.palletsprojects.com/en/2.0.x/quickstart/
# The Request Object ---->  request.form['xxx'] ---> is what we are looking at here
#          
@app.route('/itemInputTest1', methods=['POST'])
def itemRequestWithData():
    if request.method == "POST":
        if(request.form["parentId"] !=  None and request.form["childId"] != None):        
            # relay received data back to user 
            parentId = request.form["parentId"];
            childId = request.form["childId"];
            return jsonify({
                'isSuccessfull' : True,
                'errorMsg' : 'none',
                'message' : 'parentId = ' + parentId + " / childId = " + childId
                
            })
        else:
            return jsonify({
                'isSuccessfull' : False,
                'errorMsg' : 'request data missing for itemRequestWithData'
            })
        