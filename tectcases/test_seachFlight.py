import time

import pytest
import softest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.serach_flight_result_page import SerachFlightPage
from pages.yatra_launch_page import LaunchPage
from utilities.util import Utils
from ddt import ddt, unpack, data, file_data


@pytest.mark.usefixtures("setup")
@ddt
class TestSearchFlightdemo(softest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp=LaunchPage(self.driver)
        self.ut = Utils()

    # @data(("New Delhi","New York","31/10/2023","1 Stop"),("New York","New Dehli","1/13/2023","2 Stop"))
    # @data(*Utils.read_data_from_excel("D:\\Python\\POM_Hybrid\\testdata\\data.xlsx","Sheet1"))
    @data(*Utils.read_data_from_csv("D:\\Python\\POM_Hybrid\\testdata\\data.csv"))
    @unpack
    # @file_data("../testdata/testdata.yaml")
    def test_flight_1Stop(self, goingfrom, goingto, date, stops):
        serach_flight_result=self.lp.serachFlights(goingfrom, goingto, date)
        self.lp.page_scroll()
        serach_flight_result.filter_flights_by_stops(stops)
        all_stops=serach_flight_result.getSerachFlightResults()
        print(len(all_stops))
        self.ut.asserListItemText(all_stops,"1 Stop")

    # def test_flight_2Stop(self):
    #     serach_flight_result = self.lp.serachFlights("New Delhi", "New York", "31/10/2023")
    #     self.lp.page_scroll()
    #     serach_flight_result.filter_flights_by_stops("2 Stop")
    #     all_stops = serach_flight_result.getSerachFlightResults()
    #     print(len(all_stops))
    #     self.ut.asserListItemText(all_stops, "2 Stop")







