import streamlit as st 
import pickle
with open("sentiment_model.pkl","rb") as file:
    model=pickle.load(file)
with open("tfid.pkl",'rb') as file:
    vectorize=pickle.load(file)
st.set_page_config(page_title="Sentiment Analysis")    
st.title("Sentiment Analysis Predition")    

st.write(
    "Enter a sentence or review and the model "
    "will predict whether it is Positive, Negative, or Neutral.")
s=st.text_area("Enter a text or Sentence",placeholder="type something like i am happy or sad")  
if st.button("Anaylse Statement"):
    if s.strip()=="":
        st.warning("Sentiment is empty. Please type something which I acn predict")
    else:
        text_tfid=vectorize.transform ([s])
        predict=model.predict(text_tfid)[0]
        prob=model.predict_proba(text_tfid)[0]
        confidence=max(prob)*100
        if predict==-1:
            st.error("Negative Statement")
        elif predict==0:
            st.info("Neutral Statement")
        else:
            
            st.success("Positive Statement")
        st.write( f"Condience= {confidence:.2f}")
                    