import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import fitz  # PyMuPDF

# Load the CSV data
csv_file_path = 'tlist140.csv'
data = pd.read_csv(csv_file_path)

csv_file_path1 = 't200-full.csv'
data1 = pd.read_csv(csv_file_path1)
# Function to filter the data based on the 'Unique to Region' column
def filter_unique_to_region(data):
    return data[(data['Unique to Region'].str.lower() != 'no') & 
                (data['Unique to Region'].str.lower() != 'No') &
                ((data['Unique to Region'].str.lower() == 'yes') |
                 (data['Unique to Region'].str.split().str.len() > 1))]

filtered_data = filter_unique_to_region(data)

# Load PDF content
with open("tlist-sum-brief.pdf", "rb") as f:
    summary_brief_pdf = f.read()

with open("tlist-sum-briefadd.pdf", "rb") as f:
    additional_brief_pdf = f.read()

with open("MENA_sum1.pdf", "rb") as f:
    MENA_sum1_pdf = f.read()
with open("short_list.pdf", "rb") as f:
    short_list_pdf = f.read()
# Function to apply text color based on conditions
def color_text(val):
    color = 'green' if val.lower() == 'yes' else 'orange'
    return f'color: {color}'

# Streamlit App
st.set_page_config(page_title="MENA Region Games", layout="wide")

# Enable dark mode
st.markdown("<style>body {background-color: #212121;}</style>", unsafe_allow_html=True)

# Custom CSS to hide the Streamlit menu and footer
hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# Sidebar Navigation
page = st.sidebar.radio("Select Page", ["Main Page", "Summary Brief", "Additional Brief", "MENA Research"])
st.sidebar.download_button("MENA research - Download PDF", MENA_sum1_pdf, file_name="MENA_sum1.pdf")
st.sidebar.warning("based on UAE TOP 50 FREE, PAID, GROSSING - 6/30 & FREE, NEW FREE, PAID - 7/15")

# Main Page
if page == "Main Page":
    st.title("Emphasize Summarized MENA Only Regionally Unique Games That Are Succeeding")
    st.subheader("Highlighting Success Factors and Unique Features")
    
    # Display the filtered CSV data
    st.dataframe(filtered_data.style.applymap(color_text, subset=['Unique to Region']))
    
    st.image("pic1.PNG")
    st.image("pic2.PNG")
    # Generate charts from the filtered data
    st.subheader("Charts")
    
    # Count the number of items for "Why Unique"
    st.write("Count of Why Unique")
    why_unique_counts = data['Why Unique'].value_counts()  # Showing counts for all data
    st.bar_chart(why_unique_counts)
    
    # Count the number of items for "Hyper-Localized Success"
    st.write("Count of Hyper-Localized Success")
    hyper_localized_success_counts = filtered_data['Hyper-Localized Success'].value_counts()
    st.bar_chart(hyper_localized_success_counts)
    
    # Count the number of items for "Success Metrics"
    st.write("Count of Success Metrics")
    success_metrics_counts = filtered_data['Success Metrics'].value_counts()
    st.bar_chart(success_metrics_counts)
    
    # Create a new table for entries with any answer except 'no' in the "Unique to Region" column
    st.subheader("Top Android - Unique & Hyper-Localized Success")
    st.dataframe(data)
    st.image("top_chart.PNG")
    st.subheader("Addtional Game Details List")
    st.dataframe(data1)
    st.write("Top - themes in games")
    st.image("pic7.png")
    st.write("Short list - hyper localized games")
    st.image("pic8.PNG")
    st.image("pic8a.PNG")
        # Download button for the summary brief PDF
    st.download_button("Download PDF - short list", short_list_pdf, file_name="short_list.pdf")
    st.write("Android charts - appfigures.com / data.ai")
    st.image("pic3.PNG")
    st.image("pic4.PNG") 
    st.write("Ios charts - appfigures.com / data.ai")
    st.image("pic5.PNG")
    st.image("pic6.PNG") 
    
