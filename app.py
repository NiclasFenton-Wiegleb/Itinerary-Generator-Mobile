import streamlit as st
import pandas as pd
import numpy as np
import random
import folium
from PIL import Image
from streamlit_folium import st_folium, folium_static
import streamlit.components.v1 as components  # Import Streamlit


st.title("Manchester: Make Your Day!")

intro_txt = f"""Are you visiting Manchester? Do you live here and want to explore some new things to do in the city?
Check out this AI generator to plan your day out! It's constantly updated with the latest recommendations and exciting new places.
And if you already know some of the recommendations, use the arrows to find somewhere else close by."""

st.markdown(intro_txt)

route_data = "./OptimalRoutes.csv"
dataset = "./IG_neighbours.csv"

@st.cache_data
def load_data(route_data_path, dataset_path):

    route_data = pd.read_csv(route_data_path)
    dataset = pd.read_csv(dataset_path)

    return route_data, dataset

# Create a text element and let the reader know the data is loading
data_load_state = st.text("Loading data...")
# Load 10,000 rows of data into the dataframe
route_data, dataset = load_data(route_data_path=route_data, dataset_path=dataset)
# Notify the reader that the data was successfully loaded
data_load_state.text("")



# Initialise the key in session state
if 'button' not in st.session_state:
    st.session_state.button = {1:False,2:False, 3:False}

# Initialise route index in session state
if 'route_idx' not in st.session_state:
    st.session_state.route_idx = [0]

# Initialise Brunch session state
if 'brunch' not in st.session_state:
    st.session_state.brunch = 3

#Clean path for image retrieval
def retrieve_img(image_path):
    file_path = image_path.replace(" ", "_")
    file_path = file_path.replace("'", "")
    file_path = file_path.replace("`", "")
    file_path = file_path.replace("’", "")
    
    image = Image.open(file_path)

    return image


# Function to update the value in session state
def next_brunch(button):
    '''When the Next button is clicked, the text of the next
    alternative stop should be displayed'''
    if button < 3:
        st.session_state.brunch += 1
    else:
        st.session_state.brunch = 0

def previous_brunch(button):
    '''When the Previous button is clicked, the text of the previous
    alternative stop should be displayed'''
    if button <= 3 and button > 0:
        st.session_state.brunch -= 1
    else:
        st.session_state.brunch = 3

# Initialise Activity session state
if 'activity' not in st.session_state:
    st.session_state.activity = 3


# Function to update the value in session state
def next_activity(button):
    '''When the Next button is clicked, the text of the next
    alternative stop should be displayed'''
    if button < 3:
        st.session_state.activity += 1
    else:
        st.session_state.activity = 0

def previous_activity(button):
    '''When the Previous button is clicked, the text of the previous
    alternative stop should be displayed'''
    if button <= 3 and button > 0:
        st.session_state.activity -= 1
    else:
        st.session_state.activity = 3

# Initialise Drinks session state
if 'drinks' not in st.session_state:
    st.session_state.drinks = 3


# Function to update the value in session state
def next_drinks(button):
    '''When the Next button is clicked, the text of the next
    alternative stop should be displayed'''
    if button < 3:
        st.session_state.drinks += 1
    else:
        st.session_state.drinks = 0

def previous_drinks(button):
    '''When the Previous button is clicked, the text of the previous
    alternative stop should be displayed'''
    if button <= 3 and button > 0:
        st.session_state.drinks -= 1
    else:
        st.session_state.drinks = 3

# Initialise Dinner session state
if 'dinner' not in st.session_state:
    st.session_state.dinner = 3

# Function to update the value in session state
def next_dinner(button):
    '''When the Next button is clicked, the text of the next
    alternative stop should be displayed'''
    if button < 3:
        st.session_state.dinner += 1
    else:
        st.session_state.dinner = 0

def previous_dinner(button):
    '''When the Previous button is clicked, the text of the previous
    alternative stop should be displayed'''
    if button <= 3 and button > 0:
        st.session_state.dinner -= 1
    else:
        st.session_state.dinner = 3

# Initialise Evening session state
if 'evening' not in st.session_state:
    st.session_state.evening = 3

