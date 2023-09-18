from datetime import datetime

import pytest
import requests
import WeGuardLogger as WeGuard
import Executor as Execute
import globalvariables as Globalinfo
import test_GETutils as Utils


def url_formatter(page, size):
    url = "enterprise/rest/v3/policy/all?page={page}&size={size}&deviceCount=true&impersonator=false".format(page=page,
                                                                                                             size=size)
    return url


@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_0003_Policy_All == 0, reason="test skipped")
@pytest.mark.usualtest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.positivetest
@pytest.mark.run(order=10008)
def test_tc_001_Policy_ALL_10000(url):
    # Function to store profiles
    def store_profiles(platform, profile_type, profile_id, profile_name):
        if platform == "ANDROID":
            Globalinfo.Android_profiles.append((profile_type, profile_id, profile_name))
        elif platform == "IOS":
            Globalinfo.iOS_profiles.append((profile_type, profile_id, profile_name))
        elif platform == "WINDOWS":
            Globalinfo.Windows_profiles.append((profile_type, profile_id, profile_name))
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
            print("\n" + "Header: " + str(res.headers) +
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
            if Globalinfo.Windows_profiles:
                print("\nWindows Policies Information:")
                for profile in Globalinfo.Windows_profiles:
                    Globalinfo.Windows_profile_name.append(profile[2])  # Append Name (since Platform is swapped)
                    Globalinfo.Windows_profile_ids.append(profile[1])  # Append ID
                    Globalinfo.Windows_profile_type.append(profile[0])  # Append Type (since Name is swapped)
                    # print("ID:", profile[1])    # Print ID
                    # print("Names:", profile[2])  # Print Names
                    # print("Type:", profile[0])  # Print Type

                Windows_profile_ids_str = ', '.join(Globalinfo.Windows_profile_ids)
                print("\nWindows Policy IDs: " + Windows_profile_ids_str)

                Windows_Names_str = ', '.join(Globalinfo.Windows_profile_name)
                print("\nWindows Policy Names: " + Windows_Names_str)

                Windows_Type_str = ', '.join(Globalinfo.Windows_profile_type)
                print("\nWindows Policy Types: " + Windows_Type_str + "\n")
            else:
                print("No Windows Policies found.")

            # Access Android profile IDs
            if Globalinfo.Android_profiles:
                print("\nAndroid Policies Information:")
                for profile in Globalinfo.Android_profiles:
                    Globalinfo.Android_profile_ids.append(profile[1])  # Append ID
                    Globalinfo.Android_profile_name.append(profile[2])  # Append Name
                    Globalinfo.Android_profile_type.append(profile[0])  # Append Type
                    # print("ID:", profile[1])    # Print ID
                    # print("Names:", profile[2])  # Print Names
                    # print("Type:", profile[0])  # Print Types

                Android_profile_ids_str = ', '.join(Globalinfo.Android_profile_ids)
                print("\nAndroid Policy IDs: " + Android_profile_ids_str)

                Android_Names_str = ', '.join(Globalinfo.Android_profile_name)
                print("\nAndroid Policy Names: " + Android_Names_str)

                Android_Types_str = ', '.join(Globalinfo.Android_profile_type)
                print("\nAndroid Policy Types: " + Android_Types_str + "\n")
            else:
                print("No Android Policies found.")

            # Access iOS profile IDs
            if Globalinfo.iOS_profiles:
                print("\niOS Policies Information:")
                for profile in Globalinfo.iOS_profiles:
                    Globalinfo.iOS_profile_ids.append(profile[1])  # Append ID
                    Globalinfo.iOS_profile_name.append(profile[2])  # Append Name
                    Globalinfo.iOS_profile_type.append(profile[0])  # Append Type
                    # print("ID:", profile[1])   # Print ID
                    # print("Name:", profile[2])  # Print Name
                    # print("Type:", profile[0])  # Print Type

                iOS_profile_ids_str = ', '.join(Globalinfo.iOS_profile_ids)
                print("\niOS Policy IDs: " + iOS_profile_ids_str)

                iOS_Names_str = ', '.join(Globalinfo.iOS_profile_name)
                print("\niOS Policy Names: " + iOS_Names_str)

                iOS_Types_str = ', '.join(Globalinfo.iOS_profile_type)
                print("\niOS Policy Types: " + iOS_Types_str + "\n")
            else:
                print("No iOS Policies found.")

                # Store policies based on platform and type
                for policies in json_resp.get('list', []):
                    platform = policies.get('platform')
                    profile_type = policies.get('type')
                    profile_id = policies.get('id')
                    profile_name = policies.get('name')
                    store_profiles(platform, profile_type, profile_id, profile_name)

            # Print stored profiles
            print("\nAndroid Profiles:", Globalinfo.Android_profiles, "\n")
            print("\niOS Profiles:", Globalinfo.iOS_profiles, "\n")
            print("\nWindows Profiles:", Globalinfo.Windows_profiles, "\n")
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
