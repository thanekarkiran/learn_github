import os

keywords= [ 'OutOfMemory','task supervisor timed out','clock jump','Clock-Jump','Heartbeat-Timeout','MonitorInvocationsTask delayed','BroadcastOperationControlTask delayed','Could not get JDBC Connection',
'SQLTransientConnectionException','Connection is not available','RejectedExecutionException','localhost:8761 failed to respond','Connect to localhost:8761 timed out','Java heap space']    #'Predicted','Resolving']

path = "/data/apollo/cicd/target"
fname=["apollodatamgmt.log","apolloeventmgmt.log","apollokpimgmt.log"]
fname = [os.path.join(path,f) for f in fname]
env_name = "ANESCO"
strkeys=""

for inputfile in fname:
    file1 = open(inputfile, "r")

    # read file content
    readfile = file1.read()
    found_keywords=[]

    # checking condition for string found or not
    Flag = False

    for string1 in keywords:

        if string1 in readfile:

            msg = 'Error Found: ' + string1
            found_keywords.append(msg)

            Flag= True

        else: pass


    for keys in found_keywords:

        if Flag == True :

            strkeys = strkeys +"   FILENAME ::::   "+inputfile.split("/")[-1]+"      " +keys

    file1.close()


if len(strkeys) >0:

    abc = f"echo {strkeys} | mail -r devops.alerts@heliosiot.com -s"+env_name +"\' Log Monitoring Alert' kiran.thanekar@heliosiot.com"
    os.system(abc)
