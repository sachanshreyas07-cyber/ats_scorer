import requests
import streamlit as st

from frontend.services import api_client


def _show_backend_error(exc: Exception) -> None:
    if isinstance(exc, requests.ConnectionError):
        st.error("Could not reach the backend. Is it running on port 8000?")
    elif isinstance(exc, requests.HTTPError) and exc.response is not None:
        st.error(f"Backend returned {exc.response.status_code}: {exc.response.text}")
    else:
        st.error(f"Unexpected error: {exc}")


def render() -> None:
    st.markdown("""
    <div class="glass-card animate-fade-up" style="margin-bottom: 2rem;">
        <h2 style="margin: 0; background: linear-gradient(135deg, #FFFFFF 50%, var(--primary) 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 700;">📊 Analysis History</h2>
        <p style="color: #94A3B8; margin: 0.25rem 0 0 0;">Browse and manage your past resume scoring runs and reports.</p>
    </div>
    """, unsafe_allow_html=True)

    access_token = st.session_state.get("access_token")
    if not access_token:
        st.markdown("""
        <div class="custom-alert alert-warning">
            <span style="font-size: 1.2rem;">⚠️</span>
            <div>
                <strong>Authentication Required:</strong> Please sign in or create an account in the sidebar to view your analysis history.
            </div>
        </div>
        """, unsafe_allow_html=True)
        return

    try:
        history = api_client.get_history(access_token)
    except requests.RequestException as exc:
        _show_backend_error(exc)
        return

    if not history:
        st.markdown("""
        <div class="custom-alert alert-info" style="margin-bottom: 1.5rem;">
            <span style="font-size: 1.2rem;">ℹ️</span>
            <div>
                <strong>No analyses yet:</strong> You haven't run any scoring reports yet. Head over to the ATS Scorer to begin!
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🎯 Go to ATS Scorer", use_container_width=True):
            st.session_state.current_view = "scorer"
            st.rerun()
        return

    st.markdown(f"**Total analyses:** {len(history)}")
    st.markdown("---")

    for idx, entry in enumerate(history):
        filename = entry.get("filename", "resume")
        ats_score = float(entry.get("ats_score", 0))
        created_at = entry.get("created_at", "")
        analysis = entry.get("analysis_result", {}) or {}

        component_scores = analysis.get("component_scores", {}) or {}
        jd_comparison = analysis.get("jd_comparison") or analysis.get("jd_match_analysis")

        with st.expander(f"📄 {filename} — Score: {ats_score:.0f}/100 — {created_at}"):
            c1, c2, c3 = st.columns(3)
            with c1:
                st.metric("Overall", f"{ats_score:.0f}/100")
                st.metric("Formatting", f"{component_scores.get('formatting', 0):.0f}/20")
            with c2:
                st.metric("Keywords", f"{component_scores.get('keywords', 0):.0f}/25")
                st.metric("Content", f"{component_scores.get('content', 0):.0f}/25")
            with c3:
                st.metric("Skill Validation", f"{component_scores.get('skill_validation', 0):.0f}/15")
                st.metric("ATS Compatibility", f"{component_scores.get('ats_compatibility', 0):.0f}/15")

            if jd_comparison:
                st.markdown(f"**JD Match:** {jd_comparison.get('match_percentage', 0):.0f}%")

            entry_id = entry.get("id")
            if entry_id:
                if st.button("🗑️ Delete", key=f"delete_{idx}"):
                    try:
                        api_client.delete_history_entry(str(entry_id), access_token)
                        st.success("Deleted.")
                        st.rerun()
                    except requests.RequestException as exc:
                        _show_backend_error(exc)
