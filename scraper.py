from selenium import webdriver
import os




path = #path of folder which contains files you want to upload and calculate various metrices of
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.txt' in file:
            files.append(os.path.join(r,file))



#runs the following code for every file
for f in files:
    #uses google chrome to open website
    driver = webdriver.Chrome()
    driver.get(#website you want to scrap data from)
    
    #chooses the file and uploads it
    choose_file = driver.find_element_by_name(#id/name of the upload button element)
    file_location = os.path.join(f'{f}')
    choose_file.send_keys(file_location)    
    submit_assignment = driver.find_element_by_xpath(#xpath of submit button element)
    submit_assignment.click()
    
    #scraps data
    user_message = driver.find_elements_by_xpath('''xpath of the element you want to scrap data from''')[0]
    comment = user_message.text
    
    #writes the data into a file
    with open('FileName.txt','a') as huh:
        
        huh.write(' ')
        huh.write(comment)
        huh.write('\n')
    print(f)
    driver.close()