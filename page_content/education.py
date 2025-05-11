import streamlit as st

def education_page():
    # 获取语言设置
    language = st.session_state.get('language', '中文')
    
    if language == '中文':
        st.markdown("## 教育背景")
        
        st.markdown("""
        ### 市场营销学硕士（大数据营销方向）
        **香港中文大学** | *2024.08 - 2025.10*

        - 相关课程：社交媒体分析、营销机器学习、客户分析、整合营销传播、营销分析、数字营销、市场研究
        
        ### 金融学学士
        **四川大学** | *2020.09 - 2024.06*
        
        - 相关课程：国际投资、证券投资、金融风险管理、财务报表分析、金融计量经济学、金融工程
        """)
        
        st.markdown("---")
        
        st.markdown("## 证书")
        
        col1, col2, col3 = st.columns(3, gap="small")
        
        with col1:
            st.markdown("""
            ### 雅思 7.0
            **Cambridge** | *2023.10*
            """)
        
        st.markdown("---")
        
        st.markdown("## 学术项目")
        
        projects = [
            {
                "title": "3CE与aespa合作的整合营销传播策划",
                "date": "2025.01",
                "description": "通过K-pop合作，制定战略性整合营销传播计划，促进3CE品牌从价值导向定位向高端美妆市场转型。",
                "achievements": [
                    "对3CE化妆品品牌进行STP分析",
                    "使用5 Box分析方法设计整合营销传播方案，刷新品牌形象"
                ]
            },
            {
                "title": "霸王茶姬奥运营销活动效果评估",
                "date": "2024.12",
                "description": "分析社交媒体数据以评估营销活动效果。",
                "achievements": [
                    "使用Python和Octopus抓取并预处理来自微博和小红书的社交媒体数据",
                    "运用Python进行情感分析和关键词提取，评估消费者感知"
                ]
            },
            {
                "title": "百度网盘市场营销分析",
                "date": "2024.11",
                "description": "对百度网盘用户偏好和市场定位进行全面的营销分析。",
                "achievements": [
                    "设计并执行问卷调查，收集用户对各种属性的反馈",
                    "使用R Studio进行描述性分析和多元线性回归",
                    "使用Sawtooth开发选择模型进行市场份额预测"
                ]
            },
            {
                "title": "成都旅游业与经济增长 - VAR模型分析",
                "date": "2023.01",
                "description": "对旅游业对成都经济增长影响的统计分析。",
                "achievements": [
                    "分析GDP、国内游客和旅游收入的时间序列数据（2000-2020）",
                    "进行平稳性检验和Johansen协整检验",
                    "进行VAR建模，包括脉冲响应和方差分解分析"
                ]
            },
            {
                "title": "利率平价理论偏差分析",
                "date": "2022.10",
                "description": "分析美元-人民币汇率与利率平价理论的偏差。",
                "achievements": [
                    "使用时间序列方法分析汇率数据",
                    "使用STATA创建一阶和二阶差分线图",
                    "为外汇储备和交易策略提供建议"
                ]
            }
        ]
        
        for i, project in enumerate(projects):
            with st.expander(f"{project['title']} | *{project['date']}*", expanded=i==0):
                st.markdown(f"**项目描述：** {project['description']}")
                st.markdown("**主要成果：**")
                for achievement in project['achievements']:
                    st.markdown(f"- {achievement}")
        
        st.markdown("---")
    else:
        st.markdown("## Education")
        
        st.markdown("""
        ### Master of Science in Marketing (Big Data Marketing)
        **Chinese University of Hong Kong** | *August 2024 - October 2025*

        - Relevant Coursework: Social Media Analytics, Machine Learning in Marketing, Customer Analytics, Integrated Marketing Communication, Marketing Analytics, Digital Marketing, Marketing Research
        
        ### Bachelor of Economics in Finance
        **Sichuan University** | *September 2020 - June 2024*
        
        - Relevant Coursework: International Investment, Security Investment, Financial Risk Management, Financial Statement Analysis, Financial Econometrics, Financial Engineering
        """)
        
        st.markdown("---")
        
        st.markdown("## Certifications")
        
        col1, col2, col3 = st.columns(3, gap="small")
        
        with col1:
            st.markdown("""
            ### IELTS 7.0
            **Cambridge** | *October 2023*
            """)
        
        st.markdown("---")
        
        st.markdown("## Academic Projects")
        
        projects = [
            {
                "title": "The IMC Campaign for the 3CE and aespa Collaboration",
                "date": "January 2025",
                "description": "Developed a strategic IMC campaign to facilitate 3CE's brand transformation from value-oriented positioning to premium beauty segment through K-pop collaboration.",
                "achievements": [
                    "Conducted STP analysis for the 3CE cosmetics brand",
                    "Designed an IMC campaign to refresh brand image using 5 Box analysis method"
                ]
            },
            {
                "title": "Exploration of the Effectiveness of CHAGEE's Olympics Marketing Campaign",
                "date": "December 2024",
                "description": "Analyzed social media data to evaluate marketing campaign effectiveness.",
                "achievements": [
                    "Utilized Python and Octopus to scrape and preprocess social media data from Weibo and Xiaohongshu",
                    "Conducted sentiment analysis and keyword extraction using Python to evaluate consumer perceptions"
                ]
            },
            {
                "title": "Baidu Netdisk Marketing Analysis",
                "date": "November 2024",
                "description": "Comprehensive marketing analysis of Baidu Netdisk user preferences and market positioning.",
                "achievements": [
                    "Designed and executed a survey to gather user feedback on various attributes",
                    "Performed descriptive analysis and multiple linear regression using R Studio",
                    "Developed a choice model using Sawtooth for market share prediction"
                ]
            },
            {
                "title": "Tourism and Economic Growth in Chengdu - VAR Model Analysis",
                "date": "January 2023",
                "description": "Statistical analysis of tourism's impact on Chengdu's economic growth.",
                "achievements": [
                    "Analyzed time series data of GDP, Domestic Tourists and Tourism Income (2000-2020)",
                    "Performed Smoothness test and Johansen cointegration test",
                    "Conducted VAR modeling with impulse response and variance decomposition analysis"
                ]
            },
            {
                "title": "Interest Rate Parity Theory Deviation Analysis",
                "date": "October 2022",
                "description": "Analysis of USD-CNY exchange rate deviations from Interest Rate Parity theory.",
                "achievements": [
                    "Analyzed exchange rate data using time series methods",
                    "Created first-order and second-order difference line plots using STATA",
                    "Provided recommendations for foreign exchange reserves and trading strategies"
                ]
            }
        ]
        
        for i, project in enumerate(projects):
            with st.expander(f"{project['title']} | *{project['date']}*", expanded=i==0):
                st.markdown(f"**Description:** {project['description']}")
                st.markdown("**Achievements:**")
                for achievement in project['achievements']:
                    st.markdown(f"- {achievement}")
        
        st.markdown("---")