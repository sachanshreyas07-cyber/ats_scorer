from typing import Any, Dict, List, Tuple

import streamlit as st


# Score weights and thresholds
SEVERITY_RANK = {"critical": 0, "high": 1, "medium": 2, "low": 3}


def _collect_action_items(analysis: Dict[str, Any]) -> List[Tuple[str, str, str]]:
    """Return list of (severity, source_title, action_text)."""
    items: List[Tuple[str, str, str]] = []

    for issue in analysis.get("detailed_feedback") or []:
        level = (issue.get("severity_level") or "low").lower()
        title = issue.get("issue_title", "")
        for action in issue.get("action_items") or []:
            items.append((level, title, action))

    if not items:
        for suggestion in analysis.get("suggestions") or []:
            items.append(("medium", "General", suggestion))

    items.sort(key=lambda row: SEVERITY_RANK.get(row[0], 99))
    return items


def display_action_items(analysis: Dict[str, Any]) -> None:
    items = _collect_action_items(analysis)
    if not items:
        return

    st.markdown("### ⚡ Action Items")
    st.caption("Concrete steps to improve your score, sorted by urgency.")
    st.markdown("<div style='margin-bottom: 0.75rem;'></div>", unsafe_allow_html=True)

    for level, source, action in items:
        if level in ("critical", "high"):
            style = "background: rgba(239, 68, 68, 0.1); color: #F87171; border: 1px solid rgba(239, 68, 68, 0.2);"
        elif level == "medium":
            style = "background: rgba(245, 158, 11, 0.1); color: #FBBF24; border: 1px solid rgba(245, 158, 11, 0.2);"
        else:
            style = "background: rgba(255, 255, 255, 0.05); color: #F8FAFC; border: 1px solid rgba(255, 255, 255, 0.08);"
            
        badge_label = level.upper()
        
        st.markdown(
            f"""
            <div style="display: flex; align-items: start; gap: 0.75rem; margin-bottom: 0.5rem; background: rgba(255,255,255,0.02); padding: 0.75rem 1rem; border-radius: 8px; border: 1px solid rgba(255, 255, 255, 0.03);">
                <span class="custom-badge" style="{style} min-width: 80px; text-align: center; justify-content: center; font-size: 0.75rem; padding: 0.15rem 0.5rem;">{badge_label}</span>
                <span style="color: #F8FAFC; font-size: 0.95rem; line-height: 1.4;">
                    <strong style="color: var(--primary);">[{source}]</strong> {action}
                </span>
            </div>
            """,
            unsafe_allow_html=True,
        )
