import streamlit as st
import re

# Set page configuration with a nod to modernist, clean design
st.set_page_config(page_title="Barnum Bias Detector", page_icon="🧠", layout="centered")

st.title("🧠 The Barnum Bias Detector")
st.markdown("""
*Ever read a personality profile and thought, 'Wow, this is 100% me!'?*
Use this tool to audit your text for the **Barnum Effect**—the psychological tendency to believe generic, universally applicable statements are highly specific to you.
""")

user_text = st.text_area(
    "Paste your personality test description or feedback text here:",
    placeholder="e.g., 'You have a great deal of unused capacity... You pride yourself as an independent thinker...'",
    height=200
)

# Broadened keyword clusters to catch variations in personality test language
BARNUM_TRIGGERS = {
    "The Flattery Anchor": {
        "keywords": [r"potential", r"capacity", r"talent", r"hidden", r"unused", r"achieve more"],
        "desc": "Almost every human being feels they have untapped potential. Flagging this creates an instant positive emotional connection, making you more likely to accept the rest of the profile."
    },
    "The Ego Booster": {
        "keywords": [r"independent", r"thinker", r"autonomous", r"original", r"pride yourself", r"critical"],
        "desc": "Very few people view themselves as easily led or unoriginal. Describing someone as an 'independent thinker' appeals directly to individual pride."
    },
    "The Balanced Illusion": {
        "keywords": [r"weakness", r"fault", r"compensate", r"imperfection", r"flaw", r"balance"],
        "desc": "By pairing a vague weakness with an immediate reassurance or saying you 'compensate' for it, the statement appears balanced and objective, hiding its lack of actual substance."
    },
    "The Inward/Outward Split": {
        "keywords": [r"outside", r"inside", r"inward", r"outward", r"insecure", r"mask", r"appear"],
        "desc": "This leverages the universal human experience of social masking—feeling less confident or more anxious internally than the poised, professional face we present to the world."
    },
    "The Spectrum Cover": {
        "keywords": [r"sometimes", r"occasionally", r"at times", r"extrovert", r"introvert", r"cautious", r"varying"],
        "desc": "This covers both ends of a psychological spectrum using qualifiers like 'sometimes'. Because human behavior always shifts depending on context, the statement is mathematically guaranteed to be true."
    }
}

if st.button("Run Bias Audit"):
    if not user_text.strip():
        st.warning("Please paste some text first!")
    else:
        st.subheader("🕵️‍♂️ Analysis Results")
        matches_found = 0
        
        # Check text against the broader keyword lists
        for label, info in BARNUM_TRIGGERS.items():
            matched_words = []
            for kw in info["keywords"]:
                if re.search(kw, user_text, re.IGNORECASE):
                    matched_words.append(re.findall(kw, user_text, re.IGNORECASE)[0])
            
            if matched_words:
                matches_found += 1
                # Format unique matches nicely
                unique_matches = ", ".join(list(set(matched_words)))
                st.error(f"⚠️ **Detected: {label}** (Trigger words found: *{unique_matches}*)")
                st.write(f"**Psychological Breakdown:** {info['desc']}")
                st.markdown("---")
        
        if matches_found == 0:
            st.success("🎉 Low Barnum Signature! The text didn't trigger our generic baseline filters. It might actually contain specific, personalized data.")
        else:
            st.info(f"Audit complete. Found {matches_found} universal baseline triggers. Remember to take these results with a healthy dose of critical thinking!")
