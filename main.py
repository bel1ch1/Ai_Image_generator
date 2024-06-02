# test
import streamlit as st
import replicate
import time

REPLICATE_API_TOKEN = st.secrets["REPLICATE_API_TOKEN"]

st.markdown("# :red[AI Generator]")

def conf_sidebar():
    with st.sidebar:
        with st.form("form"):
            width = st.number_input("Width", min_value=256, max_value=2048, value=1024, step=16)
            height = st.number_input("Height", min_value=256, max_value=2048, value=1024, step=16)
            prompt = st.text_area("Enter youre prompt:")
            submitted = st.form_submit_button("Send", type="primary")
        return {
            "width" : width,
            "height" : height,
            "prompt" : prompt,
            "submitted" : submitted,
        }


def page(
        width: int,
        height: int,
        prompt: str,
        submitted: bool,
    ):
    if submitted:
        with st.spinner("Processing..."):
            result = replicate.run(
                "stability-ai/stable-diffusion:ac732df83cea7fff18b8472768c88ad041fa750ff7682a21affe81863cbe77e4",
                input={
                    "width": width,
                    "height": height,
                    "prompt": prompt,
                }
            )
            image = result[0]
            with st.container():
                st.image(image, caption="image")


def main():
    data = conf_sidebar()
    page(**data)


if __name__ == "__main__":
    main()
