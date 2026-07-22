import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="BioPredict AI - Precision Medicine Platform", page_icon="🧬", layout="wide")

st.title("🧬 BioPredict AI: Advanced Multi-Omics & Therapeutics Engine")

st.sidebar.header("🔬 Genomic & Clinical Parameters")
age = st.sidebar.slider("Patient Age", 18, 90, 34)
gender = st.sidebar.selectbox("Gender", ["Female", "Male", "Other"])
mutation = st.sidebar.selectbox("Target Genomic Variant", ["BRCA1 Variant (rs80357906)", "EGFR L858R", "TP53 R275H", "KRAS G12D", "Wild Type (Normal)"])
expression_level = st.sidebar.slider("mRNA Expression Level (TPM)", 0.0, 100.0, 45.5)
lifestyle = st.sidebar.selectbox("Clinical Risk Profile", ["Low Risk / Active", "Moderate", "High Risk / Immunocompromised"])

if st.sidebar.button("Run AI Simulation"):
    with st.spinner("Analyzing genomic and clinical markers..."):
        risk_multiplier = 1.5 if "BRCA1" in mutation or "TP53" in mutation else 1.1
        base_risk = min(98.5, round((age * 0.4) + (expression_level * 0.3) * risk_multiplier, 1))
        efficacy = max(12.0, round(100 - base_risk + np.random.uniform(-5, 5), 1))
        confidence = round(np.random.uniform(92.4, 98.9), 2)

    st.success("Analysis Complete!")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Disease Risk Index", value=f"{base_risk}%")
    with col2:
        st.metric(label="AI Confidence Score", value=f"{confidence}%")
    with col3:
        st.metric(label="Predicted Drug Efficacy", value=f"{efficacy}%")
    with col4:
        st.metric(label="Therapeutic Tier", value="Class-I Inhibitor")
        
    st.markdown("### 📊 Biomarker Expression Trajectory")
    chart_data = pd.DataFrame(
        np.random.randn(30, 3) * [12, 6, 3] + [60, 35, 25],
        columns=["Genomic Risk", "Proteomic Activity", "Drug Sensitivity"]
    )
    st.line_chart(chart_data)
    
    st.markdown("### 💡 Clinical Recommendation & Summary")
    if base_risk > 60:
        st.warning("High risk profile detected. Immediate targeted therapy evaluation recommended.")
    else:
        st.info("Stable profile. Standard periodic monitoring advised.")
        
    report_text = f"BioPredict AI Clinical Report\nAge: {age}\nMutation: {mutation}\nRisk Index: {base_risk}%\nEfficacy: {efficacy}%"
    st.download_button(
        label="📥 Download Clinical Report (TXT)",
        data=report_text,
        file_name="biopredict_report.txt",
        mime="text/plain"
    )
else:
    st.info("👈 Configure parameters in the sidebar and click **'Run AI Simulation'**.")
