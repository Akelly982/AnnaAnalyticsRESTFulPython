# AnnaAnalyticsRESTFulPython
 


Installation:

Open a cmd terminal on your computer and make sure you have python framework installed
#CMD   python --version

"I am using python 3.9.6"
https://www.python.org/downloads/
If you do not have python installed you may need to download it.
The version I am using is "3.9.6" but any newer version than mine should work but however keep in mind if you use a different version. 

Then...
start a new termianl pointing at AnnaAnalyticsRESTFulPython Folder 
I use the Visual Studio Code CMD terminal with the project open.

--------
#CMD's
1)  
py -3 -m venv venv
venv\Scripts\activate

2)
pip install Flask torchvision

3)
pip install -U flask-cors

4) 
flask run
--------


If their are these warning...

1)
// WARNING: You are using pip version 21.1.3; however, version 21.2.4 is available.
// You should consider upgrading via the 'c:\users\akell\desktop\repo\annaanalyticsrestfulpython\venv\scripts\python.exe -m pip install --upgrade pip' command.

1Response)
Dont worry about it works fine with the older version


2)
    If it ask for you to change the workspace environment

2Response)
    click "no"
    this is a VSCode thing



-------
-------

When you run the "Flask run" CMD
 - It should launch so use the below URL to see if the server responeses in connection to the given endpoints.

C:\Users\xxxxx\xxxxx\xxxxx\AnnaAnalyticsRESTFulPython>flask run
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)


At this point the server should be up and running and it should be recognised by the GUI.


#####################################
 WARNING--PLEASE READ THIS LAST BIT
#####################################
Once up and running keep in mind your LocalHost destination here it really matters.. 
The AnnaAnalyticsGUI is setup to look for 
"http://127.0.0.1:5000/someEndPoint"


