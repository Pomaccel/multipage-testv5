import streamlit as st


def main():
    # builds the sidebar menu
    with st.sidebar:
        st.page_link('streamlit_app.py', label='Individual Checker', icon='🔥')
        st.page_link('pages/competition.py', label='Competition Checker', icon='🛡️')

    st.title(f'🛡️ Competition Checker')

    # your content


if __name__ == '__main__':
    main()