from typing import Any, Dict, List
import streamlit as st


def display_strengths(strengths: List[str]) -> None:
    st.markdown("### 💪 Strengths")
    if not strengths:
        st.markdown("""
        <div class="custom-alert alert-info">
            <span style="font-size: 1.1rem;">💡</span>
            <div>
                Improve your resume's content density and formatting checks to unlock recognized strengths.
            </div>
        </div>
        """, unsafe_allow_html=True)
        return
        
    for item in strengths:
        st.markdown(
            f"""
            <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.5rem; background: rgba(16, 185, 129, 0.05); padding: 0.6rem; border-radius: 8px; border: 1px solid rgba(16, 185, 129, 0.15);">
                <span class="custom-badge badge-validated">✓ Strength</span>
                <span style="color: #A7F3D0; font-size: 0.95rem; font-weight: 500;">{item}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )


def display_critical_issues(analysis: Dict[str, Any]) -> None:
    critical = analysis.get("critical_issues") or []
    summary = analysis.get("issues_summary") or []

    if not critical and not summary:
        st.markdown("""
        <div class="custom-alert alert-success">
            <span style="font-size: 1.1rem;">🎉</span>
            <div>
                <strong>No Critical Issues:</strong> Your resume layout and compatibility features are looking excellent!
            </div>
        </div>
        """, unsafe_allow_html=True)
        return

    st.markdown("### 🚨 Critical Issues")
    
    st.markdown("""
    <div class="custom-alert alert-danger" style="margin-bottom: 1rem; padding: 0.75rem 1rem;">
        <span style="font-size: 1.1rem;">⚠️</span>
        <div>
            Please address the following items to avoid parsing issues in standard ATS scanners.
        </div>
    </div>
    """, unsafe_allow_html=True)

    for item in critical:
        st.markdown(
            f"""
            <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.5rem; background: rgba(239, 68, 68, 0.05); padding: 0.6rem; border-radius: 8px; border: 1px solid rgba(239, 68, 68, 0.15);">
                <span class="custom-badge badge-unvalidated">Critical</span>
                <span style="color: #FECACA; font-size: 0.95rem; font-weight: 500;">{item}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    extra = [s for s in summary if s not in critical]
    if extra:
        with st.expander("📋 Additional flagged items", expanded=False):
            st.markdown("<div style='margin-bottom: 0.5rem;'></div>", unsafe_allow_html=True)
            for item in extra:
                st.markdown(
                    f"""
                    <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.5rem; background: rgba(255, 255, 255, 0.02); padding: 0.5rem; border-radius: 8px;">
                        <span class="custom-badge badge-neutral">Flagged</span>
                        <span style="color: #94A3B8; font-size: 0.90rem;">{item}</span>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
