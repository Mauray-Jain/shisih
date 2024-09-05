from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/feedback")
def contact():
    return render_template("feedback.html")

@app.route("/service")
def service():
    return render_template("service.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/dashboard", methods = ["GET", "POST"])
def dashboard():
    # res = None
    # model = pickle.load(open('classifier.pkl','rb'))
    # ferti = pickle.load(open('fertilizer.pkl','rb'))
    if request.method == "POST":
        return render_template("dashboard.html", x = "Fertiliser to use 14-35-14 in 20 kg per hectare")
    #     temp = request.form.get('temp')
    #     humi = request.form.get('humid')
    #     mois = request.form.get('mois')
    #     soil = request.form.get('soil')
    #     crop = request.form.get('crop')
    #     nitro = request.form.get('nitro')
    #     pota = request.form.get('pota')
    #     phosp = request.form.get('phos')
    #     input = [int(temp),int(humi),int(mois),int(soil),int(crop),int(nitro),int(pota),int(phosp)]
    #     res = ferti.classes_[model.predict([input])]
    else:
        return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(port=5000)
