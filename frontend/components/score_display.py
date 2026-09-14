from typing import Any, Dict

import streamlit as st

from frontend.components._helpers import get_score_color, get_score_emoji


# Component max scores match backend/core/config.py SCORE_WEIGHTS.
# (Backend returns each component's score on its own scale, not 0–100.)
COMPONENTS = [
    ("Formatting",        "formatting",        20, "📝"),
    ("Keywords & Skills", "keywords",          25, "🔑"),
    ("Content Quality",   "content",           25, "📄"),
    ("Skill Validation",  "skill_validation",  15, "✅"),
    ("ATS Compatibility", "ats_compatibility", 15, "🤖"),
]


def display_overall_score(analysis: Dict[str, Any]) -> None:
    """Big colored score card with a short interpretation line."""
    score = float(analysis.get("ATS_score", analysis.get("ats_score", 0)))
    interpretation = analysis.get("interpretation", "")
    emoji = get_score_emoji(score)

    st.markdown("## 📊 Analysis Results")
    _, mid, _ = st.columns([1, 2, 1])
    with mid:
        st.markdown(
            f"""
            <div class="overall-score-container animate-fade-up">
                <h1 class="score-text">
                    {emoji} {score:.0f}
                </h1>
                <h3 style="margin: 0.5rem 0; color: #FFF; font-size: 1.5rem; font-weight: 600;">Overall ATS Score</h3>
                <p style="color: #94A3B8; margin-top: 0.5rem; line-height: 1.5; font-size: 1rem;">{interpretation}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )


def display_score_breakdown(analysis: Dict[str, Any]) -> None:
    """Five progress bars, one per scoring component."""
    component_scores = analysis.get("component_scores") or {}
    st.markdown("### 📈 Score Breakdown")

    left, right = st.columns(2)
    for i, (label, key, max_score, icon) in enumerate(COMPONENTS):
        value = float(component_scores.get(key, 0))
        percentage = value / max_score if max_score else 0
        fill_class = "progress-fill-excellent" if percentage >= 0.8 else "progress-fill-good" if percentage >= 0.6 else "progress-fill-poor"

        with left if i % 2 == 0 else right:
            st.markdown(
                f"""
                <div class="glass-card animate-fade-up" style="margin-bottom: 1rem; padding: 1.25rem;">
                    <div style="display: flex; justify-content: space-between; align-items: center; font-weight: 600; color: #FFF; font-size: 0.95rem;">
                        <span>{icon} {label}</span>
                        <span>{value:.0f} / {max_score}</span>
                    </div>
                    <div class="progress-track">
                        <div class="progress-fill {fill_class}" style="width: {percentage * 100}%;"></div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
