from flask import Flask, request, jsonify, render_template, send_file
import joblib
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import io
import os


app = Flask(__name__)


# Font paths
FONT_DIR = os.path.join(os.path.dirname(__file__), "fonts")

pdfmetrics.registerFont(
    TTFont(
        "NotoSans",
        os.path.join(FONT_DIR, "NotoSans-Regular.ttf")
    )
)

pdfmetrics.registerFont(
    TTFont(
        "NotoSansTelugu",
        os.path.join(FONT_DIR, "NotoSansTelugu-Regular.ttf")
    )
)

pdfmetrics.registerFont(
    TTFont(
        "NotoSansDevanagari",
        os.path.join(FONT_DIR, "NotoSansDevanagari-Regular.ttf")
    )
)

pdfmetrics.registerFont(
    TTFont(
        "NotoSansTamil",
        os.path.join(FONT_DIR, "NotoSansTamil-Regular.ttf")
    )
)


model = joblib.load("fetal_health_model.pkl")


# =========================================================
# REGISTER FONTS
# =========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FONT_DIR = os.path.join(BASE_DIR, "fonts")


pdfmetrics.registerFont(
    TTFont(
        "EnglishFont",
        os.path.join(FONT_DIR, "NotoSans-Regular.ttf")
    )
)

pdfmetrics.registerFont(
    TTFont(
        "TeluguFont",
        os.path.join(FONT_DIR, "NotoSansTelugu-Regular.ttf")
    )
)

pdfmetrics.registerFont(
    TTFont(
        "HindiFont",
        os.path.join(FONT_DIR, "NotoSansDevanagari-Regular.ttf")
    )
)

pdfmetrics.registerFont(
    TTFont(
        "TamilFont",
        os.path.join(FONT_DIR, "NotoSansTamil-Regular.ttf")
    )
)


# =========================================================
# TRANSLATIONS
# =========================================================

