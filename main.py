from flask import Flask, render_template,request 

app = Flask(__name__)

@app.get("/")
def showPage():
    return render_template('index.html')

@app.post('/analyze')
def analyze():
    text = request.form['text']
    action = request.form['action']
    answer = ""
    if(action == "cntchr"):
        answer = f"The number of characters are:-{len(text)}"
    if(action == "cntws"):
        answer  = f"The number of white spaces are:-{text.count(' ')}" 
    if(action == "ctuc"):
        answer = f"The upper case of given string is:-{text.upper()}"
    if(action == "ctlc"):
        answer = f"The lower case of given string is:-{text.lower()}"
    if(action == "cotgs"):
        answer = f"The capitalizetion of given string is:-{text.capitalize()}"
    if(action == "sogs"):
        answer = f"The spliting of given string is:-{text.split()}"  
    if(action == "utlltu"):
        answer = f"The swapcase of given string is:-{text.swapcase()}" 
    if(action == "etgsuw"):
        answer = f"The result of given string is:-{text.strip()}"
    if(action == "ctgsiilot"):
        answer = f"The result is:-{text.islower()}"
    if(action == "ctgsiiuot"):
        answer = f"The result is:-{text.isupper()}"
    if(action == "ctgsint"):
        answer = f"The result is:-{text.isnumeric()}"                                        
    return render_template('index.html',output = answer)
