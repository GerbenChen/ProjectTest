import paramiko
import gold_flow_scenario_selenium
import requests
import datetime
import time
from datetime import timedelta
access_token = ""
server_url = ""
mobile_num = ""
#create account
for i in range(12):
    gold_flow_scenario_selenium.create_driver_account(i,mobile_num)

#check last driver account
driver_last_id = gold_flow_scenario_selenium.driver_get_last_account()
start_driver_id = str(int(driver_last_id) - 12 + 1).zfill(8)

#SSH to host
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="", username="", password="")

#date
def getday(n):
    now = datetime.date.today()
    date = now - timedelta(days=now.weekday()+n)
    return date

def ssh_exec_cmd_and_wait(cmd):
    ssh.exec_command(cmd)
    time.sleep(3)
    return
#get a week and two weeks ago sunday
week_sunday = getday(1)
last_week_sunday = getday(8)

#Using cli command to create payment bill
command =  "cd rigo && python3 cli.py -e aws-stg -c addBill -p " + "'"+ '{"driverID":"%s","period":"%s","count":11,"paytm":{"fare":"37.5","additional":"0","toll":"0","tax":"2.61"},"cash":{"fare":"375","additional":"0","toll":"0","tax":"26.1"}}'% (start_driver_id,week_sunday)+ "' " + "-f true"
ssh_exec_cmd_and_wait(command)
ssh_exec_cmd_and_wait('''cd rigo && python3 cli.py -e aws-stg -c addBill -p '{"driverID":"%s","period":"%s","count":11,"paytm":{"fare":"37.5","additional":"0","toll":"0","tax":"2.61"},"cash":{"fare":"375","additional":"0","toll":"0","tax":"26.1"},"version":"0"}' -f true''' % (str(int(start_driver_id)+1).zfill(8),week_sunday))
ssh_exec_cmd_and_wait('''cd rigo && python3 cli.py -e aws-stg -c addBill -p '{"driverID":"%s","period":"%s","count":11,"paytm":{"fare":"37.5","additional":"0","toll":"0","tax":"2.61"},"cash":{"fare":"375","additional":"0","toll":"0","tax":"26.1"},"version":"1"}' -f true''' % (str(int(start_driver_id)+2).zfill(8),week_sunday))

#POST /maintain/trigger/001/autolock
url = "/maintain/trigger/001/autolock"
method = "//div/div/ul/li[4]"
gold_flow_scenario_selenium.postman_on_web(url,method)

#check debit note to driver
ssh_exec_cmd_and_wait('''
            cd rigo && python3 cli.py -e aws-stg -c addBill -p '{"driverID":"%s","period":"%s","count":11,"paytm":{"fare":"37.5","additional":"0","toll":"0","tax":"2.61"},"cash":{"fare":"375","additional":"0","toll":"0","tax":"26.1"}}' -f true'''  % (str(int(start_driver_id)+3).zfill(8),last_week_sunday))
ssh_exec_cmd_and_wait('''
            cd rigo && python3 cli.py -e aws-stg -c addBill -p '{"driverID":"%s","period":"%s","count":11,"paytm":{"fare":"37.5","additional":"0","toll":"0","tax":"2.61"},"cash":{"fare":"375","additional":"0","toll":"0","tax":"26.1"},"version":"0"}' -f true''' % (str(int(start_driver_id)+4).zfill(8),last_week_sunday))
ssh_exec_cmd_and_wait('''
            cd rigo && python3 cli.py -e aws-stg -c addBill -p '{"driverID":"%s","period":"%s","count":11,"paytm":{"fare":"37.5","additional":"0","toll":"0","tax":"2.61"},"cash":{"fare":"375","additional":"0","toll":"0","tax":"26.1"},"version":"1"}' -f true''' % (str(int(start_driver_id)+5).zfill(8),last_week_sunday))

#POST /maintain/trigger/001/reminder1
url = "/maintain/trigger/001/reminder1"

method = "//div/div/ul/li[4]"
gold_flow_scenario_selenium.postman_on_web(url,method)
#requests.post(server_url+url)

# https://receive-sms-online.info/918727923596-India
url = "https://receive-sms-online.info/919532593533-India"
text = ""
gold_flow_scenario_selenium.check_sms_content(url,text)

# POST /maintain/trigger/001/checkPayment
url = "/maintain/trigger/001/checkPayment"
method = "//div/div/ul/li[4]"
gold_flow_scenario_selenium.postman_on_web(url,method)


#cash ICICI
ssh.exec_command('''
            python3 cli.py -e aws-stg -c addBill -p '{"driverID":"%s","period":"%s","count":11,"paytm":{"fare":"375","additional":"0","toll":"0","tax":"26.1"},"cash":{"fare":"37.5","additional":"0","toll":"0","tax":"2.61"}}' -f true'''  % (str(int(start_driver_id)+6).zfill(8),last_week_sunday))
