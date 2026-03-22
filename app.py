import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# ─────────────────────────────────────────
#  PAGE CONFIG
# ─────────────────────────────────────────
st.set_page_config(
    page_title="Career Intelligence",
    page_icon="🚀",
    layout="wide"
)

# ─────────────────────────────────────────
#  CUSTOM CSS
# ─────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background-color: #f0f4ff;
}

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
    background: linear-gradient(160deg, #1e3a8a, #2563eb);
    color: white;
}
section[data-testid="stSidebar"] * {
    color: white !important;
}
section[data-testid="stSidebar"] .stRadio label {
    font-size: 16px;
    padding: 8px 0;
}

/* ── Cards ── */
.card {
    background: white;
    padding: 28px 24px;
    border-radius: 18px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.07);
    height: 100%;
    transition: transform 0.2s;
}
.card:hover {
    transform: translateY(-3px);
}
.card-icon {
    font-size: 34px;
    margin-bottom: 10px;
}
.card-title {
    font-size: 18px;
    font-weight: 700;
    color: #1e3a8a;
    margin-bottom: 6px;
}
.card-desc {
    font-size: 14px;
    color: #64748b;
    line-height: 1.6;
}

/* ── Hero ── */
.hero-title {
    font-size: 46px;
    font-weight: 700;
    color: #1e3a8a;
    line-height: 1.2;
}
.hero-sub {
    font-size: 19px;
    color: #475569;
    margin-top: 8px;
}

