import streamlit as st
import PyPDF2
import spacy
from sentence_transformers import SentenceTransformer, util
import numpy as np

# --- SOLUTION: Call set_page_config() as the very first Streamlit command ---
# It must be placed right after the imports.
st.set_page_config(layout="wide", page_title="CareerCore", page_icon="🧠")

# --- AI Model Loading ---
# We use st.cache_resource to load the models only once, which speeds up the app.

@st.cache_resource(show_spinner=False)
def load_spacy_model():
    """Loads the spaCy model and the custom EntityRuler."""
    nlp = spacy.load("en_core_web_lg")
    ruler = nlp.add_pipe("entity_ruler", before="ner")
    ruler.from_disk("skills.jsonl") # Load our custom skill patterns
    return nlp

@st.cache_resource(show_spinner=False)
def load_sentence_model():
    """Loads the Sentence Transformer model."""
    return SentenceTransformer('all-MiniLM-L6-v2')

# We create a single, custom spinner that runs while both models load.
with st.spinner("Scanning your resume..."):
    nlp = load_spacy_model()
    sentence_model = load_sentence_model()

# --- Core AI Functions ---

def extract_text_from_pdf(file_object):
    """Extracts text from a PDF file object."""
    try:
        reader = PyPDF2.PdfReader(file_object)
        return "".join(page.extract_text() for page in reader.pages)
    except Exception:
        st.error("Error reading the PDF file. It might be corrupted or protected.")
        return ""

def extract_skills_with_ner(text):
    """Uses our spaCy NER model to extract skills from text."""
    doc = nlp(text)
    skills = [ent.text for ent in doc.ents if ent.label_ == "SKILL"]
    return list(set([skill.lower() for skill in skills]))

def calculate_semantic_similarity(resume_text, jd_text):
    """Calculates the semantic similarity score between resume and JD."""
    resume_sentences = resume_text.split('.')
    jd_sentences = jd_text.split('.')
    resume_embeddings = sentence_model.encode(resume_sentences, convert_to_tensor=True)
    jd_embeddings = sentence_model.encode(jd_sentences, convert_to_tensor=True)
    cosine_scores = util.cos_sim(resume_embeddings, jd_embeddings)
    if cosine_scores.shape[1] == 0: return 0.0
    max_scores = cosine_scores.max(axis=0).values
    relevant_scores = max_scores[max_scores > 0.3]
    if len(relevant_scores) == 0: return 0.0
    avg_similarity = relevant_scores.mean().item() * 100
    return avg_similarity

# --- Streamlit UI ---
# The st.set_page_config() call was moved from here to the top of the file.

st.title("🧠 CareerCore")
st.markdown("The core components of a career profile..")

col1, col2 = st.columns(2)

with col1:
    st.header("📄 Your Resume")
    resume_file = st.file_uploader("Upload your resume (PDF)", type="pdf")

with col2:
    st.header("📋 Job Description")
    jd_text = st.text_area("Paste the job description here", height=300)

if st.button("Analyze with AI", type="primary"):
    if resume_file and jd_text:
        with st.spinner("The AI is thinking... This may take a moment."):
            resume_text = extract_text_from_pdf(resume_file)

            # --- AI-Powered Analysis ---
            resume_skills = extract_skills_with_ner(resume_text)
            jd_skills = extract_skills_with_ner(jd_text)
            
            # Keyword/NER Analysis
            matched_skills = list(set(resume_skills) & set(jd_skills))
            missing_skills = list(set(jd_skills) - set(resume_skills))
            keyword_score = (len(matched_skills) / len(jd_skills)) * 100 if jd_skills else 100

            # Semantic Analysis
            semantic_score = calculate_semantic_similarity(resume_text, jd_text)

            # --- Final Weighted Score ---
            final_score = (0.4 * keyword_score) + (0.6 * semantic_score)

        # --- Display Results ---
        st.header("🔬 Analysis Report")
        
        st.progress(int(final_score), text=f"**Overall Match Score: {final_score:.2f}%**")
        st.markdown("*(This score is a weighted average of Keyword Match and Semantic Context Similarity)*")

        metric1, metric2, metric3 = st.columns(3)
        metric1.metric("🔑 Keyword Match", f"{keyword_score:.2f}%", help="Based on skills explicitly found in both texts.")
        metric2.metric("🧠 Context Match", f"{semantic_score:.2f}%", help="How well the meaning and context of your resume match the job description.")
        metric3.metric("✅ Matched Skills", f"{len(matched_skills)} / {len(jd_skills)}")

        st.markdown("---")

        skill_col, rec_col = st.columns([2, 1])
        
        with skill_col:
            st.subheader("Skill Analysis")
            if matched_skills:
                st.success(f"**Matched Skills:** {', '.join(matched_skills)}")
            if missing_skills:
                st.warning(f"**Skills Missing from Resume:** {', '.join(missing_skills)}")

        with rec_col:
            st.subheader("💡 AI Recommendations")
            if final_score < 60:
                st.error("Significant improvements are needed. Focus on both adding missing keywords and better describing your experience to match the job's context.")
            elif final_score < 80:
                st.warning("Good match, but can be improved. Weave in missing skills and rephrase experience to align more closely with the job's responsibilities.")
            else:
                st.success("Excellent match! Your resume is well-aligned with this job description.")
            
            if missing_skills:
                st.write("- **Add Missing Skills:** Try to include: " + ", ".join(missing_skills[:3]) + "...")
            if semantic_score < 70:
                 st.write("- **Improve Context:** Your experience descriptions could be rephrased. Use similar language and action verbs as the job description to improve the semantic match.")

    else:
        st.error("Please upload a resume and paste a job description.")