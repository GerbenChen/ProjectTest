import rigo_selenium_support
from uiautomator import Device
import time
import logging
logging.basicConfig(level=logging.INFO)
#set devices SN

device_app = Device("emulator-5554")
device_meter = Device("0123456789ABCDEF")
device_app_1 = Device("emulator-5556")
share_name = ""
passenger_id = ""


def from_call_to_cancel():
    #device_app(text="RigoTaxi (Staging)").click.wait()
    #logging.info('Click RigoTaxi (Staging)')
    device_app(text="RiGO NOW").click.wait()
    logging.info('Click RiGO NOW')
    device_app(text="CONFIRM ORDER").click.wait()
    logging.info('CONFIRM ORDER')
    device_meter(text="hhsqatest001").click.wait()
    logging.info('Check Passenger')
    device_meter(text="3 Mins").click.wait()
    logging.info('Check arrived after how many time')
    device_meter(text="Arrival").click.wait()
    logging.info('Meter Arrived')
    device_app(text="OK").click.wait()
    logging.info('APP Click OK')
    device_meter(text="Hired").click.wait()
    logging.info('Start')
    device_meter(text="Stop").click.wait()
    logging.info('Stop')
    device_meter(text="Vacant").click.wait()
    logging.info('Cancel')
    device_meter(text="Yes").click.wait()
    logging.info('Double Check Cancel')

def from_call_to_print_cash():
    device_app(text="RiGO").click.wait()
    logging.info('Click RiGO')
    device_app(text="RiGO NOW").click.wait()
    logging.info('Click RiGO NOW')
    device_app(text="CONFIRM ORDER").click.wait()
    logging.info('CONFIRM ORDER')
    device_meter(text="sqa hh").click.wait()
    logging.info('Check Passenger')
    device_meter(text="3 Mins").click.wait()
    logging.info('Check arrived after how many time')
    device_meter(text="Arrival").click.wait()
    logging.info('Meter Arrived')
    device_app(text="OK").click.wait()
    logging.info('APP Click OK')
    device_meter(text="Hired").click.wait()
    logging.info('Start')
    device_meter(text="Stop").click.wait()
    logging.info('Stop')
    device_meter(text="Print").click.wait()
    logging.info('Print')
    device_meter(text="Cash").click.wait()
    logging.info('Pay For Cash')


def from_call_to_print_vacant():
    device_app(text="RiGO").click.wait()
    logging.info('Click RiGO')
    device_app(text="RiGO NOW").click.wait()
    logging.info('Click RiGO NOW')
    device_app(text="CONFIRM ORDER").click.wait()
    logging.info('CONFIRM ORDER')
    device_meter(text="sqa hh").click.wait()
    logging.info('Check Passenger')
    device_meter(text="3 Mins").click.wait()
    logging.info('Check arrived after how many time')
    device_meter(text="Arrival").click.wait()
    logging.info('Meter Arrived')
    device_app(text="OK").click.wait()
    logging.info('APP Click OK')
    device_meter(text="Hired").click.wait()
    logging.info('Start')
    device_meter(text="Stop").click.wait()
    logging.info('Stop')
    device_meter(text="Vacant").click.wait()
    logging.info('Vacant')
    device_meter(text="Yes").click.wait()
    logging.info('Yes')

def from_call_to_passenger_sos():
    device_app(text="RiGO").click.wait()
    logging.info('Click RiGO')
    device_app(text="RiGO NOW").click.wait()
    logging.info('Click RiGO NOW')
    device_app(text="CONFIRM ORDER").click.wait()
    logging.info('CONFIRM ORDER')
    device_meter(text="sqa hh").click.wait()
    logging.info('Check Passenger')
    device_meter(text="3 Mins").click.wait()
    logging.info('Check arrived after how many time')
    device_meter(text="Arrival").click.wait()
    logging.info('Meter Arrived')
    device_app(text="OK").click.wait()
    logging.info('APP Click OK')
    device_meter(text="Hired").click.wait()
    logging.info('Start')
    device_app(text="SOS").click.wait()
    logging.info('SOS')
    device_app(text="Sky Eyes").click.wait()
    logging.info('Sky Eyes')
    device_app(text="Yes").click.wait()
    logging.info('Yes')
    device_meter(text="Stop").click.wait()
    logging.info('Stop')
    device_meter(text="Vacant").click.wait()
    logging.info('Vacant')
    device_meter(text="Yes").click.wait()
    logging.info('Yes')

def from_call_to_share_info():
    device_app(text="RiGO").click.wait()
    logging.info('Click RiGO')
    device_app(text="RiGO NOW").click.wait()
    logging.info('Click RiGO NOW')
    device_app(text="CONFIRM ORDER").click.wait()
    logging.info('CONFIRM ORDER')
    device_meter(text="sqa hh").click.wait()
    logging.info('Check Passenger')
    device_meter(text="3 Mins").click.wait()
    logging.info('Check arrived after how many time')
    device_meter(text="Arrival").click.wait()
    logging.info('Meter Arrived')
    device_app(text="OK").click.wait()
    logging.info('APP Click OK')
    device_meter(text="Hired").click.wait()
    logging.info('Start')
    device_app(text="Share Info.").click.wait()
    logging.info('Share Info.')
    device_app(text="%s" % share_name).click.wait()
    logging.info('%s' % share_name)
    device_app(text="Send").click.wait()
    logging.info('Send')
    device_app_1(text="Yes").click.wait()
    logging.info('Yes')
    device_meter(text="Stop").click.wait()
    logging.info('Stop')
    device_meter(text="Vacant").click.wait()
    logging.info('Vacant')
    device_meter(text="Yes").click.wait()
    logging.info('Yes')

def from_call_to_check_sos_video():
    device_app(text="RiGO").click.wait()
    logging.info('Click RiGO')
    device_app(text="RiGO NOW").click.wait()
    logging.info('Click RiGO NOW')
    device_app(text="CONFIRM ORDER").click.wait()
    logging.info('CONFIRM ORDER')
    device_meter(text="sqa hh").click.wait()
    logging.info('Check Passenger')
    device_meter(text="3 Mins").click.wait()
    logging.info('Check arrived after how many time')
    device_meter(text="Arrival").click.wait()
    logging.info('Meter Arrived')
    device_app(text="OK").click.wait()
    logging.info('APP Click OK')
    device_meter(text="Hired").click.wait()
    logging.info('Start')
    device_app(text="Share Info.").click.wait()
    logging.info('Share Info.')
    device_app(text="%s" % share_name).click.wait()
    logging.info('%s' % share_name)
    device_app(text="Send").click.wait()
    logging.info('Send')
    device_app_1(text="Yes").click.wait()
    logging.info('Yes')
    device_meter(text="Stop").click.wait()
    logging.info('Stop')
    device_meter(text="Vacant").click.wait()
    logging.info('Vacant')
    device_meter(text="Yes").click.wait()
    logging.info('Yes')

