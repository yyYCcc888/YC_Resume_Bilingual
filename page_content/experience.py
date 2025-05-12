import streamlit as st

def experience_page():
    # 获取语言设置
    language = st.session_state.get('language', '中文')
    
    if language == '中文':
        st.markdown("## 工作经验")
        
        st.markdown("""
        ### 行业研究员
        **中信建投** | *2023.04 - 2023.05*
        - 通过阅读10余篇行研报告，分析IDC行业上、中、下游针间的关系及其针对不同梯队IDC的运营名单
        - 使用雪球获取IDC行业的基本资讯以及行业和部分企业研报，通过东方财富网、Wind数据库等工具搜集IDC行业与龙头企业财务数据与市场数据，并通过Excel对数据进行整理并分析
        - 计算相关基础财务指标如ROE、资产负债率后，使用杜邦分析法对光环新网的财务指标进行着重分析，并对其进行估值，提出合理的发展建议

        ### 销售助理
        **兴业证券** | *2023.08 - 2023.09*
        - 对市场上各类公募基金的财务数据进行提取，并根据其投资策略进行分类，分析其业绩
        - 跟踪全市场IPO及定增联主、分销承销团业务机会并梳理相关投资机构信息，达成业务合作
        - 与客户沟通，推广符合客户需求的理财产品

        ### 策划部成员
        **四川大学"香港文化协会"** | *2020.09 - 2024.07*
        - 负责撰写活动策划书，如活动预告，策划文稿，活动记录及会议文稿等，具备活动策划及文字处理能力
        - 撰写活动执行计划，细化活动执行点，推进活动按预期开展，筹备并监督活动物料准备情况，明确活动预算及流程，解决现场各类突发状况并实施监督进度，活动均按计划0延误开展
        - 组织粤语歌唱大赛等活动开展，监督活动整套流程实施，顺利举办活动，活动参与人数达200人

        """)

        st.markdown("## 专业技能")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 技术技能
            - **编程语言**：Python、R
            - **数据分析**：Pandas、 NumPy、 Matplotlib、 Seaborn
            - **机器学习**：Scikit-learn、 XGBoost、 NLP
            - **数据可视化**：Tableau、 Power BI、 Seaborn、 Plotly、 词云
            - **统计分析**：情感分析、回归分析、聚类分析
            - **办公软件**：精通Office办公软件
            - **AI工具**：ChatGPT、Deepseek、Copilot
            """)
            
        with col2:
            st.markdown("""
            ### 软技能
            - **沟通能力**：演讲、报告撰写
            - **分析思维**：数据驱动下的决策制定
            - **项目管理**：任务优先级排序，时间管理
            - **研究能力**：市场研究，竞争分析
            - **团队协作**：强大的协作精神
            - **工作能力**：快速学习，问题处理
            """)
    else:
        st.markdown("## Professional Experience")
        
        st.markdown("""
        ### Sales Assistant
        **Industrial Securities** | *August 2023 - September 2023*
        - Sought the IPO information, distribution and underwriting opportunities to reach business cooperation
        - Extracted the financial data of various types of public funds in the market and classified them based on their investment strategies to analyse their performance
        - Communicated with clients and promoted appropriate financial products for their requirements

        ### Industry Research Analyst
        **China Securities** | *April 2022 - May 2022*
        - Participated in the industry research for the IDC industry, analysing the industry chain of upstream, midstream and downstream companies, policies about PUE requirements, as well important indicators like data center scale, market share, industry concentration
        - Conducted the fundamental analysis of one leading company in the IDC industry by extracting financial data and marketing data via Wind
        - Calculated the company's financial ratios in Excel, such as ROE, asset liability ratio, etc. to analyse its financial condition and profitability compared with other industry companies
        - Adopted the Dupont analysis method and PE valuation method to value the company, predict its future profit and put forward feasible suggestions of company's business expansion
        - Independently integrated all parts into an industry research report

        ### Member of the Planning Department
        **HK Culture Association of SCU** | *September 2020 - July 2024*
        - Responsible for drafting event planning documents, including event announcements, planning manuscripts, activity records, and meeting minutes, demonstrating strong text processing abilities
        - Developed detailed event execution plans, refined implementation details, and ensured activities proceeded as scheduled. Managed the preparation of event materials and supervision, clarified budgets and processes while effectively handling various on-site emergencies while monitoring progress
        - Organized and oversaw the entire process of activities such as the Cantonese Singing Competition (with a participation of 200 people), ensuring smooth progress from the initial phase to final summary

        ### Research Projects

        **Exploration of the Effectiveness of CHAGEE's Olympics Marketing Campaign** | *December 2024*
        - Conducted STP analysis for CHAGEE, utilized Octopus to scrape and preprocess social media data, and conducted sentiment analysis and keyword extraction using Python to evaluate consumer perceptions.

        **Baidu Netdisk Marketing Analysis** | *November 2024*
        - Designed a survey to gather user feedback on various attributes of Baidu Netdisk, performed descriptive analysis on cleaned data and used R Studio for multiple linear regression to assess the impact of each attribute, and developed a choice model using Sawtooth to design a questionnaire and analyzed the data with R Studio to predict future market share.
        """)

        st.markdown("## Additional Information")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### Technical Skills
            - **Programming Languages:** Python, R
            - **Data Analysis:** Pandas, NumPy, Matplotlib, Seaborn
            - **Machine Learning:** Scikit-learn, XGBoost, NLP
            - **Data Visualization:** Tableau, Power BI, Seaborn, Plotly, Word Clouds
            - **Statistical Analysis:** Sentiment Analysis, Regression Analysis, Cluster Analysis
            - **Design Tools:** Canva, Adobe Photoshop, Figma
            - **Office Suite:** Microsoft Office
            - **AI Tools:** ChatGPT, Deepseek, Copilot
            """)
            
        with col2:
            st.markdown("""
            ### Soft Skills
            - **Communication:** Presentation Skills, Technical Writing, Report Writing
            - **Analytical Thinking:** Data-driven Decision Making
            - **Project Management:** Task Prioritization, Timeline Management
            - **Research:** Market Research, Competitive Analysis
            - **Teamwork:** Strong Collaborative Spirit
            - **Adaptability:** Quick Learning, Problem-solving
            """)
        
        st.markdown("---")
