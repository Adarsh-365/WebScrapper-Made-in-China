


import requests
from bs4 import BeautifulSoup
import random

import time
import xlwt
from xlwt import Workbook
import xlsxwriter

# Workbook() takes one, non-optional, argument
# which is the filename that we want to create.


Contact_1=None
Contact_2=None
Contact_3=None



# from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup


from selenium.webdriver.firefox.options import Options

# create webdriver object


# get google.co.in










# company_name_list=[]
# company_revenu_list=[]



# row = 1
# column = 0



user_agents_list = [
    'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
]

Login=False

def Function(a,b):
  global Login
  name="data_"+str(a)+"_"+str(b)
  Excell=name+".xlsx"
  # workbook = xlsxwriter.Workbook(Excell)

  # # The workbook object is then used to add new
  # # worksheet via the add_worksheet() method.
  # worksheet = workbook.add_worksheet()

  # # Use the worksheet object to write
  # # data via the write() method.

  # worksheet.write('A1', 'Product Name')
  # worksheet.write('B1', 'Company Name')
  # worksheet.write('C1', 'Member Type')
  # worksheet.write('D1', 'Audited')
  # worksheet.write('E1', 'Contact1')
  # worksheet.write('F1', 'Contact2')
  # worksheet.write('G1', 'Fax Number')
  # worksheet.write('H1', 'Revenu')
  wb = Workbook()
  # driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
# 
  # options = webdriver.ChromeOptions()
    
  # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
  #   driver = webdriver.Chrome(
  #   service= Service(chromedriver_path), 
  #   options=options,
  #   )
  options = Options()
  options.add_argument('--headless')
  driver = webdriver.Firefox()
  # add_sheet is used to create sheet.
  sheet1 = wb.add_sheet('Sheet 1')

  row = 1
  column = 0
 
  for i in range(a,b,1):
    # name="data_1_5"
    url="https://www.made-in-china.com/multi-search/smps/F1--CC_Guangdong_Shenzhen--CP_Guangdong--BT_1/"+str(i)+".html"
    print("page",i+1)

