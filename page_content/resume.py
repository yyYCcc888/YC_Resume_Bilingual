import streamlit as st
import base64
import os

def resume_page():
    # 获取语言设置
    language = st.session_state.get('language', '中文')
    
    if language == '中文':
        st.markdown("## 个人简历")
        
        # 添加中英文简历下载按钮
        col1, col2 = st.columns(2)
        
        with col1:
            pdf_file_path = os.path.join("static", "docs", "new_CHAN_YinSen_Resume_CN.pdf")
            if os.path.exists(pdf_file_path):
                with open(pdf_file_path, "rb") as pdf_file:
                    PDFbyte = pdf_file.read()
                
                st.download_button(
                    label="下载中文简历",
                    data=PDFbyte,
                    file_name="陈彦宸_简历.pdf",
                    mime='application/pdf'
                )
            else:
                st.warning("中文简历PDF文件未找到")
            with open("static/docs/new_resume_CHAN, Yin Sen.pdf", "rb") as pdf_file:
                PDFbyte = pdf_file.read()
            
            st.download_button(
                label="下载英文简历",
                data=PDFbyte,
                file_name="CHAN_Yin_Sen_Resume.pdf",
                mime='application/pdf'
            )
        
        st.markdown("""
        ### 陈彦宸
        - **电话**: 59584365（香港）15980247560（大陆）
        - **邮箱**: [1378188281@qq.com](mailto:1378188281@qq.com)
        - **性别**：女
        
        ### 教育背景
        **硕士：香港中文大学，市场营销（大数据分析）** | *香港，2024.08-2025.10*
        - 专业课程：社交媒体分析、机器学习、客户分析、整合营销传播、营销分析、数字营销、市场研究等

        **本科：四川大学，金融学** | *成都，2020.09-2024.06*
        - 专业课程：公司金融、国际金融、金融经济学、货币金融学、金融计量学、投资学等

        ### 工作经验
        **中信建投，行业研究员** | *成都, 2023.04-2023.05*
        - 通过阅读10余篇行研报告，分析IDC行业上、中、下游针间的关系及其针对不同梯队IDC的运营名单
        - 使用雪球获取IDC行业的基本资讯以及行业和部分企业研报，通过东方财富网、Wind数据库等工具搜集IDC行业与龙头企业财务数据与市场数据，并通过Excel对数据进行整理并分析
        - 计算相关基础财务指标如ROE、资产负债率后，使用杜邦分析法对光环新网的财务指标进行着重分析，并对其进行估值，提出合理的发展建议

        **兴业证券，销售助理** | *上海, 2023.08-2023.09*
        - 对市场上各类公募基金的财务数据进行提取，并根据其投资策略进行分类，分析其业绩
        - 跟踪全市场IPO及定增联主、分销承销团业务机会并梳理相关投资机构信息，达成业务合作
        - 与客户沟通，推广符合客户需求的理财产品

        **四川大学"香港文化协会"，策划部成员** | *成都, 2020.09-2024.07*
        - 负责撰写活动策划书，如活动预告，策划文稿，活动记录及会议文稿等，具备活动策划及文字处理能力
        - 撰写活动执行计划，细化活动执行点，推进活动按预期开展，筹备并监督活动物料准备情况，明确活动预算及流程，解决现场各类突发状况并实施监督进度，活动均按计划0延误开展
        - 组织粤语歌唱大赛等活动开展，监督活动整套流程实施，顺利举办活动，活动参与人数达200人

        ### 项目成果
        **霸王茶姬奥运营销活动效果评估** | *2024.12*
        - 使用Octopus抓取数据并清洗，运用Python进行情感分析和关键词提取，评估消费者感知。

        **百度网盘市场分析** | *2024.11*
        - 设计问卷收集用户对网盘各属性数据，对清洗后的数据进行描述性分析，并使用R Studio进行多元线性回归以评估各属性的影响，运用Sawtooth设计选择模型问卷并通过R Studio分析数据以预测未来市场份额。

        ### 技能/其他
        - **语言**：雅思7.0，粤语
        - **技能**：熟悉使用office办公软件，STATA、Python、R studio及其他数据分析软件等；熟练掌握AI驱动的工具，应用于自然语言处理、数据分析，以及提升办公软件的使用效率
        - **爱好**：乒乓球、网球（四川大学第八届网球比赛女子单打第二名、团体赛第一名，香港中文大学校队成员）；钢琴（中央音乐学院满级优秀，多次获得国家级奖项）

        ### 个人评价
        - 实践经历丰富，具备多段实践经历，对金融证券市场有一定的了解全面能力较强，具备较强的统筹协调能力，且有一定的金融知识储备及会计相关知识，熟悉金融证券公司工作流程，具备扎实的专业知识
        - 在项目实践中，展现出敏锐的市场洞察力和准确的客户分析能力，善于运用数据分析工具进行市场趋势和客户需求的评估，具备较强的沟通表达能力，能够与客户建立良好的关系
        - 创新创造力强，喜欢提前计划一切但不失应变能力，能主动学习新知识，拥有开朗有趣的灵魂
        - 工作责任感强，对于工作秉着认真负责的，积极向上的态度，不断更新充实自我
        """)
    else:
        st.markdown("## Resume")
        
        # 添加中英文简历下载按钮
        col1, col2 = st.columns(2)
        
        with col1:
            with open("static/docs/new_resume_CHAN, Yin Sen.pdf", "rb") as pdf_file:
                PDFbyte = pdf_file.read()
            
            st.download_button(
                label="Download English Resume",
                data=PDFbyte,
                file_name="CHAN_Yin_Sen_Resume.pdf",
                mime='application/pdf'
            )
            
        with col2:
            with open("static/docs/new_CHAN_YinSen_Resume_CN.pdf", "rb") as pdf_file:
                PDFbyte = pdf_file.read()
            
            st.download_button(
                label="Download Chinese Resume",
                data=PDFbyte,
                file_name="陈彦宸_简历.pdf",
                mime='application/pdf'
            )
            
        st.markdown("""
        ### CHAN, Yin Sen (YC)
        - **Phone**: +00852 56659168
        - **Email**: [1378188281@qq.com](mailto:1378188281@qq.com)
        - **Gender**: Female

        ### Education
        #### Chinese University of Hong Kong | MSc in Marketing (Big Data Marketing) | 08/2024-10/2025
        - Main Modules: Social Media Analytics, Machine Learning in Marketing, Customer Analytics, Integrated Marketing Communication, Marketing Analytics, Digital Marketing, Marketing Research

        #### Sichuan University | Bachelor of Economics in Finance | 09/2020-06/2024
        - Main Modules: International Investment, Security Investment, Financial Risk Management, Financial Statement Analysis, Financial Econometrics, Financial Engineering

        ### Professional Experience
        #### Sales Assistant, Industrial Securities | 08/2023-09/2023
        - Sought the IPO information, distribution and underwriting opportunities to reach business cooperation
        - Extracted the financial data of various types of public funds in the market and classified them based on their investment strategies to analyse their performance
        - Communicated with clients and promoted appropriate financial products for their requirements

        #### Industry Research Analyst, China Securities | 04/2022-05/2022
        - Participated in the industry research for the IDC industry, analysing the industry chain of upstream, midstream and downstream companies, policies about PUE requirements, as well important indicators like data center scale, market share, industry concentration
        - Conducted the fundamental analysis of one leading company in the IDC industry by extracting financial data and marketing data via Wind
        - Calculated the company's financial ratios in Excel, such as ROE, asset liability ratio, etc. to analyse its financial condition and profitability compared with other industry companies
        - Adopted the Dupont analysis method and PE valuation method to value the company, predict its future profit and put forward feasible suggestions of company's business expansion
        - Independently integrated all parts into an industry research report

        #### Member of the Planning Department, HK Culture Association of SCU | 09/2020-07/2024
        - Responsible for drafting event planning documents, including event announcements, planning manuscripts, activity records, and meeting minutes, demonstrating strong text processing abilities
        - Developed detailed event execution plans, refined implementation details, and ensured activities proceeded as scheduled. Managed the preparation of event materials and supervision, clarified budgets and processes while effectively handling various on-site emergencies while monitoring progress
        - Organized and oversaw the entire process of activities such as the Cantonese Singing Competition (with a participation of 200 people), ensuring smooth progress from the initial phase to final summary

        ### Research Projects
        #### Exploration of the Effectiveness of CHAGEE's Olympics Marketing Campaign | 12/2024
        - Conducted STP analysis for CHAGEE, utilized Octopus to scrape and preprocess social media data, and conducted sentiment analysis and keyword extraction using Python to evaluate consumer perceptions.

        #### Baidu Netdisk Marketing Analysis | 11/2024
        - Designed a survey to gather user feedback on various attributes of Baidu Netdisk, performed descriptive analysis on cleaned data and used R Studio for multiple linear regression to assess the impact of each attribute, and developed a choice model using Sawtooth to design a questionnaire and analyzed the data with R Studio to predict future market share.

        ### Additional Information
        - **Language Proficiency**: English (IELTS 7.0), Chinese (Native Speaker), Cantonese (Fluent in Listening)
        - **Technical Skills**: Proficient in using Office suite, STATA, Python, R Studio, and other data analysis software; skilled in utilizing AI-driven tools
        - **Talents**: Tennis (First place in team competition of the 8th Sichuan University Tennis Tournament, a member of the school team of CUHK), Piano (Grade 10, Several National Awards)        """)
