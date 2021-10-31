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
#CMD's
 
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

### WARNING--PLEASE READ THIS LAST BIT
Once up and running keep in mind your LocalHost destination here it really matters.. 
The AnnaAnalyticsGUI is setup to look for 
"http://127.0.0.1:5000/someEndPoint"



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
this is a VSCode thing
