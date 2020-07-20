import requests
from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.apis import http_method


def snmpconf(task, chained_url, headers):
    restconf_url = f"https://{task.host.hostname}/restconf/"

    task.run(
        task=http_method,
        name="RESTCONF PUT_POST",
        method="put",
        url=restconf_url + chained_url,
        auth=("john", "cisco"),
        headers=headers["put_post"],
        verify=False,
        json=task.host["snmp_configure"]
)

def bgpconf(task, chained_url, headers):
    restconf_url = f"https://{task.host.hostname}/restconf/"

    task.run(
        task=http_method,
        name="RESTCONF PUT_POST",
        method="put",
        url=restconf_url + chained_url,
        auth=("john", "cisco"),
        headers=headers["put_post"],
        verify=False,
        json=task.host["bgp_configure"]
)

def ntpconf(task, chained_url, headers):
    restconf_url = f"https://{task.host.hostname}/restconf/"

    task.run(
        task=http_method,
        name="RESTCONF PUT_POST",
        method="put",
        url=restconf_url + chained_url,
        auth=("john", "cisco"),
        headers=headers["put_post"],
        verify=False,
        json=task.host["ntp_configure"]
)

def bannerconf(task, chained_url, headers):
    restconf_url = f"https://{task.host.hostname}/restconf/"

    task.run(
        task=http_method,
        name="RESTCONF PUT_POST",
        method="put",
        url=restconf_url + chained_url,
        auth=("john", "cisco"),
        headers=headers["put_post"],
        verify=False,
        json=task.host["banner_configure"]
)

def main():
    requests.packages.urllib3.disable_warnings()

    snmp_url = "data/Cisco-IOS-XE-native:native/Cisco-IOS-XE-native:snmp-server"
    router_url = "data/Cisco-IOS-XE-native:native/Cisco-IOS-XE-native:router"
    ntp_url = "data/Cisco-IOS-XE-native:native/Cisco-IOS-XE-native:ntp"
    banner_url = "data/Cisco-IOS-XE-native:native/Cisco-IOS-XE-native:banner"
    headers = {
        "get": {"Accept": "application/yang-data+json"},
        "put_post": {
            "Content-Type": "application/yang-data+json",
            "Accept": "application/yang-data+json, application/yang-data.errors+json",
        },
    }

    nr = InitNornir()
    snmp_result = nr.run(task=snmpconf,name="PUSHING SNMP VIA RESTCONF",chained_url=snmp_url,headers=headers,)
    bgp_result = nr.run(task=bgpconf,name="PUSHING BGP VIA RESTCONF",chained_url=router_url,headers=headers,)
    ntp_result = nr.run(task=ntpconf,name="PUSHING NTP VIA RESTCONF",chained_url=ntp_url,headers=headers,)
    banner_result = nr.run(task=bannerconf,name="PUSHING BANNER VIA RESTCONF",chained_url=banner_url,headers=headers,)

    print_result(snmp_result)
    print_result(bgp_result)
    print_result(ntp_result)
    print_result(banner_result)

if __name__ == "__main__":
    main()
