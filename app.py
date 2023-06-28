import pandas as pd
import plotly.graph_objects as go
import streamlit as st

def add_background_image():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://wallpapercave.com/wp/wp9542654.png");
            background-attachment: fixed;
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def main():
    df = pd.read_csv('2023_nba_playoffs.csv')

    st.title('🏀2023 NBA Playoffs Stat Recap')
    st.markdown('Select a statistical category to view the leaders for that stat.')

    # Apply CSS to adjust the width of the select box
    st.markdown(
        """
        <style>
        .stSelectbox > div:first-child {
            width: 300px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    selected_option = st.selectbox('Select a category', ['Points Per Game', 'Assists Per Game', 'Rebounds Per Game', 'Games Played', 'Minutes Per Game', 'Field Goals Made', 'Field Goals Attempted', 'Field Goal Percentage', 'Three Pointers Made', 'Three Pointers Attempted', 'Three Point Percentage', 'Free Throws Made', 'Free Throws Attempted', 'Free Throw Percentage', 'Offensive Rebounds Per Game', 'Defensive Rebounds Per Game', 'Steals Per Game', 'Blocks Per Game', 'Turnovers Per Game', 'Personal Fouls Per Game'])

    if selected_option == 'Points Per Game':
        stat_column = 'PPG'
        title = 'Points Per Game'
    elif selected_option == 'Assists Per Game':
        stat_column = 'APG'
        title = 'Assists Per Game'
    elif selected_option == 'Rebounds Per Game':
        stat_column = 'RPG'
        title = 'Rebounds Per Game'
    elif selected_option == 'Games Played':
        stat_column = 'GP'
        title = 'Games Played'
    elif selected_option == 'Minutes Per Game':
        stat_column = 'MPG'
        title = 'Minutes Per Game'
    elif selected_option == 'Field Goals Made':
        stat_column = 'FGM'
        title = 'Field Goals Made'
    elif selected_option == 'Field Goals Attempted':
        stat_column = 'FGA'
        title = 'Field Goals Attempted'
    elif selected_option == 'Field Goal Percentage':
        stat_column = 'FG%'
        title = 'Field Goal Percentage'
    elif selected_option == 'Three Pointers Made':
        stat_column = '3PM'
        title = 'Three Pointers Made'
    elif selected_option == 'Three Pointers Attempted':
        stat_column = '3PA'
        title = 'Three Pointers Attempted'
    elif selected_option == 'Three Point Percentage':
        stat_column = '3P%'
        title = 'Three Point Percentage'
    elif selected_option == 'Free Throws Made':
        stat_column = 'FTM'
        title = 'Free Throws Made'
    elif selected_option == 'Free Throws Attempted':
        stat_column = 'FTA'
        title = 'Free Throws Attempted'
    elif selected_option == 'Free Throw Percentage':
        stat_column = 'FT%'
        title = 'Free Throw Percentage'
    elif selected_option == 'Offensive Rebounds Per Game':
        stat_column = 'ORB'
        title = 'Offensive Rebounds Per Game'
    elif selected_option == 'Defensive Rebounds Per Game':
        stat_column = 'DRB'
        title = 'Defensive Rebounds Per Game'
    elif selected_option == 'Steals Per Game':
        stat_column = 'SPG'
        title = 'Steals Per Game'
    elif selected_option == 'Blocks Per Game':
        stat_column = 'BPG'
        title = 'Blocks Per Game'
    elif selected_option == 'Turnovers Per Game':
        stat_column = 'TOV'
        title = 'Turnovers Per Game'
    elif selected_option == 'Personal Fouls Per Game':
        stat_column = 'PF'
        title = 'Personal Fouls Per Game'

    # Sort the DataFrame by the selected stat column in ascending order
    df = df.sort_values(by=stat_column, ascending=True)

    # Create a dictionary of colors for each unique team
    team_colors = {
        'MIL': '#00471B',
        'MIA': '#98002E',
        'CLE': '#860038',
        'NYK': '#F58426',
        'PHI': '#006BB6',
        'BRK': '#000000',
        'BOS': '#007A33',
        'ATL': '#E03A3E',
        'DEN': '#0E2240',
        'MIN': '#0C2340',
        'PHX': '#1D1160',
        'LAC': '#C8102E',
        'SAC': '#5A2D81',
        'GSW': '#006BB6',
        'MEM': '#5D76A9',
        'LAL': '#552583',
    }

    # Create a list to store the colors for each player
    colors = [team_colors.get(team, 'gray') for team in df['Team']]

    # Create a horizontal bar chart using plotly.graph_objects
    fig = go.Figure()

    # Add horizontal bars with custom colors and labels
    fig.add_trace(go.Bar(
        x=df[stat_column],
        y=df['Player'],
        orientation='h',
        marker=dict(color=colors),
        text=df[stat_column],  # Display the selected stat values as text labels
        textposition='inside'  # Display text labels inside the bars
    ))

    # Update layout parameters
    fig.update_layout(
        title=title,
        xaxis_title=title,
        yaxis_title='Player',
        height=len(df) * 50,  # Adjust the multiplication factor as needed
        margin=dict(l=150)  # Adjust the left margin as needed
    )

    # Display the plot
    st.plotly_chart(fig)

# Run the Streamlit app
if __name__ == '__main__':
    main()
    add_background_image()