# url="https://www.made-in-china.com/multi-search/smps/F1--CC_Guangdong_Shenzhen--CP_Guangdong--BT_1/1.html"
    
    
    # def Write_in_Page1_data(r):
    #     with open("DATA_of_page1.html", "w", encoding="utf-8") as f:
    #         f.write(r.text)
            
    
    
    
    
    # r = requests.get(url, headers={'User-Agent': random.choice(user_agents_list)})
    # Write_in_Page1_data(r)
    
    if not Login:
          
        username="triangle.sim@gmail.com"
        password="Tspl1951-"
        driver.get("https://login.made-in-china.com/sign-in/?baseNextPage=https%3A%2F%2Fwww.made-in-china.com%2Fmulti-search%2Fsmps%2FF1--CC_Guangdong_Shenzhen--CP_Guangdong--BT_1%2F1.html")
    
        # driver.get("https://github.com/login")
        # find username/email field and send the username itself to the input field
        driver.find_element("id", "logonInfo.logUserName").send_keys(username)
        # find password input field and insert password as well
        driver.find_element("id", "logonInfo.logPassword").send_keys(password)
        # click login button
        driver.find_element("id", "sign-in-submit").click()
        Login=True
    
    
        # html = driver.page_source

    
    
    
    
    # with open("DATA_of_page1.html","r", encoding="utf-8") as f:
    #     html_doc=f.read()
    
    # def Write_in_text(r):
    #     with open("scrap22.html", "w", encoding="utf-8") as f:
    #         f.write(r.text)
            


   

    # r = requests.get(url, headers={'User-Agent': random.choice(user_agents_list)})
    # Write_in_text(r)
    # with open("scrap22.html","r", encoding="utf-8") as f:
    #     html=f.read()
    time.sleep(5)
    driver.get(url)
    html = driver.page_source
  
    soup = BeautifulSoup(html, 'html.parser')
    # soup = BeautifulSoup(html_doc, 'html.parser')
    
    company_name_elements = soup.find_all('div', {'class': 'prod-info'})
    count=0
    # print(company_name_elements)
  
    for element in company_name_elements:
        # print(element)
        # time.sleep(5000)
        print(count)
        count+=1
        try:
            company_name = element.find('h2', {'class': 'product-name'})
            product_name=company_name.text.strip()#complete
        except:
            product_name=None
            
        company_name_1 = element.find('div', {'class': 'company-name-wrapper'})
        # print(company_name_1)
        try:
            company_name = company_name_1.find('span').text
        except:
            company_name=None
        try:
            company_links = company_name_1.find('a')['href']
        except:
            company_links=None
        try:    
            Supiler = company_name_1.find_all('img')
            Member=Supiler[0]["alt"]
            Audited=Supiler[1]["alt"]
        except:
            Member=None
            Audited=None
           
        print(Member,Audited)        
        print(product_name)
        print(company_name)
        print(company_links)
        # time.sleep(500)
        print(i,"End of comany data-----------------------")
        
        
    # =============================================================================
    #     
    # =============================================================================
        if company_links:
            if company_links[0:6]=="https:":
                
                url=company_links
                
            else:
                url="https:"+company_links
    
        # def Write_in_company_site(r):
        #     with open("DATA_Page1.html", "w", encoding="utf-8") as f:
        #         f.write(r.text)
                
    
    
    
    
        # r = requests.get(url, headers={'User-Agent': random.choice(user_agents_list)})
        # Write_in_company_site(r)
        
            time.sleep(3)
            driver.get(url)
            html = driver.page_source
            
            # with open("DATA_Page1.html","r", encoding="utf-8") as f:
            #     html_doc1=f.read()
        
            soup = BeautifulSoup(html, 'html.parser')
        
            nav_menu = soup.find('div', {'class': 'sr-nav-wrap'})
            # print(soup)
            if nav_menu:
                nav_links = nav_menu.find('ul', {'class': 'sr-nav-main'})
                nav_links = nav_links.find_all('a', {'class': 'sr-nav-title'})
            
                about_us_link = nav_links[2]['href']  # Index 2 corresponds to the "About Us" link
                try:
                    contact_us_link=nav_links[5]['href']
                except:
                    contact_us_link=nav_links[4]['href']
        
        
            else:
                nav_menu = soup.find('div', {'class': 'sr-virtual-nav J-nav cf'})
        
                nav_links = nav_menu.find('ul', {'class': 'sr-virtual-nav-main'})
                nav_links1 = nav_links.find_all('li', {'class': 'sr-virtual-nav-item'})
        
                list_link=[]
                for item in nav_links1:
                    nav_links2 = item.find('a', {'class': 'sr-virtual-nav-title'})['href']
                    list_link.append(nav_links2)
                    
                about_us_link=list_link[3]
                contact_us_link=list_link[6]
            # Print or use the About Us link as needed
            # print(contact_us_link)
            if contact_us_link:
                time.sleep(2)
                driver.get(contact_us_link)
                html_doc1 = driver.page_source
                
                
                
                soup = BeautifulSoup(html_doc1, 'html.parser')
                nav_menu = soup.find('div', {'class': 'sr-layout-block contact-block'})
            
                nav_menu = nav_menu.find('div', {'class': 'contact-info'})
                all_menu= nav_menu.find_all('div', {'class': 'info-item'})
            
                Data_of_contact=[]
                for menu in all_menu:
                    data= menu.find('div', {'class': 'info-fields'})
                    try:
                        mob_no=data.text.strip()
                    except:
                        mob_no=None
                    Data_of_contact.append(mob_no)
                try:
                    Contact_1=Data_of_contact[3]
                except:
                    Contact_1=None
                try:
                    Contact_2=Data_of_contact[4]
                except:
                    Contact_2=None
                    
                try:
                    
                    Contact_3=Data_of_contact[5]
                    
                except:
                    Contact_3=None
                if Contact_1:
                    for c in Contact_1:
                        if c=="-" or c.isnumeric():
                                pass
                        else:
                            Contact_1=None
                            break
                if Contact_2:       
                    for c in Contact_2:
                        if c=="-" or c.isnumeric():
                                pass
                        else:
                            Contact_2=None
                            break
                if Contact_3:
                    for c in Contact_3:
                        if c=="-" or c.isnumeric():
                                pass
                        else:
                            Contact_3=None
                            break
                print(Contact_1,Contact_2,Contact_3)
                
            # def Write_in_about_us(r):
            #     with open("about_us_page1.html", "w", encoding="utf-8") as f:
            #         f.write(r.text)
                    
        
        
            # r_about_us_link = requests.get(about_us_link, headers={'User-Agent': random.choice(user_agents_list)})
            # Write_in_about_us(r_about_us_link)
            if about_us_link:
                time.sleep(3)
                driver.get(about_us_link)
                html = driver.page_source
                
                # with open("about_us_page1.html","r", encoding="utf-8") as f:
                #     about_us_doc1=f.read()
            
                soup = BeautifulSoup(html, 'html.parser')
            
                label_element = soup.find('div', {'class': 'sr-layout-block pad-block J-block', 'id': 'richNav_3'})
            
            
                fields_element = label_element.find_all('div', {'class': 'sr-comProfile-fields'})
            
            
            
                # print(fields_element)
            
                for label_element in fields_element:
                        # print()
                       
                      if "$" in label_element.text.strip():
                          print(label_element.text.strip())
                          revenu=label_element.text.strip()
                          # company_revenu_list.append(revenu)
                      else:
                          print("not_found")
                          revenu="not_found"
                          # company_revenu_list.append(revenu)
            
                 
               
                # print(product_name)
                # print(company_name)
                # print(company_links)
                Data_text=name+".txt"
                with open(Data_text,"a") as f:
                    info=str(product_name)+","+str(company_name)+","+str(Member)+","+str(Audited)+","+str(Contact_1)+","+str(Contact_2)+","+str(Contact_3) +","+str(revenu)+'\n'
                    f.write(info)
                    
                # worksheet.write('A'+str(row), str(product_name))
                # worksheet.write('B'+str(row), str(company_name))
                # worksheet.write('C'+str(row), str(Member))
                # worksheet.write('D'+str(row), str(Audited))
                # worksheet.write('E'+str(row), str(Contact_1))
                # worksheet.write('F'+str(row), str(Contact_2))
                # worksheet.write('G'+str(row), str(Contact_3))
                # worksheet.write('H'+str(row),  str(revenu))
                    
                sheet1.write(row, column, str(product_name))
                sheet1.write(row, column+1, str(company_name))
                sheet1.write(row, column+2, str(Member))
                sheet1.write(row, column+3, str(Audited))
                sheet1.write(row, column+4, str(Contact_1))
                sheet1.write(row, column+5, str(Contact_2))
                sheet1.write(row, column+6, str(Contact_3))
                sheet1.write(row, column+7, str(revenu))
                row+=1  
               
                wb.save(Excell)
               
          
        
             
        
        
        
# Function(105, 110)
       
        
        
        
