import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta
import altair as alt

# Page configuration
st.set_page_config(
    page_title="IELTS Prep Hub - Huzaifa",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E88E5;
        text-align: center;
    }
    .resource-card {
        background-color: #f5f7f9;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 10px;
        border-left: 4px solid #1E88E5;
    }
    .resource-header {
        color: #1E88E5;
        font-size: 1.2rem;
        margin-bottom: 5px;
    }
    .progress-card {
        background-color: #f0f7ff;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0px;
    }
    .tip-card {
        background-color: #e3f2fd;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0px;
        border-left: 4px solid #4CAF50;
    }
    .highlight {
        background-color: #fffde7;
        padding: 2px 5px;
        border-radius: 3px;
    }
</style>
""", unsafe_allow_html=True)

# Header with logo
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.markdown("<h1 class='main-header'>🎯 IELTS Prep Hub</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Your all-in-one smart portal for 8+ Band IELTS preparation</p>", unsafe_allow_html=True)

# User profile and progress
with st.sidebar:
    st.image("https://via.placeholder.com/150x150.png?text=Huzaifa", width=150)
    st.title("👋 Hi, Huzaifa!")
    
    today = datetime.now()
    target_date_str = st.sidebar.date_input("Target Exam Date", today + timedelta(days=60))
    target_date = datetime.combine(target_date_str, datetime.min.time())
    days_left = (target_date - today).days
    
    st.info(f"📅 **{days_left} days** left until your exam")
    
    # Mock progress data
    progress_data = {
        "Reading": 75,
        "Writing": 65,
        "Listening": 80,
        "Speaking": 70
    }
    
    st.subheader("📊 Your Progress")
    for skill, progress in progress_data.items():
        st.markdown(f"{skill}: {progress}%")
        st.progress(progress/100)
    
    st.title("📂 Navigation")
    section = st.radio("Go to", [
        "🏠 Dashboard",
        "📚 Books & PDFs",
        "🎧 Podcasts & Audio",
        "📺 Video Lessons",
        "📝 Mock Tests & Practice",
        "🗣️ Speaking Practice",
        "✍️ Writing Practice",
        "📆 Study Plan",
        "📌 Tips & Tools",
        "🏅 My Progress"
    ])

# Daily challenge function
def daily_challenge():
    st.subheader("🎯 Daily Challenge")
    challenges = [
        "Learn and use 5 new academic vocabulary words today",
        "Practice a 30-minute IELTS listening test",
        "Write a Task 2 essay on 'Environmental Issues'",
        "Read a news article from The Economist and summarize it",
        "Practice speaking for 15 minutes on your favorite hobby",
        "Analyze a complex chart or graph and describe it in writing"
    ]
    
    vocab_words = ["Mitigate", "Scrutinize", "Paradigm", "Ubiquitous", "Implement", 
                  "Preliminary", "Robust", "Coherent", "Pragmatic", "Facilitate"]
    
    with st.container():
        st.markdown(f"""
        <div class="tip-card">
            <h3>Today's Challenge:</h3>
            <p>{random.choice(challenges)}</p>
            <h4>Vocabulary Boost:</h4>
            <p>Try to use these words today: <span class="highlight">{", ".join(random.sample(vocab_words, 3))}</span></p>
        </div>
        """, unsafe_allow_html=True)

# Function for rendering resource links with icons
def resource_link(title, url, icon="🔗", description=""):
    return f"""
    <div class="resource-card">
        <h3 class="resource-header">{icon} {title}</h3>
        <p>{description}</p>
        <a href="{url}" target="_blank">Access Resource →</a>
    </div>
    """

# Dashboard
if section == "🏠 Dashboard":
    st.header("🏠 Your IELTS Dashboard")
    
    # Progress summary
    col1, col2 = st.columns(2)
    
    with col1:
        daily_challenge()
    
    with col2:
        st.subheader("🚀 Quick Links")
        st.markdown("""
        - [📝 Today's Practice Test](#)
        - [📚 Continue Reading Practice](#)
        - [✍️ Writing Task Feedback](#)
        - [🎧 Today's Listening Exercise](#)
        """)
    
    # Study streak
    streak_data = pd.DataFrame({
        'date': pd.date_range(start=today-timedelta(days=9), end=today, freq='D'),
        'minutes': [45, 30, 60, 0, 75, 90, 30, 45, 60, 120]
    })
    
    st.subheader("⏱️ Your Study Streak")
    chart = alt.Chart(streak_data).mark_bar().encode(
        x=alt.X('date:T', title='Date'),
        y=alt.Y('minutes:Q', title='Minutes Studied'),
        color=alt.condition(
            alt.datum.minutes > 0,
            alt.value('#1E88E5'),
            alt.value('#e0e0e0')
        ),
        tooltip=['date', 'minutes']
    ).properties(height=200)
    
    st.altair_chart(chart, use_container_width=True)
    
    # Recent feedback
    st.subheader("📋 Recent Feedback")
    st.markdown("""
    <div class="progress-card">
        <h4>Writing Task 2 - Technology Essay</h4>
        <p>Overall Band: <strong>7.0</strong></p>
        <p>Strengths: Good paragraph structure, appropriate vocabulary</p>
        <p>Areas to improve: Work on complex sentence structures, develop ideas more fully</p>
    </div>
    """, unsafe_allow_html=True)

elif section == "📚 Books & PDFs":
    st.header("📚 Books and PDF Resources")
    
    st.markdown(resource_link(
        "Cambridge IELTS Books 1–19 (PDF + Audio)",
        "https://www.ieltsxpress.com/download-all-cambridge-ielts-books-pdf-audio-for-free-cambridge-1-14-free-download/",
        "📕",
        "Official Cambridge IELTS practice tests with audio files"
    ), unsafe_allow_html=True)
    
    st.markdown(resource_link(
        "Barron's IELTS Superpack PDF",
        "https://archive.org/details/barronsielts20164th528p",
        "📗",
        "Comprehensive IELTS guide with practice tests and strategies"
    ), unsafe_allow_html=True)
    
    st.markdown(resource_link(
        "IELTS Writing Task 2 eBook by IELTS Liz",
        "https://ieltsliz.com/ideas-for-ielts-essays-e-book/",
        "📘",
        "Expert tips and sample essays for Writing Task 2"
    ), unsafe_allow_html=True)
    
    st.markdown(resource_link(
        "Official IELTS Guide PDF",
        "https://ielts.idp.com/-/media/pdfs/ielts-preparation-materials.ashx",
        "📙",
        "Official guide from IELTS examiners with test format details"
    ), unsafe_allow_html=True)
    
    st.markdown(resource_link(
        "IELTS Academic Word List PDF",
        "https://www.ieltsbuddy.com/support-files/academic-word-list.pdf",
        "📔",
        "Essential academic vocabulary for IELTS success"
    ), unsafe_allow_html=True)

elif section == "🎧 Podcasts & Audio":
    st.header("🎧 IELTS Podcasts & Listening Practice")
    
    st.markdown(resource_link(
        "IELTS Speaking for Success – Spotify",
        "https://open.spotify.com/show/1HkLkU0sZC0gk1bX1i1U1x",
        "🎙️",
        "Expert tips and practice for improving IELTS speaking scores"
    ), unsafe_allow_html=True)
    
    st.markdown(resource_link(
        "BBC Learning English – 6 Minute English",
        "https://www.bbc.co.uk/learningenglish",
        "🇬🇧",
        "Short, topical discussions to improve listening comprehension"
    ), unsafe_allow_html=True)
    
    st.markdown(resource_link(
        "IELTS Energy Podcast – All Ears English",
        "https://www.allearsenglish.com/episodes/ielts",
        "⚡",
        "Dynamic podcast with strategies and motivation for test-takers"
    ), unsafe_allow_html=True)
    
    st.markdown(resource_link(
        "Luke's English Podcast",
        "https://teacherluke.co.uk/",
        "🎧",
        "Popular podcast for improving natural English listening skills"
    ), unsafe_allow_html=True)
    
    st.markdown(resource_link(
        "TED Talks Audio – Spotify",
        "https://open.spotify.com/show/2WTmtt13C6v0CZkOe5zSKz",
        "🔊",
        "Engaging talks on various topics for advanced listening practice"
    ), unsafe_allow_html=True)
    
    # Interactive listening practice
    st.subheader("🎯 Quick Listening Practice")
    with st.expander("Listen and choose the correct answer"):
        st.audio("https://soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
        st.radio("The speaker mainly discusses:", [
            "Environmental challenges in urban areas",
            "Economic benefits of public transportation",
            "Historical development of city infrastructure",
            "Social implications of urban planning"
        ])
        if st.button("Check Answer"):
            st.success("Correct! The speaker discusses economic benefits of public transportation.")

elif section == "📺 Video Lessons":
    st.header("📺 Best IELTS Video Channels")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(resource_link(
            "IELTS Liz – YouTube",
            "https://www.youtube.com/@ieltsliz",
            "🎬",
            "Clear explanations and tips from an experienced IELTS teacher"
        ), unsafe_allow_html=True)
        
        st.markdown(resource_link(
            "E2 IELTS – YouTube",
            "https://www.youtube.com/@E2IELTS",
            "📹",
            "High-quality lessons with practice exercises and mock tests"
        ), unsafe_allow_html=True)
    
    with col2:
        st.markdown(resource_link(
            "IELTS Advantage – YouTube",
            "https://www.youtube.com/@IELTSadvantage",
            "🎥",
            "Strategic approaches to achieve band 7+ scores"
        ), unsafe_allow_html=True)
        
        st.markdown(resource_link(
            "AcademicEnglishHelp – YouTube",
            "https://www.youtube.com/@AcademicEnglishHelp",
            "📺",
            "Academic vocabulary and structures for IELTS writing"
        ), unsafe_allow_html=True)
    
    # Featured video
    st.subheader("🔥 Featured Video of the Day")
    st.video("https://www.youtube.com/watch?v=2LQqCSrjC8M")

elif section == "📝 Mock Tests & Practice":
    st.header("📝 Practice Tests & Mock Exams")
    
    st.markdown(resource_link(
        "ChatGPT IELTS Speaking Practice",
        "https://chatgpt.com/g/g-LDICowG2o-ielts-speaking-english-language-learning",
        "🤖",
        "AI-powered speaking practice with feedback and scoring"
    ), unsafe_allow_html=True)
    
    st.markdown(resource_link(
        "ChatGPT IELTS Writing Practice",
        "https://chatgpt.com/g/g-6WZpFnXna-ielts-writing-english-language-learning",
        "✍️",
        "AI writing coach with instant essay feedback"
    ), unsafe_allow_html=True)
    
    st.markdown(resource_link(
        "ChatGPT IELTS AI Checker",
        "https://chatgpt.com/g/g-YScypAShQ-ielts-ai-checker-speaking-and-writing-official-r",
        "🔍",
        "Performance analysis and band score prediction"
    ), unsafe_allow_html=True)
    
    st.markdown(resource_link(
        "Cambridge IELTS Practice Tests (1–13)",
        "https://practicepteonline.com/cambridge-ielts-1-13-tests/",
        "📝",
        "Official past papers from Cambridge Assessment"
    ), unsafe_allow_html=True)
    
    st.markdown(resource_link(
        "British Council IELTS Practice Tests",
        "https://takeielts.britishcouncil.org/take-ielts/prepare",
        "🇬🇧",
        "Free preparation materials from test administrators"
    ), unsafe_allow_html=True)
    
    # Quick practice test
    st.subheader("⚡ Quick Practice Test")
    with st.expander("Reading Mini-Test (5 minutes)"):
        st.markdown("""
        ### Read the passage and answer the questions below:
        
        The humble bicycle has experienced a resurgence in popularity in recent years, particularly in urban areas where traffic congestion and environmental concerns have prompted citizens and city planners alike to consider alternative modes of transportation. Many cities have invested in cycling infrastructure, including dedicated lanes, secure parking facilities, and bike-sharing schemes.
        
        **Questions:**
        """)
        
        st.radio("1. According to the passage, what has contributed to the increased popularity of bicycles?", [
            "Reduced cost of bicycles",
            "Traffic congestion and environmental concerns",
            "Government subsidies for cyclists",
            "Decline in public transportation options"
        ])
        
        st.radio("2. What investments have cities made to support cycling?", [
            "Free bicycles for commuters",
            "Reduced taxes for bicycle owners",
            "Cycling infrastructure such as lanes and parking",
            "Mandatory cycling training for residents"
        ])
        
        if st.button("Check Answers"):
            st.success("Correct answers: 1. Traffic congestion and environmental concerns, 2. Cycling infrastructure such as lanes and parking")

elif section == "🗣️ Speaking Practice":
    st.header("🗣️ Speaking Practice Tools")
    
    st.markdown(resource_link(
        "IELTS Speaking for Success – Spotify",
        "https://open.spotify.com/show/1HkLkU0sZC0gk1bX1i1U1x",
        "🎙️",
        "Expert tips and practice for improving IELTS speaking scores"
    ), unsafe_allow_html=True)
    
    st.markdown(resource_link(
        "IELTS Liz – Speaking Questions & Tips",
        "https://ieltsliz.com/ielts-speaking-free-lessons-essential-tips/",
        "👄",
        "Comprehensive guide to all three parts of the speaking test"
    ), unsafe_allow_html=True)
    
    st.markdown(resource_link(
        "Cue Card Generator",
        "https://ieltstools.com/speaking-part-2-cue-cards",
        "🎭",
        "Practice tool for Part 2 speaking topics with timer"
    ), unsafe_allow_html=True)
    
    st.markdown(resource_link(
        "Speechling – Free AI Coach",
        "https://speechling.com/",
        "🔊",
        "Record your speech and get feedback from AI and coaches"
    ), unsafe_allow_html=True)
    
    st.markdown(resource_link(
        "Record Your Voice – Practice Self Review",
        "https://vocaroo.com/",
        "🎤",
        "Simple tool to record and analyze your speaking practice"
    ), unsafe_allow_html=True)
    
    # Speaking practice tool
    st.subheader("🎯 Speaking Practice Generator")
    if st.button("Generate Random Speaking Topic"):
        topics = [
            "Describe a time when you helped someone.",
            "Talk about your favorite book or movie.",
            "Describe a place you would like to visit in the future.",
            "Talk about a skill you would like to learn.",
            "Describe a person who has influenced you positively.",
            "Talk about a festival or celebration in your country.",
            "Describe a memorable journey you have taken."
        ]
        
        st.markdown(f"""
        <div class="tip-card">
            <h3>Speaking Topic:</h3>
            <p>{random.choice(topics)}</p>
            <p>Preparation time: 1 minute</p>
            <p>Speaking time: 2 minutes</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.button("Start Timer (3 minutes)")

elif section == "✍️ Writing Practice":
    st.header("✍️ Writing Task 1 & 2 Resources")
    
    st.markdown(resource_link(
        "IELTS Liz Writing Task 1 and 2",
        "https://ieltsliz.com/ielts-writing-task-1-lessons-and-tips/",
        "📝",
        "Detailed guidance for both writing tasks with sample answers"
    ), unsafe_allow_html=True)
    
    st.markdown(resource_link(
        "IELTS Mentor – Sample Essays",
        "https://www.ielts-mentor.com/",
        "📄",
        "Large collection of essay questions with sample responses"
    ), unsafe_allow_html=True)
    
    st.markdown(resource_link(
        "IELTS Buddy – Band 9 Model Essays",
        "https://www.ieltsbuddy.com/ielts-essay.html",
        "🏆",
        "High-scoring sample essays with examiner comments"
    ), unsafe_allow_html=True)
    
    st.markdown(resource_link(
        "Write & Improve by Cambridge",
        "https://writeandimprove.com/",
        "✅",
        "AI-powered writing feedback with Cambridge assessment criteria"
    ), unsafe_allow_html=True)
    
    st.markdown(resource_link(
        "Grammarly Writing Assistant",
        "https://www.grammarly.com/",
        "📊",
        "AI tool for grammar, spelling, and style improvement"
    ), unsafe_allow_html=True)
    
    # Writing topic generator
    st.subheader("📝 Writing Task Generator")
    task_type = st.selectbox("Select Task Type", ["Task 1 (Academic)", "Task 1 (General)", "Task 2"])
    
    if st.button("Generate Random Topic"):
        if task_type == "Task 1 (Academic)":
            topics = [
                "The graph below shows the percentage of people who use different types of transportation to work in one European city in 2000 and 2020.",
                "The pie charts illustrate the main reasons for migration to and from the UK in 2007.",
                "The diagram shows how electricity is generated in a hydroelectric power station.",
                "The table below gives information about the underground railway systems in six cities."
            ]
        elif task_type == "Task 1 (General)":
            topics = [
                "Write a letter to your local council suggesting improvements to a public park in your area.",
                "Write a letter to a friend inviting them to visit you during the holidays.",
                "Write a letter to a company requesting information about a product you recently purchased.",
                "Write a letter to your manager requesting time off work for personal reasons."
            ]
        else:  # Task 2
            topics = [
                "Some people believe that university students should pay all the costs of their studies because they will earn a higher salary after graduation. Others think that education should be free. Discuss both views and give your opinion.",
                "In many countries, the number of people who are overweight is increasing. What do you think are the causes of this? What solutions can you suggest?",
                "Some people think that the main purpose of schools is to turn children into good citizens and workers, rather than to benefit them as individuals. To what extent do you agree or disagree?",
                "Technology is making communication easier in today's world, but at the expense of personal contact as many people choose to work at home in front of a computer screen. Do the advantages outweigh the disadvantages?"
            ]
        
        st.markdown(f"""
        <div class="tip-card">
            <h3>Writing {task_type}:</h3>
            <p>{random.choice(topics)}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.text_area("Write your response here:", height=300)
        st.button("Submit for AI Feedback")

elif section == "📆 Study Plan":
    st.header("📆 Smart Study Plan for Busy Schedule")
    
    # Calendar view
    st.subheader("📅 Your Personalized Study Calendar")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="progress-card">
            <h3>Monday</h3>
            <p>🎧 20 min: Listening (podcast during commute)</p>
            <p>📚 20 min: Reading (1 passage from Cambridge Book)</p>
            <p>📝 20 min: Writing Task 1</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="progress-card">
            <h3>Tuesday</h3>
            <p>🎧 20 min: Listening (BBC Learning English)</p>
            <p>📚 20 min: Reading (news article analysis)</p>
            <p>📝 20 min: Writing Task 2</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="progress-card">
            <h3>Wednesday</h3>
            <p>🎧 20 min: Listening (TED Talk)</p>
            <p>🗣️ 20 min: Speaking Practice</p>
            <p>📝 20 min: Vocabulary Review</p>
        </div>
        """, unsafe_allow_html=True)
    
    col4, col5, col6 = st.columns(3)
    
    with col4:
        st.markdown("""
        <div class="progress-card">
            <h3>Thursday</h3>
            <p>🎧 20 min: Listening (practice test)</p>
            <p>📚 20 min: Reading (Cambridge test)</p>
            <p>📝 20 min: Grammar Review</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col5:
        st.markdown("""
        <div class="progress-card">
            <h3>Friday</h3>
            <p>🎧 20 min: Listening (podcast)</p>
            <p>📚 20 min: Reading comprehension</p>
            <p>📝 20 min: Writing Task Practice</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col6:
        st.markdown("""
        <div class="progress-card">
            <h3>Weekend</h3>
            <p>⏱️ 1 Full-Length Mock Test</p>
            <p>🗣️ 30 min: Speaking Practice (record & review)</p>
            <p>📋 30 min: Review and correction</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Time management tips
    st.subheader("⏱️ Time Management Tips")
    st.markdown("""
    <div class="tip-card">
        <h3>Study Smart, Not Hard:</h3>
        <ul>
            <li>Use commute time for listening practice</li>
            <li>Set up 5-minute vocabulary sessions during breaks</li>
            <li>Use spaced repetition rather than cramming</li>
            <li>Track your progress to stay motivated</li>
            <li>Create a dedicated study space to improve focus</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif section == "📌 Tips & Tools":
    st.header("📌 Smart Tips & Tools")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🛠️ Essential Tools")
        st.markdown(resource_link(
            "Anki - Spaced Repetition Flashcards",
            "https://apps.ankiweb.net/",
            "🧠",
            "The most effective tool for vocabulary memorization"
        ), unsafe_allow_html=True)
        
        st.markdown(resource_link(
            "Immersive Reader - Chrome Extension",
            "https://chrome.google.com/webstore/detail/immersive-reader/pnpkakdeahedldcgpkjbdjonajgbniff?hl=en",
            "👓",
            "Enhanced reading tool for better comprehension"
        ), unsafe_allow_html=True)
        
        st.markdown(resource_link(
            "Headspace - Mindfulness App",
            "https://www.headspace.com/",
            "🧘",
            "Meditation app to reduce exam anxiety"
        ), unsafe_allow_html=True)
    
    with col2:
        st.subheader("💡 Expert Tips")
        st.markdown("""
        <div class="tip-card">
            <h3>Reading Section:</h3>
            <ul>
                <li>Read the questions before the passage</li>
                <li>Practice skimming and scanning techniques</li>
                <li>Underline key words in questions</li>
                <li>Don't spend too much time on one question</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="tip-card">
            <h3>Speaking Section:</h3>
            <ul>
                <li>Use the STAR method for Part 2 (Situation, Task, Action, Result)</li>
                <li>Record yourself and identify repetitive phrases</li>
                <li>Practice speaking with a timer</li>
                <li>Learn linking phrases for fluency</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # IELTS Success Formula
    st.subheader("🏆 IELTS Success Formula")
    
    formula_data = pd.DataFrame({
        'Factor': ['Consistent Practice', 'Quality Resources', 'Feedback Loops', 'Test Strategies', 'Stress Management'],
        'Impact': [85, 75, 80, 70, 65]
    })
    
    chart = alt.Chart(formula_data).mark_bar().encode(
        x=alt.X('Impact:Q', title='Impact Score'),
        y=alt.Y('Factor:N', title='Success Factors', sort='-x'),
        color=alt.value('#1E88E5'),
        tooltip=['Factor', 'Impact']
    ).properties(height=250)
    
    st.altair_chart(chart, use_container_width=True)

elif section == "🏅 My Progress":
    st.header("🏅 Track Your Progress")
    
    # Mock test scores
    st.subheader("📊 Mock Test Scores")
    
    # Sample data
    dates = [today - timedelta(days=x*7) for x in range(5, 0, -1)]
    reading_scores = [6.5, 7.0, 7.0, 7.5, 8.0]
    listening_scores = [6.0, 6.5, 7.0, 7.5, 7.5]
    writing_scores = [6.0, 6.0, 6.5, 6.5, 7.0]
    speaking_scores = [6.5, 7.0, 7.0, 7.0, 7.5]
    
    progress_df = pd.DataFrame({
        'Date': dates,
        'Reading': reading_scores,
        'Listening': listening_scores,
        'Writing': writing_scores,
        'Speaking': speaking_scores
    })
    
    progress_df['Overall'] = progress_df[['Reading', 'Listening', 'Writing', 'Speaking']].mean(axis=1)
    progress_df['Date'] = progress_df['Date'].dt.strftime('%b %d')
    
    # Convert to long format for charting
    progress_long = pd.melt(
        progress_df, 
        id_vars=['Date'], 
        value_vars=['Reading', 'Listening', 'Writing', 'Speaking', 'Overall'],
        var_name='Skill',
        value_name='Score'
    )
    
    # Create line chart
    chart = alt.Chart(progress_long).mark_line(point=True).encode(
        x=alt.X('Date:N', title='Test Date'),
        y=alt.Y('Score:Q', scale=alt.Scale(domain=[5.5, 9.0]), title='Band Score'),
        color='Skill:N',
        tooltip=['Date', 'Skill', 'Score']
    ).properties(height=300)
    
    st.altair_chart(chart, use_container_width=True)
    
    # Target score tracker
    st.subheader("🎯 Target Score Tracker")
    
    col1, col2, col3, col4 = st.columns(4)
    target_score = 8.0
    
    with col1:
        current_reading = reading_scores[-1]
        st.metric("Reading", current_reading, f"{current_reading - target_score:.1f}" if current_reading - target_score < 0 else "+0.0")
    
    with col2:
        current_listening = listening_scores[-1]
        st.metric("Listening", current_listening, f"{current_listening - target_score:.1f}" if current_listening - target_score < 0 else "+0.0")
    
    with col3:
        current_writing = writing_scores[-1]
        st.metric("Writing", current_writing, f"{current_writing - target_score:.1f}" if current_writing - target_score < 0 else "+0.0")
    
    with col4:
        current_speaking = speaking_scores[-1]
        st.metric("Speaking", current_speaking, f"{current_speaking - target_score:.1f}" if current_speaking - target_score < 0 else "+0.0")
    
    # Practice log
    st.subheader("📝 Practice Log")
    
    with st.expander("Add Practice Entry"):
        col1, col2 = st.columns(2)
        with col1:
            practice_date = st.date_input("Date", today)
            practice_duration = st.number_input("Duration (minutes)", min_value=5, max_value=240, value=30, step=5)
        
        with col2:
            practice_type = st.selectbox("Practice Type", ["Reading", "Writing", "Listening", "Speaking", "Vocabulary", "Grammar", "Full Test"])
            practice_resource = st.text_input("Resource Used")
        
        practice_notes = st.text_area("Notes")
        st.button("Save Practice Entry")
    
    # Sample practice entries
    st.markdown("""
    <div class="resource-card">
        <h3>May 13, 2025 - Writing Task 2 (45 minutes)</h3>
        <p>Resource: Cambridge IELTS 18, Test 2</p>
        <p>Notes: Practiced essay on environmental issues. Need to work on coherence.</p>
    </div>
    
    <div class="resource-card">
        <h3>May 12, 2025 - Listening Practice (30 minutes)</h3>
        <p>Resource: BBC 6-Minute English</p>
        <p>Notes: Struggled with note-taking during Section 3. Need more practice.</p>
    </div>
    
    <div class="resource-card">
        <h3>May 10, 2025 - Full Mock Test (3 hours)</h3>
        <p>Resource: Cambridge IELTS 17, Test 1</p>
        <p>Notes: Reading time management improved. Speaking still needs work.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Weak areas analysis
    st.subheader("🔍 Focus Areas")
    
    weakness_data = pd.DataFrame({
        'Area': ['Complex Grammar', 'Academic Vocabulary', 'Speaking Fluency', 'Reading Speed', 'Listening Note-taking'],
        'Improvement Needed': [35, 25, 30, 15, 40]
    })
    
    chart = alt.Chart(weakness_data).mark_bar().encode(
        x=alt.X('Improvement Needed:Q', title='Improvement Needed (%)'),
        y=alt.Y('Area:N', title='Skill Area', sort='-x'),
        color=alt.condition(
            alt.datum['Improvement Needed'] > 30,
            alt.value('#E57373'),  # Red for high need
            alt.value('#4FC3F7')   # Blue for lower need
        ),
        tooltip=['Area', 'Improvement Needed']
    ).properties(height=250)
    
    st.altair_chart(chart, use_container_width=True)

# Add a footer
st.markdown("""
<div style="text-align: center; margin-top: 40px; padding: 20px; background-color: #f5f7f9; border-radius: 10px;">
    <p>🎯 IELTS Prep Hub by Huzaifa - Updated May 2025</p>
    <p>Keep practicing consistently - You'll achieve your target score! 💪</p>
</div>
""", unsafe_allow_html=True)