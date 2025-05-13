import streamlit as st

st.set_page_config(page_title="IELTS Prep Hub - Huzaifa", layout="centered")
st.title("🎯 IELTS Prep Hub - By Huzaifa")
st.caption("Your all-in-one smart portal for 8+ Band IELTS preparation")

st.sidebar.title("📂 Navigation")
section = st.sidebar.radio("Go to", [
    "📚 Books & PDFs",
    "🎧 Podcasts & Audio",
    "📺 Video Lessons",
    "📝 Mock Tests & Practice",
    "🗣️ Speaking Practice",
    "✍️ Writing Practice",
    "📆 Study Plan",
    "📌 Tips & Tools"
])

if section == "📚 Books & PDFs":
    st.header("📚 Books and PDF Resources")
    st.markdown("""
    - [Cambridge IELTS Books 1–19 (PDF + Audio)](https://www.ieltsxpress.com/download-all-cambridge-ielts-books-pdf-audio-for-free-cambridge-1-14-free-download/)
    - [Barron’s IELTS Superpack PDF](https://archive.org/details/barronsielts20164th528p)
    - [IELTS Writing Task 2 eBook by IELTS Liz](https://ieltsliz.com/ideas-for-ielts-essays-e-book/)
    - [Official IELTS Guide PDF](https://ielts.idp.com/-/media/pdfs/ielts-preparation-materials.ashx)
    - [IELTS Academic Word List PDF](https://www.ieltsbuddy.com/support-files/academic-word-list.pdf)
    """)

elif section == "🎧 Podcasts & Audio":
    st.header("🎧 IELTS Podcasts & Listening Practice")
    st.markdown("""
    - [IELTS Speaking for Success – Spotify](https://open.spotify.com/show/1HkLkU0sZC0gk1bX1i1U1x)
    - [BBC Learning English – 6 Minute English](https://www.bbc.co.uk/learningenglish)
    - [IELTS Energy Podcast – All Ears English](https://www.allearsenglish.com/episodes/ielts)
    - [Luke’s English Podcast](https://teacherluke.co.uk/)
    - [TED Talks Audio – Spotify](https://open.spotify.com/show/2WTmtt13C6v0CZkOe5zSKz)
    """)

elif section == "📺 Video Lessons":
    st.header("📺 Best IELTS Video Channels")
    st.markdown("""
    - [IELTS Liz – YouTube](https://www.youtube.com/@ieltsliz)
    - [E2 IELTS – YouTube](https://www.youtube.com/@E2IELTS)
    - [IELTS Advantage – YouTube](https://www.youtube.com/@IELTSadvantage)
    - [AcademicEnglishHelp – YouTube](https://www.youtube.com/@AcademicEnglishHelp)
    """)

elif section == "📝 Mock Tests & Practice":
    st.header("📝 Practice Tests & Mock Exams")
    st.markdown("""
    - [Cambridge IELTS Practice Tests (1–13)](https://practicepteonline.com/cambridge-ielts-1-13-tests/)
    - [British Council IELTS Practice Tests](https://takeielts.britishcouncil.org/take-ielts/prepare)
    - [IELTS Online Tests – Free Full Exams](https://ieltsonlinetests.com/)
    - [IELTS Practice with AI Feedback](https://ieltsonlinetests.com/ielts-preparation-practice-exams)
    """)

elif section == "🗣️ Speaking Practice":
    st.header("🗣️ Speaking Practice Tools")
    st.markdown("""
    - [IELTS Speaking for Success – Spotify](https://open.spotify.com/show/1HkLkU0sZC0gk1bX1i1U1x)
    - [IELTS Liz – Speaking Questions & Tips](https://ieltsliz.com/ielts-speaking-free-lessons-essential-tips/)
    - [Cue Card Generator](https://ieltstools.com/speaking-part-2-cue-cards)
    - [Speechling – Free AI Coach](https://speechling.com/)
    - [Record Your Voice – Practice Self Review](https://vocaroo.com/)
    """)

elif section == "✍️ Writing Practice":
    st.header("✍️ Writing Task 1 & 2 Resources")
    st.markdown("""
    - [IELTS Liz Writing Task 1 and 2](https://ieltsliz.com/ielts-writing-task-1-lessons-and-tips/)
    - [IELTS Mentor – Sample Essays](https://www.ielts-mentor.com/)
    - [IELTS Buddy – Band 9 Model Essays](https://www.ieltsbuddy.com/ielts-essay.html)
    - [Write & Improve by Cambridge](https://writeandimprove.com/)
    - [Grammarly Writing Assistant](https://www.grammarly.com/)
    """)

elif section == "📆 Study Plan":
    st.header("📆 Smart Study Plan for Busy Schedule")
    st.markdown("""
    **Weekdays (1–1.5 hrs):**
    - 20 min: Listening (podcast during commute)
    - 20 min: Reading (1 passage from Cambridge Book)
    - 20 min: Writing Task (alternate between Task 1 & 2)
    - 10 min: Vocabulary review (Word List)

    **Weekends (2–3 hrs):**
    - 1 Full-Length Mock Test
    - 30 min: Speaking Practice (record & review)
    - 30 min: Review and correction of past mistakes
    """)

elif section == "📌 Tips & Tools":
    st.header("📌 Smart Tips & Tools")
    st.markdown("""
    - Use [Anki](https://apps.ankiweb.net/) for daily vocabulary revision
    - Keep a journal of common writing structures
    - Use Chrome plugin [Immersive Reader](https://chrome.google.com/webstore/detail/immersive-reader/pnpkakdeahedldcgpkjbdjonajgbniff?hl=en) for reading enhancement
    - Track progress weekly in Notion or Excel
    - Practice mindfulness before exams with [Headspace](https://www.headspace.com/)
    """)

st.success("🎉 You're all set, Huzaifa! Come back here daily for 8+ Band preparation.")
