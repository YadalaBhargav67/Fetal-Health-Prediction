const form = document.getElementById("predictionForm");

const result = document.getElementById("result");

const resultStatus = document.getElementById("resultStatus");

const confidence = document.getElementById("confidence");

const normalProbability =
    document.getElementById("normalProbability");

const suspectProbability =
    document.getElementById("suspectProbability");

const pathologicalProbability =
    document.getElementById("pathologicalProbability");

const resetButton =
    document.getElementById("resetButton");

const downloadButton =
    document.getElementById("downloadButton");



/*
    Get the 21 CTG values
*/

function getFeatures() {

    return [

        Number(document.getElementById("baseline_value").value),

        Number(document.getElementById("accelerations").value),

        Number(document.getElementById("fetal_movement").value),

        Number(document.getElementById("uterine_contractions").value),

        Number(document.getElementById("light_decelerations").value),

        Number(document.getElementById("severe_decelerations").value),

        Number(document.getElementById("prolongued_decelerations").value),

        Number(
            document.getElementById(
                "abnormal_short_term_variability"
            ).value
        ),

        Number(
            document.getElementById(
                "mean_value_of_short_term_variability"
            ).value
        ),

        Number(
            document.getElementById(
                "percentage_of_time_abnormal_long_term_variability"
            ).value
        ),

        Number(
            document.getElementById(
                "mean_value_of_long_term_variability"
            ).value
        ),

        Number(
            document.getElementById("histogram_width").value
        ),

        Number(
            document.getElementById("histogram_min").value
        ),

        Number(
            document.getElementById("histogram_max").value
        ),

        Number(
            document.getElementById(
                "histogram_number_of_peaks"
            ).value
        ),

        Number(
            document.getElementById(
                "histogram_number_of_zeroes"
            ).value
        ),

        Number(
            document.getElementById("histogram_mode").value
        ),

        Number(
            document.getElementById("histogram_mean").value
        ),

        Number(
            document.getElementById("histogram_median").value
        ),

        Number(
            document.getElementById("histogram_variance").value
        ),

        Number(
            document.getElementById("histogram_tendency").value
        )

    ];
}



/*
    Send CTG data to Flask
*/

form.addEventListener("submit", async function(event) {

    event.preventDefault();

    const features = getFeatures();


    try {

        const response = await fetch("/predict", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                features: features
            })

        });


        const data = await response.json();


        if (!response.ok) {

            alert(data.error || "Prediction failed.");

            return;

        }


        /*
            Display result
        */

        result.style.display = "block";

        resultStatus.textContent = data.result;

        confidence.textContent = data.confidence;

        normalProbability.textContent =
            data.probabilities.Normal + "%";

        suspectProbability.textContent =
            data.probabilities.Suspect + "%";

        pathologicalProbability.textContent =
            data.probabilities.Pathological + "%";


        /*
            Scroll to result
        */

        result.scrollIntoView({
            behavior: "smooth"
        });

    }


    catch (error) {

        console.error(error);

        alert("Unable to connect to the Flask server.");

    }

});



/*
    Reset form
*/

resetButton.addEventListener("click", function() {

    form.reset();

    result.style.display = "none";

});



/*
    Download report
*/

downloadButton.addEventListener("click", async function() {

    const features = getFeatures();

    const languageSelect =
        document.getElementById("languageSelect");

    const selectedLanguage =
        languageSelect ? languageSelect.value : "en";


    const reportData = {

        result: resultStatus.textContent,

        prediction:
            resultStatus.textContent === "Normal"
                ? 1
                : resultStatus.textContent === "Suspect"
                    ? 2
                    : 3,

        confidence: confidence.textContent,

        probabilities: {

            Normal:
                normalProbability.textContent.replace("%", ""),

            Suspect:
                suspectProbability.textContent.replace("%", ""),

            Pathological:
                pathologicalProbability.textContent.replace("%", "")
        },

        features: features,

        /*
            Selected report language
        */

        language: selectedLanguage

    };


    try {

        const response = await fetch(
            "/download-report",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(reportData)
            }
        );


        if (!response.ok) {

            alert("Unable to generate report.");

            return;
        }


        const blob = await response.blob();

        const url = URL.createObjectURL(blob);

        const link = document.createElement("a");

        link.href = url;

        link.download = "fetal_health_report.pdf";

        link.click();

        URL.revokeObjectURL(url);

    }


    catch (error) {

        console.error(error);

        alert("Error generating report.");

    }

});



/*
    Language Selection
*/

const languageSelect =
    document.getElementById("languageSelect");


const translations = {

    en: {

        title: "Fetal Health Prediction",

        language: "Language",

        predict: "Predict Fetal Health",

        download: "Download Report",

        visualizations: "View Model Visualizations",

        prediction: "Prediction",

        confidence: "Confidence",

        normal: "Normal",

        suspect: "Suspect",

        pathological: "Pathological"

    },


    te: {

        title: "పిండం ఆరోగ్య అంచనా",

        language: "భాష",

        predict: "పిండం ఆరోగ్యాన్ని అంచనా వేయండి",

        download: "నివేదికను డౌన్‌లోడ్ చేయండి",

        visualizations: "మోడల్ విజువలైజేషన్లను చూడండి",

        prediction: "ఫలితం",

        confidence: "విశ్వసనీయత",

        normal: "సాధారణం",

        suspect: "అనుమానాస్పదం",

        pathological: "అసాధారణం"

    },


    hi: {

        title: "भ्रूण स्वास्थ्य पूर्वानुमान",

        language: "भाषा",

        predict: "भ्रूण स्वास्थ्य की भविष्यवाणी करें",

        download: "रिपोर्ट डाउनलोड करें",

        visualizations: "मॉडल विज़ुअलाइज़ेशन देखें",

        prediction: "पूर्वानुमान",

        confidence: "विश्वसनीयता",

        normal: "सामान्य",

        suspect: "संदिग्ध",

        pathological: "असामान्य"

    },


    ta: {

        title: "கருவின் ஆரோக்கிய கணிப்பு",

        language: "மொழி",

        predict: "கருவின் ஆரோக்கியத்தை கணிக்கவும்",

        download: "அறிக்கையை பதிவிறக்கவும்",

        visualizations: "மாதிரி காட்சிப்படுத்தல்களைப் பார்க்கவும்",

        prediction: "முடிவு",

        confidence: "நம்பகத்தன்மை",

        normal: "இயல்பானது",

        suspect: "சந்தேகத்திற்குரியது",

        pathological: "அசாதாரணமானது"

    }

};



/*
    Change webpage language
*/

if (languageSelect) {

    languageSelect.addEventListener("change", function() {

        const selectedLanguage =
            languageSelect.value;

        const text =
            translations[selectedLanguage];


        /*
            Change page title
        */

        const title =
            document.querySelector("h1");

        if (title) {
            title.textContent = text.title;
        }


        /*
            Change language label
        */

        const languageLabel =
            document.querySelector(
                ".language-selector label"
            );

        if (languageLabel) {
            languageLabel.textContent =
                text.language + ":";
        }


        /*
            Change prediction button
        */

        const predictButton =
            document.querySelector(
                'button[type="submit"]'
            );

        if (predictButton) {
            predictButton.textContent =
                text.predict;
        }


        /*
            Change download button
        */

        if (downloadButton) {
            downloadButton.textContent =
                text.download;
        }


        /*
            Change visualization button
        */

        const visualizationButton =
            document.querySelector(
                ".visualization-button"
            );

        if (visualizationButton) {
            visualizationButton.textContent =
                text.visualizations;
        }

    });

}