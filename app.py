import streamlit as st
from ChatPDF import main as chat_pdf
from streamlit import add_vertical_space

def landing_page():
    # Styling
    st.markdown("""
    <style>
        .main-header {
            text-align: center;
            padding: 2rem 0;
            background-color: #f8f9fa;
            border-radius: 10px;
            margin-bottom: 2rem;
        }
        .feature-card {
            padding: 1.5rem;
            border-radius: 10px;
            background-color: white;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 1rem;
        }
        .cta-section {
            text-align: center;
            padding: 2rem;
            margin: 2rem 0;
            background-color: #f0f7ff;
            border-radius: 10px;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Hero Section
    st.markdown('<div class="main-header">', unsafe_allow_html=True)
    st.title('AgroGPT')
    st.subheader('Your AI-Powered Agricultural Knowledge Assistant')
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Main Features
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        st.header('🌾 Agricultural Knowledge Base')
        st.write('Access comprehensive agricultural information through our intelligent chatbot.')
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        st.header('📊 Data Analysis')
        st.write('Get insights from agricultural documents and research papers.')
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        st.header('🤖 AI Assistant')
        st.write('Chat with our AI to get instant answers to your agricultural queries.')
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        st.header('📚 Document Intelligence')
        st.write('Upload and analyze agricultural documents with our advanced AI.')
        st.markdown('</div>', unsafe_allow_html=True)
    
    # CTA Section
    st.markdown('<div class="cta-section">', unsafe_allow_html=True)
    st.markdown('### Start Using AgroGPT Today')
    if st.button('Try the AI Assistant'):
        st.session_state['show_chat'] = True
    st.markdown('</div>', unsafe_allow_html=True)

def main():
    if 'show_chat' not in st.session_state:
        st.session_state['show_chat'] = False
    
    # Sidebar
    with st.sidebar:
        st.title('AgroGPT')
        st.markdown('### Navigation')
        if st.button('🏠 Home'):
            st.session_state['show_chat'] = False
        if st.button('💬 AI Assistant'):
            st.session_state['show_chat'] = True
        
        add_vertical_space(3)
        st.markdown('---')
        st.write("Made by Giya A")
    
    # Main content
    if st.session_state['show_chat']:
        chat_pdf()
    else:
        landing_page()

if __name__ == '__main__':
    main()
