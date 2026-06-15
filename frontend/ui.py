import streamlit as st
from agent.email_agent import EmailAgent

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Smart Email Automation Agent",
    page_icon="🚀",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg,#eef2ff,#f8fafc);
}

/* Hide Streamlit default items */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Main container */
.block-container{
    padding-top: 1rem;
    padding-bottom: 2rem;
}

/* Title */
.main-title{
    text-align:center;
    font-size:52px;
    font-weight:800;
    background: linear-gradient(90deg,#8b5cf6,#6d28d9);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.sub-title{
    text-align:center;
    color:#64748b;
    font-size:18px;
    margin-bottom:30px;
}

/* Cards */
.card{
    background:white;
    padding:25px;
    border-radius:20px;
    box-shadow:0px 8px 20px rgba(0,0,0,0.08);
    border:1px solid #e5e7eb;
}

/* Input boxes */
.stTextInput input{
    border-radius:12px;
    border:2px solid #dbeafe;
}

/* Buttons */
.stButton > button{
    width:100%;
    height:55px;
    border:none;
    border-radius:15px;
    background:linear-gradient(
        90deg,
        #2563eb,
        #7c3aed
    );
    color:white;
    font-size:18px;
    font-weight:bold;
}

/* Metrics */
[data-testid="metric-container"]{
    background:white;
    padding:15px;
    border-radius:15px;
    box-shadow:0px 4px 15px rgba(0,0,0,0.05);
}

/* Footer */
.footer{
    text-align:center;
    color:#64748b;
    font-size:14px;
    margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
with st.sidebar:

    st.title("🚀 Agent Dashboard")

    st.markdown("---")

    st.markdown("""
    ### Features

    ✅ AI Email Generation

    ✅ SMTP Integration

    ✅ Workflow Automation

    ✅ Activity Logging

    ✅ Modern UI
    """)

    st.markdown("---")

    st.success("🟢 System Online")

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown("""
<div class='main-title'>
⚡📨 Smart AI Email Automation
</div>

<div class='sub-title'>
Generate and Send AI-Powered Emails Instantly
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# MAIN SECTION
# --------------------------------------------------
left, right = st.columns(2)

with left:

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.markdown("### 📧 Email Configuration")

    receiver = st.text_input(
        "Recipient Email",
        placeholder="example@gmail.com"
    )

    goal = st.selectbox(
        "Select Email Type",
        [
            "welcome",
            "reminder",
            "internship"
        ]
    )

    send_btn = st.button(
        "🚀 Generate & Send Email"
    )

    st.markdown("</div>", unsafe_allow_html=True)

with right:

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.markdown("### 🤖 Agent Workflow")

    st.success("✅ Analyze Goal")

    st.info("📄 Select Template")

    st.warning("✍️ Generate Content")

    st.info("📤 Send Email")

    st.success("📁 Save Log")

    st.markdown("</div>", unsafe_allow_html=True)

# --------------------------------------------------
# EMAIL PROCESS
# --------------------------------------------------
if send_btn:

    if receiver == "":

        st.error(
            "Please enter receiver email."
        )

    else:

        with st.spinner(
            "🤖 Agent Working..."
        ):

            agent = EmailAgent()

            result = agent.run(
                receiver,
                goal
            )

        st.success(
            "✅ Email Sent Successfully"
        )

        st.markdown("### 📄 Generated Email")

        st.text_area(
            "",
            result,
            height=250
        )

# --------------------------------------------------
# METRICS
# --------------------------------------------------
st.markdown("---")

st.markdown("## 📊 System Statistics")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "📄 Templates",
        "3"
    )

with c2:
    st.metric(
        "🤖 Agent Status",
        "Active"
    )

with c3:
    st.metric(
        "📨 SMTP",
        "Connected"
    )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("---")

st.markdown("""
<div class='footer'>
Built with ❤️ using Python • Streamlit • SMTP • Agentic AI
</div>
""", unsafe_allow_html=True)

