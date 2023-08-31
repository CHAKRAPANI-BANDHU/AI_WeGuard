# def url_formatter2(name, userName, ac, pac):
#     url2 = "uploader/upload/file/v2?name={name}&userName={userName}&ac={ac}&pac={pac}".format(name=name,
#                                                                                              userName=userName, ac=ac,
#                                                                                              pac=pac)
#     return url2

def url_formatter(name, userName, ac, fileName):
    uploader = "uploader/upload/file/v2?name={name}&userName={userName}&ac={ac}&chunkNumber=1&totalChunks=1&fileName={fileName}".format(
        name=name, userName=userName,
        ac=ac, fileName=fileName, )
    return uploader

# # Upload SVG file in WeBox
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_WeBox_SVGUpload == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10202)
# def test_WeBoxUploadSVG(url):
#     now1 = datetime.now()
#     if VariableX.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         WeBoxuploader = url_formatter(VariableX.name, VariableX.userName, VariableX.activationCode,
#                                       VariableX.productActivationCode)
#         apiUrl = VariableX.BaseURL + WeBoxuploader
#         Headers = {'x-token': 'lqa7nt69izjgcg0uv4rl'}
#         with open("WeBoxFiles_DeviceUploads/FilesUpload/Advanced.svg", 'rb') as svg_file:
#             Files = {'file': svg_file.read()}
#         res = requests.post(url=apiUrl, files=Files, headers=Headers, timeout=VariableX.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#   print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug("--------------------File is uploaded successfully-----------------")
#         assert res.status_code == 200
#     except Exception as e:
#         WeGuard.logger.error("Exception: " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.error("Time taken: " + str(now2 - now1))
#         WeGuard.logger.error("--------------------Failed to upload a file-----------------")
#         assert False

# # Upload wav file in WeBox
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_WeBox_WAVUpload == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10204)
# def test_WeBoxUploadWav(url):
#     now1 = datetime.now()
#     if VariableX.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         WeBoxuploader = url_formatter(VariableX.name, VariableX.userName, VariableX.activationCode,
#                                       VariableX.productActivationCode)
#         apiUrl = VariableX.BaseURL + WeBoxuploader
#         Headers = {'x-token': 'lqa7nt69izjgcg0uv4rl'}
#
#         # Open the file using 'with' statement
#         with open("WeBoxFiles_DeviceUploads/FilesUpload/file_example_WAV_2MG.wav", 'rb') as file:
#             files = {'file': file.read()}  # Read the file content
#
#         res = requests.post(url=apiUrl, files=files, headers=Headers)
#
#         curl_str1 = Utils.getCurlEquivalent(res)
#   print(curl_str1)
#         WeGuard.logger.debug(res.content)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug("--------------------File is uploaded successfully-----------------")
#
#         if res.status_code == 200:
#             print("File upload was successful!")
#             # Add your further actions for a successful upload here
#         else:
#             print("File upload failed! Status code:", res.status_code)
#             # Add your assertions or actions for upload failure here
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.error("Time taken: " + str(now2 - now1))
#         WeGuard.logger.error("--------------------Failed to upload a file-----------------")
#         assert False