command = "cd rigo && python3 cli.py -e aws-stg -c addBill -p " + "'" '{"driverID":"%s","period":"%s","count":11,"paytm":{"fare":"375","additional":"0","toll":"0","tax":"26.1"},"cash":{"fare":"37.5","additional":"0","toll":"0","tax":"2.61"},"version":"0"}'% (str(int(start_driver_id)+7).zfill(8),last_week_sunday) +"' " + "-f true"
ssh.exec_command(command)
ssh.exec_command('''
            cd rigo && python3 cli.py -e aws-stg -c addBill -p '{"driverID":"%s","period":"%s","count":11,"paytm":{"fare":"375","additional":"0","toll":"0","tax":"26.1"},"cash":{"fare":"37.5","additional":"0","toll":"0","tax":"2.61"},"version":"1"}' -f true''' % (str(int(start_driver_id)+8).zfill(8),last_week_sunday))

#cash NonICICI
ssh_exec_cmd_and_wait('''
            cd rigo && python3 cli.py -e aws-stg -c addBill -p '{"driverID":"%s","period":"%s","count":11,"paytm":{"fare":"375","additional":"0","toll":"0","tax":"26.1"},"cash":{"fare":"37.5","additional":"0","toll":"0","tax":"2.61"}}' -f true''' % (str(int(start_driver_id)+9).zfill(8),last_week_sunday))
ssh_exec_cmd_and_wait('''
            cd rigo && python3 cli.py -e aws-stg -c addBill -p '{"driverID":"%s","period":"%s","count":11,"paytm":{"fare":"375","additional":"0","toll":"0","tax":"26.1"},"cash":{"fare":"37.5","additional":"0","toll":"0","tax":"2.61"},"version":"0"}' -f true''' % (str(int(start_driver_id)+10).zfill(8),last_week_sunday))
ssh_exec_cmd_and_wait('''
            cd rigo && python3 cli.py -e aws-stg -c addBill -p '{"driverID":"%s","period":"%s","count":11,"paytm":{"fare":"375","additional":"0","toll":"0","tax":"26.1"},"cash":{"fare":"37.5","additional":"0","toll":"0","tax":"2.61"},"version":"1"}' -f true''' % (str(int(start_driver_id)+11).zfill(8),last_week_sunday))

#POST /maintain/trigger/001/statement
url = "/maintain/trigger/001/statement"
method = "//div/div/ul/li[4]"
gold_flow_scenario_selenium.postman_on_web(url,method)

#check bill
ssh.exec_command('''python3 cli.py -e aws-stg -c icicis -d %s -o /home/scm/rigo/ ''' %  last_week_sunday)

#bill tune

ssh_exec_cmd_and_wait('''cd rigo && python3 cli.py -e aws-stg -c icicir -p '{"period":"%s","driverID":"%s","amount" :"29.27"}' ''' % (week_sunday, str(int(start_driver_id)+5).zfill(8)))
ssh_exec_cmd_and_wait('''cd rigo && python3 cli.py -e aws-stg -c icicir -p '{"period":"%s","driverID":"%s","amount" :"310.51"}' ''' % (week_sunday, str(int(start_driver_id)+6).zfill(8)))
ssh_exec_cmd_and_wait('''cd rigo && python3 cli.py -e aws-stg -c icicir -p '{"period":"%s","driverID":"%s","amount" :"310.51"}' ''' % (week_sunday, str(int(start_driver_id)+7).zfill(8)))
ssh_exec_cmd_and_wait('''cd rigo && python3 cli.py -e aws-stg -c icicir -p '{"period":"%s","driverID":"%s","amount" :"292.65"}' ''' % (week_sunday, str(int(start_driver_id)+8).zfill(8)))
ssh_exec_cmd_and_wait('''cd rigo && python3 cli.py -e aws-stg -c icicir -p '{"period":"%s","driverID":"%s","amount" :"310.51"}' ''' % (week_sunday, str(int(start_driver_id)+9).zfill(8)))
ssh_exec_cmd_and_wait('''cd rigo && python3 cli.py -e aws-stg -c icicir -p '{"period":"%s","driverID":"%s","amount" :"310.51"}' ''' % (week_sunday, str(int(start_driver_id)+10).zfill(8)))
ssh_exec_cmd_and_wait('''cd rigo && python3 cli.py -e aws-stg -c icicir -p '{"period":"%s","driverID":"%s","amount" :"292.65"}' ''' % (week_sunday, str(int(start_driver_id)+11).zfill(8)))

#POST /maintain/trigger/001/checkPayment
url = "/maintain/trigger/001/checkPayment"
method = "//div/div/ul/li[4]"
gold_flow_scenario_selenium.postman_on_web(url,method)

#Paid or Online Paid Value No Tune to Yes

#POST /maintain/trigger/621bb10f-29d4-4ba8-8df5-be5e90efd949/dailyReminder
url = "/maintain/trigger/621bb10f-29d4-4ba8-8df5-be5e90efd949/dailyReminder"
method = "//div/div/ul/li[4]"
gold_flow_scenario_selenium.postman_on_web(url,method)

# https://receive-sms-online.info/919532593533-India
url = "https://receive-sms-online.info/919532593533-India"
text = ""
gold_flow_scenario_selenium.check_sms_content(url,text)
gold_flow_scenario_selenium.browser.quit()