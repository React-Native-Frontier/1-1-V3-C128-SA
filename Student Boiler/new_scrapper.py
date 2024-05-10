from selenium import webdriver 
from selenium.webdriver.common.by import By  
from bs4 import BeautifulSoup  
import time 
import pandas as pd 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC  
# import request module


browser = webdriver.Chrome() 

new_planets_data = []  

def scrape_more_data(hyperlink):
        # Use request to get the hyperlink and store in page variable
        
        # Create soup using BeautifulSoup
        
        # Create empty temp_list
        
        # Create a list information_to_extract with text of each div for which information is needed
        
        

        # Run a for loop for each info_name in  information_to_extract
        
                # Add try block
                
                    # Get the value needed using find() and find_next() and append to temp_list

                # Add a except block

                    # Add Unknown to temp_list
                    
        # append temp_list to new_planets_data
        

# Read the scrapped_data.csv in planet_df_1

# Loop through each row 

    # Print hyperlink
    
    # Call scrap_more_data and pass hyperlink
    
    # Print Data scrapping at hyperlink completed
    

headers = ["planet_type","discovery_date", "mass", "planet_radius", "orbital_radius", "orbital_period", "detection_method"]
new_planet_df_1 = pd.DataFrame(new_planets_data,columns = headers)
new_planet_df_1.to_csv('new_scraped_data.csv',index=True, index_label="id")
