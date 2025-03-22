import streamlit as st
import numpy as np
import pandas as pd





st.set_page_config(
    page_title="MCDA Toolkit",
    page_icon=" ",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar navigation


st.sidebar.title("MCDA Toolkit")

page = st.sidebar.radio("Select a method:", ["Home", "Weighted Sum Model (WSM)", "Other Models Coming Soon..."])

# ---- Home Page ---- #
if page == "Home":
    st.title("MCDA Decision Support Platform")
    st.markdown("""
    Welcome to the Multi-Criteria Decision Analysis (MCDA) toolkit.

    This platform allows you to:
    - Upload or use sample datasets
    - Choose from a variety of MCDA models
    - Normalize and weight your criteria
    - Rank and score alternatives
    - Gain insights through interactive tables and visualizations

    Start by selecting a method from the sidebar.
    """)

# ---- WSM Page ---- #
elif page == "Weighted Sum Model (WSM)":
    st.title("Weighted Sum Model (WSM) - MCDA")
    st.markdown("""
    This Streamlit app demonstrates the Weighted Sum Model (WSM) for multi-criteria decision analysis.

    **How it works:**
    - You input or upload a dataset with alternatives and criteria.
    - Criteria are classified as beneficial (maximize) or non-beneficial (minimize).
    - Scores are normalized:
        - Beneficial: value / max(value)
        - Non-beneficial: 1 - (value / max(value))
    - Weighted scores are calculated and summed: **WSM Score = Σ(weight × normalized score)**
    - Alternatives are ranked based on WSM score.
    """)

    # Default synthetic dataset
    def get_default_data():
        data = {
            'Alternative': ['A1', 'A2', 'A3', 'A4', 'A5'],
            'Cost': [200, 150, 300, 250, 180],  # Non-beneficial
            'Quality': [8, 7, 6, 9, 8],         # Beneficial
            'Time': [10, 12, 8, 9, 11],         # Non-beneficial
            'Risk': [3, 5, 2, 4, 3]             # Beneficial
        }
        return pd.DataFrame(data), ['min', 'max', 'min', 'max']

    # ---- Step 1: Upload or Use Default Data ---- #
    st.subheader("Step 1: Input Data")
    use_default = st.radio("Choose data input method:", ["Use default synthetic data", "Upload your own CSV"])

    if use_default == "Use default synthetic data":
        df, criteria_types = get_default_data()
    else:
        uploaded_file = st.file_uploader("Upload CSV with alternatives and criteria", type="csv")
        if uploaded_file:
            df = pd.read_csv(uploaded_file)
            if 'Alternative' not in df.columns:
                st.error("Dataset must have a column named 'Alternative'.")
                st.stop()
            criteria = df.columns[1:]
            criteria_types = []
            for crit in criteria:
                crit_type = st.selectbox(f"Is '{crit}' beneficial or non-beneficial?", ['max', 'min'], key=crit)
                criteria_types.append(crit_type)
        else:
            st.stop()

    st.dataframe(df)
    criteria = df.columns[1:]

    # ---- Step 2: Input Criteria Weights ---- #
    st.subheader("Step 2: Assign Criteria Weights")
    def_weight = [1/len(criteria)] * len(criteria)
    weights = []
    for i, crit in enumerate(criteria):
        weight = st.number_input(f"Weight for {crit}", min_value=0.0, max_value=1.0, value=def_weight[i], step=0.01)
        weights.append(weight)

    weights = np.array(weights)
    weights = weights / weights.sum()

    # ---- Step 3: Normalize Data ---- #
    st.subheader("Step 3: Normalized Data")
    norm_df = df.copy()
    for i, crit in enumerate(criteria):
        if criteria_types[i] == 'max':
            norm_df[crit] = df[crit] / df[crit].max()
        else:
            norm_df[crit] = 1 - (df[crit] / df[crit].max())

    st.dataframe(norm_df)

    # ---- Step 4: Calculate WSM Scores ---- #
    st.subheader("Step 4: WSM Scores and Ranking")

    norm_values = norm_df[criteria].values
    scores = np.dot(norm_values, weights)

    result_df = df[['Alternative']].copy()
    result_df['WSM Score'] = scores
    result_df['Rank'] = result_df['WSM Score'].rank(ascending=False).astype(int)

    st.dataframe(result_df.sort_values(by='Rank'))

    # ---- Interpretation ---- #
    st.markdown("""
    ### Interpretation
    - Higher WSM scores indicate better alternatives.
    - Ranking reflects overall performance across all weighted, normalized criteria.
    """)

# ---- Placeholder for future models ---- #
else:
    st.title("Coming Soon")
    st.markdown("More MCDA methods will be added here. Stay tuned!")
