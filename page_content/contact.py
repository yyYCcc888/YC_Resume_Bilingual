import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def contact_page():
    # 获取语言设置
    language = st.session_state.get('language', '中文')
    
    if language == '中文':
        st.markdown("## 与我联络")
        
        st.markdown("""
        欢迎通过以下方式与我联系：
        
        ### 联系方式
        - **邮箱**: [1378188281@qq.com](mailto:1378188281@qq.com)
        - **电话**: +852 56659168 | +86 15980247560
        - **地址**: 中国香港特别行政区荃湾
        """)
        
        st.markdown("### 留言箱")
        
        with st.form("contact_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                name = st.text_input("姓名")
                email = st.text_input("邮箱")
                
            with col2:
                subject = st.text_input("主题")
                
            message = st.text_area("留言内容", height=150)
            
            submitted = st.form_submit_button("发送留言")
            
            if submitted:
                if name and email and subject and message:
                    try:
                        # 邮件设置
                        sender_email = "yanchen88988@gmail.com"  # 发送邮件的邮箱
                        sender_password = "jher cvur xttr ukvg"  # 邮箱的应用专用密码
                        receiver_email = "1378188281@qq.com"  # 接收邮件的邮箱
                        
                        # 创建邮件内容
                        msg = MIMEMultipart()
                        msg['From'] = sender_email
                        msg['To'] = receiver_email
                        msg['Subject'] = f"网站留言: {subject}"
                        
                        body = f"""
                        收到新的留言：
                        
                        姓名: {name}
                        邮箱: {email}
                        主题: {subject}
                        消息: {message}
                        """
                        
                        msg.attach(MIMEText(body, 'plain'))
                        
                        # 连接到SMTP服务器并发送邮件
                        with smtplib.SMTP('smtp.gmail.com', 587) as server:
                            server.starttls()
                            server.login(sender_email, sender_password)
                            server.send_message(msg)
                        
                        st.success("感谢您的留言！我会尽快回复。")
                    except Exception as e:
                        st.error(f"发送失败：{str(e)}")
                else:
                    st.warning("请填写所有必填字段。")
        
        st.markdown("---")
        
        st.markdown("""
        ### 工作时间
        我通常在周一至周五的上午10:00至下午5:00期间可以进行线上会议。
        如需安排通话或视频会议，请发送邮件与我联系。
        """)
    else:
        st.markdown("## Contact Me")
        
        st.markdown("""
        Feel free to reach out to me through any of the following channels:
        
        ### Direct Contact
        - **Email**: [1378188281@qq.com](mailto:1378188281@qq.com)
        - **Phone**: +852 56659168 | +86 15980247560
        - **Location**: Tsuen Wan NT, Hong Kong SAR, China
        """)
        
        st.markdown("### Send Me a Message")
        
        with st.form("contact_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                name = st.text_input("Name")
                email = st.text_input("Email")
                
            with col2:
                subject = st.text_input("Subject")
                
            message = st.text_area("Message", height=150)
            
            submitted = st.form_submit_button("Send Message")
            
            if submitted:
                if name and email and subject and message:
                    try:
                        # 邮件设置
                        sender_email = "yanchen88988@gmail.com"  # 发送邮件的邮箱
                        sender_password = "jher cvur xttr ukvg"  # 邮箱的应用专用密码
                        receiver_email = "1378188281@qq.com"  # 接收邮件的邮箱
                        
                        # 创建邮件内容
                        msg = MIMEMultipart()
                        msg['From'] = sender_email
                        msg['To'] = receiver_email
                        msg['Subject'] = f"网站留言: {subject}"
                        
                        body = f"""
                        收到新的留言：
                        
                        姓名: {name}
                        邮箱: {email}
                        主题: {subject}
                        消息: {message}
                        """
                        
                        msg.attach(MIMEText(body, 'plain'))
                        
                        # 连接到SMTP服务器并发送邮件
                        with smtplib.SMTP('smtp.gmail.com', 587) as server:
                            server.starttls()
                            server.login(sender_email, sender_password)
                            server.send_message(msg)
                        
                        st.success("Thank you for your message! I will reply soon.")
                    except Exception as e:
                        st.error(f"Failed to send: {str(e)}")
                else:
                    st.warning("Please fill in all required fields.")
        
        st.markdown("---")
        
        st.markdown("""
        ### Available Hours
        I am generally available for virtual meetings Monday through Friday, 10:00 AM - 5:00 PM (UTC+8).
        Please email me to schedule a call or video conference.
        """)