/* ── Section headers ── */
.section-header {
    font-size: 26px;
    font-weight: 700;
    color: #1e3a8a;
    margin-bottom: 4px;
}
.section-divider {
    height: 4px;
    width: 60px;
    background: linear-gradient(90deg, #2563eb, #60a5fa);
    border-radius: 10px;
    margin-bottom: 20px;
}

/* ── Skill badge ── */
.skill-badge-have {
    display: inline-block;
    background: #dcfce7;
    color: #166534;
    border-radius: 20px;
    padding: 5px 14px;
    margin: 4px;
    font-size: 13px;
    font-weight: 600;
}
.skill-badge-missing {
    display: inline-block;
    background: #fee2e2;
    color: #991b1b;
    border-radius: 20px;
    padding: 5px 14px;
    margin: 4px;
    font-size: 13px;
    font-weight: 600;
}

/* ── Score box ── */
.score-box {
    background: linear-gradient(135deg, #1e3a8a, #2563eb);
    color: white;
    padding: 24px;
    border-radius: 18px;
    text-align: center;
}
.score-number {
    font-size: 52px;
    font-weight: 700;
    line-height: 1;
}
.score-label {
    font-size: 14px;
    opacity: 0.85;
    margin-top: 4px;
}

/* ── Resource link ── */
.resource-row {
    background: white;
    border-radius: 12px;
    padding: 14px 18px;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}
.resource-name {
    font-weight: 600;
    color: #1e3a8a;
    font-size: 15px;
}
.resource-link {
    color: #2563eb;
    font-size: 13px;
    text-decoration: none;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
#  DATA
# ─────────────────────────────────────────
career_data = {
    "Data Scientist": {
        "salary": "₹8L – ₹25L per year",
        "emoji": "🔬",
        "skills": ["Python", "Statistics", "Machine Learning", "SQL", "Data Visualization"]
    },
    "AI Engineer": {
        "salary": "₹10L – ₹30L per year",
        "emoji": "🤖",
        "skills": ["Python", "Deep Learning", "TensorFlow", "NLP", "MLOps"]
    },
    "Frontend Developer": {
        "salary": "₹5L – ₹18L per year",
        "emoji": "🎨",
        "skills": ["HTML", "CSS", "JavaScript", "React", "UI/UX"]
    },
    "Backend Developer": {
        "salary": "₹6L – ₹20L per year",
        "emoji": "⚙️",
        "skills": ["Python", "Node.js", "APIs", "Databases", "System Design"]
    },
    "Cybersecurity Analyst": {
        "salary": "₹6L – ₹22L per year",
        "emoji": "🔐",
        "skills": ["Networking", "Ethical Hacking", "Security Tools", "Risk Analysis", "Linux"]
    },
    "Cloud Engineer": {
        "salary": "₹8L – ₹28L per year",
        "emoji": "☁️",
        "skills": ["AWS", "Azure", "Docker", "Kubernetes", "Linux"]
    }
}

learning_resources = {
    "Python":           ("learnpython.org",          "https://www.learnpython.org"),
    "Statistics":       ("Khan Academy",              "https://www.khanacademy.org/math/statistics-probability"),
    "Machine Learning": ("Coursera – Andrew Ng",      "https://www.coursera.org/learn/machine-learning"),
    "SQL":              ("SQLZoo",                    "https://sqlzoo.net"),
    "Data Visualization":("Matplotlib Docs",          "https://matplotlib.org/stable/tutorials/index.html"),
    "Deep Learning":    ("DeepLearning.AI",           "https://www.deeplearning.ai"),
    "TensorFlow":       ("TensorFlow Tutorials",      "https://www.tensorflow.org/learn"),
    "NLP":              ("Hugging Face Course",       "https://huggingface.co/learn/nlp-course"),
    "MLOps":            ("MLOps.community",           "https://mlops.community"),
    "HTML":             ("W3Schools HTML",            "https://www.w3schools.com/html"),
    "CSS":              ("W3Schools CSS",             "https://www.w3schools.com/css"),
    "JavaScript":       ("javascript.info",           "https://javascript.info"),
    "React":            ("React Official Docs",       "https://react.dev/learn"),
    "UI/UX":            ("Google UX Design – Coursera","https://www.coursera.org/professional-certificates/google-ux-design"),
    "Node.js":          ("Node.js Docs",              "https://nodejs.org/en/learn"),
    "APIs":             ("REST API Tutorial",         "https://restfulapi.net"),
    "Databases":        ("PostgreSQL Tutorial",       "https://www.postgresqltutorial.com"),
    "System Design":    ("System Design Primer",      "https://github.com/donnemartin/system-design-primer"),
    "Networking":       ("Cisco CCNA",                "https://www.cisco.com/c/en/us/training-events/training-certifications/certifications/entry/ccna.html"),
    "Ethical Hacking":  ("TryHackMe",                 "https://tryhackme.com"),
    "Security Tools":   ("Cybrary",                   "https://www.cybrary.it"),
    "Risk Analysis":    ("ISACA Resources",           "https://www.isaca.org/resources"),
    "Linux":            ("Linux Journey",             "https://linuxjourney.com"),
    "AWS":              ("AWS Training",              "https://aws.amazon.com/training"),
    "Azure":            ("Microsoft Learn",           "https://learn.microsoft.com/en-us/azure"),
    "Docker":           ("Docker Docs",               "https://docs.docker.com/get-started"),
    "Kubernetes":       ("Kubernetes Tutorials",      "https://kubernetes.io/docs/tutorials"),
}

# ─────────────────────────────────────────
#  SIDEBAR
# ─────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🚀 Career Intelligence")
    st.markdown("---")
    menu = st.radio(
        "Navigate",
        ["🏠  Home", "📊  Skill Gap Analyzer", "📈  Progress Tracker"],
        label_visibility="collapsed"
    )
    st.markdown("---")
    st.markdown("**Built with Streamlit & Plotly**")


# ═══════════════════════════════════════════
#  HOME PAGE
# ═══════════════════════════════════════════
if menu == "🏠  Home":
    st.markdown('<div class="hero-title">Career Intelligence Dashboard 🚀</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-sub">Build Skills. Track Progress. Get Job Ready.</div>', unsafe_allow_html=True)
    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-icon">📊</div>
            <div class="card-title">Skill Gap Analysis</div>
            <div class="card-desc">Select your target role and see exactly which skills you're missing — with a visual chart.</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-icon">💰</div>
            <div class="card-title">Salary Insights</div>
            <div class="card-desc">Know the real market salary range for your target role before you start applying.</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <div class="card-icon">📈</div>
            <div class="card-title">Progress Tracking</div>
            <div class="card-desc">Track your weekly study hours and skill completion to stay on schedule.</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # ── Quick stats row ──
    st.markdown('<div class="section-header">Quick Overview</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    q1, q2, q3, q4 = st.columns(4)
    q1.metric("Total Roles Available", len(career_data))
    q2.metric("Total Skills Tracked", sum(len(v["skills"]) for v in career_data.values()))
    q3.metric("Learning Resources", len(learning_resources))
    q4.metric("Pages", "3")

    st.write("")
    st.success("👈 Use the sidebar to navigate to the Skill Gap Analyzer and start your journey!")


# ═══════════════════════════════════════════
#  SKILL GAP ANALYZER
# ═══════════════════════════════════════════
elif menu == "📊  Skill Gap Analyzer":
    st.markdown('<div class="section-header">📊 Skill Gap Analyzer</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    # Role selector
    role_options = list(career_data.keys())
    selected_role = st.selectbox(
        "🎯 Choose Your Target Role",
        role_options,
        format_func=lambda r: f"{career_data[r]['emoji']}  {r}"
    )

    required_skills = career_data[selected_role]["skills"]

    # Skills the user has
    user_skills = st.multiselect(
        "✅ Select Skills You Already Have",
        required_skills,
        help="Pick every skill from the list that you already know."
    )

    missing_skills = [s for s in required_skills if s not in user_skills]
    score = int((len(user_skills) / len(required_skills)) * 100) if required_skills else 0

    st.write("")

    # ── Score + Metrics ──
    m0, m1, m2, m3 = st.columns([1.2, 1, 1, 1])

    with m0:
        st.markdown(f"""
        <div class="score-box">
            <div class="score-number">{score}%</div>
            <div class="score-label">Job Readiness Score</div>
        </div>
        """, unsafe_allow_html=True)

    with m1:
        st.metric("Required Skills", len(required_skills))
    with m2:
        st.metric("Skills You Have ✅", len(user_skills))
    with m3:
        st.metric("Skills Missing ❌", len(missing_skills))

    st.write("")
    st.progress(score / 100)
    st.caption(f"You are **{score}%** ready for the **{selected_role}** role.")

    st.write("")

    # ── Bar Chart ──
    st.markdown('<div class="section-header" style="font-size:20px">Skill Gap Chart</div>', unsafe_allow_html=True)

    colors = ["#22c55e" if s in user_skills else "#ef4444" for s in required_skills]
    labels = ["✅ Have" if s in user_skills else "❌ Missing" for s in required_skills]

    fig = go.Figure(go.Bar(
        x=required_skills,
        y=[1] * len(required_skills),
        marker_color=colors,
        text=labels,
        textposition="inside",
        insidetextanchor="middle",
        textfont=dict(color="white", size=13)
    ))
    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        yaxis_visible=False,
        xaxis=dict(tickfont=dict(size=13)),
        height=280,
        margin=dict(l=10, r=10, t=20, b=10),
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)

    st.write("")

    # ── Skill Badges ──
    col_have, col_miss = st.columns(2)

    with col_have:
        st.markdown("**Skills You Have ✅**")
        if user_skills:
            badges = "".join(f'<span class="skill-badge-have">✅ {s}</span>' for s in user_skills)
            st.markdown(badges, unsafe_allow_html=True)
        else:
            st.info("No skills selected yet.")

    with col_miss:
        st.markdown("**Skills You're Missing ❌**")
        if missing_skills:
            badges = "".join(f'<span class="skill-badge-missing">❌ {s}</span>' for s in missing_skills)
            st.markdown(badges, unsafe_allow_html=True)
        else:
            st.success("No missing skills — you're fully ready! 🎉")

    st.write("")

    # ── Salary Info ──
    st.info(f"💰 **Salary Range for {selected_role}:** {career_data[selected_role]['salary']}")

    st.write("")

    # ── Learning Resources ──
    if missing_skills:
        st.markdown('<div class="section-header" style="font-size:20px">📚 Recommended Resources</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
        st.caption("Click the links below to start learning each missing skill.")

        for skill in missing_skills:
            if skill in learning_resources:
                name, url = learning_resources[skill]
                st.markdown(f"""
                <div class="resource-row">
                    <span class="resource-name">🔴 {skill}</span>
                    <a class="resource-link" href="{url}" target="_blank">📖 {name} →</a>
                </div>
                """, unsafe_allow_html=True)

    elif score == 100:
        st.balloons()
        st.success("🎉 Congratulations! You have ALL the required skills. Start applying now!")


# ═══════════════════════════════════════════
#  PROGRESS TRACKER
# ═══════════════════════════════════════════
elif menu == "📈  Progress Tracker":
    st.markdown('<div class="section-header">📈 Skill Progress Tracker</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    col_input, col_chart = st.columns([1, 1.5])

    with col_input:
        st.markdown("#### Enter Your Progress")
        total_skills   = st.number_input("Total Skills Required",  min_value=1,  max_value=50, value=10)
        completed      = st.number_input("Skills Completed So Far", min_value=0, max_value=50, value=0)
        hours_daily    = st.number_input("Study Hours Per Day",     min_value=0, max_value=24, value=2)
        hours_weekly   = st.number_input("Study Hours This Week",   min_value=0, max_value=168, value=6)

        progress = int((completed / total_skills) * 100) if total_skills else 0

        st.write("")
        st.markdown(f"""
        <div class="score-box">
            <div class="score-number">{progress}%</div>
            <div class="score-label">Overall Learning Progress</div>
        </div>
        """, unsafe_allow_html=True)

        st.write("")
        st.progress(progress / 100)

    with col_chart:
        st.markdown("#### Progress Breakdown")

        # Donut chart
        remaining = total_skills - completed
        donut = go.Figure(go.Pie(
            labels=["Completed ✅", "Remaining 🔄"],
            values=[max(completed, 0), max(remaining, 0)],
            hole=0.6,
            marker_colors=["#22c55e", "#e2e8f0"],
            textinfo="label+percent",
            textfont_size=13
        ))
        donut.update_layout(
            showlegend=False,
            margin=dict(l=10, r=10, t=10, b=10),
            height=280,
            paper_bgcolor="white"
        )
        st.plotly_chart(donut, use_container_width=True)

    st.write("")

    # ── Study hours feedback ──
    st.markdown("#### 🔥 Weekly Study Summary")

    h1, h2, h3 = st.columns(3)
    h1.metric("Hours This Week",    f"{hours_weekly}h")
    h2.metric("Hours Per Day",      f"{hours_daily}h")
    h3.metric("Skills Left",        remaining)

    st.write("")

    if hours_weekly == 0:
        st.warning("⚠️ You haven't studied this week. Start today — even 1 hour counts!")
    elif hours_weekly < 5:
        st.info(f"📘 You studied {hours_weekly} hours this week. Try to aim for at least 7 hours.")
    elif hours_weekly < 10:
        st.success(f"🔥 Great work! {hours_weekly} hours this week. Keep it up!")
    else:
        st.success(f"🚀 Excellent! {hours_weekly} hours this week — you're on fire!")

    # ── Estimated completion ──
    if hours_daily > 0 and remaining > 0:
        days_needed = (remaining * 7) // hours_daily   # rough estimate: 7h per skill
        st.info(f"⏱️ At **{hours_daily}h/day**, you could complete all remaining skills in roughly **{days_needed} days**.")
    elif remaining == 0:
        st.success("✅ You've completed all skills — amazing work!")