# PDF Pages
elif page == "Summary Brief":
    st.title("Summary Brief")
    st.subheader("Trends in Regionally Unique Games")

    # Display the summary brief as markdown text
    st.markdown("""
    
    ### Emphasize Summarized MENA Only Regionally Unique Games That Are Succeeding 
    #### Highlighting Success Factors and Unique Features
    <span style="color: #FF9900;">        
    
   
    In the MENA region, games that incorporate local culture, traditions, and preferences tend to resonate well with players. This summary highlights some of the top regionally unique games and the factors contributing to their success.

    **Revenge of Sultans:**
    - **Description:** A strategy game set in a historical Arabian context.
    - **Region:** Predominantly popular in Saudi Arabia and UAE.
    - **Unique to Region:** Incorporates Middle Eastern culture and history.
    - **Why Unique:** Utilizes themes and narratives that resonate with local players.
    - **Hyper-Localized Success:** High engagement due to cultural relevance.
    - **Success Metrics:** High downloads, significant in-app purchases, and active daily users.
    
    **Arabian Nights:**
    - **Description:** An adventure game inspired by the classic tales of the Arabian Nights.
    - **Region:** Popular in Gulf countries.
    - **Unique to Region:** Features characters and stories from regional folklore.
    - **Why Unique:** Appeals to cultural nostalgia and local storytelling traditions.
    - **Hyper-Localized Success:** Strong player retention and word-of-mouth popularity.
    - **Success Metrics:** High retention rates and positive user reviews.
    
    **Quran Quiz:**
    - **Description:** An educational game that quizzes players on their knowledge of the Quran.
    - **Region:** Widely used across the MENA region.
    - **Unique to Region:** Focuses on religious education, important to the region.
    - **Why Unique:** Combines gaming with educational content relevant to local religious practices.
    - **Hyper-Localized Success:** High engagement during religious periods such as Ramadan.
    - **Success Metrics:** Consistent daily active users and high engagement during peak periods.
    </span>
    """, unsafe_allow_html=True)

    st.markdown("""            
    **Arabian Nights: The Adventure of Sindbad:**
    - **Description:** A narrative-driven adventure game based on Arabian folklore.
    - **Unique Features:** Highlights the importance of cultural relevance in game development.
    - **Success Factors:** High engagement due to cultural connections and relevance.
    
    **Yalla Ludo:**
    - **Description:** A social multiplayer game combining Ludo and Domino games with online features.
    - **Unique Features:** Demonstrates the popularity of localized board games with social elements.
    - **Success Factors:** Strong social features, local language support, high player engagement.
    
    **Fortnite MENA:**
    - **Description:** A customized version of Fortnite with regional servers and localized content.
    - **Unique Features:** Demand for global games with local flavor.
    - **Success Factors:** Regional servers, localized content, high player engagement.
    
    **8 Ball Pool:**
    - **Description:** An online multiplayer pool game with features tailored to the MENA region.
    - **Unique Features:** High engagement with multiplayer features and regional relevance.
    - **Success Factors:** Custom events and localized content.
    
    **Jawaker Hand, Trix & Solitaire:**
    - **Description:** Digital versions of popular card games with online multiplayer.
    - **Unique Features:** Traditional card games prevalent in the Middle East.
    - **Success Factors:** High engagement through multiplayer features and culturally relevant updates.
    
    **Ludo King:**
    - **Description:** Digital version of the classic board game Ludo, featuring online multiplayer.
    - **Unique Features:** Popular board game with online multiplayer twist.
    - **Success Factors:** High engagement through multiplayer features.
    
    **Mobile Legends: Bang Bang:**
    - **Description:** Multiplayer online battle arena (MOBA) game with various heroes and abilities.
    - **Unique Features:** High engagement with multiplayer features.
    - **Success Factors:** High engagement and multiplayer features.
    
    **MONOPOLY GO!:**
    - **Description:** Digital version of the classic board game Monopoly with online multiplayer.
    - **Unique Features:** Popular board game with an online multiplayer twist.
    - **Success Factors:** High engagement through multiplayer features.
    
    **PUBG Mobile:**
    - **Description:** Battle royale game with realistic graphics and large-scale battles.
    - **Unique Features:** High engagement and custom events tailored to the MENA region.
    - **Success Factors:** Custom events and Arabic language support.
    
    **Conclusion:**
    The success of games in the MENA region is highly dependent on their ability to incorporate local cultural elements, offer localized content, and provide strong social features. By focusing on these factors, game developers can create more targeted and appealing games for this market.
    """)
    
    # Download button for the summary brief PDF
    st.download_button("Download PDF", summary_brief_pdf, file_name="tlist-sum-brief.pdf")