# # Upload gif file in WeBox
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_WeBox_GIFUpload == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10205)
# def test_WeBoxUploadGif(url):
#     now1 = datetime.now()
#     if VariableX.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         WeBoxuploader = url_formatter(VariableX.name, VariableX.userName, VariableX.activationCode, VariableX.productActivationCode)
#         apiUrl = VariableX.BaseURL + WeBoxuploader
#         Headers = {'x-token': 'lqa7nt69izjgcg0uv4rl'}
#         # Open the file using 'with' statement
#         with open("WeBoxFiles_DeviceUploads/FilesUpload/Daishi.gif", 'rb') as file:
#             files = {'file': file.read()}  # Read the file content
#         res = requests.post(url=apiUrl, files=files, headers=Headers)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug("--------------------File is uploaded successfully-----------------")
#         curl_str1 = Utils.getCurlEquivalent(res)
#   print(curl_str1)
#         WeGuard.logger.debug(res.content)
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.error("Time taken: " + str(now2 - now1))
#         WeGuard.logger.error("--------------------Failed to upload a file-----------------")
#         assert False
#
#
# # Upload mp3 file in WeBox
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_WeBox_MP3Upload == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10206)
# def test_WeBoxUploadMp3(url):
#     now1 = datetime.now()
#     if VariableX.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         WeBoxuploader = url_formatter(VariableX.name, VariableX.userName, VariableX.activationCode, VariableX.productActivationCode)
#         apiUrl = VariableX.BaseURL + WeBoxuploader
#         Headers = {'x-token': 'lqa7nt69izjgcg0uv4rl'}
#        # Open the file using 'with' statement
#         with open("WeBoxFiles_DeviceUploads/FilesUpload/Over the Horizon.mp3", 'rb') as file:
#             files = {'file': file.read()}  # Read the file content
#         res = requests.post(url=apiUrl, files=files, headers=Headers)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug("--------------------File is uploaded successfully-----------------")
#         curl_str1 = Utils.getCurlEquivalent(res)
#   print(curl_str1)
#         WeGuard.logger.debug(res.content)
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.error("Time taken: " + str(now2 - now1))
#         WeGuard.logger.error("--------------------Failed to upload a file-----------------")
#         assert False
#
#
# # Upload ogg file in WeBox
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_WeBox_OGGUpload == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10207)
# def test_WeBoxUploadOgg(url):
#     now1 = datetime.now()
#     if VariableX.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         WeBoxuploader = url_formatter(VariableX.name, VariableX.userName, VariableX.activationCode, VariableX.productActivationCode)
#         apiUrl = VariableX.BaseURL + WeBoxuploader
#         Headers = {'x-token': 'lqa7nt69izjgcg0uv4rl'}
#         Files = {
#             'file': open("WeBoxFiles_DeviceUploads/FilesUpload/file_example_OOG_1MG (1).ogg", 'rb')}
#         res = requests.post(url=apiUrl, files=Files, headers=Headers, timeout=VariableX.timeout)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug("--------------------File is uploaded successfully but OGG is not supported -----------------")
#         curl_str1 = Utils.getCurlEquivalent(res)
#   print(curl_str1)
#         WeGuard.logger.debug(res.content)
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.error("Time taken: " + str(now2 - now1))
#         WeGuard.logger.error("--------------------Failed to upload a file-----------------")
#         assert False
#
# # Upload webm file in WeBox
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_WeBox_WEBMUpload == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.negativetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10209)
# def test_WeBoxUploadWEBM(url):
#     now1 = datetime.now()
#     if VariableX.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         WeBoxuploader = url_formatter(VariableX.name, VariableX.userName, VariableX.activationCode, VariableX.productActivationCode)
#         apiUrl = VariableX.BaseURL + WeBoxuploader
#         Headers = {'x-token': 'lqa7nt69izjgcg0uv4rl'}
#         files = {'file': open("WeBoxFiles_DeviceUploads/FilesUpload/FilesUpload/elephants-dream.webm", 'rb')}
#         res = requests.post(url=apiUrl, files=files, headers=Headers)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug("--------------------File is uploaded successfully but WEBM is not supported -----------------")
#         curl_str1 = Utils.getCurlEquivalent(res)
#   print(curl_str1)
#         WeGuard.logger.debug(res.content)
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.error("Time taken: " + str(now2 - now1))
#         WeGuard.logger.error("--------------------Failed to upload a file-----------------")
#         assert False
#
#
# # Upload mov file in WeBox
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_WeBox_MOVUpload == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10203)
# def test_WeBoxUploadMov(url):
#     now1 = datetime.now()
#     if VariableX.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         WeBoxuploader = url_formatter(VariableX.name, VariableX.userName, VariableX.activationCode, VariableX.productActivationCode)
#         apiUrl = VariableX.BaseURL + WeBoxuploader
#         Headers = {'x-token': 'lqa7nt69izjgcg0uv4rl'}
#         files = {
#             'file': open("WeBoxFiles_DeviceUploads/FilesUpload/file_example_MOV_1280_1_4MB.mov", 'rb')}
#         res = requests.post(url=apiUrl, files=files, headers=Headers)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug("--------------------File is uploaded successfully-----------------")
#         curl_str1 = Utils.getCurlEquivalent(res)
#   print(curl_str1)
#         WeGuard.logger.debug(res.content)
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.error("Time taken: " + str(now2 - now1))
#         WeGuard.logger.error("--------------------Failed to upload a file-----------------")
#         assert False
#
#
# # Upload txt file in WeBox
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_WeBox_TXTUpload == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10210)
# def test_WeBoxUploadTXT(url):
#     now1 = datetime.now()
#     if VariableX.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         WeBoxuploader = url_formatter(VariableX.name, VariableX.userName, VariableX.activationCode, VariableX.productActivationCode)
#         apiUrl = VariableX.BaseURL + WeBoxuploader
#         Headers = {'x-token': 'lqa7nt69izjgcg0uv4rl'}
#         Files = {'file': open("WeBoxFiles_DeviceUploads/FilesUpload/chakrapani.txt", 'rb')}
#         res = requests.post(url=apiUrl, files=Files, headers=Headers, timeout=VariableX.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#   print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug("--------------------File is uploaded successfully-----------------")
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.error("Time taken: " + str(now2 - now1))
#         WeGuard.logger.error("--------------------Failed to upload a file-----------------")
#         assert False
#
#
# # Upload pptx file in WeBox
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_WeBox_PPTXUpload == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10215)
# def test_WeBoxUploadPPTX(url):
#     now1 = datetime.now()
#     if VariableX.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         WeBoxuploader = url_formatter(VariableX.name, VariableX.userName, VariableX.activationCode, VariableX.productActivationCode)
#         apiUrl = VariableX.BaseURL + WeBoxuploader
#         Headers = {'x-token': 'lqa7nt69izjgcg0uv4rl'}
#         Files = {'file': open("WeBoxFiles_DeviceUploads/FilesUpload/Chakrapani_22_11_2019_WeTalk.pptx",
#                               'rb')}
#         res = requests.post(url=apiUrl, files=Files, headers=Headers, timeout=VariableX.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#   print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug("--------------------File is uploaded successfully-----------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.error("Time taken: " + str(now2 - now1))
#         WeGuard.logger.error("--------------------Failed to upload a file-----------------")
#         assert False
#
#
# # Uploaddoc file in WeBox
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_WeBox_DOCUpload == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10213)
# def test_WeBoxUploadDoc(url):
#     now1 = datetime.now()
#     if VariableX.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         WeBoxuploader = url_formatter(VariableX.name, VariableX.userName, VariableX.activationCode, VariableX.productActivationCode)
#         apiUrl = VariableX.BaseURL + WeBoxuploader
#         Headers = {'x-token': 'lqa7nt69izjgcg0uv4rl'}
#         Files = {'file': open("WeBoxFiles_DeviceUploads/FilesUpload/Chakrapani Resume.doc", 'rb')}
#         res = requests.post(url=apiUrl, files=Files, headers=Headers, timeout=VariableX.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#   print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug("--------------------File is uploaded successfully-----------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.error("Time taken: " + str(now2 - now1))
#         WeGuard.logger.error("--------------------Failed to upload a file-----------------")
#         assert False
#
#
# # Upload xlsx file in WeBox
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_WeBox_XLSXUpload == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10211)
# def test_WeBoxUploadXlsx(url):
#     now1 = datetime.now()
#     if VariableX.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         WeBoxuploader = url_formatter(VariableX.name, VariableX.userName, VariableX.activationCode, VariableX.productActivationCode)
#         apiUrl = VariableX.BaseURL + WeBoxuploader
#         Headers = {'x-token': 'lqa7nt69izjgcg0uv4rl'}
#         Files = {
#             'file': open("WeBoxFiles_DeviceUploads/FilesUpload/358195082934346_AI Kiosk.xlsx", 'rb')}
#         res = requests.post(url=apiUrl, files=Files, headers=Headers, timeout=VariableX.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#   print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug("--------------------File is uploaded successfully-----------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.error("Time taken: " + str(now2 - now1))
#         WeGuard.logger.error("--------------------Failed to upload a file-----------------")
#         assert False
#
#
# # Upload pdf file in WeBox
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_WeBox_PDFUpload == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10214)
# def test_WeBoxUploadPdf(url):
#     now1 = datetime.now()
#     if VariableX.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         WeBoxuploader = url_formatter(VariableX.name, VariableX.userName, VariableX.activationCode, VariableX.productActivationCode)
#         apiUrl = VariableX.BaseURL + WeBoxuploader
#         Headers = {'x-token': 'lqa7nt69izjgcg0uv4rl'}
#         Files = {'file': open(
#             "WeBoxFiles_DeviceUploads/FilesUpload/postconference-05-19-2020-1589867801.pdf", 'rb')}
#         res = requests.post(url=apiUrl, files=Files, headers=Headers, timeout=VariableX.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#   print(curl_str1)
#         WeGuard.logger.debug(res.content)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug("--------------------File is uploaded successfully-----------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.error("Time taken: " + str(now2 - now1))
#         WeGuard.logger.error("--------------------Failed to upload a file-----------------")
#         assert False
#
#
# # Upload png file in WeBox
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_WeBox_PNGUpload == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10217)
# def test_WeBoxUploadPng(url):
#     now1 = datetime.now()
#     if VariableX.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         WeBoxuploader = url_formatter(VariableX.name, VariableX.userName, VariableX.activationCode, VariableX.productActivationCode)
#         apiUrl = VariableX.BaseURL + WeBoxuploader
#         Headers = {'x-token': 'lqa7nt69izjgcg0uv4rl'}
#         Files = {'file': open("WeBoxFiles_DeviceUploads/FilesUpload/m2m-in-motion-logo.png", 'rb')}
#         res = requests.post(url=apiUrl, files=Files, headers=Headers, timeout=VariableX.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#   print(curl_str1)
#         WeGuard.logger.debug(res.content)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug("--------------------File is uploaded successfully-----------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.error("Time taken: " + str(now2 - now1))
#         WeGuard.logger.error("--------------------Failed to upload a file-----------------")
#         assert False
#
#
# # Upload jpg file in WeBox
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_WeBox_JPGUpload == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10219)
# def test_WeBoxUploadJpg(url):
#     now1 = datetime.now()
#     if VariableX.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         WeBoxuploader = url_formatter(VariableX.name, VariableX.userName, VariableX.activationCode, VariableX.productActivationCode)
#         apiUrl = VariableX.BaseURL + WeBoxuploader
#         Headers = {'x-token': 'lqa7nt69izjgcg0uv4rl'}
#         Files = {
#             'file': open("WeBoxFiles_DeviceUploads/FilesUpload/DSC_0307.JPG",'rb')}
#         res = requests.post(url=apiUrl, files=Files, headers=Headers, timeout=VariableX.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#   print(curl_str1)
#         WeGuard.logger.debug(res.content)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug("--------------------File is uploaded successfully-----------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.error("Time taken: " + str(now2 - now1))
#         WeGuard.logger.error("-------------------- Failed to upload a file-----------------")
#         assert False
#
#
# # Uploaddocx file in WeBox
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_WeBox_DOCXUpload == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10212)
# def test_WeBoxUploadDocx(url):
#     now1 = datetime.now()
#     if VariableX.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         WeBoxuploader = url_formatter(VariableX.name, VariableX.userName, VariableX.activationCode, VariableX.productActivationCode)
#         apiUrl = VariableX.BaseURL + WeBoxuploader
#         Headers = {'x-token': 'lqa7nt69izjgcg0uv4rl'}
#         Files = {'file': open("WeBoxFiles_DeviceUploads/FilesUpload/Force stop an app.docx", 'rb')}
#         res = requests.post(url=apiUrl, files=Files, headers=Headers, timeout=VariableX.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#   print(curl_str1)
#         WeGuard.logger.debug(res.content)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug("--------------------File is uploaded successfully-----------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.error("Time taken: " + str(now2 - now1))
#         WeGuard.logger.error("--------------------Failed to upload a file-----------------")
#         assert False
#
#
# # Upload zip file in WeBox
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_WeBox_ZIPUpload == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10216)
# def test_WeBoxUploadZip(url):
#     now1 = datetime.now()
#     if VariableX.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         WeBoxuploader = url_formatter(VariableX.name, VariableX.userName, VariableX.activationCode, VariableX.productActivationCode)
#         apiUrl = VariableX.BaseURL + WeBoxuploader
#         Headers = {'x-token': 'lqa7nt69izjgcg0uv4rl'}
#         Files = {
#             'file': open("WeBoxFiles_DeviceUploads/FilesUpload/167Y1D5804-16032020111610.7z", 'rb')}
#         res = requests.post(url=apiUrl, files=Files, headers=Headers, timeout=VariableX.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#   print(curl_str1)
#         WeGuard.logger.debug(res.content)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug("--------------------File is uploaded successfully-----------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.error("Time taken: " + str(now2 - now1))
#         WeGuard.logger.error("--------------------Failed to upload a file-----------------")
#         assert False
#
#
# # Upload apk file in WeBox
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_WeBox_APKUpload == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.negativetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10217)
# def test_WeBoxUploadapk(url):
#     now1 = datetime.now()
#     if VariableX.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         WeBoxuploader = url_formatter(VariableX.name, VariableX.userName, VariableX.activationCode, VariableX.productActivationCode)
#         apiUrl = VariableX.BaseURL + WeBoxuploader
#         Headers = {'x-token': 'lqa7nt69izjgcg0uv4rl'}
#         files = {
#             'file': open("WeBoxFiles_DeviceUploads/FilesUpload/Chakrapani Testing Info.apk", 'rb')}
#         res = requests.post(url=apiUrl, files=files, headers=Headers)
#         curl_str1 = Utils.getCurlEquivalent(res)
#   print(curl_str1)
#         WeGuard.logger.debug(res.content)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug("-------------------- Apk is uploaded successfully but APK is not supported -----------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.error("Time taken: " + str(now2 - now1))
#         WeGuard.logger.error("--------------------Failed to upload a file-----------------")
#         assert False
#
#
# # Upload mp4 file in WeBox
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_WeBox_MP4Upload == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.positivetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10218)
# def test_WeBoxUploadMP4(url):
#     now1 = datetime.now()
#     if VariableX.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         WeBoxuploader = url_formatter(VariableX.name, VariableX.userName, VariableX.activationCode, VariableX.productActivationCode)
#         apiUrl = VariableX.BaseURL + WeBoxuploader
#         Headers = {'x-token': 'lqa7nt69izjgcg0uv4rl'}
#         Files = {'file': open("WeBoxFiles_DeviceUploads/FilesUpload/hst_1.mp4", 'rb')}
#         res = requests.post(url=apiUrl, files=Files, headers=Headers, timeout=VariableX.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#   print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug("--------------------File is uploaded successfully-----------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.error("Time taken: " + str(now2 - now1))
#         WeGuard.logger.error("--------------------Failed to upload a file-----------------")
#         assert False
#
#
# # Upload webm file in WeBox
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_WeBox_WEBMUpload == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.negativetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10219)
# def test_WeBoxUploadWEBM(url):
#     now1 = datetime.now()
#     if VariableX.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         WeBoxuploader = url_formatter(VariableX.name, VariableX.userName, VariableX.activationCode, VariableX.productActivationCode)
#         apiUrl = VariableX.BaseURL + WeBoxuploader
#         Headers = {'x-token': 'lqa7nt69izjgcg0uv4rl'}
#         files = {'file': open("WeBoxFiles_DeviceUploads/FilesUpload/elephants-dream.webm", 'rb')}
#         res = requests.post(url=apiUrl, files=files, headers=Headers)
#         curl_str1 = Utils.getCurlEquivalent(res)
#   print(curl_str1)
#         WeGuard.logger.debug(res.content)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug("--------------------File is uploaded successfully-----------------")
#         WeGuard.logger.debug("--------------------WEBM is not supported-----------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.error("Time taken: " + str(now2 - now1))
#         WeGuard.logger.error("--------------------Failed to upload a file-----------------")
#         assert False
#
#
# # Upload csv file in WeBox
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_WeBox_CSVUpload == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.negativetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10220)
# def test_WeBoxUploadCSV(url):
#     now1 = datetime.now()
#     if VariableX.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         WeBoxuploader = url_formatter(VariableX.name, VariableX.userName, VariableX.activationCode, VariableX.productActivationCode)
#         apiUrl = VariableX.BaseURL + WeBoxuploader
#         Headers = {'x-token': 'lqa7nt69izjgcg0uv4rl'}
#         Files = {
#             'file': open("WeBoxFiles_DeviceUploads/FilesUpload/transactions-06-02-2020-1591086845.csv",
#                          'rb')}
#         res = requests.post(url=apiUrl, files=Files, headers=Headers, timeout=VariableX.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#   print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug("--------------------File is uploaded successfully-----------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.error("Time taken: " + str(now2 - now1))
#         WeGuard.logger.error("--------------------Failed to upload a file-----------------")
#         assert False
#
#
# # Upload mpeg file in WeBox
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(Execute.test_tc_001_WeBox_MPEGUpload == 0,
#                     reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
# @pytest.mark.negativetest
# @pytest.mark.usualtest
# @pytest.mark.webox
# @pytest.mark.regressiontest
# @pytest.mark.run(order=10221)
# def test_WeBoxUploadMPEG(url):
#     now1 = datetime.now()
#     if VariableX.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         WeBoxuploader = url_formatter(VariableX.name, VariableX.userName, VariableX.activationCode, VariableX.productActivationCode)
#         apiUrl = VariableX.BaseURL + WeBoxuploader
#         Headers = {'x-token': 'lqa7nt69izjgcg0uv4rl'}
#         Files = {'file': open("WeBoxFiles_DeviceUploads/FilesUpload/Black Hole.mpg", 'rb')}
#         res = requests.post(url=apiUrl, files=Files, headers=Headers, timeout=VariableX.timeout)
#         curl_str1 = Utils.getCurlEquivalent(res)
#   print(curl_str1)
#         print("\n" + "Header: " + str(res.headers) +
#                              "\n" + "Request URL: " + apiUrl +
#                              "\n" + "Request Method: " + res.request.method +
#                              "\n" + "Status Code: " + str(res.status_code) +
#                              "\n" + "Response: " + str(res.content) + "\n")
#         WeGuard.logger.debug("--------------------File is uploaded successfully but MPEG is not supported -----------------")
#         assert res.status_code == 200
#     except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         now2 = datetime.now()
#         WeGuard.logger.error("Time taken: " + str(now2 - now1))
#         WeGuard.logger.error("--------------------Failed to upload a file-----------------")
#         assert False
