from flask import Flask, jsonify, request, render_template
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


PROJECTNAME = "Anna Analytics RESTful Python"

# Home page

@app.route('/')
def hello(name='Anna Analytics'):    # def function this can be called anything
    return render_template('home.html', siteName=PROJECTNAME)

@app.route('/test')
def testing():
    return  render_template('input1A.html')


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

# check to see if the data is implemented
def getInputData(childId):
    switcher = {
        '1A' : input1A,
        '1B' : input1B,
        '1C' : input1C,
    }
    func = switcher.get(childId, inputDefault)
    return func()


def input1A():
    return  jsonify({
        'isSuccessfull': True,
        'htmlString': render_template('input1A.html'),
        'jsScript' : render_template('input1A.js'),
    })

def input1B():
    return  jsonify({
        'isSuccessfull': True,
        'htmlString': render_template('input1B.html'),
        'jsScript' : render_template('input1B.js'),
    })

def input1C():
    return  jsonify({
        'isSuccessfull': True,
        'htmlString': render_template('input1C.html'),
        'jsScript' : render_template('input1C.js'),
    })


def inputDefault():
    return jsonify({
        'isSuccessfull': True,
        'htmlString': render_template('inputDefault.html'),
        'jsScript' : " ",
    })




# None is null for python
# here we use the FLASK request object to get our POST methods
@app.route('/itemInput', methods=['POST'])
def itemInput():
    if request.method == "POST":
        if(request.form["childId"] != None):         
            
            # get recieved data from the POST request 
            # parentId = request.form["parentId"];
            childId = request.form["childId"];

            # using switcher stmt  (an improv switch stmt)
            # return the resulting function result html
            funcResult = getInputData(childId)
            return funcResult;
        else:
            return jsonify({
                'isSuccessfull' : False,
                'errorMsg' : 'request data missing for input item Request'
            })











#------- Output -------------------------------
#----------------------------------------------

# outputs are handled individually because they all require diffrent inputs over POST / GET
# i dont worry about child id here as the previous form should identify the route to use 

# here we use the FLASK request object to get our POST methods
@app.route('/itemOutput1A', methods=['POST'])
def itemOutput1A():
    if request.method == "POST":
        if(request.form["x"] != None or request.form['y'] == None):         
            # data validation should be done by the submitting form before sending over HTTP
            # get the inputs 
            num1 = request.form['x']
            num2 = request.form['y']

            #calculate 
            result = int(num1) + int(num2)

            #setup for transfer back to gui
            return jsonify({
                'isSuccessfull' : True,
                'htmlString' : render_template('output1A.html', value=result)
            })

        else:
            return jsonify({
                'isSuccessfull' : False,
                'htmlString' : render_template('outputDataMissing.html')
            })



@app.route('/itemOutput1B', methods=['POST'])
def itemOutput1B():
    if request.method == "POST":
        if(request.form["x"] != None or request.form['y'] == None):         
            # data validation should be done by the submitting form before sending over HTTP
            # get the inputs 
            num1 = request.form['x']
            num2 = request.form['y']

            #calculate 
            result = int(num1) - int(num2)

            #setup for transfer back to gui
            return jsonify({
                'isSuccessfull' : True,
                'htmlString' : render_template('output1B.html', value=result)
            })

        else:
            return jsonify({
                'isSuccessfull' : False,
                'htmlString' : render_template('outputDataMissing.html')
            })


@app.route('/itemOutput1C', methods=['POST'])
def itemOutput1C():
    if request.method == "POST":
        if(request.form["x"] != None or request.form['y'] == None):         
            # data validation should be done by the submitting form before sending over HTTP
            # get the inputs 
            num1 = request.form['x']
            num2 = request.form['y']

            #calculate 
            result = int(num1) * int(num2)

            #setup for transfer back to gui
            return jsonify({
                'isSuccessfull' : True,
                'htmlString' : render_template('output1C.html', value=result)
            })

        else:
            return jsonify({
                'isSuccessfull' : False,
                'htmlString' : render_template('outputDataMissing.html')
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
        