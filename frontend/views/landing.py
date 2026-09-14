import streamlit as st


def render():
    # Hero Section
    st.markdown("""
    <div class="glow-card animate-fade-up" style="text-align: center; margin-bottom: 2.5rem;">
        <h1 style="font-size: 3rem; margin: 0; background: linear-gradient(135deg, #FFFFFF 35%, var(--secondary) 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 800;">🎯 ATS Resume Scorer</h1>
        <h3 style="font-size: 1.4rem; color: #94A3B8; margin-top: 0.5rem; font-weight: 500;">Optimize Your Resume for Applicant Tracking Systems</h3>
        <p style="font-size: 1rem; color: #64748B; max-width: 700px; margin: 1rem auto 1.5rem auto; line-height: 1.6;">
            Get instant, deep analysis of your resume's compatibility with modern Applicant Tracking Systems. 
            Validate skills using AI semantic engines and pinpoint areas for improvement.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Call-to-Action Button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Start Analyzing Your Resume", use_container_width=True, type="primary"):
            st.session_state.current_view = 'scorer'
            st.rerun()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Features Overview
    st.markdown("<h2 style='text-align: center; margin-bottom: 2rem;'>✨ Key Features</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="glass-card animate-fade-up" style="height: 250px;">
            <h3 style="color: var(--primary); margin-top: 0; display: flex; align-items: center; gap: 0.5rem;">📊 Multi-Score Breakdown</h3>
            <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.5;">
                We score your resume across 5 key dimensions: Formatting, Keywords, Content Quality, Skill Validation, and overall ATS compatibility.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="glass-card animate-fade-up" style="height: 250px;">
            <h3 style="color: var(--secondary); margin-top: 0; display: flex; align-items: center; gap: 0.5rem;">🔍 AI Skill Validation</h3>
            <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.5;">
                Verify that your listed skills are backed up by project work and experience. Our semantic engine checks for proof instead of empty claims.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="glass-card animate-fade-up" style="height: 250px;">
            <h3 style="color: #10B981; margin-top: 0; display: flex; align-items: center; gap: 0.5rem;">🔒 Privacy First</h3>
            <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.5;">
                Your resume never goes to third parties. All parser algorithms run on safe, secure cloud architecture with complete privacy compliance.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # How It Works
    st.markdown("<h2 style='text-align: center; margin-bottom: 2rem;'>🚀 How It Works</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="glass-card animate-fade-up" style="height: 180px; border-left: 4px solid var(--primary);">
            <h4 style="margin-top:0; color:#F8FAFC;">1️⃣ Upload Resume</h4>
            <p style="color: #94A3B8; font-size: 0.9rem; margin-bottom:0;">
                Drag & drop or upload your resume in PDF, DOC, or DOCX format.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="glass-card animate-fade-up" style="height: 180px; border-left: 4px solid var(--secondary);">
            <h4 style="margin-top:0; color:#F8FAFC;">2️⃣ Choose Match Mode</h4>
            <p style="color: #94A3B8; font-size: 0.9rem; margin-bottom:0;">
                Run a general scan, or input a target Job Description to check keyword similarity and gap analysis.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="glass-card animate-fade-up" style="height: 180px; border-left: 4px solid #10B981;">
            <h4 style="margin-top:0; color:#F8FAFC;">3️⃣ Optimize & Export</h4>
            <p style="color: #94A3B8; font-size: 0.9rem; margin-bottom:0;">
                Get actionable feedback and download a comprehensive PDF report instantly.
            </p>
        </div>
        """, unsafe_allow_html=True)
