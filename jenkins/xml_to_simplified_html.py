import matplotlib.pyplot as plotter
import glob
import xml.etree.ElementTree as et
import re
import os
import sys
import getopt
import pandas as pd
import datetime

report_name = '../reports/simplified_html.html'
reports_path = '../reports'

try:
    args, values = getopt.getopt(sys.argv[1:], 'n:r:', ['report_name', 'reports_path'])
    for key, value in args:
        if key in ("-n", "--report_name"):
            print("Report name argv " + str(value))
            report_name = str(value)
        elif key in ("-r", "--reports_path"):
            print("xml Reports path argv " + str(value))
            reports_path = str(value)
except getopt.error as err:
    print(str(err))

print("Report Name is: " + str(report_name))
print("XML Reports Path is: " + str(reports_path))


def deduce_reason(message):
    if str(message).__contains__("Browser Console Debug Logs"):
        return ",Error in Browser Console"
    elif str(message).__contains__("Element name with value"):
        return ",Element not found"
    else:
        return ""


def find_known_issue(testname, xmlpath):
    try:
        file1 = open(xmlpath, "r")
        readfile = file1.read()
        testid = re.findall(testname + '::\d+', readfile)
        if len(testid) > 0:
            testid = int(testid[0].replace(testname + '::', ''))
        else:
            testid = 0
        known_failures = os.path.join(os.environ["PYTHONPATH"], "jenkins", "known_failures.csv")
        df = pd.read_csv(known_failures)  # skiprows = [1
        comment = ""
        for index, row in df.iterrows():
            if row[0] == testid:
                comment = row[1]
                break  # break with the first reason itself.
        return comment
    except Exception as z:
        return ""


def reg_find_id(input):
    testid = re.findall(r'-?\\-?\d+\.?\d*', input)
    if len(testid) > 0:
        testid = testid[0]
    else:
        testid = 0
    return testid


def find_between(start, end, filepath=None, data=None):
    try:
        startindex = -1
        endindex = -1
        readfile = ""
        if filepath is None:
            readfile = data
        else:
            file1 = open(filepath, "r")
            readfile = file1.read()
        startindex = readfile.index(start) + len(start)
        print("startindex:" + str(startindex))
        if startindex != -1:
            endindex = readfile.index(end, startindex)
            print("endindex:" + str(endindex))
        if endindex != -1:
            return readfile[startindex:endindex]
        else:
            return ""
    except Exception as z:
        return ""

passed_table = \
    "<b><u>Passed</u></b><table style='border:1px solid black;width: 100%;border-collapse: collapse;'><tr>" \
    "<th style='border:1px solid black;'>Module</th><th style='border:1px solid black;'>Unit Test</th>" \
    "<th style='border:1px solid black;'>Status</th></tr>"

failed_table = \
    "<b><u>Failed</u></b><table style='border:1px solid black;width: 100%;border-collapse: collapse;'><tr>" \
    "<th style='border:1px solid black;'>Module</th><th style='border:1px solid black;'>Failed Unit Test</th>" \
    "<th style='border:1px solid black;'>Status</th><th style='border:1px solid black;'>Comments</th>" \
    "<th style='border:1px solid black;'>Author</th></tr>"

single_table =\
    "<table style='width: 100%;border-collapse: collapse;'>" \
    "<tr style='background: #E6E6FA;font-family: sans-serif;'><th style='border:1px solid #ccc;'>Module</th>" \
    "<th style='border:1px solid #ccc;'>Unit Test</th><th style='border:1px solid #ccc;'>Status</th>" \
    "<th style='border:1px solid #ccc;'>Comments</th><th style='border:1px solid #ccc;'>POC</th></tr>"


