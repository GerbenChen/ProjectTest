def print_logfile(log):
    logs = log + " : PASS"
    bandwidth = "#" * len(logs) * 2
    print (bandwidth)
    print ("#" + logs.center(len(bandwidth)-2, " ") + "#")
    print (bandwidth)