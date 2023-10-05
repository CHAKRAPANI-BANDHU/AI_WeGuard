import json
from datetime import datetime
import pytest
import requests
import Executor as Execute
import globalvariables as Globalinfo
import test_GETutils as Utils

def AllPolicy(page, size):
    url = f"enterprise/rest/v3/policy/all?page={page}&size={size}&deviceCount=true&impersonator=false"
    return url

# Function to store profiles separately based on type
def store_profiles(platform, policy_type, policy_id, policy_name):
    if platform == "ANDROID":
        if policy_type == "ANDROID_KIOSK":
            Globalinfo.Android_Kiosk_Policy_IDs.append(policy_id)
            Globalinfo.Android_Kiosk_Policy_Names.append(policy_name)
        elif policy_type == "ANDROID_WM":
            Globalinfo.Android_WM_Policy_IDs.append(policy_id)
            Globalinfo.Android_WM_Policy_Names.append(policy_name)
        elif policy_type == "ANDROID_BYOD":
            Globalinfo.Android_BYOD_Policy_IDs.append(policy_id)
            Globalinfo.Android_BYOD_Policy_Names.append(policy_name)
        elif policy_type == "ANDROID_NON_PLAY_KIOSK":
            Globalinfo.Android_Non_Play_Kiosk_Policy_IDs.append(policy_id)
            Globalinfo.Android_Non_Play_Kiosk_Policy_Names.append(policy_name)
        elif policy_type == "ANDROID_NON_PLAY_WM":
            Globalinfo.Android_Non_Play_WM_Policy_IDs.append(policy_id)
            Globalinfo.Android_Non_Play_WM_Policy_Names.append(policy_name)
        elif policy_type == "ANDROID_NON_PLAY_BYOD":
            Globalinfo.Android_Non_Play_BYOD_Policy_IDs.append(policy_id)
            Globalinfo.Android_Non_Play_BYOD_Policy_Names.append(policy_name)
        elif policy_type in ["ANDROID_KIOSK", "ANDROID_WM", "ANDROID_BYOD"]:
            Globalinfo.Android_Policies.append((policy_type, policy_id, policy_name))
        elif policy_type in ["ANDROID_NON_PLAY_KIOSK", "ANDROID_NON_PLAY_WM", "ANDROID_NON_PLAY_BYOD"]:
            Globalinfo.Android_Non_Play_Policies.append((policy_id, policy_name))
        elif policy_type in ["ANDROID_KIOSK", "ANDROID_WM", "ANDROID_BYOD", "ANDROID_NON_PLAY_KIOSK",
                             "ANDROID_NON_PLAY_WM", "ANDROID_NON_PLAY_BYOD"]:
            Globalinfo.Android_All_Policies.append((policy_type, policy_id, policy_name))
    elif platform == "IOS":
        Globalinfo.iOS_Policies.append((policy_type, policy_id, policy_name))
    elif platform == "WINDOWS":
        Globalinfo.Windows_Policies.append((policy_type, policy_id, policy_name))
    else:
        print(f"Invalid platform: {platform}")


