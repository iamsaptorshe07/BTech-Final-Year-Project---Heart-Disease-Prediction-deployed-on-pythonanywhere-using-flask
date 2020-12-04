from flask import Flask, render_template,request,redirect,url_for,flash
app = Flask(__name__)
import pickle
file = open('model.pkl', 'rb')
clf = pickle.load(file)
file.close()
app.secret_key='don\'t tell anyone'
@app.route('/', methods=["GET","POST"])
def main_page():
    return render_template('index.html')
@app.route('/test', methods=["GET","POST"])
def test_page():
    if request.method == "POST":
        age = request.form.get('age')
        sex = int(request.form.get('sex'))
        cp = int(request.form.get('cp'))
        trestbps = request.form.get('trestbps')
        chol = request.form.get('chol')
        fbs = int(request.form.get('fbs'))
        restecg = int(request.form.get('fbs'))
        thalach = request.form.get('thalach')
        exang = int(request.form.get('exang'))
        oldpeak = int(request.form.get('exang'))
        slope = int(request.form.get('exang'))
        ca = request.form.get('ca')
        thal = int(request.form.get('thal'))
        inputFeatures = [age,sex,cp,trestbps,chol, fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        print("Worked")
        infProb = clf.predict([inputFeatures])
        print(infProb)
        if infProb==[1]:
            s = "You may have problem in your heart! Please go through the links below!"
            return render_template('result.html',inf=s)
        elif infProb==[0]:
            s = "Cogratulations! You don't have any heart problem...\nBut if you feal seek than check out the links below!"
            return render_template('result.html', inf=s)
    else:
    	return render_template('SAT.html')
@app.route('/about', methods=["GET","POST"])
def about_page():
    return render_template('about.html')
@app.route('/helpline', methods=["GET","POST"])
def helpline_page():
    return render_template('helpline.html')


if __name__ == "__main__":
    app.run(debug = True)