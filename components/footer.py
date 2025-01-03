import streamlit as st

def render_footer():
    st.markdown(
        """
        <div style="background-color: #FFFFFF; color: black; text-align: center; padding: 20px; margin-top: 50px; border-top: 2px solid #000000; font-family: Georgia, serif;">
            <p style="font-size: 18px; font-weight: bold;">Connect with me:</p>
            <div style="display: flex; justify-content: center; gap: 20px; padding-bottom: 10px;">
                <a href="https://facebook.com/ahammadmejbah" target="_blank">
                    <img src="https://cdn-icons-png.flaticon.com/512/733/733547.png" alt="Facebook" width="30" style="transition: transform 0.2s;">
                </a>
                <a href="https://instagram.com/ahammadmejbah" target="_blank">
                    <img src="https://cdn-icons-png.flaticon.com/512/733/733558.png" alt="Instagram" width="30" style="transition: transform 0.2s;">
                </a>
                <a href="https://github.com/ahammadmejbah" target="_blank">
                    <img src="https://cdn-icons-png.flaticon.com/512/733/733553.png" alt="GitHub" width="30" style="transition: transform 0.2s;">
                </a>
                <a href="https://ahammadmejbah.com/" target="_blank">
                    <img src="https://cdn-icons-png.flaticon.com/512/919/919827.png" alt="Portfolio" width="30" style="transition: transform 0.2s;">
                </a>
                <a href="https://www.linkedin.com/in/ahammadmejbah/" target="_blank">
                    <img src="https://cdn-icons-png.flaticon.com/512/145/145807.png" alt="LinkedIn" width="30" style="transition: transform 0.2s;">
                </a>
                <a href="https://ahammadmejbah.com/" target="_blank">
                    <img src="https://cdn-icons-png.flaticon.com/512/2301/2301122.png" alt="Website" width="30" style="transition: transform 0.2s;">
                </a>
            </div>
            <br>
            <p style="font-size: 16px; font-weight: 500;">
                Scikit Learn Cheat Sheet v1.0 | Nov 2024 | 
                <a href="https://ahammadmejbah.com/" style="color: #000000; text-decoration: none;">Mejbah Ahammad</a>
            </p>
            <p style="font-size: 20px; color: #FF0000;">
                All content is © 2024 Scikit-Learn and Mejbah Ahammad. Unauthorized reproduction, distribution, or modification is strictly prohibited.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("<br><br>", unsafe_allow_html=True)
