from selenium import webdriver

# chrome driver downloaded from
# https://chromedriver.storage.googleapis.com/index.html?path=88.0.4324.96/

def get_medicament():
    # using Chrome to access web
    driver = webdriver.Chrome()

    # open the website
    driver.get('http://base-donnees-publique.medicaments.gouv.fr')

    # get the search input
    search_input = driver.find_element_by_id('txtCaracteres')

    # fill the search input
    search_input.send_keys('plaquenil')

    # get the search button
    search_button = driver.find_element_by_id('btnMedic')

    # click on the search button
    print(search_button.click())

    return {'status': 'wip'}

