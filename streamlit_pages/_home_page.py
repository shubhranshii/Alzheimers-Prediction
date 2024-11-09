import streamlit as st

def home_page():
    st.write("""
        ## Welcome to Alzheimer’s Prediction
        Alzheimer's disease (AD) is a progressive neurodegenerative disorder that impacts millions globally. While it's most commonly associated with memory loss, AD affects many cognitive functions, including reasoning, decision-making, and the ability to plan and perform familiar tasks. Personality changes and shifts in behavior can also accompany these symptoms, making AD a complex and challenging condition. Although the exact cause is not fully understood, research suggests a genetic component. For example, a variant of the APOE gene, APOE e4, is linked to an increased risk of developing Alzheimer’s.

        ## Why Early Detection Matters
        Early detection of Alzheimer’s disease is crucial as it allows for timely interventions, which can improve quality of life and slow disease progression. Identifying AD at its early stages empowers individuals and their families to plan for the future, access support services, and consider clinical trials. Early diagnosis opens the door to potential therapies that can better manage the disease and its impact, providing hope in the face of this challenging condition.

        ## Purpose of the project
        This project seeks to develop a machine learning model to facilitate the early prediction of Alzheimer’s disease. Alzheimer's is a debilitating disorder that profoundly affects individuals and families. Through the use of advanced machine learning techniques, our aim is to build a predictive model that can analyze relevant data to assess the risk of Alzheimer’s disease in individuals. This project supports early detection, leading to better patient care and the possibility of future interventions.
        
        ## How our Prediction Tool works
        Our prediction tool uses a logistic regression model trained on the Alzheimer's Disease Neuroimaging Initiative (ADNI) dataset to assess the risk of Alzheimer's disease. While this model provides valuable insights, it is not 100% accurate and should not be used as a standalone diagnostic tool. We strongly recommend consulting healthcare professionals for a comprehensive evaluation and personalized medical advice.
        
        <br>
                
        """, unsafe_allow_html=True)

    st.caption('Finished reading? Navigate to the `Prediction Page` to make some predictions')