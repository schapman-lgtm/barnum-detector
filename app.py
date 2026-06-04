import streamlit as st
import re

# Set page configuration with a nod to modernist, clean design
st.set_page_config(page_title="Barnum Bias Detector", page_icon="🧠", layout="centered")

st.title("🧠 The Barnum Bias Detector")
st.markdown("""
*Ever read a personality profile, horoscope, or piece of feedback and thought, 'Wow, this is 100% me!'?*
Use this tool to audit your text for the **Barnum Effect**—the psychological tendency to believe generic, universally applicable statements are highly specific to you.
""")

st.text_area(
    "Paste your personality test description or feedback text here:",
    placeholder="e.g., 'You have a great deal of unused capacity... You pride yourself as an independent thinker...'",
    key="user_text"
)

# A dictionary of classic Barnum triggers and their psychological breakdowns
BARNUM_TRIGGERS = {
    r"\b(unused capacity|unused potential|hidden talent)\b": {
        "label": "The Flattery Anchor",
        "desc": "Almost every human being feels they have untapped potential. Flagging this creates an instant positive emotional connection, making you more likely to accept the rest of the text."
    },
    r"\b(independent thinker|think for yourself|don't accept others' statements)\b": {
        "label": "The Ego Booster",
        "desc": "Very few people view themselves as gullible conformists. Describing someone as an 'independent thinker' appeals directly to individual pride."
    },
    r"\b(some personality weaknesses|generally able to compensate|not perfect)\b": {
        "label": "The Balanced Illusion",
        "desc": "By pairing a vague weakness with an immediate reassurance, the statement appears balanced and objective, hiding its lack of actual substance."
    },
    r"\b(outside you look|inside you feel|inwardly insecure|disciplined on the outside)\b": {
        "label": "The Inward/Outward Split",
        "desc": "This leverages the universal human experience of social masking—feeling less confident internally than the face we present to the world."
    },
    r"\b(times when you are extroverted|sometimes introverted|socially cautious)\b": {
        "label": "The Spectrum Cover",
        "desc": "This covers both ends of a psychological spectrum. Because everyone shifts behaviors depending on context, the statement is mathematically guaranteed to be true."
    }
}

if st.button("Run Bias Audit"):
    text_to_analyze = st.session_state.user_text
    
    if not text_to_analyze.strip():
        st.warning("Please paste some text first!")
    else:
        st.subheader("🕵️‍♂️ Analysis Results")
        matches_found = 0
        
        # Iterate through patterns and look for matches
        for pattern, info in BARNUM_TRIGGERS.items():
            if re.search(pattern, text_to_analyze, re.IGNORECASE):
                matches_found += 1
                # Highlight the found category
                st.error(f"⚠️ **Detected: {info['label']}**")
                st.caption(f"**Psychological Breakdown:** {info['desc']}")
                st.markdown("---")
        
        if matches_found == 0:
            st.success("🎉 Low Barnum Signature! The text didn't trigger our generic baseline filters. It might actually contain specific, personalized data.")
        else:
            st.info(f"Audit complete. Found {matches_found} universal baseline triggers. Remember to take these results with a healthy dose of critical thinking!")
