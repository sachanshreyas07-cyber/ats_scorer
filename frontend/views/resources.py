import streamlit as st


def render():
    """Render the resources page"""
    
    st.markdown("""
    <div class="glass-card animate-fade-up" style="margin-bottom: 2rem;">
        <h2 style="margin: 0; background: linear-gradient(135deg, #FFFFFF 50%, var(--primary) 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 700;">📚 Resources & Tips</h2>
        <p style="color: #94A3B8; margin: 0.25rem 0 0 0;">Learn how to format and optimize your resume for applicant tracking systems.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # ATS Tips
    st.markdown("### 🎯 ATS Optimization Guidelines")
    st.markdown("<div style='margin-bottom: 1rem;'></div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="glass-card" style="border-left: 4px solid #10B981; min-height: 380px;">
            <h3 style="color: #10B981; margin-top: 0; margin-bottom: 1rem;">✅ Do's</h3>
            <ul style="color: #94A3B8; line-height: 1.8; font-size: 0.95rem; padding-left: 1.25rem;">
                <li>Use standard section headings (Experience, Education, Skills)</li>
                <li>Include relevant keywords directly from the target job description</li>
                <li>Use clean, single-column document layouts</li>
                <li>Explicitly list tech stack skills and methodologies</li>
                <li>Quantify your achievements with numbers & metrics</li>
                <li>Stick to standard professional fonts (Arial, Calibri, Inter)</li>
                <li>Save and export your files as standard PDF or DOCX formats</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="glass-card" style="border-left: 4px solid #EF4444; min-height: 380px;">
            <h3 style="color: #EF4444; margin-top: 0; margin-bottom: 1rem;">❌ Don'ts</h3>
            <ul style="color: #94A3B8; line-height: 1.8; font-size: 0.95rem; padding-left: 1.25rem;">
                <li>Avoid inserting complex tables, text boxes, or graphics</li>
                <li>Don't put critical contact details in the header or footer area</li>
                <li>Avoid icons, images, or progress charts to represent skill levels</li>
                <li>Don't use unusual fonts or custom graphic characters</li>
                <li>Avoid two-column structures which confuse older ATS parsers</li>
                <li>Don't engage in keyword stuffing or hidden white text hacks</li>
                <li>Avoid acronyms without writing them out fully first</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<div style='margin: 2.5rem 0;'></div>", unsafe_allow_html=True)
    
    # Common ATS Keywords
    st.markdown("### 🔑 High-Impact Keywords by Industry")
    st.markdown("<div style='margin-bottom: 1rem;'></div>", unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["💻 Tech & Dev", "💼 Business & Mgmt", "🎨 Creative & Design"])
    
    with tab1:
        st.markdown("""
        <div class="glass-card" style="margin-top: 1rem;">
            <h4 style="color:var(--primary); margin-top:0;">Software Engineering & IT:</h4>
            <p style="color:#94A3B8; line-height: 1.6;">
                <strong>Programming:</strong> Python, Java, JavaScript, TypeScript, C++, Rust, Go<br>
                <strong>Web Tech:</strong> React, Node.js, Angular, Django, Spring Boot, HTML5, CSS3<br>
                <strong>DevOps & Cloud:</strong> AWS, Azure, GCP, Docker, Kubernetes, CI/CD Pipelines, Git<br>
                <strong>Methodologies:</strong> Agile, Scrum, TDD, Microservices Architecture, RESTful APIs
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("""
        <div class="glass-card" style="margin-top: 1rem;">
            <h4 style="color:var(--secondary); margin-top:0;">Operations & Leadership:</h4>
            <p style="color:#94A3B8; line-height: 1.6;">
                <strong>Management:</strong> Project Management, Stakeholder Engagement, Cross-Functional Team Leadership<br>
                <strong>Strategy:</strong> Strategic Planning, Business Development, Process Optimization, Change Management<br>
                <strong>Finance:</strong> Budget Allocation, ROI Analysis, Financial Forecasting, Cost-Benefit Analysis<br>
                <strong>Frameworks:</strong> PMP, Prince2, Six Sigma, Scrum Master, KPI Tracking
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("""
        <div class="glass-card" style="margin-top: 1rem;">
            <h4 style="color:#10B981; margin-top:0;">Design & Visual Communications:</h4>
            <p style="color:#94A3B8; line-height: 1.6;">
                <strong>Tools:</strong> Figma, Adobe Creative Suite (Photoshop, Illustrator, InDesign), Sketch<br>
                <strong>Product Design:</strong> UI/UX Design, Interaction Design, Wireframing, Prototyping, User Research<br>
                <strong>Marketing & Brand:</strong> Visual Communication, Typography, Branding Identity, Graphic Design, Web Layouts
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<div style='margin: 2.5rem 0;'></div>", unsafe_allow_html=True)
    
    # Resume Templates
    st.markdown("### 📄 ATS-Friendly Resume Templates")
    st.markdown("""
    <div class="custom-alert alert-info">
        <span style="font-size: 1.2rem;">✨</span>
        <div>
            <strong>Feature coming soon:</strong> A collection of downloadable, pre-formatted MS Word and Google Doc templates designed specifically to pass modern ATS scanners. Check back in a future update!
        </div>
    </div>
    """, unsafe_allow_html=True)
