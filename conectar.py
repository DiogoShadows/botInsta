from time import sleep

class Conectar:

    def Conexao(driver, username, password):
        driver.get("https://www.instagram.com")
        sleep(3)

        xpathUsernameField = "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input"
        xpathPasswordField = "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input"
        xpathEnterField = "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]"

        driver.find_element_by_xpath(xpathUsernameField).send_keys(username)
        driver.find_element_by_xpath(xpathPasswordField).send_keys(password)
        driver.find_element_by_xpath(xpathEnterField).click()
        sleep(10)