# Function to update the value in session state
def next_evening(button):
    '''When the Next button is clicked, the text of the next
    alternative stop should be displayed'''
    if button < 3:
        st.session_state.evening += 1
    else:
        st.session_state.evening = 0

def previous_evening(button):
    '''When the Previous button is clicked, the text of the previous
    alternative stop should be displayed'''
    if button <= 3 and button > 0:
        st.session_state.evening -= 1
    else:
        st.session_state.evening = 3



def select_route():
    st.session_state.route_idx[0] = random.randint(0, len(route_data))
    st.session_state.button[1] = True

#Fixing issue of buttons going over rows in mobile version
def fix_mobile_columns():    
    st.write('''<style>
    [data-testid="column"] {
        width: calc(16.666667% - 1rem) !important;
        flex: 1 1 calc(16.666667% - 1rem) !important;
        min-width: calc(16.666667% - 1rem) !important;
    }
    </style>''', unsafe_allow_html=True)

#Fixing horizontal scroll issue on mobil version
def fix_horizontal_scroll():
    st.write('''<style>
    div {
    overflow-x: hidden;
    }
    </style>''', unsafe_allow_html=True)

#Fixin vertical scroll issue on mobil version
def fix_vertical_scroll():
    st.write('''<style>
    [data-testid="container"] {
    max-width: 100%;
    overflow-y: hidden;
    }
    </style>''', unsafe_allow_html=True)

# Select fonts
def fonts():
    
    #div
    st.write('''<style>
    div {
    font-stretch: expanded;
    }
    </style>''', unsafe_allow_html=True)
    
    #heading - h1
    st.write('''<style>
    h1 {
    font-family: "Basis Grotesque", sans-serif;
    }
    </style>''', unsafe_allow_html=True)

    #paragraphs
    st.write('''<style>
    p {
    font-family: "Gill Sans", sans-serif;
    font-stretch: expanded;
    font-size: 15px;
    }
    </style>''', unsafe_allow_html=True)

def map_layout():

    #folium map style
    st.write('''<style>
    .folium-map {
        diplay: block;
        margin-left: auto;
        margin-right: auto;
        padding-bottom: 30px;
        width: 70%;
    }
    </style>''', unsafe_allow_html=True)

fonts()
fix_mobile_columns()

col1,col2, col3 = st.columns([1,1,1], gap="small")

# Button with callback function
button_txt = "Generate"
button = col2.button(button_txt, on_click=select_route)

