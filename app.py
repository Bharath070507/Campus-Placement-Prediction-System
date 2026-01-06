from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load trained model and scaler
classifier = pickle.load(open("classifier.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # -------- Numerical Inputs --------
        ssc_p = float(request.form["ssc_p"])
        hsc_p = float(request.form["hsc_p"])
        degree_p = float(request.form["degree_p"])
        etest_p = float(request.form["etest_p"])
        mba_p = float(request.form["mba_p"])
        projects = int(request.form["projects"])
        certification = int(request.form["certification"])

        # -------- Binary / Categorical Inputs --------
        gender_M = 1 if request.form["gender"] == "1" else 0
        workex_Yes = 1 if request.form["workex"] == "1" else 0
        ssc_b_Others = 1 if request.form["ssc_b"] == "1" else 0
        hsc_b_Others = 1 if request.form["hsc_b"] == "1" else 0

        # HSC Stream
        hsc_s = request.form["hsc_s"]
        hsc_s_Commerce = 1 if hsc_s == "Commerce" else 0
        hsc_s_Science = 1 if hsc_s == "Science" else 0

        # Degree Type
        degree_t = request.form["degree_t"]
        degree_t_Others = 1 if degree_t == "Others" else 0
        degree_t_SciTech = 1 if degree_t == "Sci&Tech" else 0

        # MBA Specialisation
        specialisation = request.form["specialisation"]
        specialisation_MktHR = 1 if specialisation == "Mkt&HR" else 0

        # -------- FINAL FEATURE VECTOR (16 FEATURES) --------
        features = np.array([[ 
            ssc_p, hsc_p, degree_p, etest_p, mba_p,
            projects, certification,
            gender_M, ssc_b_Others, hsc_b_Others,
            hsc_s_Commerce, hsc_s_Science,
            degree_t_Others, degree_t_SciTech,
            workex_Yes, specialisation_MktHR
        ]])

        # Scaling
        features_scaled = scaler.transform(features)

        # Prediction
        prediction = classifier.predict(features_scaled)
        result = "Placed ✅" if prediction[0] == 1 else "Not Placed ❌"

        return render_template("index.html", prediction=result)

    except Exception as e:
        return f"ERROR: {e}"

if __name__ == "__main__":
    app.run(debug=True)