REPORT_TRANSLATIONS = {

    "en": {

        "title": "Fetal Health Analysis Report",

        "prediction": "Prediction",

        "class": "Class",

        "confidence": "Model Confidence",

        "probabilities": "Class Probabilities",

        "normal": "Normal",

        "suspect": "Suspect",

        "pathological": "Pathological",

        "ctg_values": "CTG Input Values",

        "disclaimer":
            "For educational/research purposes. Not a medical diagnosis.",

        "features": [

            "Baseline Value",
            "Accelerations",
            "Fetal Movement",
            "Uterine Contractions",
            "Light Decelerations",
            "Severe Decelerations",
            "Prolongued Decelerations",
            "Abnormal Short Term Variability",
            "Mean Value Short Term Variability",
            "Percentage Abnormal Long Term Variability",
            "Mean Value Long Term Variability",
            "Histogram Width",
            "Histogram Min",
            "Histogram Max",
            "Histogram Number of Peaks",
            "Histogram Number of Zeroes",
            "Histogram Mode",
            "Histogram Mean",
            "Histogram Median",
            "Histogram Variance",
            "Histogram Tendency"

        ]
    },


    "te": {

        "title": "పిండం ఆరోగ్య విశ్లేషణ నివేదిక",

        "prediction": "ఫలితం",

        "class": "తరగతి",

        "confidence": "మోడల్ విశ్వసనీయత",

        "probabilities": "తరగతుల సంభావ్యతలు",

        "normal": "సాధారణం",

        "suspect": "అనుమానాస్పదం",

        "pathological": "అసాధారణం",

        "ctg_values": "CTG ఇన్‌పుట్ విలువలు",

        "disclaimer":
            "విద్యా/పరిశోధన ప్రయోజనాల కోసం మాత్రమే. ఇది వైద్య నిర్ధారణ కాదు.",

        "features": [

            "ప్రాథమిక విలువ",
            "త్వరణాలు",
            "పిండం కదలిక",
            "గర్భాశయ సంకోచాలు",
            "తేలికపాటి డీసెలరేషన్లు",
            "తీవ్రమైన డీసెలరేషన్లు",
            "దీర్ఘకాలిక డీసెలరేషన్లు",
            "అసాధారణ స్వల్పకాలిక మార్పు",
            "స్వల్పకాలిక మార్పు సగటు విలువ",
            "అసాధారణ దీర్ఘకాలిక మార్పు శాతం",
            "దీర్ఘకాలిక మార్పు సగటు విలువ",
            "హిస్టోగ్రామ్ వెడల్పు",
            "హిస్టోగ్రామ్ కనిష్టం",
            "హిస్టోగ్రామ్ గరిష్టం",
            "హిస్టోగ్రామ్ శిఖరాల సంఖ్య",
            "హిస్టోగ్రామ్ సున్నాల సంఖ్య",
            "హిస్టోగ్రామ్ మోడ్",
            "హిస్టోగ్రామ్ సగటు",
            "హిస్టోగ్రామ్ మధ్యస్థం",
            "హిస్టోగ్రామ్ వ్యత్యాసం",
            "హిస్టోగ్రామ్ ధోరణి"

        ]
    },


    "hi": {

        "title": "भ्रूण स्वास्थ्य विश्लेषण रिपोर्ट",

        "prediction": "पूर्वानुमान",

        "class": "श्रेणी",

        "confidence": "मॉडल विश्वसनीयता",

        "probabilities": "श्रेणी संभावनाएँ",

        "normal": "सामान्य",

        "suspect": "संदिग्ध",

        "pathological": "असामान्य",

        "ctg_values": "CTG इनपुट मान",

        "disclaimer":
            "केवल शैक्षिक/अनुसंधान उद्देश्यों के लिए। यह चिकित्सीय निदान नहीं है।",

        "features": [

            "बेसलाइन मान",
            "त्वरण",
            "भ्रूण की गतिविधि",
            "गर्भाशय संकुचन",
            "हल्का डीसेलेरेशन",
            "गंभीर डीसेलेरेशन",
            "लंबा डीसेलेरेशन",
            "असामान्य अल्पकालिक परिवर्तनशीलता",
            "अल्पकालिक परिवर्तनशीलता का औसत मान",
            "असामान्य दीर्घकालिक परिवर्तनशीलता का प्रतिशत",
            "दीर्घकालिक परिवर्तनशीलता का औसत मान",
            "हिस्टोग्राम चौड़ाई",
            "हिस्टोग्राम न्यूनतम",
            "हिस्टोग्राम अधिकतम",
            "हिस्टोग्राम पीक की संख्या",
            "हिस्टोग्राम शून्य की संख्या",
            "हिस्टोग्राम मोड",
            "हिस्टोग्राम माध्य",
            "हिस्टोग्राम माध्यिका",
            "हिस्टोग्राम विचरण",
            "हिस्टोग्राम प्रवृत्ति"

        ]
    },


    "ta": {

        "title": "கருவின் ஆரோக்கிய பகுப்பாய்வு அறிக்கை",

        "prediction": "முடிவு",

        "class": "வகுப்பு",

        "confidence": "மாதிரி நம்பகத்தன்மை",

        "probabilities": "வகுப்பு நிகழ்தகவுகள்",

        "normal": "இயல்பானது",

        "suspect": "சந்தேகத்திற்குரியது",

        "pathological": "அசாதாரணமானது",

        "ctg_values": "CTG உள்ளீட்டு மதிப்புகள்",

        "disclaimer":
            "கல்வி/ஆராய்ச்சி நோக்கங்களுக்காக மட்டும். இது மருத்துவ நோயறிதல் அல்ல.",

        "features": [

            "அடிப்படை மதிப்பு",
            "முடுக்கங்கள்",
            "கருவின் இயக்கம்",
            "கருப்பை சுருக்கங்கள்",
            "லேசான குறைவுகள்",
            "கடுமையான குறைவுகள்",
            "நீடித்த குறைவுகள்",
            "அசாதாரண குறுகிய கால மாறுபாடு",
            "குறுகிய கால மாறுபாட்டின் சராசரி மதிப்பு",
            "அசாதாரண நீண்ட கால மாறுபாட்டின் சதவீதம்",
            "நீண்ட கால மாறுபாட்டின் சராசரி மதிப்பு",
            "ஹிஸ்டோகிராம் அகலம்",
            "ஹிஸ்டோகிராம் குறைந்தபட்சம்",
            "ஹிஸ்டோகிராம் அதிகபட்சம்",
            "ஹிஸ்டோகிராம் உச்சங்களின் எண்ணிக்கை",
            "ஹிஸ்டோகிராம் பூஜ்ஜியங்களின் எண்ணிக்கை",
            "ஹிஸ்டோகிராம் பயன்முறை",
            "ஹிஸ்டோகிராம் சராசரி",
            "ஹிஸ்டோகிராம் இடைநிலை",
            "ஹிஸ்டோகிராம் மாறுபாடு",
            "ஹிஸ்டோகிராம் போக்கு"

        ]
    }

}


# =========================================================
# HOME PAGE
# =========================================================

@app.route("/")
def home():

    return render_template("index.html")


