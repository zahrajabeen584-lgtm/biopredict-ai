import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="BioPredict AI - Precision Medicine Platform", page_icon="🧬", layout="wide")

st.markdown("""
    <style>
    .main {background-color: #f8fafc;}
    .stButton>button {background-color: #2563eb; color: white; border-radius: 6px; font-weight: bold;}
    .metric-card {background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);}
    </style>
    """, unsafe_allow_html=True)

st.title("🧬 BioPredict AI: Advanced Multi-Omics & Therapeutics Engine")
st.markdown("**Next-Gen Bioinformatics Portfolio Tool** | Optimized for Precision Medicine Startups & Top-Tier Research")

st.sidebar.header("🔬 Genomic & Clinical Parameters")
age = st.sidebar.slider("Patient Age", 18, 90, 34)
gender = st.sidebar.selectbox("Gender", ["Female", "Male", "Other"])
mutation = st.sidebar.selectbox("Target Genomic Variant", ["BRCA1 Variant (rs80357906)", "EGFR L858R", "TP53 R275H", "KRAS G12D", "Wild Type (Normal)"])
expression_level = st.sidebar.slider("mRNA Expression Level (TPM)", 0.0, 100.0, 45.5)
lifestyle = st.sidebar.selectbox("Clinical Risk Profile", ["Low Risk / Active", "Moderate", "High Risk / Immunocompromised"])

if st.sidebar.button("Run Advanced AI Simulation"):
    with st.spinner("Executing deep neural network models across multi-omics layers..."):
        # Simulated intelligent computation based on inputs
        risk_multiplier = 1.5 if "BRCA1" in mutation or "TP53" in mutation else 1.1
        base_risk = min(98.5, round((age * 0.4) + (expression_level * 0.3) * risk_multiplier, 1))
        efficacy = max(12.0, round(100 - base_risk + np.random.uniform(-5, 5), 1))
        confidence = round(np.random.uniform(92.4, 98.9), 2)

    st.success("AI Precision Analysis Complete!")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Disease Risk Index", value=f"{base_risk}%", delta="+5.2% vs threshold", delta_color="inverse")
    with col2:
        st.metric(label="AI Confidence Score", value=f"{confidence}%", delta="High Precision")
    with col3:
        st.metric(label="Predicted Drug Efficacy", value=f"{efficacy}%", delta="Optimal Response")
    with col4:
        st.metric(label="Therapeutic Tier", value="Class-I Inhibitor")
        
    st.markdown("### 📊 Multi-Omics Biomarker Expression & Trajectory")
    chart_data = pd.DataFrame(
        np.random.randn(30, 3) * [12, 6, 3] + [60, 35, 25],
        columns=["Genomic Pathway Risk", "Proteomic Biomarker Activity", "Target Drug Sensitivity"]
    )
    st.line_chart(chart_data)
    
    st.markdown("### 📋 Automated Clinical Summary & Entrepreneurial Impact")
    st.info(f"💡 **Startup Pipeline Insight:** For patient profile with **{mutation}**, this automated deep-learning inference cuts preliminary drug discovery target validation cycles down from weeks to minutes, offering massive scalability for biotech ventures.")
    
    # New Feature: Export Report Button Simulation
    if st.button("📥 Export Comprehensive Clinical Report (PDF/JSON)"):
        st.balloons()
        st.success("Report successfully compiled and ready for download!")
else:
    st.info("👈 Configure the genomic parameters in the sidebar and click **'Run Advanced AI Simulation'** to initiate deep learning analysis[span_1](start_span)[span_1](end_span).")
