from typing import Any, Dict

import streamlit as st


def display_recommendations(analysis: Dict[str, Any]) -> None:
    suggestions = analysis.get("suggestions") or []
    if not suggestions:
        return

    st.markdown("### 💡 Recommendations")
    st.markdown("<div style='margin-bottom: 0.5rem;'></div>", unsafe_allow_html=True)
    for suggestion in suggestions:
        st.markdown(
            f"""
            <div style="display: flex; align-items: start; gap: 0.75rem; margin-bottom: 0.5rem; background: rgba(255,255,255,0.01); padding: 0.75rem 1rem; border-radius: 8px; border: 1px solid rgba(255,255,255,0.03);">
                <span class="custom-badge" style="background: var(--primary-glow); color: var(--primary); border: 1px solid var(--primary-glow); min-width: 60px; text-align: center; justify-content: center; font-size: 0.75rem; padding: 0.15rem 0.5rem;">TIP</span>
                <span style="color: #94A3B8; font-size: 0.95rem; line-height: 1.4;">{suggestion}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
