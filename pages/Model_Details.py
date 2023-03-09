import streamlit as st
import matplotlib.pyplot as plt
import os
from PIL import Image

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

st.title('_About Project - Player2Vec: Analysing Soccer Players\' Playing Style using Deep Learning_')

prob_stat="|:red[Problem Statement]|\n|--|\n|Deciding Best players to fit a team tactic|"
objectives="|:red[Objectives]|\n|--|\n|Characterize playing style into a player vector that is Human-interpretable and Suitable for data analysis|"
tasks="|:red[Tasks to acheave the Ojective]|\n|--|\n|1. Data Preparation|\n|2. Building player vector- Player2Vec|\n|3. Engineering Decision making attributes|"
data="|:red[Data Used for the Project]|\n|--|\n|Wyscout open source data containing match event data from 5 top leagues covering 1,941 matches|"
col1,col2,col3,col4=st.columns((1,1,1,1))
col1.write(prob_stat)
col2.write(objectives)
col3.write(tasks)
col4.write(data)

st.header('Designing Deep Learning Model')
st.subheader(':red[1. Data Preprocessing]')
col1,col2,col3=st.columns((1,3,1))
image_dp=Image.open(os.path.abspath('./images/data_prep1.jpg'))
col2.image(image_dp)

st.subheader(':red[2. Preparing Heatmap of a Player]')

col1,col2,col3,col4=st.columns(4)
with col1:
    """
    _A heatmap is the count of the total number of actions of action-type t performed by player p at a specific location on a spatial coordinate space i.e., the soccer pitch. For each player and action type, the following three steps are executed._
    """
with col2:
    """
	:red[Counting]: _First, Overlay a grid of size m × n on the soccer field. Next, select all the actions, of type t, performed by player p from the data set. Now, for every grid cell Xi, j, count the number of actions that started in that cell. As a result, we converted a variable-size collection of actions into a fixed-size matrix X ϵ Nm×n holding the raw counts per cell._
    """
with col3:
    """
	:red[Normalization]: _Normalize the matrix X such that each cell contains its count if player p had played only one game i.e., 90 minutes. If player p played 2000 minutes in total, then construct the normalized matrix X’=  90/2000X. Since two players having the same identical playing styles can have different minutes of play, normalization of data is quite important. For example, if player p1 played more minutes than player p2, then player p1’s matrix X will contain higher raw counts than the matrix of player p2 but after normalizing the heatmaps both players’ matrices will contain a count per 90mins._
    """
with col4:
    """
	:red[Smoothing]: _To promote smoothness in the counts of nearby cells, a Gaussian blur is applied to matrix X’. Gaussian blur, an image blurring technique in image processing, involves convolving X’ with a Gaussian function. Specifically, the value of each cell in X’ is replaced by a weighted average of itself and its neighborhood, leading to the blurred matrix X’’ ϵ R_+^mxn. The smoothened counts of X’ enhances the spatial coherence of the locations where the actions were performed.
    """

col1,col2,col3=st.columns((1,3,1))
image_dp=Image.open(os.path.abspath('./images/hm_create.jpg'))
col2.image(image_dp)

st.subheader(':red[3. Compressing Heatmaps to build Player2Vec]')
st.markdown('##### _3.1 Deep Learning for Feature Extraction and Dimensionality Reduction_ :')
st.markdown('The main step of building the Player2Vec vector is the extraction of the latent features from the Convolutional Autoencoder.')
col1,col2,col3=st.columns((1,3,1))
image_dp=Image.open(os.path.abspath('./images/main.jpg'))
col2.image(image_dp)
st.markdown("First, since the original heatmap is of size 48x48 in height and width, it will be highly computationally expensive to apply any data analytics tasks on it as the flattened heatmap will be of 2,304 dimensions in length. To counter this, we use the Convolutional Autoencoder to reduce the dimensionality of the heatmap from 2,304 dimensions to 32 dimensions. The latent feature space present in the bottleneck ‘code’ region of the CAE contains the compressed form of the original heatmap. This compression task is performed by the ‘Encoder’ part of the CAE.")
st.markdown("Second, we can then use the latent features to retrieve back the original heatmap. The reconstructed heatmap resembles the original heatmap in shape (48x48) as well as in numerical values. This reconstruction task is performed by the ‘Decoder’ part of the CAE.")

st.markdown('##### _3.2 DL Model Architecture_ :')
"""
The model architectures created and tested were inspired from the work of Masci, et al. to use Convolutional Autoencoders for hierarchical feature extraction. The design of the models tested were found to work well with three hidden layers for both encoder and decoder, containing a pair of Convolutional layers and Pooling layers.

The architecture of the best Convolutional Autoencoder model based on the visual accuracy of the reconstructed heatmaps was ‘MODEL27_CAE2’. This model not only provides good reconstructed heatmaps but also gave the best results from the Player Retrieval Task which is explained in the Evaluation section.
"""
col1,col2,col3=st.columns((1,3,1))
image_dp=Image.open(os.path.abspath('./images/CAE architecture.jpg'))
col2.image(image_dp)

"""
_Based on literature review, the architecture of the ‘MODEL27_CAE2’ was inspired to compose of:_
1.	Input layer: Input of the CAE was a heatmap of shape (48,48,1) where ‘1’ is the number of channels.
2.	Encoder layer: The inputted image is then sent to a convolutional layer with 8 filters of size (3x3), followed by an average pooling layer with pool-size (2x2). Then, a convolutional layer of 4 filters of size (3x3) followed by a similar average pooling layer. Finally, a convolutional layer of 2 filters was again followed by an average pooling layer. All the convolutional layers had ‘LeakyReLU’ as the activation function.
3.	Latent-Feature space: The latent representation is just a flatten layer that converts the shape (4,4,2) into 32 dimensions.
4.	Decoder layer: The latent features is first reshaped from 32 dimensions to (4,4,2) shape. Then using upsampling layer of size (2x2) and convolutional layer of same number of filters and sizes used in the encoder layer (but in reverse order), we recreate the heatmap with a shape of (48,48,8) where ‘8’ is the number of channels.
5.	Output layer: The output layer uses a convolutional layer with ‘sigmoid’ activation function and 1 filter to output a reconstructed heatmap of shape (48,48,1).
"""


st.subheader(':red[4. Complete Flow of the project]')
col1,col2,col3=st.columns((1,3,1))
image_dp=Image.open(os.path.abspath('./images/overall flow.jpg'))
col2.image(image_dp)