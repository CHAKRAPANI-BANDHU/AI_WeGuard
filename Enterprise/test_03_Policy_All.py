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
        Globalinfo.All_Policies.append((policy_type, policy_id, policy_name))
        if policy_type in ["ANDROID_KIOSK", "ANDROID_WM", "ANDROID_BYOD"]:
            Globalinfo.Android_Policies.append((policy_type, policy_id, policy_name))
        elif policy_type in ["ANDROID_NON_PLAY_KIOSK", "ANDROID_NON_PLAY_WM", "ANDROID_NON_PLAY_BYOD"]:
            Globalinfo.Android_Non_Play_Policies.append((policy_type, policy_id, policy_name))
        if policy_type == "ANDROID_KIOSK":
            Globalinfo.Android_Kiosk_Policies.append((policy_type, policy_id, policy_name))
        elif policy_type == "ANDROID_WM":
            Globalinfo.Android_WM_Policies.append((policy_type, policy_id, policy_name))
        elif policy_type == "ANDROID_BYOD":
            Globalinfo.Android_BYOD_Policies.append((policy_type, policy_id, policy_name))
        elif policy_type == "ANDROID_NON_PLAY_KIOSK":
            Globalinfo.Android_Non_Play_Kiosk_Policies.append((policy_type, policy_id, policy_name))
        elif policy_type == "ANDROID_NON_PLAY_WM":
            Globalinfo.Android_Non_Play_WM_Policies.append((policy_type, policy_id, policy_name))
        elif policy_type == "ANDROID_NON_PLAY_BYOD":
            Globalinfo.Android_Non_Play_BYOD_Policies.append((policy_type, policy_id, policy_name))
    elif platform == "IOS":
        Globalinfo.iOS_Policies.append((policy_type, policy_id, policy_name))
    elif platform == "WINDOWS":
        Globalinfo.Windows_Policies.append((policy_type, policy_id, policy_name))
    else:
        print(f"Invalid platform: {platform}")


