"""
Author: Sagar Patil
Purpose: Basic consumption of Cisco Meraki REST API using the 
public Cisco DevNet sandbox.
"""

import requests

# The API key is provided by DevNet in the sandbox, but may change over time. 
api_path = "https://api.meraki.com/api/v1"
header = {
        "Content": "application/json",
        "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
    }
payload = None

def get_org(resource):
    
    # GET request to get the list of organizations.
    get_resp = requests.get(f"{api_path}/{resource}", headers=header)

    # If status code >= 400, raise HTTPError
    get_resp.raise_for_status()

    # HTTP GET request succeeded, return data
    return get_resp.json()

def get_networks(resource, orgID):

    # GET /organizations/{organizationId}/networks
    get_resp = requests.get(f"{api_path}/{resource}/{orgID}/networks", headers=header)

    # networks = get_resp.json()

    # Debugging to see json response
    # import json
    # print(json.dumps(networks, indent=2))

    # Iterate through networks and print Network ID and Name
    # for network in networks:
    #     print(f"{network['id']}, Name: {network['name']}")

    return get_resp.json()

def get_ssid(networkID):
    get_ssids = requests.get(f"{api_path}/networks/{networkID}/wireless/ssids", headers=header)

    # ssids = get_ssids.json()

    # import json
    # print(json.dumps(ssids, indent=2))

    return get_ssids.json()

def main():

    orgs = get_org("organizations")

    # Interate through organizations and print if Org name is "Cisco U.", and pass Org ID to get list of networks.
    for org in orgs:
        if "Cisco U." == org['name']:
            print(f"ID: {org['id']}  Name: {org['name']}")

            # Getting a list of networks under "Cisco U." organization
            networks = get_networks("organizations", org['id'])

    # Iterate through networks and look for "Liverpool - GB" network, if found, pass network ID to get SSIDs.
    for network in networks:
        if "Liverpool - GB" in network['name']:
            ssids = get_ssid(network['id'])

    # Iterate through a list of SSIDs and print their number and name.
    for ssid in ssids:
        print(f"Number: {ssid['number']}, Name: {ssid['name']}")

if __name__ == "__main__":
    main()
