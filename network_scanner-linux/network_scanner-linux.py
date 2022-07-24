# created by Mehmet Deniz Ozkahraman

import scapy.all as scapy
import optparse
import subprocess
import re


def option_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--ipaddress", dest="ip_address", help="ip address to scan!")

    (user_input, args) = parse_object.parse_args()

    if not user_input.ip_address:
        print("Enter IP address!!")

    return user_input


def network_scanner(user_input):
    arp_request = scapy.ARP(pdst=user_input)

    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    combined_packet = broadcast_packet / arp_request

    (answered_list, unanswered_list) = scapy.srp(combined_packet, timeout=1)

    answered_list.summary()


print("""
by mdo //-


            _                      _                                                 _ _                  
 _ __   ___| |___      _____  _ __| | __    ___  ___ __ _ _ __  _ __   ___ _ __     | (_)_ __  _   ___  __
| '_ \ / _ \ __\ \ /\ / / _ \| '__| |/ /   / __|/ __/ _` | '_ \| '_ \ / _ \ '__|____| | | '_ \| | | \ \/ /
| | | |  __/ |_ \ V  V / (_) | |  |   <    \__ \ (_| (_| | | | | | | |  __/ | |_____| | | | | | |_| |>  < 
|_| |_|\___|\__| \_/\_/ \___/|_|  |_|\_\___|___/\___\__,_|_| |_|_| |_|\___|_|       |_|_|_| |_|\__,_/_/\_\  
                                      |_____|                                                             

""")

user_ip_address = option_input()

network_scanner(user_ip_address.ip_address)







