import pickle
import streamlit as st


def loading_model():
    try:
        with open("app\sales_based_on_TV\linearregression_model.pickle","br") as file:
            model = pickle.load(file)
        return model
    except FileNotFoundError as e:
        st.write(e)


def main():
    try:

        st.title("Sales Prediction based on TV Advertisement.")
        tv_ads = st.text_input("Enter an Expenditure on TV advertisement.")
        col1, col2, col3 = st.columns(3)
        if col2.button("Predict"):
            model = loading_model()
            prediction = model.predict([[int(tv_ads)]])
            st.write(f"The sales prediction based on {int(tv_ads)} expenditures on TV is {round(prediction[0],3)}.")
    except ValueError as e:
        st.write(e)

if __name__ == "__main__":
    main()