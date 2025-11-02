# heartrate_app_final.py
import streamlit as st
import matplotlib.pyplot as plt
import time

# Page setup
st.set_page_config(page_title="💓 Heart Rate Analyzer", page_icon="❤️", layout="centered")

# Session state to track page
if "page" not in st.session_state:
    st.session_state.page = "landing"

# --- Landing Page ---
if st.session_state.page == "landing":
    st.title("💓 Welcome to the Heart Rate Analyzer")
    
    st.markdown("""
    <div style="text-align:center; font-size:18px;">
    ❤️ Your heart is a powerful muscle! <br>
    Resting vs Post-Exercise Heart Rate gives insight into your cardiovascular health. <br>
    Watch your heart pulse, learn about your activity, and get personalized advice! 💪
    </div>
    """, unsafe_allow_html=True)
    
    # Simple heartbeat animation using emojis
    for i in range(3):
        st.markdown("<h1 style='text-align:center; color:red;'>❤️</h1>", unsafe_allow_html=True)
        time.sleep(0.5)
        st.markdown("<h1 style='text-align:center; color:pink;'>❤️</h1>", unsafe_allow_html=True)
        time.sleep(0.5)
    
    if st.button("Next ➡️"):
        st.session_state.page = "user_info"
        st.experimental_rerun()

# --- User Info Page ---
elif st.session_state.page == "user_info":
    st.header("👤 Enter Your Information")
    name = st.text_input("Name")
    email = st.text_input("Email")
    
    if st.button("Enter"):
        if name.strip() == "" or email.strip() == "":
            st.warning("Please fill both Name and Email to continue.")
        else:
            st.session_state.name = name
            st.session_state.email = email
            st.session_state.page = "heart_rate_analysis"
            st.experimental_rerun()

# --- Heart Rate Analysis Page ---
elif st.session_state.page == "heart_rate_analysis":
    st.header(f"Welcome {st.session_state.name}! Let's analyze your Heart Rate 💓")
    
    age = st.number_input("Age (years):", min_value=1, max_value=120, value=20)
    gender = st.selectbox("Gender:", ["Male", "Female"])
    resting_hr = st.number_input("Resting Heart Rate (bpm):", min_value=30, max_value=150, value=70)
    post_exercise_hr = st.number_input("Post-Exercise Heart Rate (bpm):", min_value=40, max_value=220, value=110)
    
    def classify_activity(resting, post):
        diff = post - resting
        if diff > 40:
            return "Highly Active", "🏃 You’re highly active — excellent cardiovascular health!"
        elif diff > 20:
            return "Active", "💪 You’re active — keep up your exercise routine!"
        elif diff > 10:
            return "Moderately Active", "⚖️ Moderate activity — add a bit more daily movement."
        else:
            return "Non-Active", "🛌 You need more physical activity — try short walks & regular exercise."

    if st.button("Analyze 💡"):
        avg_hr = (resting_hr + post_exercise_hr)/2
        activity, advice = classify_activity(resting_hr, post_exercise_hr)
        
        st.success(f"**Average Heart Rate:** {avg_hr:.2f} bpm")
        st.info(f"**Predicted Activity Level:** {activity}")
        
        st.markdown("### 💬 Advice & Insights")
        st.write(advice)
        
        # Individual reading insights
        st.markdown(f"**Resting HR:** {resting_hr} bpm — Your heart at rest; lower values usually indicate better fitness.")
        st.markdown(f"**Post-Exercise HR:** {post_exercise_hr} bpm — Shows your heart's response to activity; higher increase means higher activity capacity.")
        
        # Graph
        st.subheader("📈 Heart Rate Comparison")
        labels = ["Resting HR", "Post-Exercise HR"]
        values = [resting_hr, post_exercise_hr]
        fig, ax = plt.subplots()
        ax.bar(labels, values, color=['skyblue','salmon'])
        ax.set_ylabel("Heart Rate (bpm)")
        ax.set_title("Resting vs Post-Exercise Heart Rate")
        st.pyplot(fig)
        
        # Submit
        if st.button("Submit ✅"):
            st.balloons()
            st.success("Thank you! Your data has been recorded 🎉")
            st.markdown(f"👤 Name: {st.session_state.name}  |  📧 Email: {st.session_state.email}  |  Age: {age}  |  Gender: {gender}")
