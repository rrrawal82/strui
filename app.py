import base64
import streamlit as st
import plotly.express as px
import streamlit.components.v1 as components
df = px.data.iris()

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("./images/pbi.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://aidemoproject.s3.ap-south-1.amazonaws.com/graph_image.jpeg");
background-size: 100%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}

 
    .modal {{
    display: none; /* Hidden by default */
    position: fixed; /* Stay in place */
    z-index: 1; /* Sit on top */
    padding-top: 66px; /* Location of the box */
    left: 0;
    top: 0;
    width: 100%; /* Full width */
    height: 106%; /* Full height */
    overflow: auto; /* Enable scroll if needed */
    background-color: rgb(0,0,0); /* Fallback color */
    background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
    border-radius: 10px;
    }}

    .modal-content {{
    background-color: #040000;
    margin: auto;
    padding: 20px;
    border: 1px solid #888;
    width: 70%;
    height:80%
    }}

    .close {{
    color: #aaaaaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
    }}

    .close:hover,
    .close:focus {{
    color: #000;
    text-decoration: none;
    cursor: pointer;
    }}

    .button-chat {{
    padding-left: 36px;
    padding-right: 10px;
    border: 1px solid #000000;
    cursor: pointer;
    margin-left:85%;
    margin-top:-3%;
    }}
    .button-mic{{
    padding-left: 36px;
    padding-right: 10px;
    border: 1px solid #000000;
    cursor: pointer;

    }}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

charcater_path = 'https://aidemoproject.s3.ap-south-1.amazonaws.com/character.jpeg'
video="https://aidemoproject.s3.ap-south-1.amazonaws.com/character_video.mp4"
micImg="./images/mic.png"
chatImg="./images/chat.png"
javascript_code = f"""
       <script>
      var modal = document.getElementById("myModal");
      var btn = document.getElementById("myBtn");
      console.log("weewwewe")
      var span = document.getElementsByClassName("close")[0];
      btn.onclick = function() {{
       console.log("23232323232")
        modal.style.display = "block";
      }}

      span.onclick = function() {{
        modal.style.display = "none";
      }}

     
      window.onclick = function(event) {{
        if (event.target == modal) {{
          modal.style.display = "none";
        }}
      }}
      </script>
  
    """

st.markdown(javascript_code, unsafe_allow_html=True)

# Your Streamlit content inside the styled container
st.markdown(f'<html><div class="main" style=" position: fixed; bottom: 23px; right: 28px; display:block; "> <img src="{charcater_path}" style="border-radius: 50%;width:90% ;border:5px solid black;"><br><br>   <button class="open-button" id="myBtn" onClick="javascript:modal.style.display = "block""  style= " background-color: #010000;color: white; padding: 16px 20px;border: none;border-radius: 8px;cursor: pointer;width: 200px;height:55px">Ask about it</button> </div> <div id="myModal" class="modal"> <div class="modal-content"> <div> <span class="close">&times;</span> <video width="1000" height="700" style="margin-top:-50px;margin-left:100px"  autoplay loop  muted> <source src="{video}" type="video/mp4">  <source src="movie.ogg" type="video/ogg">  <div style="margin-left:45%;  margin-top:-3%;">  <button type="reset"  class=".button-chat" style="background-color:transparent; border-color:transparent;">  <img src="{micImg}" height="55"/></button> <button type="reset"  class="button-mic" style="background-color:transparent; border-color:transparent;">  <img src="{chatImg}" height="55"/></button> </div> </div></div></div> </html>', unsafe_allow_html=True)
