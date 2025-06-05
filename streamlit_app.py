import warnings
import streamlit as st

warnings.simplefilter(action="ignore", category=FutureWarning)

# Must be the first Streamlit command
st.set_page_config(page_title="CHAN Yin Sen's Page", layout="wide")

# Add language selector in the sidebar
language = st.sidebar.selectbox('语言 | Language', ['中文', 'English'])
st.session_state['language'] = language

# Import pages from the new directory
from page_content.home import home_page
from page_content.experience import experience_page
from page_content.education import education_page
from page_content.resume import resume_page
from page_content.contact import contact_page

# Import components
from components.footer import display_footer
from components.styles import load_css

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):
        # Load custom CSS
        load_css()

        st.sidebar.markdown("##")
        app = st.sidebar.radio(
            "", self.apps, format_func=lambda app: app["title"]
        )
        st.sidebar.markdown("---")

        app["function"]()
        
        # Display footer at the bottom of each page
        display_footer()

# Initialize the app
app = MultiApp()

# Add pages to the app
app.add_app("Home Page 首页", home_page)
app.add_app("Education Page 教育经历", education_page)
app.add_app("Experience Page 实习经历", experience_page)
app.add_app("Resume Page 简历", resume_page)
app.add_app("Contact Page 联系方式", contact_page)

# Run the app
app.run()
