import time
import datetime
import itertools

from fritzconnection.lib.fritzwlan import FritzWLAN
from fritzconnection.core.exceptions import FritzServiceError


ADDRESS = '192.168.178.1'
PASSWORD = 'stock8433'  # should not be hardcoded for real usage

# short time periods for demonstration purposes
TRACKING_DURATION = 20
TRACKING_PERIOD = 5


def get_active_macs(fwlan):
    """
    Gets a FritzWLAN instance and returns a list of mac addresses
    from the active devices
    """
    active_macs = list()
    # iterate over all wlans:
    for n in itertools.count(1):
        fwlan.service = n
        try:
            hosts_info = fwlan.get_hosts_info()
        except FritzServiceError:
            break
        else:
            active_macs.extend(entry['mac'] for entry in hosts_info)
    return active_macs


def report_devices(fwlan):
    active_macs = get_active_macs(fwlan)
    # decide here what to do with this information:
    # print the mac addresses
    for mac in active_macs:
        print(mac)
    print()  # empty line for readability


def track_devices(tracking_duration, tracking_period):
    # instanciate FritzWLAN just once for reusage
    fwlan = FritzWLAN(address=ADDRESS, password=PASSWORD)
    stop = datetime.datetime.now() + tracking_duration
    while datetime.datetime.now() < stop:
        report_devices(fwlan)
        time.sleep(tracking_period)


def main():
    tracking_duration = datetime.timedelta(seconds=TRACKING_DURATION)
    track_devices(tracking_duration, TRACKING_PERIOD)
    print('done.')


if __name__ == '__main__':
    main()