if st.session_state.button[1] == True:
    
    try:
        # Initialise listes for each entry to draw from
        title_lst = ["1. Brunch", "2. Activity", "3. Afternoon Drinks", "4. Dinner", "5. Evening Out"]
        alt_lst = ["neighbour_1", "neighbour_2", "neighbour_3"]
        stop_lst = ["stop_1", "stop_2", "stop_3", "stop_4", "stop_5"]
        state_lst = [st.session_state.brunch, st.session_state.activity, st.session_state.drinks, st.session_state.dinner, st.session_state.evening]
        next_lst = [next_brunch, next_activity, next_drinks, next_dinner, next_evening]
        prev_lst = [previous_brunch, previous_activity, previous_drinks, previous_dinner, previous_evening]
        
        long_lst = [0,0,0,0,0]
        lat_lst = [0,0,0,0,0]
        name_lst = ["", "", "", "", ""]
        address_lst = ["", "", "", "", ""]
        link_lst = ["", "", "", "", ""]

        df = pd.DataFrame(columns=["long", "lat", "name", "stop", "address", "link"])
        
        for x, item in enumerate(stop_lst):

            # fix_horizontal_scroll()

            col1,col2,col3,col4,col5,col6 = st.columns([1,1,1,1,1,1], gap="small")

            state = state_lst[x]
            next_func = next_lst[x]
            prev_func = prev_lst[x]
            y = x+10

            # Next Button
            with col6:
                with st.container():
                    st.write('''<style>
                        [data-testid="button"] {
                            margin-left: auto; 
                            margin-right: 0;
                        }
                        </style>''', unsafe_allow_html=True)
                    next_txt = "⇨"
                    next_stop = st.button(next_txt, on_click=next_func, key=x, args=[state])

            # Previous Button
            with col1:
                with st.container():
                    st.write('''<style>
                        [data-testid="button"] {
                            margin-right: auto; 
                            margin-left: 0;
                        }
                        </style>''', unsafe_allow_html=True)
                    prev_txt = "⇦"
                    prev_stop = st.button(prev_txt, on_click=prev_func, key=y, args=[state])
            

            if state == 3:

                # col4, col5, col6 = st.columns((1,2,1), gap="small")

                #Id stop for Brunch
                stop = int(route_data[item][st.session_state.route_idx])

                image_1 = retrieve_img(f"""./images/{dataset.name.iloc[stop]}_001.jpg""")
                image_2 = retrieve_img(f"""./images/{dataset.name.iloc[stop]}_002.jpg""")

                with st.container():
                    fix_vertical_scroll()
                    st.markdown(f"""## {title_lst[x]}""")  # title
                    st.markdown(f"""### {dataset.name.iloc[stop]}""")  # name
                    st.image([image_1, image_2], caption= ["", f"""Source: {dataset.img_source.iloc[stop]}"""], width = 300, use_column_width= True) # images
                    st.markdown(f"""**Address:** {dataset.address.iloc[stop]}""")  # address
                    st.markdown(f"""**Link:** {dataset.link.iloc[stop]}""") #link to website

                long_lst[x] = dataset.long_coordinates.iloc[stop] #longitude
                lat_lst[x] = dataset.lat_coordinates.iloc[stop] #latitude
                name_lst[x] = str(dataset.name.iloc[stop])
                address_lst[x] = str(dataset.address.iloc[stop])
                link_lst[x] = str(dataset.link.iloc[stop])

            
            else:

                column = str(alt_lst[state])
                stop = int(dataset[column][int(route_data[item][st.session_state.route_idx])])

                image_1 = retrieve_img(f"""./images/{dataset.name.iloc[stop]}_001.jpg""")
                image_2 = retrieve_img(f"""./images/{dataset.name.iloc[stop]}_002.jpg""")

                with st.container():
                    fix_vertical_scroll()
                    st.markdown(f"""## {title_lst[x]}""")  # title
                    st.markdown(f"""### {dataset.name.iloc[stop]}""")  # name
                    st.image([image_1, image_2], caption= ["", f"""Source: {dataset.img_source.iloc[stop]}"""], width = 300, use_column_width= True) # images
                    st.markdown(f"""**Address:** {dataset.address.iloc[stop]}""")  # address
                    st.markdown(f"""**Link:** {dataset.link.iloc[stop]}""") #link to website

                long_lst[x] = dataset.long_coordinates.iloc[stop] #longitude
                lat_lst[x] = dataset.lat_coordinates.iloc[stop] #latitude
                name_lst[x] = str(dataset.name.iloc[stop])
                address_lst[x] = str(dataset.address.iloc[stop])
                link_lst[x] = str(dataset.link.iloc[stop])
            
            df.long = long_lst
            df.lat = lat_lst
            df.name = name_lst
            df.stop = title_lst
            df.address = address_lst
            df.link = link_lst

        m = folium.Map(location=[df.lat.mean(), df.long.mean()], 
                        zoom_start=12, control_scale=True)

        #Loop through each row in the dataframe
        for i,row in df.iterrows():
            #Setup the content of the popup
            stop = str(row["stop"])
            name = str(row["name"])
            address = str(row["address"])
            link = str(row["link"])

            pop_txt = f"""<b>{stop}</b>
                    <br><b>{name}</b>
                    <br><a href={link} target="_blank">Link to website</a>
                    <br><b>Address:</b> {address}
                    """

            iframe = folium.IFrame(pop_txt)
                
            #Initialise the popup using the iframe
            popup = folium.Popup(iframe, min_width=200, max_width=200)
                
            #Add each row to the map
            folium.Marker(location=[row['lat'],row['long']],
                            popup = popup, c=row['name']).add_to(m)
        

        st_data = folium_static(m, width= 500)
    
    except:

         #Error handling - print message if error occurs

        col1, col2, col3 = st.columns([1,5,1], gap="small")
        error_txt =  "## Error: That didn't go quite as planned! 🫠 Please try again."
        col2.markdown(error_txt)

        


