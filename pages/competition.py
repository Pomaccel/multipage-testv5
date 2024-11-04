import streamlit as st

def main():
    # builds the sidebar menu
    with st.sidebar:
        st.page_link('streamlit_app.py', label='Home', icon='🔥')
        st.page_link('pages/competition.py', label='Member', icon='🛡️')

    st.title(f'🛡️ Member')

    # your content

if __name__ == '__main__':
    main()