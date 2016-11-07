# -*- coding: utf-8 -*-

from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    originHeader = {"origin" : "loadtesting"}

    @task(1)
    def notFound(self):
        with self.client.get("/does_not_exist/", headers=self.originHeader, catch_response=True) as response:
          if response.status_code == 404:
            response.success()

    @task(10)
    def validForm(self):
        request = {"language":"en","user[name]":"Load Tester","english[form_full_name]":"Full name","multilingual[form_full_name]":"Full name","user[email]":"loadtester@loadtester.hey","english[form_email]":"Email","multilingual[form_email]":"Email","user[phone]":"test","english[form_phone]":"Phone (optional)","multilingual[form_phone]":"Phone (optional)","user[city]":"London","english[form_city]":"City","multilingual[form_city]":"City","organisation[annual_turnover]":"2-turnover:Between £100,000 and £1 million:Between £100,000 and £1 million","english[form_annual_turnover]":"Annual turnover","multilingual[form_annual_turnover]":"Annual turnover","organisation[number_of_employees]":"3-staff:Between 50 and 250:Between 50 and 250","english[form_staff_number]":"Number of staff","multilingual[form_staff_number]":"Number of staff","enquiry[location_is_specific]":"true","english[form_location]":"Do you have any location in mind?","multilingual[form_location]":"Do you have any location in mind?","enquiry[primary_location]:6-potential-location:Cardiff and Wales":"Cardiff and Wales","english[form_which_part]":"Which part of the country are you considering?","multilingual[form_which_part]":"Which part of the country are you considering?","enquiry[start_date]":["7", "2020"],"english[form_when]":"When do you hope to be running your uk business?","multilingual[form_when]":"When do you hope to be running your uk business?","organisation[name]":"Load Testers Inc","english[form_registered_company]":"Registered company name","multilingual[form_registered_company]":"Registered company name","organisation[website]":"loadtesters.inc","english[form_website]":"Company website","multilingual[form_website]":"Company website","organisation[headquarters_country]":"United Kingdom","organisation[headquarters_country]":"United Kingdom","english[form_headquarters]":"Headquarters country","multilingual[form_headquarters]":"Headquarters country","organisation[industry]":"11-industry:Medical technology:Medical technology","english[form_primary_industry]":"Primary operating industry","multilingual[form_primary_industry]":"Primary operating industry","user[other]":"","english[form_other]":"Other","multilingual[form_other]":"Other","js":"true"}
        with self.client.post("/form", data=request, headers=self.originHeader, catch_response=True,  name='validFormRequest') as response:
          if response.status_code == 422:
            response.success()

    @task(3)
    def invalidForm(self):
        nonsense = {'some' : 'keys', 'and' : 'values'}
        with self.client.post("/form/", data=nonsense, catch_response=True, headers=self.originHeader, name='invalidFormRequest') as response:
          if response.status_code == 500:
            response.success()

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    # min_wait = 10000
    # max_wait = 11000
