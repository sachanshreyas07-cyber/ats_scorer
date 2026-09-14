from typing import Any, Dict, Optional

import streamlit as st


def display_jd_comparison(jd_comparison: Optional[Dict[str, Any]]) -> None:
    if not jd_comparison:
        return  # caller decides whether to render the section at all

    st.markdown("### 🎯 Job Description Match")

    match_pct = float(jd_comparison.get("match_percentage", 0))
    semantic = float(jd_comparison.get("semantic_similarity", 0))
    matched = jd_comparison.get("matched_keywords", []) or []
    missing = jd_comparison.get("missing_keywords", []) or []
    gap = jd_comparison.get("skills_gap", []) or []

    top_l, top_r = st.columns(2)
    with top_l:
        st.metric("Keyword Match Score", f"{match_pct:.0f}%")
        kw_fill_class = "progress-fill-excellent" if match_pct >= 80 else "progress-fill-good" if match_pct >= 60 else "progress-fill-poor"
        st.markdown(
            f"""
            <div class="progress-track" style="margin-bottom: 1.5rem; margin-top: 0.5rem;">
                <div class="progress-fill {kw_fill_class}" style="width: {match_pct}%;"></div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.metric("Semantic Similarity", f"{semantic * 100:.0f}%")
        sem_pct = min(max(semantic * 100.0, 0.0), 100.0)
        sem_fill_class = "progress-fill-excellent" if sem_pct >= 80 else "progress-fill-good" if sem_pct >= 60 else "progress-fill-poor"
        st.markdown(
            f"""
            <div class="progress-track" style="margin-bottom: 1.5rem; margin-top: 0.5rem;">
                <div class="progress-fill {sem_fill_class}" style="width: {sem_pct}%;"></div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with top_r:
        st.markdown("**✅ Matched keywords**")
        st.markdown("<div style='margin-bottom: 0.5rem;'></div>", unsafe_allow_html=True)
        if matched:
            badge_html = "".join(f'<span class="custom-badge badge-validated" style="margin: 0.2rem;">{kw}</span>' for kw in matched[:20])
            st.markdown(f'<div style="display: flex; flex-wrap: wrap;">{badge_html}</div>', unsafe_allow_html=True)
        else:
            st.markdown("_No matching keywords identified yet._")

    st.markdown("<div style='margin: 1.5rem 0;'></div>", unsafe_allow_html=True)
    bot_l, bot_r = st.columns(2)
    with bot_l:
        st.markdown("**❌ Missing keywords**")
        st.markdown("<div style='margin-bottom: 0.5rem;'></div>", unsafe_allow_html=True)
        if missing:
            badge_html = "".join(f'<span class="custom-badge badge-unvalidated" style="margin: 0.2rem;">{kw}</span>' for kw in missing[:15])
            st.markdown(f'<div style="display: flex; flex-wrap: wrap;">{badge_html}</div>', unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="custom-alert alert-success">
                <span style="font-size: 1.1rem;">🎉</span>
                <div>All key terms from the job description are present in your resume!</div>
            </div>
            """, unsafe_allow_html=True)
            
    with bot_r:
        st.markdown("**📊 Skills gap**")
        st.markdown("<div style='margin-bottom: 0.5rem;'></div>", unsafe_allow_html=True)
        if gap:
            badge_html = "".join(f'<span class="custom-badge" style="margin: 0.2rem; background: rgba(245, 158, 11, 0.05); color: #FBBF24; border: 1px solid rgba(245, 158, 11, 0.15);">{kw}</span>' for kw in gap[:15])
            st.markdown(f'<div style="display: flex; flex-wrap: wrap;">{badge_html}</div>', unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="custom-alert alert-success">
                <span style="font-size: 1.1rem;">🎉</span>
                <div>No significant gaps in core skills detected.</div>
            </div>
            """, unsafe_allow_html=True)
