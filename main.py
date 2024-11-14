import streamlit as st
from dotenv import load_dotenv
import pickle
from PyPDF2 import PdfReader
from streamlit_extras.add_vertical_space import add_vertical_space
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
from langchain_community.callbacks.manager import get_openai_callback
import os

# Load environment variables
load_dotenv()

def chat_with_pdf():
    st.header("Chat with PDF 💬")
    
    # upload a PDF file
    pdf = st.file_uploader("Upload your PDF", type='pdf')
    
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(text=text)

        store_name = pdf.name[:-4]
        
        if os.path.exists(f"{store_name}.pkl"):
            with open(f"{store_name}.pkl", "rb") as f:
                VectorStore = pickle.load(f)
        else:
            embeddings = OpenAIEmbeddings()
            VectorStore = FAISS.from_texts(chunks, embedding=embeddings)
            with open(f"{store_name}.pkl", "wb") as f:
                pickle.dump(VectorStore, f)

        query = st.text_input("Ask questions about your PDF file:")

        if query:
            docs = VectorStore.similarity_search(query=query, k=3)
            llm = OpenAI()
            chain = load_qa_chain(llm=llm, chain_type="stuff")
            with get_openai_callback() as cb:
                response = chain.run(input_documents=docs, question=query)
                print(cb)
            st.write(response)

