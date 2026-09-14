from typing import Any, Dict

import streamlit as st


def display_skill_validation(analysis: Dict[str, Any]) -> None:
    details = analysis.get("skill_validation_details") or {}
    validated = details.get("validated", [])
    unvalidated = details.get("unvalidated", [])
    total = details.get("total", len(validated) + len(unvalidated))
    pct = details.get("validation_pct", 0.0)

    st.markdown("### ✅ Skill Validation")

    if total == 0:
        st.markdown("""
        <div class="custom-alert alert-info">
            <span style="font-size: 1.2rem;">ℹ️</span>
            <div>
                <strong>No skills detected:</strong> We couldn't extract any structured skills from your resume content.
            </div>
        </div>
        """, unsafe_allow_html=True)
        return

    c1, c2, c3 = st.columns(3)
    c1.metric("Total Skills", total)
    c2.metric("Validated Skills", len(validated))
    c3.metric("Validation Rate", f"{pct:.0f}%")

    # Custom progress bar
    fill_class = "progress-fill-excellent" if pct >= 80 else "progress-fill-good" if pct >= 60 else "progress-fill-poor"
    st.markdown(
        f"""
        <div class="progress-track" style="margin-bottom: 1.5rem; margin-top: 0.5rem;">
            <div class="progress-fill {fill_class}" style="width: {pct}%;"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if validated:
        with st.expander(f"✅ Validated skills ({len(validated)})", expanded=False):
            st.markdown("<div style='margin-bottom: 0.5rem;'></div>", unsafe_allow_html=True)
            for entry in validated:
                skill = entry.get("skill", "?")
                projects = entry.get("projects", []) or []
                similarity = entry.get("similarity")

                project_text = ", ".join(projects[:3]) if projects else "experience section"
                sim_text = f" ({similarity * 100:.0f}% match)" if isinstance(similarity, (int, float)) else ""
                
                st.markdown(
                    f"""
                    <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.5rem; background: rgba(255,255,255,0.02); padding: 0.6rem; border-radius: 8px; border: 1px solid rgba(255,255,255,0.03);">
                        <span class="custom-badge badge-validated">{skill}</span>
                        <span style="color: #94A3B8; font-size: 0.9rem;">demonstrated in: <strong>{project_text}</strong>{sim_text}</span>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

    if unvalidated:
        with st.expander(f"⚠️ Unvalidated skills ({len(unvalidated)})", expanded=False):
            st.caption("These skills are listed on your resume but are not linked to a project or experience description.")
            st.markdown("<div style='margin-bottom: 0.5rem;'></div>", unsafe_allow_html=True)
            for skill in unvalidated:
                st.markdown(
                    f"""
                    <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.5rem; background: rgba(255,255,255,0.02); padding: 0.6rem; border-radius: 8px; border: 1px solid rgba(255,255,255,0.03);">
                        <span class="custom-badge badge-unvalidated">{skill}</span>
                        <span style="color: #64748B; font-size: 0.9rem;">Missing context or project details in your profile experience.</span>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
