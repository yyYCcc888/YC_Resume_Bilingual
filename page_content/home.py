import streamlit as st
from PIL import Image
import os

def home_page():
    # 获取全局语言设置
    language = st.session_state.get('language', '中文')
    
    left_col, right_col = st.columns(2)
    
    if language == '中文':
        left_col.markdown(
            """
            <h4>陈彦宸 </h4>
            <p>市场营销学硕士（大数据营销）<br>
            香港中文大学<br>
            香港特别行政区荃湾<br>
            <a href="mailto:1378188281@qq.com">1378188281@qq.com</a><br>
            +852 59584365 (香港), +86 15980247560 (中国大陆)</p>
            """,
            unsafe_allow_html=True
        )
    else:
        left_col.markdown(
            """
            <h4>CHAN, Yin Sen (YC)</h4>
            <p>MSc in Marketing (Big Data Marketing)<br>
            Chinese University of Hong Kong<br>
            Tsuen Wan NT, HKSAR<br>
            <a href="mailto:1378188281@qq.com">1378188281@qq.com</a><br>
            +852 59584365 (HK), +86 15980247560 (Mailand China)</p>
            """,
            unsafe_allow_html=True
        )

    # add a photo to the right column
    image_path = os.path.join("static", "images", "WechatIMG1624.jpg")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        right_col.image(image, width=200)
    else:
        right_col.warning("Profile image not found")

    st.markdown("---")

    if language == '中文':
        st.markdown(
            """
            ### 关于我
            我是一名即将毕业的市场营销学硕士研究生，学习大数据分析方向。本科在四川大学就读，专业是金融学。在此期间，我通过实习和项目建立了扎实的金融基础，并培养了数据分析和市场研究技能。在中信建投和兴业证券的实习经历让我能够进行深入的行业分析，并提出有价值的市场洞察和发展建议。

            在攻读硕士学位期间，我进一步学习了营销和数据分析方面的专业知识，掌握了社交媒体分析、机器学习和客户分析等技术。通过种种实践项目，我使用Python和R Studio等工具对营销活动和市场趋势进行全面分析，积累了丰富的经验。

            我擅长数据驱动的决策制定，具有强大的学习和团队合作能力，并能够快速适应各种挑战。我期待在营销或数据分析领域应用我的专业技能，为团队做出贡献。
            """
        )
        
        st.markdown(
            """
            ### 技能
            - 编程语言：Python、R
            - 数据分析：Pandas、NumPy、Matplotlib、Seaborn
            - 机器学习：Scikit-learn、XGBoost、NLP
            - 数据可视化：Tableau、Power BI、Seaborn、Plotly、词云
            - 统计分析：情感分析、回归分析、聚类分析
            - 沟通能力：演讲技巧、技术写作、报告撰写
            """
        )
    else:
        st.markdown(
            """
            ### About Me
            I am a soon-to-graduate master's student in Marketing with a focus on Big Data Analytics. During my undergraduate studies in Finance at Sichuan University, I built a solid foundation in finance and honed my data analysis and market research skills through internships and projects. My internships at CITIC Securities and Industrial Securities allowed me to conduct in-depth industry analyses and propose valuable market insights and development suggestions.

            In my master's program, I further developed my expertise in marketing and data analysis, mastering techniques such as social media analysis, machine learning, and customer analytics. Through practical projects, I utilized tools like Python and R Studio to conduct thorough analyses of marketing activities and market trends, gaining extensive project experience.

            I am passionate about data-driven decision-making and possess strong learning and teamwork abilities, enabling me to adapt quickly to various challenges. I look forward to applying my professional skills in the field of marketing or data analysis and contributing to a dynamic team.
            """
        )

    st.markdown("---")
    
    # Interactive component has been moved to the experience page