# Define the test function
@pytest.mark.parametrize('Page, Size', [(p, s) for p in Globalinfo.page for s in Globalinfo.pageSize])
@pytest.mark.skipif(Execute.test_tc_3000_Policy_All == 0, reason="test skipped")
@pytest.mark.usualtest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.positivetest
@pytest.mark.run(order=400000)
def test_tc_4000_Policy_ALL(Page, Size):
    if Size in [500, 100]:
        pytest.skip(f"Skipping test for pageSize {Size}")
        now1 = datetime.now()
    if Globalinfo.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = Globalinfo.BaseURL + AllPolicy(Page, Size)
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
            
            # Iterate through policy data and store profiles
            for profile in json_response.get('list', []):
                platform = profile.get('platform')
                profile_type = profile.get('type')
                profile_id = profile.get('id')
                profile_name = profile.get('name')
                store_profiles(platform, profile_type, profile_id, profile_name)
            
            # Print stored profiles
            print("\n============================ All Platform Policies Information ============================\n")
            print("\nAll Android, iOS, Windows Policies: ", Globalinfo.All_Policies, "\n")
            print("\nAll Android Play Policies: ", Globalinfo.Android_Policies, "\n")
            print("\nAll Android Non Play Policies: ", Globalinfo.Android_Non_Play_Policies, "\n")
            print("\niOS Policies: ", Globalinfo.iOS_Policies, "\n")
            print("\nWindows Policies: ", Globalinfo.Windows_Policies, "\n")
            
            # Extracted Policy Information from the API Response
            print(
                "\n============================ Extracted Policy Information from the API Response ============================\n")
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
            
            # Print Android All Policies
            if Globalinfo.All_Policies:
                print("\n============== All Platform (Android, iOS, Windows) Policies Information ==============")
                for profile in Globalinfo.All_Policies:
                    Globalinfo.All_Policy_Types.append(profile[0])
                    Globalinfo.All_Policy_IDs.append(profile[1])
                    Globalinfo.All_Policy_Names.append(profile[2])
                print(f"All Android Policy Types: {Globalinfo.All_Policy_Types}\n")
                print(f"All Android Policy IDs: {Globalinfo.All_Policy_IDs}\n")
                print(f"All Android Policy Name: {Globalinfo.All_Policy_Names}\n")
            else:
                print("No All Policies found.")
            
            print("\n============== Android Play and Non-Play (All) Policies Information ==============")
            # Access Android Play policies
            if Globalinfo.Android_Policies:
                print("\n====== Android Play Policies Information ======")
                for profile in Globalinfo.Android_Policies:
                    Globalinfo.Android_Policy_Types.append(profile[0])
                    Globalinfo.Android_Policy_IDs.append(profile[1])
                    Globalinfo.Android_Policy_Names.append(profile[2])
                print(f"Android Policy Types: {Globalinfo.Android_Policy_Types}\n")
                print(f"Android Policy IDs: {Globalinfo.Android_Policy_IDs}\n")
                print(f"Android Policy Names: {Globalinfo.Android_Policy_Names}\n")
            else:
                print("No Android Play Policies found.")
            
            # Access Android Non-Play policies
            if Globalinfo.Android_Non_Play_Policies:
                print("\n====== Android Non-Play Policies Information ======")
                for profile in Globalinfo.Android_Non_Play_Policies:
                    Globalinfo.Android_Non_Play_Policy_Types.append(profile[0])
                    Globalinfo.Android_Non_Play_Policy_IDs.append(profile[1])
                    Globalinfo.Android_Non_Play_Policy_Names.append(profile[2])
                print(f"Android Non-Play Policy Types: {Globalinfo.Android_Non_Play_Policy_Types}\n")
                print(f"Android Non-Play Policy IDs: {Globalinfo.Android_Non_Play_Policy_IDs}\n")
                print(f"Android Non-Play Policy Names: {Globalinfo.Android_Non_Play_Policy_Names}\n")
            else:
                print("No Android Non-Play Policies found.")
            
            Globalinfo.AndroidPlayNonPlayPolicyIDs = Globalinfo.Android_Policy_IDs + Globalinfo.Android_Non_Play_Policy_IDs
            print("\nAndroid Play and Non Play Policy IDs: " + str(Globalinfo.AndroidPlayNonPlayPolicyIDs), "\n")
            
            # Print KIOSK policies
            if Globalinfo.Android_Kiosk_Policies:
                print("\n======== Android KIOSK Policies ========\n")
                android_kiosk_policy_types = [profile[0] for profile in Globalinfo.Android_Kiosk_Policies]
                android_kiosk_policy_ids = [profile[1] for profile in Globalinfo.Android_Kiosk_Policies]
                android_kiosk_policy_names = [profile[2] for profile in Globalinfo.Android_Kiosk_Policies]
                print("Android KIOSK Policy Types: ", android_kiosk_policy_types)
                print("Android KIOSK Policy IDs: ", android_kiosk_policy_ids)
                print("Android KIOSK Policy Names: ", android_kiosk_policy_names)
            else:
                print("No Android KIOSK Policies found.")
            
            # Print WM policies
            if Globalinfo.Android_WM_Policies:
                print("\n======== Android WM Policies ========\n")
                android_wm_policy_types = [profile[0] for profile in Globalinfo.Android_WM_Policies]
                android_wm_policy_ids = [profile[1] for profile in Globalinfo.Android_WM_Policies]
                android_wm_policy_names = [profile[2] for profile in Globalinfo.Android_WM_Policies]
                print("Android WM Policy Types: ", android_wm_policy_types)
                print("Android WM Policy IDs: ", android_wm_policy_ids)
                print("Android WM Policy Names: ", android_wm_policy_names)
            else:
                print("No Android WM Policies found.")
            
            # Print BYOD policies
            if Globalinfo.Android_BYOD_Policies:
                print("\n======== Android BYOD Policies ========\n")
                android_byod_policy_types = [profile[0] for profile in Globalinfo.Android_BYOD_Policies]
                android_byod_policy_ids = [profile[1] for profile in Globalinfo.Android_BYOD_Policies]
                android_byod_policy_names = [profile[2] for profile in Globalinfo.Android_BYOD_Policies]
                print("Android BYOD Policy Types: ", android_byod_policy_types)
                print("Android BYOD Policy IDs: ", android_byod_policy_ids)
                print("Android BYOD Policy Names: ", android_byod_policy_names)
            else:
                print("No Android BYOD Policies found.")
            
            # Print Non-Play KIOSK policies
            if Globalinfo.Android_Non_Play_Kiosk_Policies:
                print("\n======== Android Non-Play KIOSK Policies ========\n")
                android_non_play_kiosk_policy_types = [profile[0] for profile in
                                                       Globalinfo.Android_Non_Play_Kiosk_Policies]
                android_non_play_kiosk_policy_ids = [profile[1] for profile in
                                                     Globalinfo.Android_Non_Play_Kiosk_Policies]
                android_non_play_kiosk_policy_names = [profile[2] for profile in
                                                       Globalinfo.Android_Non_Play_Kiosk_Policies]
                print("Android Non-Play KIOSK Policy Types: ", android_non_play_kiosk_policy_types)
                print("Android Non-Play KIOSK Policy IDs: ", android_non_play_kiosk_policy_ids)
                print("Android Non-Play KIOSK Policy Names: ", android_non_play_kiosk_policy_names)
            else:
                print("No Android Non-Play KIOSK Policies found.")
            
            # Print Non-Play WM policies
            if Globalinfo.Android_Non_Play_WM_Policies:
                print("\n======== Android Non-Play WM Policies ========\n")
                android_non_play_wm_policy_types = [profile[0] for profile in Globalinfo.Android_Non_Play_WM_Policies]
                android_non_play_wm_policy_ids = [profile[1] for profile in Globalinfo.Android_Non_Play_WM_Policies]
                android_non_play_wm_policy_names = [profile[2] for profile in Globalinfo.Android_Non_Play_WM_Policies]
                print("Android Non-Play WM Policy Types: ", android_non_play_wm_policy_types)
                print("Android Non-Play WM Policy IDs: ", android_non_play_wm_policy_ids)
                print("Android Non-Play WM Policy Names: ", android_non_play_wm_policy_names)
            else:
                print("No Android Non-Play WM Policies found.")
            
            # Print Non-Play BYOD policies
            if Globalinfo.Android_Non_Play_BYOD_Policies:
                print("\n======== Android Non-Play BYOD Policies ========\n")
                android_non_play_byod_policy_types = [profile[0] for profile in
                                                      Globalinfo.Android_Non_Play_BYOD_Policies]
                android_non_play_byod_policy_ids = [profile[1] for profile in Globalinfo.Android_Non_Play_BYOD_Policies]
                android_non_play_byod_policy_names = [profile[2] for profile in
                                                      Globalinfo.Android_Non_Play_BYOD_Policies]
                print("Android Non-Play WM Policy Types: ", android_non_play_byod_policy_types)
                print("Android Non-Play BYOD Policy IDs: ", android_non_play_byod_policy_ids)
                print("Android Non-Play BYOD Policy Names: ", android_non_play_byod_policy_names)
            else:
                print("No Android Non-Play BYOD Policies found.")
            
            # Print All Platform (Android, iOS, Windows) Policy IDs
            Globalinfo.AllPlatformPolicyIDs = Globalinfo.AndroidPlayNonPlayPolicyIDs + Globalinfo.iOS_Policy_IDs + Globalinfo.Windows_Policy_IDs
            print("\nAll Platform (Android, iOS, Windows) Policy IDs : " + str(Globalinfo.AllPlatformPolicyIDs) + "\n")
        
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
