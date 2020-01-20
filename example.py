from selenium import webdriver
import os



#path of folder which contains files you want to upload and calculate various metrices of
path = 'C:\\Users\\ROHAN\\Desktop\\readme'
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
    driver.get('http://textalyser.net/')
    
    #uploads the file and then click on submit button
    choose_file = driver.find_element_by_name('file_to_analyze')
    file_location = os.path.join(f'{f}')
    choose_file.send_keys(file_location)    
    submit_assignment = driver.find_element_by_xpath('/html/body/form/input')
    submit_assignment.click()
    
    #finds the data you want to scrap
    user_message = driver.find_elements_by_xpath('/html/body/table[8]/tbody/tr[4]/td[2]')[0]
    comment = user_message.text
    
    #writes the extracted on a file
    with open('lexicaldensit.txt','a') as huh:
        huh.write(f[30:])
        huh.write(' ')
        huh.write(comment)
        huh.write('\n')
    print(f)
    driver.close()