# Define the test function
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_4000_Policy_All == 0, reason="test skipped")
@pytest.mark.usualtest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.positivetest
@pytest.mark.run(order=400000)
def test_tc_4000_Policy_ALL_10000(url):
    now1 = datetime.now()
    if Globalinfo.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = Globalinfo.BaseURL + AllPolicy(Globalinfo.page_1, Globalinfo.page_1000)
        Headers = {'Authorization': 'Bearer ' + Globalinfo.bearerToken}
        res = requests.get(url=apiUrl, headers=Headers)
        if res.status_code == 200:
            print("\n" + "200 The request was a success!" + "\n")
            curl_str1 = Utils.getCurlEquivalent(res)
            print(curl_str1)
            print(
                "\n" + "Request URL: " + apiUrl +
                "\n" + "Request Method: " + res.request.method +
                "\n" + "Status Code: " + str(res.status_code) +
                "\n" + "Response: " + str(res.content) + "\n\n")
            json_response = json.loads(res.content)
            # Store profiles based on platform and type
            for profile in json_response.get('list', []):
                platform = profile.get('platform')
                profile_type = profile.get('type')
                profile_id = profile.get('id')
                profile_name = profile.get('name')
                store_profiles(platform, profile_type, profile_id, profile_name)
            
            # Access Windows profile IDs
            if Globalinfo.Windows_Policies:
                print("\n============== Windows Policies Information ==============")
                for profile in Globalinfo.Windows_Policies:
                    Globalinfo.Windows_Policy_Names.append(profile[2])
                    Globalinfo.Windows_Policy_IDs.append(profile[1])
                    Globalinfo.Windows_Policy_Types.append(profile[0])
                Windows_Policy_IDs_str = ', '.join(Globalinfo.Windows_Policy_IDs)
                print("\nWindows Policy IDs: " + Windows_Policy_IDs_str)
                Windows_Names_str = ', '.join(Globalinfo.Windows_Policy_Names)
                print("\nWindows Policy Names: " + Windows_Names_str)
                Windows_Type_str = ', '.join(Globalinfo.Windows_Policy_Types)
                print("\nWindows Policy Types: " + Windows_Type_str + "\n")
            else:
                print("No Windows Policies found.")
            
            # Print Android All Policies
            if Globalinfo.Android_All_Policies:
                print("\n============== Android Play and Non-Play (All) Policies Information ==============")
                for profile in Globalinfo.Android_All_Policies:
                    print(f"Android All Policy Type: {profile[0]}")
                    print(f"Android All Policy ID: {profile[1]}")
                    print(f"Android All Policy Name: {profile[2]}\n")
            else:
                print("No All Android Policies found.")
            
            # Access Android policies
            if Globalinfo.Android_Policies:
                print("\n====== Android Policies Information ======")
                for profile in Globalinfo.Android_Policies:
                    print(f"Android Policy Type: {profile[0]}")
                    print(f"Android Policy ID: {profile[1]}")
                    print(f"Android Policy Name: {profile[2]}\n")
            else:
                print("No Android Policies found.")
            
            # Access Android Non-Play policies
            if Globalinfo.Android_Non_Play_Policies:
                print("\n====== Android Non-Play Policies Information ======")
                for profile in Globalinfo.Android_Non_Play_Policies:
                    print(f"Android Non-Play Policy ID: {profile[0]}")
                    print(f"Android Non-Play Policy Name: {profile[1]}\n")
            else:
                print("No Android Non-Play Policies found.")
            
            # Access iOS profile IDs
            if Globalinfo.iOS_Policies:
                print("\n============== iOS Policies Information ==============")
                for profile in Globalinfo.iOS_Policies:
                    Globalinfo.iOS_Policy_IDs.append(profile[1])
                    Globalinfo.iOS_Policy_Names.append(profile[2])
                    Globalinfo.iOS_Policy_Types.append(profile[0])
                iOS_Policy_IDs_str = ', '.join(Globalinfo.iOS_Policy_IDs)
                print("\niOS Policy IDs: " + iOS_Policy_IDs_str)
                iOS_Names_str = ', '.join(Globalinfo.iOS_Policy_Names)
                print("\niOS Policy Names: " + iOS_Names_str)
                iOS_Types_str = ', '.join(Globalinfo.iOS_Policy_Types)
                print("\niOS Policy Types: " + iOS_Types_str + "\n")
            else:
                print("No iOS Policies found.")
            
            # Print stored profiles
            print("\n======== Android All Policies ========\n")
            print("\nAndroid All Policies: ", Globalinfo.Android_All_Policies, "\n")
            print("\n======== Android Policies ========", Globalinfo.Android_Policies, "\n")
            # Print the collected play policy IDs and policy names
            print("\nAndroid Policies: ", Globalinfo.Android_Policies, "\n")
            print("Android Kiosk Policy IDs:", Globalinfo.Android_Kiosk_Policy_IDs, "\n")
            print("Android Kiosk Policy Names:", Globalinfo.Android_Kiosk_Policy_Names, "\n")
            print("Android WM Policy IDs:", Globalinfo.Android_WM_Policy_IDs, "\n")
            print("Android WM Policy Names:", Globalinfo.Android_WM_Policy_Names, "\n")
            print("Android BYOD Policy IDs:", Globalinfo.Android_BYOD_Policy_IDs, "\n")
            print("Android BYOD Policy Names:", Globalinfo.Android_BYOD_Policy_Names, "\n")
            # Print the collected non-play policy IDs and policy names
            print("\n======== Android Non Play Policies ========\n")
            print("\nAndroid All Non Play Policies: ", Globalinfo.Android_Non_Play_Policies, "\n")
            print("Android Non Kiosk Policy IDs:", Globalinfo.Android_Non_Play_Kiosk_Policy_IDs, "\n")
            print("Android Non Kiosk Policy Names:", Globalinfo.Android_Non_Play_Kiosk_Policy_Names, "\n")
            print("Android Non WM Policy IDs:", Globalinfo.Android_Non_Play_WM_Policy_IDs, "\n")
            print("Android Non WM Policy Names:", Globalinfo.Android_Non_Play_WM_Policy_Names, "\n")
            print("Android Non BYOD Policy IDs:", Globalinfo.Android_Non_Play_BYOD_Policy_IDs, "\n")
            print("Android Non BYOD Policy Names:", Globalinfo.Android_Non_Play_BYOD_Policy_Names, "\n")
            print("\n======== iOS Policies ========\n", Globalinfo.iOS_Policies, "\n")
            print("\n======== Windows Policies ========\n", Globalinfo.Windows_Policies, "\n")
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
        print("------------------- GET Policy - Failed  ---------------------------\n\n")
        assert False
