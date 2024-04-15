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

def get_org(resource):
    
    # GET request to get the list of organizations.
    get_resp = requests.get(f"{api_path}/{resource}", headers=header)

    # If status code >= 400, raise HTTPError
    get_resp.raise_for_status()

    # HTTP GET request succeeded, return data
    return get_resp.json()

def create_org(resource):

    # Payload data to create new organization.
    payload = {
        "name": "Test1000 Organization"
    }

    # POST request to create new organization.
    post_resp = requests.post(f"{api_path}/{resource}", headers=header, data=payload)

    # If status code >= 400, raise HTTPError
    post_resp.raise_for_status()

    return post_resp.json()

def main():
    orgs = get_org("organizations")
    for org in orgs:
        print(f"ID: {org['id']}  Name: {org['name']}")

    create_org("organizations")

    print("New Organization Created")

    orgs = get_org("organizations")
    for org in orgs:
        if org['name'] == "Test1000 Organization":
            print(f"ID: {org['id']}  Name: {org['name']}")


if __name__ == "__main__":
    main()
