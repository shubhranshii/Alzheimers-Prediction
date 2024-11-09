from config import TEAM_MEMBERS
import streamlit as st


def team_members():
    st.markdown(f"<h1 style='text-align:center;'>Meet our team</h1>", unsafe_allow_html=True)
    st.markdown("<br><br><div class='team-container'>", unsafe_allow_html=True)

    left, mid, right = st.columns(3)

    with left:
        st.markdown(
            f"""
            <a href={TEAM_MEMBERS[0]['links'][0]} target="_blank">
                <div class='team-member'>
                    <h3>{TEAM_MEMBERS[0]['name']}</h3>
                    <p>{TEAM_MEMBERS[0]['enrollment']}</p>
                </div>
            </a>
            <br>
            """,
            unsafe_allow_html=True
        )

    with mid:
        st.markdown(
            f"""
            <a href={TEAM_MEMBERS[1]['links'][0]} target="_blank">
                <div class='team-member'>
                    <h3>{TEAM_MEMBERS[1]['name']}</h3>
                    <p>{TEAM_MEMBERS[1]['enrollment']}</p>
                </div>
            </a>
            <br>
            """,
            unsafe_allow_html=True
        )

    with right:
        st.markdown(
            f"""
            <a href={TEAM_MEMBERS[2]['links'][0]} target="_blank">
                <div class='team-member'>
                    <h3>{TEAM_MEMBERS[2]['name']}</h3>
                    <p>{TEAM_MEMBERS[2]['enrollment']}</p>
                </div>
            </a>
            <br>
            """,
            unsafe_allow_html=True
        )


        