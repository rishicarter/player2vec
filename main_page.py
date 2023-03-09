import streamlit as st
from data_driver import player2vec_data

# App Config
st.set_page_config(
    page_title="Player2Vec App",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state='collapsed',
    menu_items={
        'About': "Player2Vec: Web App to compare football players' playing style!"
    }
)

# Functions

def display_similar_players(selected_similar_players):
    text=""
    for i in range(selected_similar_players):
        text+=f"{i+1}. Ronaldo "
    return text

# App Info
st.title('Player2Vec: Analysing Soccer Players\' Playing Style using DL')
st.markdown('Analysing 4000+ soccer players\' playing styles using Convolutional Autoencoder \
           and compressing player data from 2000 matches, using WYSCOUT open-source dataset, into a player vector called Player2Vec.')
st.caption('### :red[Check out my Thesis write up here] - [LINK](https://github.com/rishicarter/MScProject_SOTON/blob/main/RishiAluri_Dissertation.pdf)')

st.subheader('Application of knowing a players\' play Style')
st.markdown('Football fans frequently debate the top players in the sport by comparing their individual playing styles. However, with the limited number of positions on the field and the similarities in styles among players, it is difficult for data analysts to differentiate them based on playing style. Nonetheless, it is crucial for football clubs to understand their players\' playing styles for practical reasons such as:')
row_space1,col1,col2,col3,row_space2=st.columns((1,3,3,3,1))
col1.caption('| 📈:red[Player Development Monitoring] |\n| - |')
col2.caption('| 🔁:red[Player Recplacement - Scouting] |\n| - |')
col3.caption('| 👯‍♂️:red[Player Similarity Analysis - Strategy/Scouting] |\n| - |')

# Player Similarity
similarity_container=st.container()
similarity_container.subheader('Player Similarity Analysis')
similarity_container.caption(':red[NOTE] - player data w.r.t to season 2018-19')
with similarity_container:
    row_space1,col_sim_name,row_space2,col_sim_options,row_space3,disp_row=st.columns((0.5,2.5,0.5,2.5,0.5,2.5))
    selected_player_name=col_sim_name.selectbox('Select a Player', options=['Messi','Ronaldo'], key='sim_player_name')
    selected_similar_players=col_sim_options.select_slider('Number of Similar Players', options=(range(2,6)),
                                  value=2, key='similar_num')
    test=f"Top :red[{selected_similar_players}] similar player to :red[{selected_player_name}] are:\n| :red[Selected player] | :red[Similar Players Ranking] |\n|-|-|\n| {selected_player_name} | {display_similar_players(selected_similar_players)} |"
    disp_row.write(test)
    with similarity_container.expander('Comaprision based on Heatmaps:'):
        # st.write('#### Comaprision based on Heatmaps:')
        st.write('Hi')
    
    with similarity_container.expander('Comparision based on Key Performance Indicators:'):
        st.write('Hi')

# Player Compare
compare_container=st.container()
compare_container.subheader('Player Compare')
compare_container.caption(':red[NOTE] - player data w.r.t to season 2018-19')
with compare_container:
    row_space1,col_comp_name1,row_space2,col_vs,col_comp_name2,row_space3=st.columns((1,4,1,2,4,1))
    selected_player_name1=col_comp_name1.selectbox('Select a Player', options=['Messi','Ronaldo'], key='comp_player_name1')
    selected_player_name2=col_comp_name2.selectbox('Select a Player', options=['Messi','Ronaldo'], key='comp_player_name2')
    col_vs.markdown('# :red[VS]')
    with compare_container.expander('Comaprision based on Heatmaps:'):
        # st.write('#### Comaprision based on Heatmaps:')
        st.write('Hi')
    
    with compare_container.expander('Comparision based on Key Performance Indicators:'):
        st.write('Hi')