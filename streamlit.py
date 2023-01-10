import streamlit as st
import pandas as pd
import numpy as np
import plotly_express as px
import plotly.graph_objects as go
	
st.title('Data visulization hosting')
	



# 사이드바 만들기
with st.sidebar:
    option = st.selectbox(
        '데이터 선택',
        ("premier", "convenience_store", "Soccer")
    )
    st.write("Selected : ", option)





        
if option == "premier":
    data_load_state = st.text('Loading data...')
    data = pd.read_csv("premier.csv")
    data_load_state.text("Done!")
    option1 = st.selectbox(
        '상세정보',
        ("Goal","Conversion Rate", "ASST", "A_point","GA_point", "MA_point")
    )


    if option1 == "MA_point":
        fig=px.bar(data.sort_values(option1, ascending=True).head(10) , 
        x = 'PLAYER', y=option1, title=option1 + "  TOP10", text=option1,color='PLAYER')
    elif option1 == "Goal":
        fig=px.bar(data.head(10) , 
        x = 'PLAYER', y='G', title="Goal TOP10", text='G', color='PLAYER')
    else:
        fig=px.bar(data.sort_values(option1, ascending=False).head(10) , 
        x = 'PLAYER', y=option1, title=option1 + "  TOP10", text=option1,color='PLAYER')
        
    st.plotly_chart(fig)

    if st.checkbox('Show raw data'):
        st.subheader('Raw data')
        if option1 == "MA_point":
            st.write(data.sort_values(option1, ascending=True))
        elif option1 == "Goal":
            st.write(data)
        else:
            st.write(data.sort_values(option1, ascending=False))


elif option == "convenience_store":
    data_load_state = st.text('Loading data...')
    data_load_state.text("Done!")

    option1 = st.selectbox(
        '상세정보',
        ("GS25","Emart24")
    )

    data = pd.read_csv(option1+".csv")
    df = data[['lat','lon']]

    st.map(df)
    if st.checkbox('Show raw data'):
        st.subheader('Raw data')
        st.write(data)
    
elif option == "Soccer":
    data_load_state = st.text('Loading data...')
    data_load_state.text("Done!")

    option1 = st.selectbox(
        '상세정보',
        ("player","Match")
    )

    if option1 == "player":
        data = pd.read_csv(option1+".csv")
        option2 = st.selectbox(
        '상세정보',
        ("Lionel Messi","Cristiano Ronaldo",
        "Manuel Neuer","Luis Suarez","Neymar",
        "Zlatan Ibrahimovic","Arjen Robben","Eden Hazard",
        "Mesut Oezil","Sergio Aguero")
        )
        categories = list(data.columns[10:12])+list(data.columns[15:])
        player = ["Lionel Messi","Cristiano Ronaldo",
        "Manuel Neuer","Luis Suarez","Neymar",
        "Zlatan Ibrahimovic","Arjen Robben","Eden Hazard",
        "Mesut Oezil","Sergio Aguero"]
    
        fig = go.Figure(go.Scatterpolar(
            r = list(data.iloc[player.index(option2)][10:12])+list(data.iloc[player.index(option2)][15:]),
            theta = categories,
            fill = 'toself',
            name = option2
        ))
        
        fig = fig.update_layout(polar=dict(
            radialaxis=dict(
                visible=True, range=[0,100])
        ), showlegend=False, title_text = option2
        )
        fig = fig.update_layout(
            autosize=False,
            width=1000,
            height=850,
            margin=dict(
                l=50,
                r=50,
                b=100,
                t=100,
                pad=4
            ),
            
        )
        st.plotly_chart(fig)

        if st.checkbox('Show raw data'):
            st.subheader('Raw data')
            st.write(data)


    elif option1 == "Match":
        option2 = st.selectbox(
        '상세정보',
        ("Manchester","North_London",
        "NorthWest_London","EL")
        )
        data = pd.read_csv(option2+".csv")
        fig = px.pie(data, values=data['Winner'].value_counts(), names=data['Winner'].value_counts().index, title=option2)
        st.plotly_chart(fig)
        if st.checkbox('Show raw data'):
            st.subheader('Raw data')
            st.write(data)


    

