import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base_driver import BaseDriver
from utilities.util import Utils


class SerachFlightPage(BaseDriver):
    log =Utils.custom_logger(logLevel=logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        # self.wait = wait
    FILTER_BY_0_STOP ="//p[normalize-space()='0']"
    FILTER_BY_1_STOP = "//p[normalize-space()='1']"
    FILTER_BY_2_STOP = "//p[normalize-space()='2']"
    SERACH_FLIGHT_RESULTS="//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'1 Stop')]"

    def getFiletrBy0Stop(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.FILTER_BY_0_STOP)

    def getFiletrBy1Stop(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.FILTER_BY_1_STOP)

    def getFiletrBy2Stop(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.FILTER_BY_2_STOP)

    def filter_flights_by_stops(self,by_stop):
        if by_stop=="1 Stop":
            self.getFiletrBy1Stop().click()
            self.log.debug("select flight with 1 stops")
            time.sleep(3)

    def getSerachFlightResults(self):
        return self.wait_for_presence_of_all_elements_located(By.XPATH,self.SERACH_FLIGHT_RESULTS)


