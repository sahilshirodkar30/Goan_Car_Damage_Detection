import streamlit as st
from model_helper import predict
import streamlit as st
import torch
import streamlit as st
import subprocess

st.title("Check Installed Packages")

try:
    import torch
    st.write("Torch version:", torch.__version__)
except ImportError:
    st.error("Torch is NOT installed")

# Show pip freeze to confirm
installed = subprocess.check_output(["pip", "freeze"]).decode("utf-8")
st.code(installed)

st.title("Torch Test App")
st.write("PyTorch version:", torch.__version__)
st.write("CUDA available:", torch.cuda.is_available())


st.title("Vechile Damage Detection ")

uploaded_image = st.file_uploader("Upload the file ",type=['jpg','png'])

if uploaded_image:
    image_path = "temp_file.jpg"
    with open(image_path,"wb") as f:
        f.write(uploaded_image.getbuffer())
        st.image(uploaded_image,caption="Uploaded File")
        prediction = predict(image_path)
        st.info(f"Predicted Class: {prediction}")
