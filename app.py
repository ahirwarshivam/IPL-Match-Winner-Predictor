import streamlit as st
import base64
import pickle
import pandas as pd
import plotly.graph_objects as go


st.set_page_config(
    page_title="IPL Prediction AI",
)

# Background Image
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

bg_img = get_base64("pitch_bck.jpeg")

page_bg = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background:
        linear-gradient(
            rgba(0,0,0,0.45),
            rgba(0,0,0,0.45)
        ),
        url("data:image/jpg;base64,{bg_img}");

    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

[data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
}}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# Load model and dataset
pipe = pickle.load(open('rf_pipe.pkl', 'rb'))
final_data = pickle.load(open('final_data.pkl', 'rb'))

# Title
st.markdown("""
<div style='text-align:center; margin-bottom:20px;'>
<span style='
background:#1F2937;
padding:10px 25px;
border-radius:25px;
color:white;
font-weight:bold;
font-size:20px;'>
🔴 LIVE IPL PREDICTION ENGINE ACTIVE
</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<h1 style='
text-align:center;
color:white;
font-size:75px;
font-weight:1000;
margin-bottom:5px;
'>
IPL MATCH WINNER PREDICTOR
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h3 style='
text-align:center;
color:#B0B0B0;
margin-bottom:40px;
'>
Real-Time Win Probability Engine Powered by Machine Learning
</h3>
""", unsafe_allow_html=True)


# Teams and Venues
teams = sorted(final_data['batting_team'].unique())
venues = sorted(final_data['venue'].unique())

# Team Colors
team_colors = {
    "Chennai Super Kings": "#F9CD05",
    "Mumbai Indians": "#004BA0",
    "Royal Challengers Bangalore": "#EC1C24",
    "Kolkata Knight Riders": "#A855F7",
    "Rajasthan Royals": "#EA1A85",
    "Sunrisers Hyderabad": "#FF822A",
    "Delhi Capitals": "#17479E",
    "Punjab Kings": "#D71920",
    "Gujarat Lions": "#FF6F00",
    "Deccan Chargers": "#1E90FF",
    "Kochi Tuskers Kerala":"#6EE7B7",
    "Pune Warriors": "#005BAC",
    "Rising Pune Supergiant": "#7B3F98"
}


# Teams and Venues
teams = sorted(final_data['batting_team'].unique())
venues = sorted(final_data['venue'].unique())

# Team Selection
col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox(
        "Search or Select Batting Team",
        teams,
        index=None,
        placeholder="Enter Batting team name..."
    )

with col2:
    bowling_team = st.selectbox(
        "Search or Select Bowling Team",
        teams,
        index=None,
        placeholder="Enter Bowling team name..."
    )

# Validation
if batting_team and bowling_team:
    if batting_team == bowling_team:
        st.error("Batting and Bowling team cannot be the same, Choose the right one.")

# Venue Selection
venue = st.selectbox(
    "Search or Select Venue",
    venues,
    index=None,
    placeholder="Enter the Venue name..."
)

# Target Score
target = st.number_input(
    "Target Score",
    min_value=1,
    step=1
)

# Match Situation Inputs
col3, col4, col5 = st.columns(3)

with col3:
    score = st.number_input(
        "Current Score",
        min_value=0,
        step=1
    )

with col4:
    overs = st.number_input(
        "Overs",
        min_value=0,
        max_value=20,
        step=1
    )

    balls = st.number_input(
        "Balls",
        min_value=0,
        max_value=5,
        step=1
    )

with col5:
    wickets = st.number_input(
        " Wickets Fallen",
        min_value=0,
        max_value=10,
        step=1
    )

# Prediction Button
predict_btn = st.button("Predict Probability")

st.markdown('</div>', unsafe_allow_html=True)


