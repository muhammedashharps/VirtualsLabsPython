import streamlit as st
st.set_page_config(page_title="Virtual Labs NSSCE", page_icon="🐍", layout= "wide")

def display_library():
    st.title("Digital Library: Python eBooks")

    # Mock data for eBooks (replace this with actual data or links)
    ebooks = [
        {
            "title": "Beyond The Basic Stuff With Python",
            "author": "Al Sweigart",
            "image": "https://automatetheboringstuff.com/images/cover_beyond_thumb.jpg",
            "download_link": "https://example.com/python_crash_course.pdf"
        },
        {
            "title": "Automate the Boring Stuff with Python",
            "author": "Al Sweigart",
            "image": "https://automatetheboringstuff.com/images/cover_automate2_thumb.jpg",
            "download_link": "https://example.com/automate_boring_stuff.pdf"
        },
        {
            "title": "The Big Book of Small Python Projects",
            "author": "Al Sweigart",
            "image": "https://automatetheboringstuff.com/images/cover_bigbookpython_thumb.jpg",
            "download_link": "https://example.com/fluent_python.pdf"
        }
    ]

    st.markdown("---")
    st.subheader("Feel free to download these free eBooks and enhance your Python skills.")
    st.divider()

    for ebook in ebooks:
        st.markdown(
            f"""
            <div style="display:flex">
                <img src="{ebook['image']}" alt="{ebook['title']}" width="100" height="150">
                <div style="margin-left: 20px;">
                    <h3>{ebook['title']}</h3>
                    <p>Author: {ebook['author']}</p>
                    <a href="{ebook['download_link']}" download="{ebook['title']}.pdf">Download PDF</a>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.divider()

if __name__ == "__main__":
    display_library()

