# # Constants
# all_players= './Wyscout/final_results_allplayers.h5'

#imports
import pandas as pd
import os
import streamlit as st

# Functions
@st.cache_data
def fetch_players_data(filepath):
    temp_df=pd.read_hdf(filepath,'all_players')
    return temp_df


# Class driver
class player2vec_data:
    filepath=os.path.abspath(os.path.join('Wyscout','final_results_allplayers.h5'))
    player_data_df=None
    selected_player=""
    def __init__(self):
        self.player_data_df=fetch_players_data(self.filepath)
    def set_player_data_df(self,name):
        self.player_data_df[self.player_data_df.player_name.str.contains(str(name))]
    def get_player_names(self):
        return self.player_data_df['player_name'].unique()
    def get_filtered_list(self,name):
        self.selected_player=name
        self.set_player_data_df(name)
        return self.player_data_df
    def get_n_hms(self,n=2):
        pass
        
    # Get top 2-5 players HMS
    
    # Get top 2-5 players KPI features
    
    # Compare Any two players HMS and Features
    
