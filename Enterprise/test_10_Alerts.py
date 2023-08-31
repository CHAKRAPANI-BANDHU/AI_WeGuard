# from datetime import datetime
# import pytest
# import requests
# import globalvariables as Globals
# import test_GETutils as Utils
# import WeGuardlogger as WeGuard
# import Executor as Execute
# import WeBoxpayloadinfo as Variable
#
#
# def url_formatter(accountId, start, end, page, size):
#     url = "notification/rest/alert/account/{accountId}?start={start}&end={end}&page={page}&size={size}".format(
#         accountId=accountId, start=start, end=end, page=page, size=size)
#     return url
#
#
# def url_formatter2(accountId, start, end, page, size, type, level):
#     url2 = "notification/rest/alert/account/{accountId}?start={start}&end={end}&page={page}&size={size}&type={type}&level={level}".format(
#         accountId=accountId, start=start, end=end, page=page, size=size, type=type, level=level)
#     return url2
#
#
# def url_formatter3(accountId, start, end, page, size, type):
#     url3 = "notification/rest/alert/account/{accountId}?start={start}&end={end}&page={page}&size={size}&type={type}".format(
#         accountId=accountId, start=start, end=end, page=page, size=size, type=type)
#     return url3
#
#
# def url_formatter4(accountId, start, end, page, size, level, ack):
#     url4 = "notification/rest/alert/account/{accountId}?start={start}&end={end}&page={page}&size={size}&level={level}&ack={ack}".format(
#         accountId=accountId, start=start, end=end, page=page, size=size, level=level, ack=ack)
#     return url4
#
#
# # GET method to get crtical alerts that are not acknowledged by use after clicking on Alert notification icon
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_Alerts_CRITICAL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10448)
# def test_tc_000001_UnacknowledgedCriticalAlerts(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         UnacknowledgedCriticalAlerts = url_formatter4(Globals.accountId, Variable.isomonth, Variable.isoend,
#                                                       Globals.page_1, Globals.page_100, 'CRITICAL', 'unread')
#         apiUrl = Globals.BaseURL + UnacknowledgedCriticalAlerts
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Displaying Unacknowledged Critical Alerts all alert types and levels ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not displaying Unacknowledged Critical Alerts all alert types and levels ---------------------------\n")
#         assert False
#
#
# # GET method to GET all level and types alert notifications of Todays
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_TodaysAlerts == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10403)
# def test_tc_000002_TodaysAlertsTypesLevelAll(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         TodaysAlertsTypesLevelAll = url_formatter(Globals.accountId, Variable.isostart, Variable.isoend, Globals.page_1,
#                                                   Globals.page_100)
#         apiUrl = Globals.BaseURL + TodaysAlertsTypesLevelAll
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Displaying Todays all alert types and levels ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not displaying all alert types and levels ---------------------------\n")
#         assert False
#
#
# # GET method to GET all level and types alert notifications of Yesterday's
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_Yesterday == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10444)
# def test_tc_000003_YesterdaysAlertsTypesLevelAll(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         AlertsTypesLevelAllYesterday = url_formatter(Globals.accountId, Variable.isocustom, Variable.isoyesterday,
#                                                      Globals.page_1, Globals.page_100)
#         apiUrl = Globals.BaseURL + AlertsTypesLevelAllYesterday
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Displaying Yesterday's all alert types and levels ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not displaying all alert types and levels ---------------------------\n")
#         assert False
#
#
# # GET method to GET all level and types alert notifications of Custom Date Range
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_CustomDateRange == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10445)
# def test_tc_000004_CustomDateRangeAlertsTypesLevelAll(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         AlertsTypesLevelAllCustomDateRange = url_formatter(Globals.accountId, Variable.iso1weekcustom, Variable.isoend,
#                                                            Globals.page_1, Globals.page_100)
#         apiUrl = Globals.BaseURL + AlertsTypesLevelAllCustomDateRange
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Displaying Custom Date Range all alert types and levels ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not displaying all alert types and levels ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=Battery and level=Low
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_Battery_LOW == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10404)
# def test_tc_000005_BatteryLow(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         BatteryLowAlert = url_formatter2(Globals.accountId, Variable.isostart, Variable.isoend, Globals.page_1,
#                                          Globals.page_100, 'BATTERY', 'LOW')
#         apiUrl = Globals.BaseURL + BatteryLowAlert
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=Battery and level=Low ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=Battery and level=Low ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=Battery and level=Warning
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_Battery_WARNING == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10405)
# def test_tc_000006_BATTERY_WARNING(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         BatteryWarningAlert = url_formatter2(Globals.accountId, Variable.isostart, Variable.isoend, Globals.page_1,
#                                              Globals.page_100, 'BATTERY', 'WARNING')
#         apiUrl = Globals.BaseURL + BatteryWarningAlert
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print(res.content)
#         WeGuard.logger.warning(
#             "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + " \n Response headers: " + str(
#                 res.headers) + "\n Request Response: " + str(res.content))
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=Battery and level=Warning ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=Battery and level=Warning ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=Battery and level=Critical
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_Battery_CRITICAL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10406)
# def test_tc_000007_BATTERY_CRITICAL(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         BatteryCriticalAlert = url_formatter2(Globals.accountId, Variable.isostart, Variable.isoend, Globals.page_1,
#                                               Globals.page_100, 'BATTERY', 'CRITICAL')
#         apiUrl = Globals.BaseURL + BatteryCriticalAlert
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=Battery and level=Critical ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=Battery and level=Critical ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=DATA_USAGE and level=Low
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_DATA_USAGE_LOW == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10407)
# def test_tc_000008_DATA_USAGE_LOW(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         DataUsageLowAlert = url_formatter2(Globals.accountId, Variable.isostart, Variable.isoend, Globals.page_1,
#                                            Globals.page_100, 'DATA_USAGE', 'LOW')
#         apiUrl = Globals.BaseURL + DataUsageLowAlert
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=Data Usage and level=Low ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=Data Usage and level=Low ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=DATA_USAGE and level=Warning
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_DATA_USAGE_WARNING == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10408)
# def test_tc_000009_DATA_USAGE_WARNING(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         DataUsageWarningAlert = url_formatter2(Globals.accountId, Variable.isostart, Variable.isoend, Globals.page_1,
#                                                Globals.page_100, 'DATA_USAGE', 'WARNING')
#         apiUrl = Globals.BaseURL + DataUsageWarningAlert
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=Battery and level=Warning ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=Battery and level=Warning ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=DATA_USAGE and level=Critical
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_DATA_USAGE_CRITICAL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10409)
# def test_tc_000010_DATA_USAGE_CRITICAL(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         DataUsageCriticalAlert = url_formatter2(Globals.accountId, Variable.isostart, Variable.isoend, Globals.page_1,
#                                                 Globals.page_100, 'DATA_USAGE', 'CRITICAL')
#         apiUrl = Globals.BaseURL + DataUsageCriticalAlert
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=DATA_USAGE and level=Critical ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=DATA_USAGE and level=Critical ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=KIOSK_LOCKED and level=ALL
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_KIOSK_LOCKED_Regular == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10410)
# def test_tc_000011_KIOSK_LOCKED_LOW(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         KioskLockedAlert = url_formatter2(Globals.accountId, Variable.isostart, Variable.isoend, Globals.page_1,
#                                           Globals.page_100, 'KIOSK_LOCKED', 'ALL')
#         apiUrl = Globals.BaseURL + KioskLockedAlert
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=KIOSK_LOCKED and level=ALL ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=KIOSK_LOCKED and level=ALL ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=KIOSK_UNLOCKED and level=Critical
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_KIOSK_UNLOCKED_CRITICAL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10411)
# def test_tc_000012_KIOSK_UNLOCKED_CRITICAL(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         KioskUnlockedCriticalAlert = url_formatter2(Globals.accountId, Variable.isostart, Variable.isoend,
#                                                     Globals.page_1, Globals.page_100, 'KIOSK_UNLOCKED', 'CRITICAL')
#         apiUrl = Globals.BaseURL + KioskUnlockedCriticalAlert
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=KIOSK_UNLOCKED and level=Critical ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=KIOSK_UNLOCKED and level=Critical ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=Admin_LOCKED and level=Critical
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_ADMIN_LOCKED_CRITICAL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10412)
# def test_tc_000013_ADMIN_LOCKED_CRITICAL(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         AdminLockedCriticalAlert = url_formatter2(Globals.accountId, Variable.isostart, Variable.isoend, Globals.page_1,
#                                                   Globals.page_100, 'ADMIN_LOCKED', 'CRITICAL')
#         apiUrl = Globals.BaseURL + AdminLockedCriticalAlert
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=ADMIN_LOCKED and level=Critical ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=ADMIN_LOCKED and level=Critical ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=DEVICE_REBOOTED and level=ALL
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_DEVICE_REBOOTED_CRITICAL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10413)
# def test_tc_000014_DEVICE_REBOOTED_LOW(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         DeviceRebootedAlert = url_formatter2(Globals.accountId, Variable.isostart, Variable.isoend, Globals.page_1,
#                                              Globals.page_100, 'DEVICE_REBOOTED', 'ALL')
#         apiUrl = Globals.BaseURL + DeviceRebootedAlert
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=DEVICE_REBOOTED and level=Low ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=DEVICE_REBOOTED and level=Low ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=DEVICE_WIPED and level=ALL
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_DEVICE_WIPED_CRITICAL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10414)
# def test_tc_000015_DEVICE_WIPED_LOW(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         DeviceWipedAlert = url_formatter2(Globals.accountId, Variable.isostart, Variable.isoend, Globals.page_1,
#                                           Globals.page_100, 'DEVICE_WIPED', 'ALL')
#         apiUrl = Globals.BaseURL + DeviceWipedAlert
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=DEVICE_WIPED and level=ALL ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=DEVICE_WIPED and level=ALL ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=DEVICE_DELETED and level=Critical
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_DEVICE_DELETED_CRITICAL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10415)
# def test_tc_000016_DEVICE_DELETED_LOW(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         DeviceDeletedCriticalAlert = url_formatter2(Globals.accountId, Variable.isostart, Variable.isoend,
#                                                     Globals.page_1, Globals.page_100, 'DEVICE_DELETED', 'CRITICAL')
#         apiUrl = Globals.BaseURL + DeviceDeletedCriticalAlert
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=DEVICE_DELETED and level=Critical ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=DEVICE_DELETED and level=Critical ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=ROOTED_ENROLL and level=Critical
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_ROOTED_ENROLL_CRITICAL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10416)
# def test_tc_000017_ROOTED_ENROLL_LOW(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         RootedDeviceEnrollCriticalAlert = url_formatter2(Globals.accountId, Variable.isostart, Variable.isoend,
#                                                          Globals.page_1, Globals.page_100, 'ROOTED_ENROLL', 'ALL')
#         apiUrl = Globals.BaseURL + RootedDeviceEnrollCriticalAlert
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=ROOTED_ENROLL and level=All ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=ROOTED_ENROLL and level=All ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=MEMORY_ALERT and level=Low
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_MEMORY_ALERT_LOW == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10417)
# def test_tc_000018_MEMORY_ALERT_LOW(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         MemoryLowAlert = url_formatter2(Globals.accountId, Variable.isostart, Variable.isoend, Globals.page_1,
#                                         Globals.page_100, 'MEMORY_ALERT', 'LOW')
#         apiUrl = Globals.BaseURL + MemoryLowAlert
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=MEMORY_ALERT and level=Low ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=MEMORY_ALERT and level=Low ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=MEMORY_ALERT and level=Warning
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_MEMORY_ALERT_WARNING == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10418)
# def test_tc_000019_MEMORY_ALERT_WARNING(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         MemoryWarningAlert = url_formatter2(Globals.accountId, Variable.isostart, Variable.isoend, Globals.page_1,
#                                             Globals.page_100, 'MEMORY_ALERT', 'WARNING')
#         apiUrl = Globals.BaseURL + MemoryWarningAlert
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=MEMORY_ALERT and level=Warning ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=MEMORY_ALERT and level=Warning ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=MEMORY_ALERT and level=Critical
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_MEMORY_ALERT_CRITICAL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10419)
# def test_tc_000020_MEMORY_ALERT_CRITICAL(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         MemoryCriticalAlert = url_formatter2(Globals.accountId, Variable.isostart, Variable.isoend, Globals.page_1,
#                                              Globals.page_100, 'MEMORY_ALERT', 'CRITICAL')
#         apiUrl = Globals.BaseURL + MemoryCriticalAlert
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=MEMORY_ALERT and level=Critical ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=MEMORY_ALERT and level=Critical ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=DISC_USAGE and level=Low
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_DISC_USAGE_LOW == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10420)
# def test_tc_000021_DISC_USAGE_LOW(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         DiscUsageLowAlert = url_formatter2(Globals.accountId, Variable.isostart, Variable.isoend, Globals.page_1,
#                                            Globals.page_100, 'DISC_USAGE', 'LOW')
#         apiUrl = Globals.BaseURL + DiscUsageLowAlert
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=DISC_USAGE and level=Low ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=DISC_USAGE and level=Low ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=DISC_USAGE and level=Warning
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_DISC_USAGE_WARNING == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10421)
# def test_tc_000022_DISC_USAGEWarning(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         DiscUsageWarningAlert = url_formatter2(Globals.accountId, Variable.isostart, Variable.isoend, Globals.page_1,
#                                                Globals.page_100, 'DISC_USAGE', 'WARNING')
#         apiUrl = Globals.BaseURL + DiscUsageWarningAlert
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=DISC_USAGE and level=Warning ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=DISC_USAGE and level=Warning ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=DISC_USAGE and level=Critical
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_DISC_USAGE_CRITICAL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10422)
# def test_tc_000023_DISC_USAGE_CRITICAL(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         DiscUsageCriticalAlert = url_formatter2(Globals.accountId, Variable.isostart, Variable.isoend, Globals.page_1,
#                                                 Globals.page_100, 'DISC_USAGE', 'CRITICAL')
#         apiUrl = Globals.BaseURL + DiscUsageCriticalAlert
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=DISC_USAGE and level=Critical ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=DISC_USAGE and level=Critical ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=DEVICE_FALLEN and level=Critical
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_DEVICE_FALLEN_CRITICAL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10423)
# def test_tc_000024_DEVICE_FALLEN_LOW(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         DeviceFallenCriticalAlert = url_formatter2(Globals.accountId, Variable.isostart, Variable.isoend,
#                                                    Globals.page_1, Globals.page_100, 'DEVICE_FALLEN', 'LOW')
#         apiUrl = Globals.BaseURL + DeviceFallenCriticalAlert
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=DEVICE_FALLEN and level=Critical ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=DEVICE_FALLEN and level=Critical ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=DEVICE_MARKED_REPLACED and level=Critical
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_DEVICE_MARKED_REPLACED_CRITICAL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10424)
# def test_tc_000025_DEVICE_MARKED_REPLACED_CRITICAL(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         DeviceMarkedAsReplacedCriticalAlert = url_formatter2(Globals.accountId, Variable.isostart, Variable.isoend,
#                                                              Globals.page_1, Globals.page_100,
#                                                              'DEVICE_MARKED_REPLACED', 'CRITICAL')
#         apiUrl = Globals.BaseURL + DeviceMarkedAsReplacedCriticalAlert
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=DEVICE_MARKED_REPLACED and level=Critical ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=DEVICE_MARKED_REPLACED and level=Critical ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=DEVICE_MARKED_LOST and level=Critical
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_DEVICE_MARKED_LOST_CRITICAL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10425)
# def test_tc_000026_DEVICE_MARKED_LOST_CRITICAL(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         DeviceMarkedAsLostCriticalAlert = url_formatter2(Globals.accountId, Variable.isostart, Variable.isoend,
#                                                          Globals.page_1, Globals.page_100, 'DEVICE_MARKED_LOST',
#                                                          'CRITICAL')
#         apiUrl = Globals.BaseURL + DeviceMarkedAsLostCriticalAlert
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=DEVICE_MARKED_LOST and level=Critical ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=DEVICE_MARKED_LOST and level=Critical ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=KIOSK_LOCKED and level=Critical
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_DEVICE_MARKED_STOLEN_CRITICAL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10426)
# def test_tc_000027_DEVICE_MARKED_STOLEN_CRITICAL(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         DeviceMarkedAsStolenCriticalAlert = url_formatter2(Globals.accountId, Variable.isostart, Variable.isoend,
#                                                            Globals.page_1, Globals.page_100, 'DEVICE_MARKED_STOLEN',
#                                                            'CRITICAL')
#         apiUrl = Globals.BaseURL + DeviceMarkedAsStolenCriticalAlert
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=DEVICE_MARKED_STOLEN and level=Critical ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=DEVICE_MARKED_STOLEN and level=Critical ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=DEVICE_CONNECTED_BACK and level=Critical
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_DEVICE_CONNECTED_BACK_CRITICAL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10427)
# def test_tc_000028_DEVICE_CONNECTED_BACKCritical(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         DeviceConnectedBackCriticalAlert = url_formatter2(Globals.accountId, Variable.isostart, Variable.isoend,
#                                                           Globals.page_1, Globals.page_100, 'DEVICE_CONNECTED_BACK',
#                                                           'CRITICAL')
#         apiUrl = Globals.BaseURL + DeviceConnectedBackCriticalAlert
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=DEVICE_CONNECTED_BACK and level=Critical ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=DEVICE_CONNECTED_BACK and level=Critical ---------------------------\n")
#         assert False
#
#
# # Types are different and level is ALL
# # GET method to GET Alert notifications of type=Battery and level=All
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_BATTERY_ALL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10428)
# def test_tc_000029_BATTERY_ALL(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         BATTERYALL = url_formatter3(Globals.accountId, Variable.isostart, Variable.isoend, Globals.page_1,
#                                     Globals.page_100, 'BATTERY')
#         apiUrl = Globals.BaseURL + BATTERYALL
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=Battery and level=All ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=Battery and level=All ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=KIOSK_LOCKED and level=Warning
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_DATA_USAGE_WARNING == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10429)
# def test_tc_000030_DATA_USAGE(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         DATA_USAGEALL = url_formatter3(Globals.accountId, Variable.isostart, Variable.isoend, Globals.page_1,
#                                        Globals.page_100, 'DATA_USAGE')
#         apiUrl = Globals.BaseURL + DATA_USAGEALL
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=DATA_USAGE and level=All ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=DATA_USAGE and level=All ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=KIOSK_LOCKED and level=All
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_KIOSK_LOCKED_Regular == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10430)
# def test_tc_000031_KIOSK_LOCKED(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         KIOSK_LOCKEDALL = url_formatter3(Globals.accountId, Variable.isostart, Variable.isoend, Globals.page_1,
#                                          Globals.page_100, 'KIOSK_LOCKED')
#         apiUrl = Globals.BaseURL + KIOSK_LOCKEDALL
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=KIOSK_LOCKED and level=All ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=KIOSK_LOCKED and level=All ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=KIOSK_UNLOCKED and level=All
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_KIOSK_UNLOCKED_CRITICAL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10431)
# def test_tc_000032_KIOSK_UNLOCKED(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         KIOSK_UNLOCKEDALL = url_formatter3(Globals.accountId, Variable.isostart, Variable.isoend, Globals.page_1,
#                                            Globals.page_100, 'KIOSK_UNLOCKED')
#         apiUrl = Globals.BaseURL + KIOSK_UNLOCKEDALL
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=KIOSK_UNLOCKED and level=All ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=KIOSK_UNLOCKED and level=All ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=ADMIN_LOCKED and level=All
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_ADMIN_LOCKED_CRITICAL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10432)
# def test_tc_000033_ADMIN_LOCKED(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         ADMIN_LOCKEDALL = url_formatter3(Globals.accountId, Variable.isostart, Variable.isoend, Globals.page_1,
#                                          Globals.page_100, 'ADMIN_LOCKED')
#         apiUrl = Globals.BaseURL + ADMIN_LOCKEDALL
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=ADMIN_LOCKED and level=All ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=ADMIN_LOCKED and level=All ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=DEVICE_REBOOTED and level=All
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_DEVICE_REBOOTED_CRITICAL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10433)
# def test_tc_000034_DEVICE_REBOOTED(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         DEVICE_REBOOTEDALL = url_formatter3(Globals.accountId, Variable.isostart, Variable.isoend, Globals.page_1,
#                                             Globals.page_100, 'DEVICE_REBOOTED')
#         apiUrl = Globals.BaseURL + DEVICE_REBOOTEDALL
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=DEVICE_REBOOTED and level=All ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=DEVICE_REBOOTED and level=All ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=DEVICE_WIPED and level=All
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_DEVICE_WIPED_CRITICAL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10434)
# def test_tc_000035_DEVICE_WIPED(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         DEVICE_WIPEDALL = url_formatter3(Globals.accountId, Variable.isostart, Variable.isoend, Globals.page_1,
#                                          Globals.page_100, 'DEVICE_WIPED')
#         apiUrl = Globals.BaseURL + DEVICE_WIPEDALL
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=DEVICE_WIPED and level=All ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=DEVICE_WIPED and level=All ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=DEVICE_DELETED and level=All
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_DEVICE_DELETED_CRITICAL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10435)
# def test_tc_000036_KIOSK_DEVICE_DELETED(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         DEVICE_DELETEDALL = url_formatter3(Globals.accountId, Variable.isostart, Variable.isoend, Globals.page_1,
#                                            Globals.page_100, 'DEVICE_DELETED')
#         apiUrl = Globals.BaseURL + DEVICE_DELETEDALL
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=DEVICE_DELETED and level=All ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=DEVICE_DELETED and level=All ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=ROOTED_ENROLL and level=All
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_ROOTED_ENROLL_CRITICAL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10436)
# def test_tc_000037_ROOTED_ENROLL(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         ROOTED_ENROLLALL = url_formatter3(Globals.accountId, Variable.isostart, Variable.isoend, Globals.page_1,
#                                           Globals.page_100, 'ROOTED_ENROLL')
#         apiUrl = Globals.BaseURL + ROOTED_ENROLLALL
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=ROOTED_ENROLL and level=All ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=ROOTED_ENROLL and level=All ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=MEMORY_ALERT and level=All
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_MEMORY_ALERT_CRITICAL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10437)
# def test_tc_000038_MEMORY_ALERT(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         MEMORY_ALERTALL = url_formatter3(Globals.accountId, Variable.isostart, Variable.isoend, Globals.page_1,
#                                          Globals.page_100, 'MEMORY_ALERT')
#         apiUrl = Globals.BaseURL + MEMORY_ALERTALL
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=MEMORY_ALERT and level=All ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=MEMORY_ALERT and level=All ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=DISC_USAGE and level=All
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_DISC_USAGE_CRITICAL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10438)
# def test_tc_000039_DISC_USAGE(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         DISC_USAGEALL = url_formatter3(Globals.accountId, Variable.isostart, Variable.isoend, Globals.page_1,
#                                        Globals.page_100, 'DISC_USAGE')
#         apiUrl = Globals.BaseURL + DISC_USAGEALL
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=DISC_USAGE and level=All ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=DISC_USAGE and level=All ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=DEVICE_FALLEN and level=All
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_DEVICE_FALLEN_CRITICAL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10439)
# def test_tc_000040_DEVICE_FALLEN(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         DEVICE_FALLENALL = url_formatter3(Globals.accountId, Variable.isostart, Variable.isoend, Globals.page_1,
#                                           Globals.page_100, 'DEVICE_FALLEN')
#         apiUrl = Globals.BaseURL + DEVICE_FALLENALL
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=DEVICE_FALLEN and level=All ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=DEVICE_FALLEN and level=All ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=DEVICE_MARKED_REPLACED and level=All
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_DEVICE_MARKED_REPLACED_CRITICAL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10440)
# def test_tc_000041_DEVICE_MARKED_REPLACED(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         DEVICE_MARKED_REPLACEDALL = url_formatter3(Globals.accountId, Variable.isostart, Variable.isoend,
#                                                    Globals.page_1, Globals.page_100, 'DEVICE_MARKED_REPLACED')
#         apiUrl = Globals.BaseURL + DEVICE_MARKED_REPLACEDALL
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=DEVICE_MARKED_REPLACED and level=All ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=DEVICE_MARKED_REPLACED and level=All ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=DEVICE_MARKED_LOST and level=All
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_DEVICE_MARKED_LOST_CRITICAL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10441)
# def test_tc_000042_DEVICE_MARKED_LOST(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         DEVICE_MARKED_LOSTALL = url_formatter3(Globals.accountId, Variable.isostart, Variable.isoend, Globals.page_1,
#                                                Globals.page_100, 'DEVICE_MARKED_LOST')
#         apiUrl = Globals.BaseURL + DEVICE_MARKED_LOSTALL
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=DEVICE_MARKED_LOST and level=All ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=DEVICE_MARKED_LOST and level=All ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=DEVICE_MARKED_STOLEN and level=All
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_DEVICE_MARKED_STOLEN_CRITICAL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10442)
# def test_tc_000043_DEVICE_MARKED_STOLEN(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         DEVICE_MARKED_STOLENALL = url_formatter3(Globals.accountId, Variable.isostart, Variable.isoend, Globals.page_1,
#                                                  Globals.page_100, 'DEVICE_MARKED_STOLEN')
#         apiUrl = Globals.BaseURL + DEVICE_MARKED_STOLENALL
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=DEVICE_MARKED_STOLEN and level=All ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=DEVICE_MARKED_STOLEN and level=All ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=DEVICE_CONNECTED_BACK and level=All
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_DEVICE_CONNECTED_BACK_CRITICAL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10443)
# def test_tc_000044_DEVICE_CONNECTED_BACK(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         DEVICE_CONNECTED_BACKALL = url_formatter3(Globals.accountId, Variable.isostart, Variable.isoend, Globals.page_1,
#                                                   Globals.page_100, 'DEVICE_CONNECTED_BACK')
#         apiUrl = Globals.BaseURL + DEVICE_CONNECTED_BACKALL
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=DEVICE_CONNECTED_BACK and level=All ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=DEVICE_CONNECTED_BACK and level=All ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=SIM_LOCK_CHANGED and level=All
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_SIM_LOCK_CHANGED_ALL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10443)
# def test_tc_000045_SIM_LOCK_CHANGED(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         SIM_LOCK_CHANGED = url_formatter3(Globals.accountId, Variable.isostart, Variable.isoend, Globals.page_1,
#                                           Globals.page_100, 'SIM_LOCK_CHANGED')
#         apiUrl = Globals.BaseURL + SIM_LOCK_CHANGED
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type = SIM_LOCK_CHANGED and level=All ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type =SIM_LOCK_CHANGED and level=All ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=RESET_PASSWORD and level=All
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_RESET_PASSWORD_ALL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10443)
# def test_tc_000046_RESET_PASSWORD(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         RESET_PASSWORD = url_formatter3(Globals.accountId, Variable.isostart, Variable.isoend, Globals.page_1,
#                                         Globals.page_100, 'RESET_PASSWORD')
#         apiUrl = Globals.BaseURL + RESET_PASSWORD
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type = RESET_PASSWORD and level=All ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type = RESET_PASSWORD and level=All ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=SIM_REMOVED and level=All
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_SIM_REMOVED_ALL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10443)
# def test_tc_000047_SIM_REMOVED(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         SIM_REMOVED = url_formatter3(Globals.accountId, Variable.isostart, Variable.isoend, Globals.page_1,
#                                      Globals.page_100, 'SIM_REMOVED')
#         apiUrl = Globals.BaseURL + SIM_REMOVED
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=SIM_REMOVED and level=All ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=SIM_REMOVED and level=All ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=SIM_CHANGED and level=All
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_SIM_CHANGED_ALL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10443)
# def test_tc_000048_SIM_CHANGED(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         SIM_CHANGED = url_formatter3(Globals.accountId, Variable.isostart, Variable.isoend, Globals.page_1,
#                                      Globals.page_100, 'SIM_CHANGED')
#         apiUrl = Globals.BaseURL + SIM_CHANGED
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=SIM_CHANGED and level=All ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=SIM_CHANGED and level=All ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=SIM_ADDED and level=All
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_SIM_ADDED_ALL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10443)
# def test_tc_000049_SIM_ADDED(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         SIM_ADDED = url_formatter3(Globals.accountId, Variable.isostart, Variable.isoend, Globals.page_1,
#                                    Globals.page_100, 'SIM_ADDED')
#         apiUrl = Globals.BaseURL + SIM_ADDED
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=SIM_ADDED and level=All ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=SIM_ADDED and level=All ---------------------------\n")
#         assert False
#
#
# # GET method to GET Alert notifications of type=UNINSTALL_WEGUARD and level=All
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_AlertsModule_UNINSTALL_WEGUARD_ALL == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.sanitytest
# @pytest.mark.sprint20
# @pytest.mark.alerts
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10443)
# def test_tc_000050_UNINSTALL_WEGUARD(url):
#     now1 = datetime.now()
#     if Globals.bearerToken == '':
#         pytest.skip("Empty Bearer token. Skipping test")
#     try:
#         UNINSTALL_WEGUARD = url_formatter3(Globals.accountId, Variable.isostart, Variable.isoend, Globals.page_1,
#                                            Globals.page_100, 'UNINSTALL_WEGUARD')
#         apiUrl = Globals.BaseURL + UNINSTALL_WEGUARD
#         Headers = {'Authorization': 'Bearer {}'.format(Globals.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=Globals.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#         print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug(
#             "\n--------------------------- Alert notifications of type=UNINSTALL_WEGUARD and level=All ---------------------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
#         WeGuard.logger.debug(
#             "\n--------------------------- Not available alert notifications of type=UNINSTALL_WEGUARD and level=All ---------------------------\n")
#         assert False
