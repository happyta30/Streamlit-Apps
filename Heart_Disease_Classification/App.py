import streamlit as st
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

st.set_page_config(
    page_title="App",
    page_icon="👋", )

#definisi masing-masing variabel    
def preprocess_sex(Sex):
    Sex_M = 0
    Sex_F = 0

    if Sex == 'M':
        Sex_M = 1
    elif Sex == 'F':
        Sex_F = 1

    return Sex_M, Sex_F


def preprocess_chestpain(ChestPainType):
    ChestPainType_ATA = 0
    ChestPainType_NAP = 0
    ChestPainType_ASY = 0
    ChestPainType_TA  = 0

    if ChestPainType == 'ATA':
        ChestPainType_ATA = 1
    elif ChestPainType == 'NAP':
        ChestPainType_NAP = 1
    elif ChestPainType == 'ASY':
        ChestPainType_ASY = 1
    elif ChestPainType == 'TA':
        ChestPainType_TA = 1

    return ChestPainType_ATA, ChestPainType_NAP, ChestPainType_ASY, ChestPainType_TA


def preprocess_restingecg(RestingECG):
    RestingECG_Normal = 0
    RestingECG_ST     = 0
    RestingECG_LVH    = 0

    if RestingECG == 'Normal':
        RestingECG_Normal = 1
    elif RestingECG == 'ST':
        RestingECG_ST = 1
    elif RestingECG == 'LVH':
        RestingECG_LVH = 1

    return RestingECG_Normal, RestingECG_ST, RestingECG_LVH


def preprocess_exerciseangina(ExerciseAngina):
    ExerciseAngina_N = 0
    ExerciseAngina_Y = 0

    if ExerciseAngina == 'No':
        ExerciseAngina_N = 1
    elif ExerciseAngina == 'Yes':
        ExerciseAngina_Y = 1

    return ExerciseAngina_N, ExerciseAngina_Y


def preprocess_stslope(ST_Slope):
    ST_Slope_Up   = 0
    ST_Slope_Flat = 0
    ST_Slope_Down = 0

    if ST_Slope == 'Up':
        ST_Slope_Up = 1
    elif ST_Slope == 'Flat':
        ST_Slope_Flat = 1
    elif ST_Slope == 'Down':
        ST_Slope_Down = 1

    return ST_Slope_Up, ST_Slope_Flat, ST_Slope_Down

    
#Load joblib
def classifier_model(classifier):
    with open('model_rf.pkl', 'rb') as f:
        classifier = pickle.load(f)
        return classifier

st.title('Heart Disease Prediction')

#input data
Age          = st.selectbox ("Age : ",range(28,78))
RestingBP    = st.selectbox("Resting BP:", range(90,171))
Cholesterol  = st.selectbox("Cholesterol:",  range(32,409))
FastingBS    = st.selectbox("Fasting BS:", range(0,2))
MaxHR        = st.selectbox("Max HR:", range(60,203))
Oldpeak      = st.number_input("Oldpeak :")

Sex_M, Sex_F = preprocess_sex(st.radio("Select Gender: ", ('male', 'female')))

        
ChestPainType_ATA, ChestPainType_NAP, \
ChestPainType_ASY, ChestPainType_TA                 = preprocess_chestpain(st.radio("Select Chest Pain Type : ", ('ATA', 'NAP','ASY','TA')))
        
RestingECG_Normal, RestingECG_ST, RestingECG_LVH    = preprocess_restingecg(st.radio("Select Resting ECG: ", ('Normal', 'ST','LVH')))
        
ExerciseAngina_N, ExerciseAngina_Y                  = preprocess_exerciseangina(st.radio("Select Exercise Angina : ", ('No', 'Yes')))
        
ST_Slope_Up, ST_Slope_Flat, ST_Slope_Down           = preprocess_stslope(st.radio("Select ST Slope : ", ('Up', 'Flat','Down')))

#Predict
submit = st.button('Predict')

if submit:
    prediction = classifier_model.predict([[Age, RestingBP, Cholesterol, FastingBS, MaxHR, Oldpeak, \
                   Sex_M, Sex_F, \
                   ChestPainType_ASY, ChestPainType_ATA, ChestPainType_NAP, ChestPainType_TA, \
                   RestingECG_LVH, RestingECG_Normal, RestingECG_ST, \
                   ExerciseAngina_N, ExerciseAngina_Y, \
                   ST_Slope_Down, ST_Slope_Flat, ST_Slope_Up]])
    
    if prediction == 1:
        st.write('Selamat, kamu SEHAT')
    else:
        st.write(" Maaf, sepertinya kamu memiliki penyakit jantung 😔. Semoga Lekas Sembuh!!!")