elif page == "Additional Brief":
    st.title("Additional Brief")
    st.subheader("Insights and Recommendations")

    # Display the additional brief as markdown text
    st.markdown("""
    ### Trends in Regionally Unique Games
    <span style="color: #FF9900;">  
    ** Cultural Relevance**
    - Games that incorporate local culture, folklore, and history resonate with players in the region, providing a sense of ownership and trust.
    
    **1. Localized Board Games**
    - Traditional board games with an online multiplayer twist are popular, indicating a preference for social, family-friendly entertainment.
    
    **2. Regional Servers and Localization**
    - Games that offer regional servers and localized content are successful, highlighting the importance of catering to local preferences and language support.
    </span>
    """, unsafe_allow_html=True)

    st.markdown("""
    ### Hyper-Localized Game Themes
    
    **1. Local Cultural Heritage**
    - Games that incorporate elements from local folklore, art, and traditions are well-received.
    - Example: Arabian Nights: The Adventure of Sindbad
    
    **2. Family-Friendly Entertainment**
    - Games that offer social, multiplayer experiences suitable for all ages are popular in the region.
    - Example: Yalla Ludo
    
    **3. Localized Game Genres**
    - Games that blend global genres with local twists, such as Ludo with online multiplayer features, are successful in the region.
    - Example: Ludo King
    
    ### Insights
    - **Cultural relevance is crucial for success in the MENA region.**
    - **Localized board games with online multiplayer features are popular.**
    - **Regional servers and localized content are essential for success.**
    - **Games that incorporate local cultural elements are well-received.**
    - **Family-friendly entertainment and localized game genres are popular in the region.**
    
    ### Recommendations
    - **Prioritize cultural relevance and localization in game development.**
    - **Incorporate local cultural  elements, language support, and regional servers to cater to the MENA region's unique preferences.**
    - **Develop games that blend global genres with local twists to increase their chances of success in the region.**
    - **Focus on family-friendly entertainment and localized game genres to appeal to a broader audience in the MENA region.**
    - **Approach cultural incorporation sensitively, avoiding stereotypes and tokenization to ensure authenticity and respect for the region's culture.**
    """)

    # Download button for the additional brief PDF
    st.download_button("Download PDF", additional_brief_pdf, file_name="tlist-sum-briefadd.pdf")


elif page == "MENA Research":
    st.title("MENA Research")
    st.subheader("More Insights and Recommendations")

        # Open the PDF file with PyMuPDF
    with open("MENA_sum1.pdf", "rb") as file:
        pdf_document = fitz.open(stream=file.read(), filetype="pdf")

    # Initialize a variable to store the text
    text = ''

    # Loop through each page in the PDF file
    for page_num in range(len(pdf_document)):
        # Get the current page
        page = pdf_document.load_page(page_num)

        # Extract the text from the page
        page_text = page.get_text()

        # Add the text to the total text
        text += page_text

    # Close the PDF file
    pdf_document.close()

    # Display the extracted text
    st.text_area("Extracted pdf Text", text, height=500)

st.info("build by dw  v1.2 7/24/24")