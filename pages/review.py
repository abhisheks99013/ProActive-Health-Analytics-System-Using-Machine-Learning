import streamlit as st

# Simulated reviews for demonstration (replace with actual data in real application)
reviews = [
    {"username": "Abhishek", "review": "Great application! The features are very user-friendly and intuitive. I've had a wonderful experience using it."},
    {"username": "Ananya Shetty", "review": "I love the clean design and ease of use. However, it would be nice to have more customization options."},
    {"username": "Radhika", "review": "The performance is excellent, but I encountered a few bugs. Overall, it's a solid product."},
    {"username": "Aryan Chaudhary", "review": "Fantastic app! The support team was very helpful in resolving my issue quickly."},
    {"username": "Aisha", "review": "A good tool for the job, but it could benefit from additional features and enhancements."},
    {"username": "Asha", "review": "The app is easy to navigate, but I found the setup process a bit confusing. More tutorials would be helpful."},
    {"username": "Divya", "review": "Very useful application. It has greatly improved my workflow. I recommend it to others in my field."},
    {"username": "Swetha", "review": "The user interface is sleek and modern. I appreciate the attention to detail and usability."},
    {"username": "Aaliya", "review": "Good functionality, but there are occasional lags. Looking forward to updates that address these issues."},
    {"username": "Calvin", "review": "An overall positive experience. The app meets my needs and performs well."},
    {"username": "Neha", "review": "The app is excellent but could use some additional features for advanced users. Great overall experience!"}, 
    {"username": "Raj", "review": "Good tool but occasionally slow. Looking forward to performance improvements."},
    {"username": "Simran", "review": "I like the design and features. The app is very useful for my daily tasks."}
]

def app():
    
    # Center-align the content and style the review section
    st.markdown("""
    <style>
        body {
            font-family: 'Roboto', sans-serif;
        }
        .title {
            text-align: center;
            font-size: 2.5em;
            color: #003366;
            font-weight: bold;
            position: relative;
            animation: fadeIn 1s ease-out;
            text-shadow: 2px 2px 6px rgba(0, 0, 0, 0.3);
        }
        @keyframes fadeIn {
            0% {
                opacity: 0;
                transform: translateY(-20px);
            }
            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }
        .container { 
            position: relative; 
            max-width: 800px; 
            margin: 0 auto; 
            padding: 20px;
        }
        .review-card { 
            position: relative; 
            background-color: #fff; 
            border-radius: 10px; 
            box-shadow: 0 4px 8px rgba(0,0,0,0.2); 
            padding: 20px; 
            margin-bottom: 20px; 
            transition: transform 0.6s ease, box-shadow 0.6s ease; 
            z-index: 1;
        }
        .review-card:hover { 
            transform: scale(1.1); 
            box-shadow: 0 12px 24px rgba(0,0,0,0.3); 
        }
        .background-blur { 
            position: fixed; 
            top: 0; 
            left: 0; 
            width: 100%; 
            height: 100%; 
            background-color: rgba(0,0,0,0.7); 
            backdrop-filter: blur(12px); 
            transition: opacity 0.6s ease, visibility 0.6s ease, transform 0.6s ease; 
            opacity: 0; 
            visibility: hidden; 
            z-index: 0;
        }
        .background-blur.active { 
            opacity: 1; 
            visibility: visible; 
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Create a container for the background blur
    st.markdown('<div class="background-blur"></div>', unsafe_allow_html=True)

    # Heading with animation
    st.markdown('<div class="title">Review Page</div>', unsafe_allow_html=True)

    # Create a container for review cards
    st.markdown('<div class="container">', unsafe_allow_html=True)
    
    for review in reviews:
        # Create a review card
        st.markdown(f"""
        <div class="review-card" onmouseover="this.style.zIndex=2" onmouseout="this.style.zIndex=1">
            <p><strong>{review['username']}</strong></p>
            <p>{review['review']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    app()