try:
    total_cases = 0
    failed = 0
    skipped = 0
    executiontime = 0
    xmlpaths = glob.glob(os.path.join(reports_path, "*.xml"))
    for xmlpath in xmlpaths:
        tree = et.parse(xmlpath)
        for testsuite in tree.getroot().findall("testsuite"):
            for x in testsuite.attrib:
                if x == "errors" or x == "failures":
                    failed = int(failed) + int(testsuite.attrib[x])
                elif x == "tests":
                    total_cases = int(total_cases) + int(testsuite.attrib[x])
                elif x == "skipped":
                    skipped = int(skipped) + int(testsuite.attrib[x])
                elif x == "time":
                    executiontime = float(executiontime) + float(testsuite.attrib[x])
            for y in testsuite.findall('testcase'):
                testfailed = False
                for z in y.findall('failure'):
                    testfailed = True
                    #info_line = find_between("*** " + str(y.attrib['name']), "***", filepath=xmlpath)
                    info_line = ""
                    #print("info line: " + info_line)
                    #print(find_between("::author::", "::", data=info_line))
                    single_table = single_table + \
                    "<tr>" \
                    "<td style='border:1px solid #ccc;'>" + str(y.attrib['classname']) + "</td>" \
                    "<td style='border:1px solid #ccc;'>" + str(y.attrib['name']) + "</td>" \
                    "<td style='border:1px solid #ccc; color:#ff0000;'> Failed </td>" \
                    "<td style='border:1px solid #ccc;'>"
                    #temp = find_known_issue(str(y.attrib['name']), xmlpath)
                    temp = ""
                    strtemp = ""
                    if len(temp) > 0:
                        strtemp = strtemp + "Bug id:"
                        temp = temp.replace(",", "")
                        bugs = temp.split()
                        for i in range(2, len(bugs)):
                            strtemp = strtemp + " " + '<a href="https://cyware.atlassian.net/browse/' + bugs[i] + '" target="_blank">' + bugs[i] + "</a>"

                    single_table = single_table + \
                    strtemp + deduce_reason("") + "</td>" \
                    "<td style='border:1px solid #ccc;'>" + find_between("::author::", "::", data=info_line) + "</td>" \
                    "</tr>"
                    print("Test Suite:" + str(y.attrib['classname']) + " - Failed Test: " + str(y.attrib['name']))
                    # print(str(z.attrib['type']))
                if not testfailed:
                    single_table = single_table + \
                    "<tr>" \
                    "<td style='border:1px solid #ccc;'>" + str(y.attrib['classname']) + "</td>" \
                    "<td style='border:1px solid #ccc;'>" + str(y.attrib['name']) + "</td>" \
                    "<td style='border:1px solid #ccc; color:#008000;'> Passed </td>" \
                    "<td style='border:1px solid #ccc;'></td>" \
                    "<td style='border:1px solid #ccc;'></td>" \
                    "</tr>"
                    print("Test Suite:" + str(y.attrib['classname']) + " - Passed Test: " + str(y.attrib['name']))
    #ofailed_table = failed_table + "</table>"
    #opassed_table = passed_table + "</table><br>"
    single_table = single_table + "</table><br>"
    # print(failed)
    # print(total_cases)
    # print(executiontime)
    pieLabels = 'Pass', 'Fail', 'Skipped'
    populationShare = [total_cases - failed - skipped, failed, skipped]
    figureObject, axesObject = plotter.subplots()
    axesObject.pie(populationShare, labels=pieLabels, autopct='%1.2f', startangle=90)
    axesObject.axis('equal')
    plotter.savefig(os.path.join(reports_path, "results.png"))
    # Write html report file
    with open(report_name, "wb+") as writer:
        writer.write(('<b>Date: </b> ' + str(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')) + "<br>").encode())
        writer.write(('<b>Execution Time:</b> ' + str(int(executiontime)) + " sec <br>").encode())
        writer.write(('<b>Total Cases:</b> ' + str(total_cases) + "<br>").encode())
        writer.write(('<b>Passed:</b> ' + str(total_cases - failed - skipped) + "<br>").encode())
        writer.write(('<b>Skipped:</b> ' + str(skipped) + "<br>").encode())
        writer.write(('<b>Failed:</b> ' + str(failed) + "<br><br>").encode())
        #writer.write(emailcontent.encode())
        writer.write(single_table.encode())
        #writer.write(passed_table.encode())
        #if failed > 0:
        #    writer.write(failed_table.encode())
except Exception as e:
    print("Error: Some issue occurred while preparing email report, details:" + str(e))