# =========================================================
# PREDICTION
# =========================================================

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    features = data["features"]


    if len(features) != 21:

        return jsonify({

            "error":
                "Exactly 21 CTG features are required"

        }), 400


    prediction = model.predict([features])[0]

    prediction = int(prediction) + 1


    if prediction == 1:

        result = "Normal"

    elif prediction == 2:

        result = "Suspect"

    else:

        result = "Pathological"


    probabilities = model.predict_proba([features])[0]

    confidence = float(max(probabilities)) * 100


    return jsonify({

        "prediction": prediction,

        "result": result,

        "confidence": round(confidence, 2),

        "probabilities": {

            "Normal":
                round(
                    float(probabilities[0]) * 100,
                    2
                ),

            "Suspect":
                round(
                    float(probabilities[1]) * 100,
                    2
                ),

            "Pathological":
                round(
                    float(probabilities[2]) * 100,
                    2
                )

        }

    })


# =========================================================
# DOWNLOAD REPORT
# =========================================================

@app.route("/download-report", methods=["POST"])
def download_report():

    data = request.json


    result = data["result"]

    prediction = data["prediction"]

    confidence = data["confidence"]

    probabilities = data["probabilities"]

    features = data["features"]


    # Get selected language

    language = data.get("language", "en")


    # Get translation dictionary

    text = REPORT_TRANSLATIONS.get(

        language,

        REPORT_TRANSLATIONS["en"]

    )


    # =====================================================
    # TRANSLATE PREDICTION RESULT
    # =====================================================

    if result == "Normal":

        translated_result = text["normal"]

    elif result == "Suspect":

        translated_result = text["suspect"]

    else:

        translated_result = text["pathological"]


    # =====================================================
    # CREATE PDF
    # =====================================================

    buffer = io.BytesIO()

    pdf = canvas.Canvas(

        buffer,

        pagesize=A4

    )


    width, height = A4


    # =====================================================
    # SELECT FONT
    # =====================================================

    if language == "te":

        font_name = "TeluguFont"

    elif language == "hi":

        font_name = "HindiFont"

    elif language == "ta":

        font_name = "TamilFont"

    else:

        font_name = "EnglishFont"


    # =====================================================
    # TITLE
    # =====================================================

    pdf.setFont(

        font_name,

        20

    )


    pdf.drawCentredString(

        width / 2,

        height - 50,

        text["title"]

    )


    # =====================================================
    # BASIC RESULT INFORMATION
    # =====================================================

    pdf.setFont(

        font_name,

        12

    )


    y = height - 100


    pdf.drawString(

        50,

        y,

        f"{text['prediction']}: {translated_result}"

    )


    y -= 25


    pdf.drawString(

        50,

        y,

        f"{text['class']}: {prediction}"

    )


    y -= 25


    pdf.drawString(

        50,

        y,

        f"{text['confidence']}: {confidence}%"

    )


    y -= 40


    # =====================================================
    # CLASS PROBABILITIES
    # =====================================================

    pdf.setFont(

        font_name,

        14

    )


    pdf.drawString(

        50,

        y,

        text["probabilities"]

    )


    y -= 25


    pdf.setFont(

        font_name,

        12

    )


    pdf.drawString(

        50,

        y,

        f"{text['normal']}: {probabilities['Normal']}%"

    )


    y -= 20


    pdf.drawString(

        50,

        y,

        f"{text['suspect']}: {probabilities['Suspect']}%"

    )


    y -= 20


    pdf.drawString(

        50,

        y,

        f"{text['pathological']}: {probabilities['Pathological']}%"

    )


    y -= 40


    # =====================================================
    # CTG INPUT VALUES
    # =====================================================

    pdf.setFont(

        font_name,

        14

    )


    pdf.drawString(

        50,

        y,

        text["ctg_values"]

    )


    y -= 25


    pdf.setFont(

        font_name,

        10

    )


    # =====================================================
    # FEATURE VALUES
    # =====================================================

    for name, value in zip(

        text["features"],

        features

    ):

        pdf.drawString(

            50,

            y,

            f"{name}: {value}"

        )


        y -= 15


        if y < 50:

            pdf.showPage()


            pdf.setFont(

                font_name,

                10

            )


            y = height - 50


    # =====================================================
    # DISCLAIMER
    # =====================================================

    pdf.setFont(

        font_name,

        9

    )


    pdf.drawString(

        50,

        30,

        text["disclaimer"]

    )


    # =====================================================
    # SAVE PDF
    # =====================================================

    pdf.save()


    buffer.seek(0)


    return send_file(

        buffer,

        as_attachment=True,

        download_name="fetal_health_report.pdf",

        mimetype="application/pdf"

    )


# =========================================================
# VISUALIZATIONS
# =========================================================

@app.route("/visualizations")
def visualizations():

    return render_template(

        "visualizations.html"

    )


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":

    app.run(debug=True)