if predict_btn:

    runs_left = target - score
    balls_bowled = overs * 6 + balls
    balls_left = 120 - balls_bowled
    wickets_left = 10 - wickets

    balls_bowled = overs * 6 + balls

    if balls_bowled == 0:
        current_rr = 0
    else:
        current_rr = score * 6 / balls_bowled

    if balls_left == 0:
        required_rr = 0
    else:
        required_rr = (runs_left * 6) / balls_left

    input_df = pd.DataFrame({
        'venue': [venue],
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'runs_left': [runs_left],
        'balls_left': [balls_left],
        'wickets_left': [wickets_left],
        'current_rr': [current_rr],
        'required_rr': [required_rr]
    })

    result = pipe.predict_proba(input_df)

    loss = result[0][0]
    win = result[0][1]

    winner_team = batting_team if win > loss else bowling_team
    winner_prob = round(max(win, loss) * 100)

    batting_color = team_colors.get(batting_team, "#FFFFFF")
    bowling_color = team_colors.get(bowling_team, "#FFFFFF")

    st.markdown(f"""
    <div style="
    background: rgba(255,215,0,0.12);
    border: 2px solid gold;
    border-radius: 20px;
    padding: 20px;
    margin-top: 20px;
    margin-bottom: 30px;
    text-align: center;
    backdrop-filter: blur(10px);
    ">

    <h2 style="
    color: gold;
    margin-bottom: 10px;
    ">
    🏆 PREDICTED WINNER
    </h2>

    <h1 style="
    color: white;
    font-size: 50px;
    margin-bottom: 10px;
    ">
    {winner_team}
    </h1>

    <h3 style="
    color: #E5E7EB;
    ">
    {winner_prob}% Win Probability
    </h3>

    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(f"""
        <h2 style='text-align:center;color:{batting_color};'>
        {batting_team}
        </h2>

        <h1 style='text-align:center;color:white;font-size:80px;'>
        {round(win * 100)}%
        </h1>

        <h3 style='text-align:center;color:white;'>
        Win Probability
        </h3>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown(f"""
        <h2 style='text-align:center;color:{bowling_color};'>
        {bowling_team}
        </h2>

        <h1 style='text-align:center;color:white;font-size:80px;'>
        {round(loss * 100)}%
        </h1>

        <h3 style='text-align:center;color:white;'>
        Win Probability
        </h3>
        """, unsafe_allow_html=True)

    # Section Distributor
    st.markdown("""
    <hr style="
    height:3px;
    border:none;
    border-radius:10px;
    background:linear-gradient(to right,#FFD700,#FF8C00,#FFD700);
    width:95%;
    margin:auto;
    margin-top:25px;
    margin-bottom:25px;
    box-shadow:0 0 10px rgba(255,215,0,0.6);
    ">
    """, unsafe_allow_html=True)
    # Upto there

    st.markdown("### Match Win Probability Breakdown")

    col3, col4 = st.columns(2)

    with col3:
        st.markdown(f"""
        <p style='color:white;font-size:22px;font-weight:bold;'>
        {batting_team}
        </p>

        <div style="
        width:100%;
        background:#2d2d2d;
        height:22px;
        border-radius:12px;
        ">
            <div style="
            width:{round(win * 100)}%;
            background:#00A3FF;
            height:22px;
            border-radius:12px;
            text-align:center;
            color:white;
            font-weight:bold;
            ">
            {round(win * 100)}%
            </div>
       
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <p style='color:white;font-size:22px;font-weight:bold;'>
        {bowling_team}
        </p>
        
        <div style="
        width:100%;
        background:#2d2d2d;
        height:22px;
        border-radius:12px;
        ">

        <div style="
        width:{round(loss * 100)}%;
        background:#00A3FF;
        height:22px;
        border-radius:12px;
        text-align:center;
        color:white;
        font-weight:bold;
        ">
        {round(loss * 100)}%
        </div>
        
        """, unsafe_allow_html=True)

    values = [round(win * 100), round(loss * 100)]
    labels = [batting_team, bowling_team]

    pull = [0, 0]

    if values[0] > values[1]:
        pull = [0.12, 0]
    else:
        pull = [0, 0.12]

    fig = go.Figure(
        data=[
            go.Pie(
                labels=labels,
                values=values,
                hole=0.55,
                pull=pull,
                textinfo="label+percent"
            )
        ]
    )

    fig.update_layout(
        title="Win Probability Distribution",
        height=450,
        width=850,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(
            color='white',
            size=16
        )
    )

    # Section distributor
    st.markdown("""
    <hr style="
    height:3px;
    border:none;
    border-radius:10px;
    background:linear-gradient(to right,#FFD700,#FF8C00,#FFD700);
    width:95%;
    margin:auto;
    margin-top:25px;
    margin-bottom:25px;
    box-shadow:0 0 10px rgba(255,215,0,0.6);
    ">
    """, unsafe_allow_html=True)

    # bar graph adding
    col_left, spacer, col_right = st.columns([8, 1, 6])

    import plotly.express as px

    rr_df = pd.DataFrame({
        "Metric": ["Current RR", "Required RR"],
        "Run Rate": [round(current_rr, 1), round(required_rr, 1)]
    })

    fig_rr = px.bar(
        rr_df,
        x="Metric",
        y="Run Rate",
        text="Run Rate",
        title="Current RR vs Required RR"
    )

    fig_rr.update_traces(
        width=0.45,
        marker_color=["#00FF99", "#FF4B4B"],
        textposition="outside",
        textfont_size=18
    )

    fig_rr.add_scatter(
        x=["Current RR", "Required RR"],
        y=[round(current_rr, 2), round(required_rr, 2)],
        mode="lines+markers",
        line=dict(
            dash="dash",
            width=3,
            color="white"
        ),
        name="Comparison"
    )


    fig_rr.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white')
    )

    # Donut distribution

    with col_left:
        st.markdown(
            "<h3 style='text-align:center;'>Win Distribution</h3>",
            unsafe_allow_html=True
        )
        fig.update_traces(
            textposition="inside",
            textinfo="percent"
        )
        st.plotly_chart(fig, use_container_width=False)

    with col_right:
        st.markdown(
            "<h3 style='text-align:center;'>Run Rate Analysis</h3>",
            unsafe_allow_html=True
        )
        st.plotly_chart(fig_rr, use_container_width=True)


    # Bae graph suggestion

    if current_rr > required_rr:
        st.markdown("""
        <div style="
        background-color:rgba(0,255,0,0.15);
        color:white;
        padding:15px;
        border-radius:10px;
        text-align:center;
        font-size:20px;
        font-weight:bold;
        ">
        Batting team is scoring faster than the required rate.
        </div>
        """, unsafe_allow_html=True)

    else:
        st.markdown("""
        <div style="
        background-color:rgba(255,165,0,0.15);
        color:white;
        padding:15px;
        border-radius:10px;
        text-align:center;
        font-size:20px;
        font-weight:bold;
        ">
        Required run rate is higher than current run rate.
        </div>
        """, unsafe_allow_html=True)