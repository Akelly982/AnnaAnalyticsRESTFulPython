# AnnaAnalyticsRESTFulPython

## Installation:
### Firstly external to our software:
Open a cmd terminal on your computer and make sure you have python framework installed
```bash
python --version
```

"I am using python version 3.9.6"

If you dont have it installed use the [python website](https://www.python.org/downloads/) to download and install the python framework.

The version I am using is "3.9.6" but any newer version than mine should work but however keep in mind if you use a different version. 

<br>

### Second with our software:

You can place this folder where ever you want mine is in my "repo" / "repositories" folder on my desktop because it comes from Github but that is up to you. 

Start a new termianl pointing at AnnaAnalyticsRESTFulPython Folder 
I use the Visual Studio Code CMD terminal with the project open.

---
# Installation CMD's
 
1)
```bash
py -3 -m venv venv
venv\Scripts\activate
```
2)
```bash
pip install Flask torchvision
```

3)
```bash
pip install -U flask-cors
```

4) 
```bash
flask run
```

---

When you run the "Flask run" CMD
 - It should launch the server.
 - When this happens it should print out the below dialog to the terminal you are using. use the link to it displays to quickly access the homepage and ensure it is running 

```python
C:\Users\xxxxx\xxxxx\xxxxx\AnnaAnalyticsRESTFulPython>flask run
Environment: production
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
Debug mode: off
Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

At this point the server should be up and running and it should be recognised by the GUI when requested.


<br>

## WARNING--PLEASE READ THIS BIT
Once up and running keep in mind your LocalHost destination here it really matters.. 
The AnnaAnalyticsGUI is setup to look for 
"http://127.0.0.1:5000/someEndPoint"


# Last bit of installation
once the above works ensure you install scikit for the sklearn linear regression
[scikit site install section](https://scikit-learn.org/stable/install.html )
If Flask is now running close it down in the cmd console using "(Press CTRL+C to quit)" just in case this makes a difference but we will need it sort of to install to the venv environment.

Again scikit / sklearn requires python check with 
```bash
python --version
```

Potential conflicts <br>
In order to avoid potential conflicts with other packages it is strongly recommended to use a virtual environment (venv) or a conda environment.
NOTE: The above venv was installed when setting up our flask environment

<br>

install scikit / sklearn <br>
    // (venv) C:\Users\XxXxXx\xXXxxXXxx\repo\AnnaAnalyticsRESTFulPython>  <-- you need to lauch the virtural environment venv then run the CMD <br>
    // otherwise it just installs to you machine as a whole <br>
    // To get this to happen I lauched flask and opened a new command line within VSCode <br>
```bash
pip install -U scikit-learn
```

AKNote when ran installs below packages    (notice joblib) <br>
    //threadpoolctl, scipy, joblib, scikit-learn

To check installation of scikit went correctly <br>
CMD#  To see which version and where scikit-learn is installed
```bash
python -m pip show scikit-learn 
```

CMD# To see all packages installed in the active virtualenv   
```bash
python -m pip freeze
```

CMD#      
```bash
python -c "import sklearn; sklearn.show_versions()"
```



---

## Installation Errors with internall software CMDS

1 Error: <br>
// WARNING: You are using pip version 21.1.3; however, version 21.2.4 is available.
// You should consider upgrading via the 'c:\users\akell\desktop\repo\annaanalyticsrestfulpython\venv\scripts\python.exe -m pip install --upgrade pip' command.

<br>

1 Response:  <br>
Dont worry about it works fine with the older version


---

2 Error:  <br>
    If it ask for you to change the workspace environment
    
<br>

2 Response:  <br>
click "no"
this is some Venv / VSCode thing I didnt worry about it..





<!-- ---

### Copyrights: 

I should write somthing here 

-->


---

### Moral Rights:

I would like to acknowlege external code used within this project and their comprehensive documentation
1. [Flask](https://flask.palletsprojects.com/en/2.0.x/)
2. [python](https://www.python.org/)
3. [scikit-learn](https://scikit-learn.org/stable/index.html)


Additionall references and Tutorials
1. [Avinash Sajjanshetty / Flask REST api tutorial](https://colab.research.google.com/github/pytorch/tutorials/blob/gh-pages/_downloads/6c042f3d39855d2a2de414758e5f9836/flask_rest_api_tutorial.ipynb)


AIT Teachers/Supervisors:
1. Kriss Mahatumaratana


---

### Contributors:

Aidan Kelly
