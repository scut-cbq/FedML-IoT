import csv
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), "./")))
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), "../")))
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), "../../")))
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), "../../../")))
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), "../../../../")))

def build_ip_table(path):
    ip_config = dict()
    os.chdir(os.getcwd()[0:os.getcwd().find('FedML-IoT')+9])
    with open(path, newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        # skip header line
        next(csv_reader)

        for row in csv_reader:
            receiver_id, receiver_ip = row
            ip_config[receiver_id] = receiver_ip
    return ip_config