def main():
    # Updated CSS for white button text
    st.markdown("""
        <style>
            /* Button styling */
            .stButton > button {
                color: white !important;
                background-color: #007bff !important;
                border: none;
            }
            .stButton > button p {
                color: white !important;
            }
            .stButton > button:hover {
                color: white !important;
            }
            .stButton button div[data-testid="stMarkdownContainer"] p {
                color: white !important;
            }
            .stButton button div[data-testid="stMarkdownContainer"] {
                color: white !important;
            }
            
            /* Navigation styling */
            .nav-button {
                margin: 5px;
                padding: 8px 15px;
                border-radius: 5px;
                background-color: white;
                cursor: pointer;
            }
        </style>
    """, unsafe_allow_html=True)
    
    # Navigation buttons
    col1, col2, col3 = st.columns([8, 1.2, 1.2])
    with col2:
        if st.button('💬 Chat', key='nav_chat', help='Open AI Assistant', use_container_width=True):
            st.switch_page("pages/1_Chat.py")
    # with col3:
    #     if st.button('🏠 Home', key='nav_home', help='Return Home', use_container_width=True):
    #         st.switch_page("main.py")

    # Button text color fix
    st.markdown("""
        <style>
            /* Style for button text */
            .stButton button div[data-testid="stMarkdownContainer"] {
                color: white !important;
            }
        </style>
    """, unsafe_allow_html=True)

    # Initialize session state
    if 'show_chat' not in st.session_state:
        st.session_state['show_chat'] = False

    # Main content
    if st.session_state['show_chat']:
        chat_with_pdf()
    else:
        # Header with Hitachi logo
        st.markdown(
            r"""
            <div class="header-container">
                <h1 class='heading-text'>AgroGPT</h1>
            </div>
            """, unsafe_allow_html=True
        )
        
        st.subheader('Your AI-Powered Agricultural Knowledge Assistant')
        st.markdown("Transforming agricultural knowledge sharing through AI")

        # Landing page styling
        st.markdown("""
            <style>
                .stApp, .section, .hero-section, .feature-section, .stats-section, 
                .testimonial-section, .feature-card, .cta-section {
                    background-color: #e0f0e3 !important;  /* Pastel green */
                }
                
                /* Fix text color */
                .stMarkdown, .stHeader, p, h1, h2, h3 {
                    color: #333333 !important;
                }
                
                /* Ensure metric values are visible */
                [data-testid="stMetricValue"] {
                    color: #333333 !important;
                }
                
                /* Ensure metric labels are visible */
                [data-testid="stMetricLabel"] {
                    color: #666666 !important;
                }
                /* Hide sidebar by default */
                [data-testid="stSidebar"][aria-expanded="true"] {
                    display: none;
                }
                [data-testid="stSidebar"][aria-expanded="false"] {
                    display: none;
                }
                
                /* Show sidebar on hover */
                [data-testid="stSidebar"]:hover {
                    display: flex !important;
                    margin-right: 0 !important;
                }

                .section {
                    padding: 4rem 0;
                    border-bottom: 1px solid #eee;
                }
                .header-container {
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    width: 100%;
                    padding: 20px 0;
                    background-color: #e0f0e3;
                    margin-bottom: 20px;
                }
                .heading-text {
                    text-align: center;
                    margin: 0;
                    padding: 0;
                    font-size: 50px;
                    color: black;
                }
                .logo-img {
                    width: 120px;
                    margin-right: 10px;
                }
                .hero-section {
                    background-color: #e0f0e3;
                    text-align: center;
                    padding: 2rem 0;
                }
                .feature-section {
                    background-color: #e0f0e3;
                }
                .feature-card {
                    padding: 2rem;
                    border-radius: 15px;
                    background-color: #e0f0e3;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                    margin-bottom: 2rem;
                    transition: transform 0.3s ease;
                }
                .feature-card:hover {
                    transform: translateY(-5px);
                }
                .stats-section {
                    background-color: #e0f0e3;
                    text-align: center;
                }
                .testimonial-section {
                    background-color: #e0f0e3;
                }
                .cta-section {
                    background-color: #e0f0e3;
                    text-align: center;
                    padding: 4rem 0;
                }
                .img-fluid {
                    max-width: 100%;
                    height: auto;
                    border-radius: 10px;
                }
            </style>
        """, unsafe_allow_html=True)

        # Platform Overview Section
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.header('Agricultural Intelligence Platform')
        col1, col2 = st.columns([1, 1])
        with col1:
            # Placeholder for the flow diagram image
            st.image("https://via.placeholder.com/400x300?text=Agricultural+Flow+Diagram", 
                    caption="Agricultural Intelligence Flow Diagram",
                    use_column_width=True)
        with col2:
            st.markdown("""
            - **Smart Document Processing**: Convert agricultural documents into actionable insights
            - **AI-Powered Analysis**: Advanced algorithms for agricultural data interpretation
            - **Real-time Assistance**: Instant answers to farming queries
            """)
        st.markdown('</div>', unsafe_allow_html=True)

        # Features Section
        st.markdown('<div class="feature-section section">', unsafe_allow_html=True)
        st.header('Key Features')
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

        # Stats Section with image
        st.markdown('<div class="stats-section section">', unsafe_allow_html=True)
        # Placeholder for stats visualization
        st.image("https://via.placeholder.com/800x200?text=Statistics+Visualization",
                caption="Agricultural Statistics Overview",
                use_column_width=True)
        stat1, stat2, stat3 = st.columns(3)
        with stat1:
            st.metric(label="Active Users", value="10,000+")
        with stat2:
            st.metric(label="Documents Processed", value="50,000+")
        with stat3:
            st.metric(label="Success Rate", value="98%")
        st.markdown('</div>', unsafe_allow_html=True)

        # Testimonials Section
        st.markdown('<div class="testimonial-section section">', unsafe_allow_html=True)
        st.header('What Our Users Say')
        test1, test2 = st.columns(2)
        with test1:
            st.markdown('<div class="feature-card">', unsafe_allow_html=True)
            st.markdown("👤")
            st.markdown("*'AgriCopilot has revolutionized how we access agricultural information.'*")
            st.markdown('</div>', unsafe_allow_html=True)
        with test2:
            st.markdown('<div class="feature-card">', unsafe_allow_html=True)
            st.markdown("👤")
            st.markdown("*'This tool has transformed our farming practices for the better.'*")
            st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # CTA Section
        st.markdown('<div class="cta-section">', unsafe_allow_html=True)
        st.header('Get Started with AgroGPT Today')
        st.subheader("Your Agricultural Knowledge Companion")
        if st.button("Start Now"):
            st.write("Redirecting to registration page...")
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
