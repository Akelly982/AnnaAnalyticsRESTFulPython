from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import json
import numpy as np

# we are not training data here so we just set up pretrained Linear models
from sklearn import linear_model


app = Flask(__name__)
CORS(app)


PROJECTNAME = "Anna Analytics RESTful Python"

# Home page
@app.route('/')
def hello(name='Anna Analytics'):    # def function this can be called anything
    return render_template('home.html', siteName=PROJECTNAME)



#===============================================================
#==== functions / inline code / runs in console ================


#Note why we are going to use JSON for DataModel Persistence
# https://scikit-learn.org/stable/modules/model_persistence.html#security-maintainability-limitations
# Essentially Joblib and Pickle allow for code injection if unpickled code is untrusted
# here this should not be the case but to be safe we will use JSON data model persistence

#parentFolder
PARENTDIR = "dataModels/"

#Model DIR 
DIR_APM1_ASSESMENT_MODEL = 'JsonAPM1AssesmentModel.txt'
DIR_ASSIGNMENT_PREDICTION_MODEL_2 = 'JsonAssignmentPredictionModel_2.txt'


#Setup Models
# ------------------------------------------------------------
# ----------- APM1_ASSESMENT_MODEL ---------------------------
#Get persitant model data
with open(PARENTDIR + DIR_APM1_ASSESMENT_MODEL,'r') as file:
  tempJson = json.load(file)

#Create a LinearRegression Model
APM1model = linear_model.LinearRegression()

#fill the new linear model with our pretrained data 
    #important to !!Note!! 
    # tempJson == Dictionairy
        # tempJson['coef'] has data type of list and needs to be converted to a ndarray
        # tempJson['intercept'] has data type of list and needs to be converted to a ndarray
            # ndArray is numpy array / n-dimensional array
APM1model.coef_ = np.array(tempJson['coef']) 
APM1model.intercept_ = np.array(tempJson['intercept'])


#create function for using the model againts externall input's x,y,z.....
#  ["assignment1Score"]
def APM1_AssesmentModel(assignment1Score):
    #convert to be in a 2d array
    x = np.array([[assignment1Score]]) 
    
    #submit to model to get result
    #returned result should be of 2d array as well
    predictionResult = APM1model.predict(x)
    #since it is one field we can cast int

    return int(predictionResult)



# ------------------------------------------------------------
# ----------- ASSIGNMENT_PREDICTION_MODEL_2 ---------------------------
#Get persitant model data
with open(PARENTDIR + DIR_ASSIGNMENT_PREDICTION_MODEL_2,'r') as file:
  tempJson = json.load(file)

#Create a LinearRegression Model
modelAPM2 = linear_model.LinearRegression()

#fill the new linear model with our pretrained data 
    #important to !!Note!! 
    # tempJson == Dictionairy
        # tempJson['coef'] has data type of list and needs to be converted to a ndarray
        # tempJson['intercept'] has data type of list and needs to be converted to a ndarray
            # ndArray is numpy array / n-dimensional array
modelAPM2.coef_ = np.array(tempJson['coef']) 
modelAPM2.intercept_ = np.array(tempJson['intercept'])


#create function for using the model againts externall input's x,y,z.....
# ['isMale', 'rank_highest_education', 'scoreAss_25334', 'scoreAss_25335', 'scoreAss_25336', 'scoreAss_25337', 'scoreAss_25338', 'scoreAss_25339']
def APM2_AssesmentModel(isMale, rank_highest_education, scoreAss_25334, scoreAss_25335, scoreAss_25336, scoreAss_25337, scoreAss_25338, scoreAss_25339):
    #convert to be in a 2d array
    x = np.array([[isMale, rank_highest_education, scoreAss_25334, scoreAss_25335, scoreAss_25336, scoreAss_25337, scoreAss_25338, scoreAss_25339]]) 
    
    #submit to model to get result
    #returned result should be of 2d array as well
    predictionResult = modelAPM2.predict(x)
    #since it is one field we can cast int
    return int(predictionResult)


# ------------------------------------------------------------
# ------------------------------------------------------------













#===============================================================
#==== EndPoints ================================================

@app.route('/testJson')
def testing():
    predResult = APM2_AssesmentModel(1,4,77,66,55,88,66,77)
    return jsonify({
        'modelResult': predResult
    }) 


#------- isAlive / flask running ---------------------------
#---------------------------------------------

@app.route('/isAlive', methods=['POST','GET'])
def isAlive():
    if request.method == "POST" or request.method == "GET":
        return jsonify({
            'isSuccessfull': True,
            'data': "I am Flask and I am alive communicate with me..",
            'errorMsg' : 'none' 
        })
        

#------- Outputs -------------------------------
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




# outputAssignmentPredictMach1.html
@app.route('/assigmentPredictMach1', methods=['POST'])
def assigmentPredictMach1():
    if request.method == "POST":
        if(request.form["x"] != None):          
            # data validation should be done by the submitting form before sending over HTTP
            # get the inputs 
            num = request.form['x']     #assignment 1 score 

            #run against persistent AI 
            result = APM1_AssesmentModel(num)

            #setup for transfer back to gui
            return jsonify({
                'isSuccessfull' : True,
                'htmlString' : render_template('outputAssignmentPredictMach1.html', value=result)
            })
        else:
            return jsonify({
                'isSuccessfull' : False,
                'htmlString' : render_template('outputDataMissing.html')
            })



# def APM2_AssesmentModel(isMale, rank_highest_education, scoreAss_25334, scoreAss_25335, scoreAss_25336, scoreAss_25337, scoreAss_25338, scoreAss_25339):
# outputAssignmentPredictMach2.html
@app.route('/assigmentPredictMach2', methods=['POST'])
def assigmentPredictMach2():
    if request.method == "POST":
        if(request.form["isMale"] != None and 
            request.form["rank_highest_education"] != None and 
            request.form["scoreAss_25334"] != None and
            request.form["scoreAss_25335"] != None and
            request.form["scoreAss_25336"] != None and
            request.form["scoreAss_25337"] != None and         
            request.form["scoreAss_25338"] != None and
            request.form["scoreAss_25339"] != None):

            # data validation should be done by the submitting form before sending over HTTP
            # get the inputs 
            isMale = request.form['isMale']
            rank_highest_education = request.form['rank_highest_education'] 
            scoreAss_25334 = request.form['scoreAss_25334'] 
            scoreAss_25335 = request.form['scoreAss_25335']  
            scoreAss_25336 = request.form['scoreAss_25336'] 
            scoreAss_25337 = request.form['scoreAss_25337'] 
            scoreAss_25338 = request.form['scoreAss_25338'] 
            scoreAss_25339 = request.form['scoreAss_25339'] 

            #run against persistent AI 
            result = APM2_AssesmentModel(isMale, rank_highest_education, scoreAss_25334, scoreAss_25335, scoreAss_25336, scoreAss_25337, scoreAss_25338, scoreAss_25339)

            #setup for transfer back to gui
            return jsonify({
                'isSuccessfull' : True,
                'htmlString' : render_template('outputAssignmentPredictMach2.html', value=result)
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
        