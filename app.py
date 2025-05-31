import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model dan preprocessing pipeline
models = joblib.load("model.pkl")  # dictionary berisi model2
scaler = joblib.load("scaler.pkl")  # StandardScaler
pca = joblib.load("pca.pkl")        # PCA
label_encoder = joblib.load("label_encoder.pkl")  # LabelEncoder

# Daftar fitur yang digunakan
top_features = [
    'Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade',
    'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade',
    'Tuition_fees_up_to_date', 'Scholarship_holder', 'Age_at_enrollment',
    'Debtor', 'Gender', 'Application_mode'
]

# Judul aplikasi
st.title("🎓 Prediksi Status Mahasiswa")

# Input fitur dari pengguna
st.subheader("Masukkan Nilai Fitur Mahasiswa")

user_input = {}
for feature in top_features:
    user_input[feature] = st.number_input(f"{feature}", step=1.0)

# Tombol prediksi
if st.button("🔍 Prediksi Status"):
    # Konversi input ke DataFrame
    sample_df = pd.DataFrame([user_input])

    # Scaling dan PCA
    scaled = scaler.transform(sample_df)
    reduced = pca.transform(scaled)

    # Pilih model (misalnya Gradient Boosting)
    model = models

    # Prediksi
    prediction = model.predict(reduced)[0]
    label = label_encoder.inverse_transform([prediction])[0]

    st.success(f"📌 Prediksi Model: **{label}**")
