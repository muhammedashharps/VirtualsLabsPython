import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Virtual Labs NSSCE", page_icon="🐍", layout= "wide")
st.sidebar.success("Select a page above: ")

def load_anime(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    else:
        return r.json()
animation = load_anime("https://lottie.host/b35b3ec6-2fba-459c-8d45-ad56b94defb5/VFrO8dqH5S.json")

with st.container():
     st.title("VIRTUAL LABS NSSCE")
     st.link_button("Projects", url = "/Projects")
     st.write("---")

with st.container():
    try:
        st_lottie(animation, height = 200)
    except:
        print("Error Loading Animation")

with st.container():
    import streamlit as st
    st.title("Welcome to Python Virtual Labs")
    st.write("---")

    st.header("Why Python?")

    st.markdown(
        "**Python is not just a programming language; it's a gateway to endless possibilities.\n"
        "From web development to artificial intelligence, Python is the language that empowers you to turn your ideas into reality. It's easy to learn, versatile, and widely used in the tech industry.**")


    st.write("---")

    st.header("What Makes Our Labs Special?")

    st.markdown(
        "1. **Interactive Coding Environments: Dive into coding exercises right from your browser. No installations, no hassle – just pure coding fun.**")

    st.markdown(
        "2. **Projects: Apply your knowledge to real-world scenarios.**")

    st.markdown(
        "3. **Receive instant feedback on your knowledge with tests.**")

    st.markdown(
        "4. **Collaborative Learning: Connect with fellow learners with our discord server, share insights, and collaborate on coding challenges. Learning is more fun when it's a community effort!**")

    st.image("https://cdn-icons-png.flaticon.com/512/5234/5234762.png", width=150)

    st.write("---")

    st.header("Explore Our Labs:")

    st.markdown(
        "- **Tutorials: Start your Python journey with hands-on exercises designed for beginners.**")

    st.markdown(
        "- **Simulations: Visualise your code in an interactive way.**")

    st.markdown(
        "- **Projects: Get started with small to medium projects.**")

    st.markdown(
        "- **Tests: Evaluate your knowledge with extensive tests..**")

    st.write("---")



    st.header("Get Started Today")

    st.markdown(
        '''**No matter your skill level, there's always something new to discover in the world of Python.
        Join us in the adventure of learning, exploring, and creating. Start coding now!**''')

    st.divider()
    st.link_button("Join Our Discord Server", url = "nil")

