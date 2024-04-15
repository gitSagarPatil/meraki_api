"""
Author: Sagar Patil
Purpose: Basic consumption of Cisco Meraki REST API using the 
public Cisco DevNet sandbox.
"""

import requests


def meraki_get(resource):
    
    # The API key is provided by DevNet in the sandbox, but may change over time. 
    api_path = "https://api.meraki.com/api/v1"
    header = {
        "Content": "application/json",
        "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
    }

    get_resp = requests.get(f"{api_path}/{resource}", headers=header)

    # If status code >= 400, raise HTTPError
    get_resp.raise_for_status()

    # HTTP GET request succeeded, return data
    return get_resp.json()

def main():

    # Get the list of organizations from the sandbox
    # {api_path}/organizations
    orgs = meraki_get("organizations")
    print("Organizations discovered:")

    # Debugging line, pretty-print JSON to see structure
    # import json
    # print(json.dumps(orgs, indent=2))

    # Iterate over each org. It prints out each discovered organizations, 
    # but also performs a linear search for the Devnet ID.
    devnet_id = 0
    for org in orgs:
        print(f"ID: {org['id']}  Name: {org['name']}")
        if "devnet" in org['name'].lower():
            devnet_id = org['id']

    
    if devnet_id:
        networks = meraki_get(f"organizations/{devnet_id}/networks")

        print(f"\nNetworks seen for the DevNet org ID {devnet_id}:")

        devnet_network = ""
        for network in networks:
            print(f"Network ID: {network['id']}  Name: {network['name']}")
            if "devnet" in network["name"].lower():
                devnet_network = network["id"]

        # If we found the DevNet network ...
        if devnet_network:
            # Get the devices from the DevNet network
            # GET /networks/{networkID}/devices
            devices = meraki_get(f"networks/{devnet_network}/devices")

            # Debugging line
            # import json
            # print(json.dumps(devices, indent=2))

            # Print out the networks along with their network IDs
            print(f"\nDevices seen on DevNet network {devnet_network}:")

            # Print the hardware model and LAN-side IP address
            for device in devices:
                print(f"Model: {device['model']} IP: {device['lanIp']}")

if __name__ == "__main__":
    main()
