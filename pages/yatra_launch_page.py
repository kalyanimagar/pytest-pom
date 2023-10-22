import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from base.base_driver import BaseDriver
from pages.serach_flight_result_page import SerachFlightPage


class LaunchPage(BaseDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        # self.wait=wait
    DEPARET_FROM_FILED="//input[@id='BE_flight_origin_city']"
    GOING_TO_FIELD="//input[@id='BE_flight_arrival_city']"
    GOING_TO_RESULTS="//div[@class='viewport']//div//li"
    SELECT_DATE_FIELD="//input[@id='BE_flight_origin_date']"
    ALL_DATES="//div[@id='monthWrapper']//tbody//td"
    SERACH_BUTTON="//input[@value='Search Flights']"

    def getDepartFromField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.DEPARET_FROM_FILED)

    def getGoingToField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.GOING_TO_FIELD)

    def getGoingToResults(self):
        return self.wait_for_presence_of_all_elements_located(By.XPATH,self.GOING_TO_RESULTS)

    def getDepartureDateField(self):
        return self.wait_until_element_is_clickable(By.XPATH,self.SELECT_DATE_FIELD)

    def getAlllDatesFields(self):
        return self.wait_until_element_is_clickable(By.XPATH,self.ALL_DATES)

    def getSerachButton(self):
        return self.wait_until_element_is_clickable(By.XPATH,self.SERACH_BUTTON)

    def  enterDepartFromLocation(self,departlocation):
        self.getDepartFromField().click()
        self.getDepartFromField().send_keys(departlocation)
        self.getDepartFromField().send_keys(Keys.ENTER)
        time.sleep(5)

    def enterGoingToLocation(self,goingToLocation):
        self.getGoingToField().click()
        self.getGoingToField().send_keys(goingToLocation)
        result = self.getGoingToResults()
        time.sleep(2)
        for citi in result:
            if goingToLocation in citi.text:
                citi.click()
                break
        time.sleep(5)

    def enterDepartureDate(self,departureDate):
        self.getDepartureDateField().click()
        dates=self.getAlllDatesFields().find_elements(By.XPATH,self.ALL_DATES)
        for date in dates:
            if date.get_attribute('data-date') == departureDate:
                date.click()
                break
        time.sleep(5)

    def click_submit(self):
        self.getSerachButton().click()
        time.sleep(4)

    def serachFlights(self,departfromlocation,goingtilocation,departuredate):
        self.enterDepartFromLocation(departfromlocation)
        self.enterGoingToLocation(goingtilocation)
        self.enterDepartureDate(departuredate)
        self.click_submit()
        search_flight = SerachFlightPage(self.driver)
        return search_flight

