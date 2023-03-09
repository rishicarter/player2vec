# # Constants
# all_players= './Wyscout/final_results_allplayers.h5'

#imports
import pandas as pd
import os

# Class driver
class player2vec_data:
    filepath=os.path.abspath(os.path.join('Wyscout','final_results_allplayers.h5'))
    player_data_df=None
    def __init__(self):
        self.player_data_df=pd.read_hdf(self.filepath,'all_players')
        
    def __init__(self, filter_player='Messi'):
        pass
    
    # Get top 2-5 players HMS
    
    # Get top 2-5 players KPI features
    
    # Compare Any two players HMS and Features
    
