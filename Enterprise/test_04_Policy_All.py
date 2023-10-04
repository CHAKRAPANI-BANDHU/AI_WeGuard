from datetime import datetime

import pytest
import requests
import Executor as Execute
import globalvariables as Globalinfo
import test_GETutils as Utils


def url_formatter(page, size):
    url = "enterprise/rest/v3/policy/all?page={page}&size={size}&deviceCount=true&impersonator=false".format(page=page,
                                                                                                             size=size)
    return url


@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_4000_Policy_All == 0, reason="test skipped")
@pytest.mark.usualtest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.positivetest
@pytest.mark.run(order=400000)
def test_tc_4001_Policy_ALL_10000(url):
    # Function to store profiles
    def store_profiles(platform, policy_type, policy_id, policy_name):
        if platform == "ANDROID":
            Globalinfo.Android_Policies.append((policy_type, policy_id, policy_name))
        elif platform == "IOS":
            Globalinfo.iOS_Policies.append((policy_type, policy_id, policy_name))
        elif platform == "WINDOWS":
            Globalinfo.Windows_Policies.append((policy_type, policy_id, policy_name))
        else:
            print("Invalid platform")

    now1 = datetime.now()
    if Globalinfo.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        LicenseUrl = url_formatter(Globalinfo.page_1, Globalinfo.page_1000)
        apiUrl = Globalinfo.BaseURL + LicenseUrl
        Headers = {'Authorization': 'Bearer ' + Globalinfo.bearerToken}
        res = requests.get(url=apiUrl, headers=Headers)
        if res.status_code == 200:
            print("\n" + "200 The request was a success!" + "\n")
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            print(#"\n" + "Header: " + str(res.headers) + "\n"
                "\n" + "Request URL: " + apiUrl +
                "\n" + "Request Method: " + res.request.method +
                "\n" + "Status Code: " + str(res.status_code) +
                "\n" + "Response: " + str(res.content) + "\n\n")
            json_resp = res.json()
            # Store profiles based on platform and type
            for profile in json_resp.get('list', []):
                platform = profile.get('platform')
                profile_type = profile.get('type')
                profile_id = profile.get('id')
                profile_name = profile.get('name')
                store_profiles(platform, profile_type, profile_id, profile_name)

            # Extract and store IDs from JSON response
            # extract_and_store_ids(json_resp, 'platform', 'id')
            # Access Windows profile IDs
            if Globalinfo.Windows_Policies:
                print("\nWindows Policies Information:")
                for profile in Globalinfo.Windows_Policies:
                    Globalinfo.Windows_Policy_Names.append(profile[2])  # Append Name 
                    Globalinfo.Windows_Policy_IDs.append(profile[1])  # Append Policy ID
                    Globalinfo.Windows_Policy_Types.append(profile[0])  # Append Type 

                Windows_Policy_IDs_str = ', '.join(Globalinfo.Windows_Policy_IDs)
                print("\nWindows Policy IDs: " + Windows_Policy_IDs_str)

                Windows_Names_str = ', '.join(Globalinfo.Windows_Policy_Names)
                print("\nWindows Policy Names: " + Windows_Names_str)

                Windows_Type_str = ', '.join(Globalinfo.Windows_Policy_Types)
                print("\nWindows Policy Types: " + Windows_Type_str + "\n")
            else:
                print("No Windows Policies found.")

            # Access Android profile IDs
            if Globalinfo.Android_Policies:
                print("\nAndroid Policies Information:")
                for profile in Globalinfo.Android_Policies:
                    Globalinfo.Android_Policy_IDs.append(profile[1])  # Append Policy ID
                    Globalinfo.Android_Policy_Names.append(profile[2])  # Append Name
                    Globalinfo.Android_Policy_Types.append(profile[0])  # Append Type

                Android_Policy_IDs_str = ', '.join(Globalinfo.Android_Policy_IDs)
                print("\nAndroid Policy IDs: " + Android_Policy_IDs_str)

                Android_Names_str = ', '.join(Globalinfo.Android_Policy_Names)
                print("\nAndroid Policy Names: " + Android_Names_str)

                Android_Types_str = ', '.join(Globalinfo.Android_Policy_Types)
                print("\nAndroid Policy Types: " + Android_Types_str + "\n")
            else:
                print("No Android Policies found.")

            # Access iOS profile IDs
            if Globalinfo.iOS_Policies:
                print("\niOS Policies Information:")
                for profile in Globalinfo.iOS_Policies:
                    Globalinfo.iOS_Policy_IDs.append(profile[1])  # Append ID
                    Globalinfo.iOS_Policy_Names.append(profile[2])  # Append Name
                    Globalinfo.iOS_Policy_Types.append(profile[0])  # Append Type

                iOS_Policy_IDs_str = ', '.join(Globalinfo.iOS_Policy_IDs)
                print("\niOS Policy IDs: " + iOS_Policy_IDs_str)

                iOS_Names_str = ', '.join(Globalinfo.iOS_Policy_Names)
                print("\niOS Policy Names: " + iOS_Names_str)

                iOS_Types_str = ', '.join(Globalinfo.iOS_Policy_Types)
                print("\niOS Policy Types: " + iOS_Types_str + "\n")
            else:
                print("No iOS Policies found.")

                # Store policies based on platform and type
                for policies in json_resp.get('list', []):
                    platform = policies.get('platform')
                    policy_type = policies.get('type')
                    policy_id = policies.get('id')
                    policy_name = policies.get('name')
                    store_profiles(platform, policy_type, policy_id, policy_name)

            # Print stored profiles
            print("\nAndroid Policies:", Globalinfo.Android_Policies, "\n")
            print("\niOS Policies:", Globalinfo.iOS_Policies, "\n")
            print("\nWindows Policies:", Globalinfo.Windows_Policies, "\n")
        elif res.status_code == 400:
            print("\n" + "400 Bad Request!" + "\n")
            assert False, "Received 400 Bad Request response"
        elif res.status_code == 404:
            print("\n" + "404 Result not found!" + "\n")
            assert False, "Received 404 response"
        elif res.status_code == 500:
            print("\n" + "500 Internal Server Error!" + "\n")
            assert False, "Received 500 response"
        else:
            print("Request did not succeed! Status code:", res.status_code)
            assert False, f"Received {res.status_code} response"
    except BaseException as e:
        print("Exception : " + str(e))
        now2 = datetime.now()
        print("Time taken: " + str(now2 - now1))
        print("------------------- TC 001 LOGIN FAIL ---------------------------\n\n")
        assert False
