from selenium.webdriver.common.by import By
import time
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd

def login(user):
    dateselector = random.choice([13, 14, 21, 22])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://tecmed.vida24.com/")
    driver.maximize_window()
    driver.find_element(By.XPATH, '//input[@id="username"]').send_keys("merimna.patras")
    driver.find_element(By.XPATH, '//input[@id="password"]').send_keys("!XZAj_T84TL4")
    driver.find_element(By.XPATH, '//button[@id="submit"]').click()
    driver.find_element(By.XPATH, '//li[@id="sidebar_patients"]').click()
    time.sleep(3)
    driver.find_element("xpath", '//input[@class="form-control input-sm"]').send_keys(str(user))
    time.sleep(3)
    driver.find_element("xpath", '//i[@class="fa fa-fw fa-eye"]').click()
    time.sleep(3)
    driver.find_element("xpath", '//li[@class="treeview "]/a').click()
    time.sleep(3)
    ###########################################################################################################################
    #                                               AROPE - START                                                             #
    ###########################################################################################################################
    driver.find_element("xpath", '//a[text()=" AROPE"]').click()
    time.sleep(3)
    AROPE_MESSAGE = driver.find_element("xpath","//div[@class='nav-tabs-custom']")
    if AROPE_MESSAGE.text == 'Δεν υπάρχουν δεδομένα':
        driver.find_element("xpath", "//div[@class='box-tools pull-right']").click()
        time.sleep(3)
        driver.execute_script("$('#date').attr('value','2022-12-"+str(dateselector)+"')")
        time.sleep(3)
        driver.find_element("xpath", "//select[@name='question[where_she_lives]']/option[text()='Ελλάδα']").click()
        time.sleep(3)
        number_of_adults =random.choice([1, 2, 3, 4])
        driver.find_element("xpath", "//input[@name='question[number_of_adults]']").send_keys(number_of_adults)
        time.sleep(3)
        number_of_under_14_years_old=0
        if number_of_adults < 2:
            number_of_under_14_years_old =random.choice([0, 1, 2])
        driver.find_element("xpath", "//input[@name='question[number_of_under_14_years_old]']").send_keys(number_of_under_14_years_old)
        time.sleep(3)
        if number_of_adults <=2:
            relative_1 = random.randint(800, 1200) *14
            relative_2 =random.randint(500, 850) *14
            driver.find_element("xpath", "//input[@name='question[relative_1]']").send_keys(relative_1)
            driver.find_element("xpath", "//input[@name='question[relative_2]']").send_keys(relative_2)
        elif number_of_adults >2:
            relative_1 = random.randint(800, 1200) * 14
            relative_2 = random.randint(500, 850) * 14
            relative_3 = random.randint(400, 650) * random.randint(0, 12)
            driver.find_element("xpath", "//input[@name='question[relative_1]']").send_keys(relative_1)
            driver.find_element("xpath", "//input[@name='question[relative_2]']").send_keys(relative_2)
            driver.find_element("xpath", "//input[@name='question[relative_3]']").send_keys(relative_3)


        time.sleep(3)
        driver.find_element("xpath", "//input[@name='question[pay_their_rent]' and @value="+str(random.choice([0,1]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[keep_their_home]' and @value="+str(random.choice([0,1]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[face_unexpected_expenses]' and @value="+str(random.choice([0,1]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[go_on_holiday]' and @value="+str(random.choice([0,1]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[eat_meat]' and @value="+str(random.choice([0,1]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[television_set]' and @value="+str(random.choice([0,1]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[washing_machine]' and @value="+str(random.choice([0,1]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[washing_machine]' and @value="+str(random.choice([0,1]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[car]' and @value="+str(random.choice([0,1]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[telephone]' and @value="+str(random.choice([0,1]))+"]/following-sibling::label").click()
        time.sleep(2)
        driver.find_element("xpath", "//button[@class='btn btn-primary pull-right']").click()
        time.sleep(3)

    ###########################################################################################################################
    #                                      AROPE - END,   INICIARE  - START                                                   #
    ###########################################################################################################################
    time.sleep(5)
    driver.find_element("xpath", '//a[text()=" INICIARE"]').click()
    time.sleep(3)
    INICIARE_MESSAGE = driver.find_element("xpath","//div[@class='nav-tabs-custom']")
    if INICIARE_MESSAGE.text == 'Δεν υπάρχουν δεδομένα':
        driver.find_element("xpath", "//div[@class='box-tools pull-right']").click()
        time.sleep(3)
        driver.execute_script("$('#date').attr('value','2022-12-" +str(dateselector)+ "')")
        driver.find_element("xpath", "//input[@name='question[cyanosis]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[dyspnea_with_mild_exertion]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[dyspnea_at_rest]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[respiratory_rate]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[respiratory_rhythm]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[adventitious_breath_sounds]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[intake_and_output_balance]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[oral_food_intake]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[food_intake]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[altered_nutritional]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[chocking]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[chewing_ability]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[desire_to_eat]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[elimination_pattern]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[urinary_incontinence]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[responds_to_full_bladder_in_timely_manner]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[maintains_control]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[bowelelimination]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[walks_with_effective_gait]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[positions_self]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[moves_with_ease]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[hygiene_type]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[shampoos_hair]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[dressings]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[rest_quality]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[sleep_quality]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[sleep_pattern]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[skin_integrity]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[sensation]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[tissue_perfusion]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[attentiveness]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[communication_clear_for_age]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[accurate_interpretation_of_messages_received]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[verbalizes_a_coherent_message]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[perceived_threat_to_health]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[acknowledges_risk_factors]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[perceived_impact_on_future_lifestyle]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[requested_involvement_in_health_decisions]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[concern_regarding_illness_or_injury]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[sets_realistic_goals]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[maintains_self_esteem]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[adapts_to_life_change]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[behaviors_to_promote_health]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[asks_health_related_questions]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[treatment_regimen]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[provides_rationale_for_adopting_a_health_behavior]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[verbalizes_a_coherent_message]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[specific_disease_process]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        time.sleep(2)
        driver.find_element("xpath", "//button[@class='btn btn-primary pull-right']").click()
        time.sleep(3)
    ###########################################################################################################################
    #                                  INICIARE - END,  1.KATASTASI UGEIAS   - START                                          #
    ###########################################################################################################################
    time.sleep(3)
    driver.find_element("xpath", '//a[text()=" 1.ΚΑΤΑΣΤΑΣΗ ΥΓΕΙΑΣ"]').click()
    KATASTASTI_UGEIAS_MESSAGE = driver.find_element("xpath", "//div[@class='nav-tabs-custom']")
    if KATASTASTI_UGEIAS_MESSAGE.text == 'Δεν υπάρχουν δεδομένα':
        driver.find_element("xpath", "//div[@class='box-tools pull-right']").click()
        time.sleep(3)
        driver.execute_script("$('#date').attr('value','2022-12-"+str(dateselector)+"')")
        driver.find_element("xpath", "//input[@name='question[cerebrovascular]' and @value='1']/following-sibling::label").click()

        driver.find_element("xpath", "//input[@name='question[diabetes]' and @value="+str(random.choice([0,1]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[chronic_pulmonary]' and @value="+str(random.choice([0,1]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[heart_failure]' and @value="+str(random.choice([0,1]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[tumor_without_metastase]' and @value="+str(random.choice([0,1]))+"]/following-sibling::label").click()

        driver.find_element("xpath", "//input[@name='question[dementia]' and @value='1']/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[peripheral]' and @value='1']/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[dialysis]' and @value='1']/following-sibling::label").click()

        driver.find_element("xpath", "//input[@name='question[general]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[health_12_months_ago]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[mobility]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[self_care]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[usual_activities]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[pain]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()

        driver.find_element("xpath", "//input[@name='question[good_bad_health]']").send_keys(random.randint(50, 100))

        driver.find_element("xpath", "//input[@name='question[take_your_medication]' and @value="+str(random.choice([0,1]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[discontinued_taking]' and @value="+str(random.choice([0,1]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[forgotten_medication]' and @value="+str(random.choice([0,1]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[forgotten_medication_during_weekend]' and @value="+str(random.choice([0,1]))+"]/following-sibling::label").click()

        driver.find_element("xpath", "//input[@name='question[fail_prescribed_dose]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()

        driver.find_element("xpath", "//input[@name='question[days]']").send_keys(str(random.randint(0, 5)))

        #driver.find_element("xpath", "//input[@name='question[height]']").send_keys(str(random.randint(1.65, 1.90)))
        #driver.find_element("xpath", "//input[@name='question[weight]']").send_keys(str(random.randint(70, 115)))
        #smoker =random.choice([0,1,2])
        #driver.find_element("xpath", "//input[@name='question[smoker]']").send_keys(str(smoker))
        #if smoker == 1:
            #driver.find_element("xpath", "//input[@name='question[type]']").send_keys(str(random.choice([0,1])))
            #periodicity =random.choice(['per_day','per_week2'])
            # driver.find_element("xpath", "//input[@name='question[+str(periodicity)+]']").send_keys(str(random.randint(1,20)))
        driver.find_element("xpath", "//input[@name='question[medicines_without_doctor]' and @value="+str(random.choice([0,1]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[medicines_more_dose]' and @value="+str(random.choice([0,1]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[how_often_do _you_drink]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[how_often_do _you_drink_day]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[how_often_do _you_drink_day_second]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[any_drugs]' and @value='1']/following-sibling::label").click()

        driver.find_element("xpath", "//input[@name='question[number_of_times]']").send_keys('-')
        driver.find_element("xpath", "//input[@name='question[geriatric]']").send_keys('-')
        driver.find_element("xpath", "//input[@name='question[psychiatric]']").send_keys('-')
        driver.find_element("xpath", "//input[@name='question[internal_medicine]']").send_keys('-')
        driver.find_element("xpath", "//input[@name='question[surgery]']").send_keys('-')
        driver.find_element("xpath", "//input[@name='question[neurology]']").send_keys('-')
        driver.find_element("xpath", "//input[@name='question[general_ward]']").send_keys('-')
        driver.find_element("xpath", "//input[@name='question[other]']").send_keys('-')

        driver.find_element("xpath", "//input[@name='question[number_of_times_2]']").send_keys('-')
        driver.find_element("xpath", "//input[@name='question[professional_6]']").send_keys('-')
        driver.find_element("xpath", "//input[@name='question[general_practitioner]']").send_keys('-')
        driver.find_element("xpath", "//input[@name='question[geriatrician]']").send_keys('-')
        driver.find_element("xpath", "//input[@name='question[neurologist]']").send_keys('-')
        driver.find_element("xpath", "//input[@name='question[psychiatric_2]']").send_keys('-')
        driver.find_element("xpath", "//input[@name='question[physiotherapist]']").send_keys('-')
        driver.find_element("xpath", "//input[@name='question[occupational_therapist]']").send_keys('-')
        driver.find_element("xpath", "//input[@name='question[social_worker]']").send_keys('-')
        driver.find_element("xpath", "//input[@name='question[psychologist]']").send_keys('-')
        driver.find_element("xpath", "//input[@name='question[other_eg]']").send_keys('-')

        driver.find_element("xpath", "//input[@name='question[not_receive_any_services]']").send_keys('-')
        driver.find_element("xpath", "//input[@name='question[distict_nurse]']").send_keys('-')
        driver.find_element("xpath", "//input[@name='question[home_help]']").send_keys('-')
        driver.find_element("xpath", "//input[@name='question[day_care]']").send_keys('-')
        driver.find_element("xpath", "//input[@name='question[transportation]']").send_keys('-')
        driver.find_element("xpath", "//input[@name='question[other_eg_2]']").send_keys('-')

        driver.find_element("xpath", "//input[@name='question[i_have_not_participate]']").send_keys('-')
        driver.find_element("xpath", "//input[@name='question[individual_or_family]']").send_keys('-')
        driver.find_element("xpath", "//input[@name='question[support_groups]']").send_keys('-')
        driver.find_element("xpath", "//input[@name='question[online_support_group]']").send_keys('-')
        driver.find_element("xpath", "//input[@name='question[social_club]']").send_keys('-')
        driver.find_element("xpath", "//input[@name='question[faith_based_group]']").send_keys('-')
        driver.find_element("xpath", "//input[@name='question[other_eg_3]']").send_keys('-')
        driver.find_element("xpath", "//input[@name='question[name_of_medicine]']").send_keys('-')

        driver.find_element("xpath", "//input[@name='question[strenght]']").send_keys('-')
        driver.find_element("xpath", "//input[@name='question[number_of_times_per_day]']").send_keys('-')
        driver.find_element("xpath", "//input[@name='question[number_of_days]']").send_keys('-')
        driver.find_element("xpath", "//input[@name='question[i_am_not_talking]']").send_keys('-')

        driver.find_element("xpath", "//input[@name='question[are_you_currently]' and @value='1']/following-sibling::label").click()
        time.sleep(3)
        driver.find_element("xpath", "//button[@class='btn btn-primary pull-right']").click()
    ###########################################################################################################################
    #                          1.KATASTASI UGEIAS - END |  2.ΦΥΣΙΚΟ-ΛΕΙΤΟΥΡΓΙΚΗ ΙΚΑΝΟΤΗΤΑ - START                             #
    ###########################################################################################################################
    driver.find_element("xpath", '//a[text()=" 2.ΦΥΣΙΚΟ-ΛΕΙΤΟΥΡΓΙΚΗ ΙΚΑΝΟΤΗΤΑ"]').click()
    time.sleep(3)
    fysiko_leitourgiki_ikanotita_MESSAGE = driver.find_element("xpath", "//div[@class='nav-tabs-custom']")
    if fysiko_leitourgiki_ikanotita_MESSAGE.text == 'Δεν υπάρχουν δεδομένα':
        driver.find_element("xpath", "//div[@class='box-tools pull-right']").click()
        time.sleep(3)
        driver.execute_script("$('#date').attr('value','2022-12-" + str(dateselector) + "')")
        shortness_of_breath = str(random.choice([0,1]))
        driver.find_element("xpath", "//input[@name='question[shortness_of_breath]' and @value="+shortness_of_breath+"]/following-sibling::label").click()
        if shortness_of_breath ==0:
            driver.find_element("xpath", "//input[@name='question[cyanosis]' and @value="+str(random.choice([0,1,2]))+"]/following-sibling::label").click()
            driver.find_element("xpath", "//input[@name='question[dyspnea_with_exertion]' and @value="+str(random.choice([0,1,2]))+"]/following-sibling::label").click()
            driver.find_element("xpath", "//input[@name='question[dyspnea_rest]' and @value="+str(random.choice([0,1,2]))+"]/following-sibling::label").click()
            driver.find_element("xpath", "//input[@name='question[respiratory_rate]' and @value="+str(random.choice([0,1,2]))+"]/following-sibling::label").click()
            driver.find_element("xpath", "//input[@name='question[adventitious_breath]' and @value="+str(random.choice([0,1,2]))+"]/following-sibling::label").click()
        elif shortness_of_breath ==1:
            driver.find_element("xpath", "//input[@name='question[cyanosis]' and @value="+str(random.choice([2,3,4]))+"]/following-sibling::label").click()
            driver.find_element("xpath", "//input[@name='question[dyspnea_with_exertion]' and @value="+str(random.choice([2,3,4]))+"]/following-sibling::label").click()
            driver.find_element("xpath", "//input[@name='question[dyspnea_rest]' and @value="+str(random.choice([2,3,4]))+"]/following-sibling::label").click()
            driver.find_element("xpath", "//input[@name='question[respiratory_rate]' and @value="+str(random.choice([2,3,4]))+"]/following-sibling::label").click()
            driver.find_element("xpath", "//input[@name='question[adventitious_breath]' and @value="+str(random.choice([2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[position]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[walks]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[moves]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[previous_fall]' and @value="+str(random.choice([0,1]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[urinary_incontinence]' and @value="+str(random.choice([0,1]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[visual_problem]' and @value="+str(random.choice([0,1]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[functional_limitation]' and @value="+str(random.choice([0,1]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[wearing_glasses]' and @value="+str(random.choice([0,1,2]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[hearing_aid]' and @value="+str(random.choice([0,1,2]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[rest_quality]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[sleep_quality]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[sleep_pattern]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//button[@class='btn btn-primary pull-right']").click()
    ###########################################################################################################################
    #                          2.ΦΥΣΙΚΟ-ΛΕΙΤΟΥΡΓΙΚΗ ΙΚΑΝΟΤΗΤΑ - END  | 3.ΓΝΩΣΤΙΚΗ ΙΚΑΝΟΤΗΤΑ    - START                        #
    ###########################################################################################################################
    driver.find_element("xpath", '//a[text()=" 3.ΓΝΩΣΤΙΚΗ ΙΚΑΝΟΤΗΤΑ"]').click()
    time.sleep(3)
    fysiko_leitourgiki_ikanotita_MESSAGE = driver.find_element("xpath", "//div[@class='nav-tabs-custom']")
    if fysiko_leitourgiki_ikanotita_MESSAGE.text == 'Δεν υπάρχουν δεδομένα':
        driver.find_element("xpath", "//div[@class='box-tools pull-right']").click()
        time.sleep(3)
        driver.execute_script("$('#date').attr('value','2022-12-" + str(dateselector) + "')")
        driver.find_element("xpath", "//input[@name='question[attentiveness]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[communication_clear]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[accurate_interpretation]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[verbalizes]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//button[@class='btn btn-primary pull-right']").click()
    ###########################################################################################################################
    #                              3.ΓΝΩΣΤΙΚΗ ΙΚΑΝΟΤΗΤΑ - END  |   4.ΒΑΣΙΚΕΣ ΑΝΑΓΚΕΣ   - START                                #
    ###########################################################################################################################
    driver.find_element("xpath", '//a[text()=" 4.ΒΑΣΙΚΕΣ ΑΝΑΓΚΕΣ"]').click()
    time.sleep(3)
    fysiko_leitourgiki_ikanotita_MESSAGE = driver.find_element("xpath", "//div[@class='nav-tabs-custom']")
    if fysiko_leitourgiki_ikanotita_MESSAGE.text == 'Δεν υπάρχουν δεδομένα':
        driver.find_element("xpath", "//div[@class='box-tools pull-right']").click()
        time.sleep(3)
        driver.execute_script("$('#date').attr('value','2022-12-" + str(dateselector) + "')")
        driver.find_element("xpath", "//input[@name='question[altered]' and @value=" + str(
            random.choice([0, 1])) + "]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[swallowing_status]' and @value=" + str(
            random.choice([0, 1])) + "]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[nutritional_status]' and @value=" + str(
            random.choice([0, 1])) + "]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[appetite]' and @value=" + str(
            random.choice([0, 1])) + "]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[output_balance]' and @value=" + str(
            random.choice([0, 1])) + "]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[oral_food]' and @value=" + str(
            random.choice([0, 1])) + "]/following-sibling::label").click()
        driver.find_element("xpath","//input[@name='question[teething_problem]' and @value='1']/following-sibling::label").click()
        driver.find_element("xpath", "//button[@class='btn btn-primary pull-right']").click()
    ###########################################################################################################################
    #             4.ΒΑΣΙΚΕΣ ΑΝΑΓΚΕΣ - END  |   5.ΣΥΝΑΙΣΘΗΜΑΤΙΚΗ ΔΙΑΧΕΙΡΙΣΗ ΚΑΙ ΚΟΙΝΩΝΙΚΕΣ ΣΧΕΣΕΙΣ   - START                   #
    ###########################################################################################################################
    driver.find_element("xpath", '//a[text()=" 5.ΣΥΝΑΙΣΘΗΜΑΤΙΚΗ ΔΙΑΧΕΙΡΙΣΗ ΚΑΙ ΚΟΙΝΩΝΙΚΕΣ ΣΧΕΣΕΙΣ"]').click()
    time.sleep(3)
    fysiko_leitourgiki_ikanotita_MESSAGE = driver.find_element("xpath", "//div[@class='nav-tabs-custom']")
    if fysiko_leitourgiki_ikanotita_MESSAGE.text == 'Δεν υπάρχουν δεδομένα':
        driver.find_element("xpath", "//div[@class='box-tools pull-right']").click()
        time.sleep(3)
        driver.execute_script("$('#date').attr('value','2022-12-" + str(dateselector) + "')")
        driver.find_element("xpath", "//input[@name='question[visits_from_friends]' and @value=" + str(
            random.choice([0, 1, 2, 3, 4])) + "]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[help_around]' and @value=" + str(
            random.choice([0, 1, 2, 3, 4])) + "]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[praise_for_job]' and @value=" + str(
            random.choice([0, 1, 2, 3, 4])) + "]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[people_who_care]' and @value=" + str(
            random.choice([0, 1, 2, 3, 4])) + "]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[get_love]' and @value=" + str(
            random.choice([0, 1, 2, 3, 4])) + "]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[problems_at_work]' and @value=" + str(
            random.choice([0, 1, 2, 3, 4])) + "]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[personal_problems]' and @value=" + str(
            random.choice([0, 1, 2, 3, 4])) + "]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[money_matters]' and @value=" + str(
            random.choice([0, 1, 2, 3, 4])) + "]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[invitations_with_other_people]' and @value=" + str(
            random.choice([0, 1, 2, 3, 4])) + "]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[usefull_advice]' and @value=" + str(
            random.choice([0, 1, 2, 3, 4])) + "]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[sick_in_bed]' and @value=" + str(
            random.choice([0, 1, 2, 3, 4])) + "]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[believer]' and @value=" + str(
            random.choice([0, 1])) + "]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[practice_any_ritual]' and @value=" + str(
            random.choice([0, 1])) + "]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[cultural_practices]' and @value=" + str(
            random.choice([0, 1])) + "]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[objectives_or_goals]' and @value=" + str(
            random.choice([0, 1])) + "]/following-sibling::label").click()
        driver.find_element("xpath", "//button[@class='btn btn-primary pull-right']").click()
###########################################################################################################################
# 5.ΣΥΝΑΙΣΘΗΜΑΤΙΚΗ ΔΙΑΧΕΙΡΙΣΗ ΚΑΙ ΚΟΙΝΩΝΙΚΕΣ ΣΧΕΣΕΙΣ - END  | 6.ΙΚΑΝΟΤΗΤΑ ΠΡΟΩΘΗΣΗΣ ΜΙΑΣ ΥΓΙΕΙΝΗΣ ΖΩΗΣ/ΘΑΝΑΤΟΥ   - START  #
###########################################################################################################################
    driver.find_element("xpath", '//a[text()=" 6.ΙΚΑΝΟΤΗΤΑ ΠΡΟΩΘΗΣΗΣ ΜΙΑΣ ΥΓΙΕΙΝΗΣ ΖΩΗΣ/ΘΑΝΑΤΟΥ"]').click()
    time.sleep(3)
    fysiko_leitourgiki_ikanotita_MESSAGE = driver.find_element("xpath", "//div[@class='nav-tabs-custom']")
    if fysiko_leitourgiki_ikanotita_MESSAGE.text == 'Δεν υπάρχουν δεδομένα':
        driver.find_element("xpath", "//div[@class='box-tools pull-right']").click()
        time.sleep(3)
        driver.execute_script("$('#date').attr('value','2022-12-" + str(dateselector) + "')")
        driver.find_element("xpath", "//input[@name='question[find_understand_use]' and @value="+str(random.choice([0,1,2,3]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[find_treatment]' and @value="+str(random.choice([0,1,2,3]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[professional_health]' and @value="+str(random.choice([0,1,2,3]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[understand_pharmacists]' and @value="+str(random.choice([0,1,2,3]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[judge_getting_second_option]' and @value="+str(random.choice([0,1,2,3]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[decision_about_illness]' and @value="+str(random.choice([0,1,2,3]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[follow_instructions_pharmacists]' and @value="+str(random.choice([0,1,2,3]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[manage_mental_health]' and @value="+str(random.choice([0,1,2,3]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[understand_health_warning]' and @value="+str(random.choice([0,1,2,3]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[understand_health_screenings]' and @value="+str(random.choice([0,1,2,3]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[judge_informantion_health_risk]' and @value="+str(random.choice([0,1,2,3]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[protect_yourserlf]' and @value="+str(random.choice([0,1,2,3]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[understand_advice_on_health]' and @value="+str(random.choice([0,1,2,3]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[undarstand_information_in_media]' and @value="+str(random.choice([0,1,2,3]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[everyday_behaviour]' and @value="+str(random.choice([0,1,2,3]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[activities_that_youre_good]' and @value="+str(random.choice([0,1,2,3]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[worried_process]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[physical_dying_precess]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[pain_dying_process]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[mental_generation]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[loss_of_faculties]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[courage]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[lack_of_control]' and @value="+str(random.choice([0,1,2,3,4]))+"]/following-sibling::label").click()
        driver.find_element("xpath", "//button[@class='btn btn-primary pull-right']").click()
###########################################################################################################################
#           6.ΙΚΑΝΟΤΗΤΑ ΠΡΟΩΘΗΣΗΣ ΜΙΑΣ ΥΓΙΕΙΝΗΣ ΖΩΗΣ/ΘΑΝΑΤΟΥ - END  | 8.ΚΟΙΝΩΝΙΚΟ-ΟΙΚΟΝΟΜΙΚΗ ΚΑΤΑΣΤΑΣΗ- START             #
###########################################################################################################################
    driver.find_element("xpath", '//a[text()=" 8.ΚΟΙΝΩΝΙΚΟ-ΟΙΚΟΝΟΜΙΚΗ ΚΑΤΑΣΤΑΣΗ"]').click()
    time.sleep(3)
    fysiko_leitourgiki_ikanotita_MESSAGE = driver.find_element("xpath", "//div[@class='nav-tabs-custom']")
    if fysiko_leitourgiki_ikanotita_MESSAGE.text == 'Δεν υπάρχουν δεδομένα':
        driver.find_element("xpath", "//div[@class='box-tools pull-right']").click()
        time.sleep(2)
        driver.execute_script("$('#date').attr('value','2022-12-" + str(dateselector) + "')")
        driver.find_element("xpath", "//input[@name='question[home_have_characteristics]' and @value=" + str(
            random.choice([0, 1])) + "]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[use_internet]' and @value=" + str(
            random.choice([0, 1, 2, 3, 4])) + "]/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[culinary]']").send_keys(random.randint(3, 17))
        driver.find_element("xpath", "//input[@name='question[home_maintenance]']").send_keys(random.randint(3, 14))
        driver.find_element("xpath", "//input[@name='question[personal_care]']").send_keys(random.randint(4, 11))
        driver.find_element("xpath", "//input[@name='question[caring_for_others]']").send_keys(random.randint(5, 14))
        driver.find_element("xpath", "//input[@name='question[physical_activity]']").send_keys(random.randint(5, 14))
        driver.find_element("xpath", "//input[@name='question[religious]']").send_keys(random.randint(5, 14))
        driver.find_element("xpath", "//input[@name='question[fun]']").send_keys(random.randint(5, 14))
        driver.find_element("xpath", "//button[@class='btn btn-primary pull-right']").click()
###########################################################################################################################
#              8.ΚΟΙΝΩΝΙΚΟ-ΟΙΚΟΝΟΜΙΚΗ ΚΑΤΑΣΤΑΣΗ - END  | 7.ΟΙΚΟΓΕΝΕΙΑ, ΣΥΝΤΡΟΦΟΙ ΚΑΙ ΦΡΟΝΤΙΣΤΕΣ - START                   #
###########################################################################################################################
    driver.find_element("xpath", '//a[text()=" 7.ΟΙΚΟΓΕΝΕΙΑ, ΣΥΝΤΡΟΦΟΙ ΚΑΙ ΦΡΟΝΤΙΣΤΕΣ"]').click()
    time.sleep(3)
    fysiko_leitourgiki_ikanotita_MESSAGE = driver.find_element("xpath", "//div[@class='nav-tabs-custom']")
    if fysiko_leitourgiki_ikanotita_MESSAGE.text == 'Δεν υπάρχουν δεδομένα':
        driver.find_element("xpath", "//div[@class='box-tools pull-right']").click()
        time.sleep(2)
        driver.execute_script("$('#date').attr('value','2022-12-" + str(dateselector) + "')")
        driver.find_element("xpath", "//input[@name='question[live_alone]' and @value='1']/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[usual_caregivers]' and @value='0']/following-sibling::label").click()
        driver.find_element("xpath", "//button[@class='btn btn-primary pull-right']").click()

if __name__ == "__main__":
    df = pd.read_excel('users.xlsx',  sheet_name='users')  # can also index sheet by name or fetch all sheets
    userlist = df['username'].tolist()
    for x in userlist:
        start = time.time()
        print(x +"  Start")
        login(x)
        end = time.time()
        print(x +"  Done , Time took to run"+str(end - start)+"seconds")