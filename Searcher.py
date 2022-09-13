# This program is used to search trough a list of IPv4 static adresses and
# IPv4 subnets and compare them to a list of Static adresses and subnets and
# print a list of the adresses it finds that are found to match.

# Imports
from copyreg import constructor
import ipaddress
import time
import progressbar
from tqdm import tqdm
from alive_progress import alive_bar


# Defintions
StaticBlockList = 'blocked-static.txt'
SubnetBlockList = 'blocked-subnets.txt'
CheckList = 'checkme.txt'
OutputFile = 'output.txt'

# Clear the output file
with open(OutputFile, 'a') as f:
    f.truncate(0)


# Check the CheckList for any static that are in the StaticBlockList
checkData = open(CheckList, 'r')
staticAdressesInChecklist = []
subnetsInCheckList = []
for line in checkData:
    if '/' not in line:
        # Remove the newline character from the end of the line before appending it to the list
        data = line.replace('\n', '')
        staticAdressesInChecklist.append(data)
    else:
        data = line.replace('\n', '')
        subnetsInCheckList.append(data)

# print('Static adresses found in CheckList: ' + str(staticAdressesInChecklist))

# For each static adress found in the CheckList, check if it is in the StaticBlockList
# Checks all static adreses in CheckList against StaticBlockList
for static in staticAdressesInChecklist:
    staticData = open(StaticBlockList, 'r')
    for line in staticData:
        if static in line:
            # Write the static adress to the output file
            output = open(OutputFile, 'a')
            output.write(static+'\n')
            output.close()

# print('Subnet adresses found in CheckList: ' + str(subnetsInCheckList))
# Checks all ip subnets in CheckList against SubnetBlockList
for subnet in subnetsInCheckList:
    subnetData = open(SubnetBlockList, 'r')
    for line in subnetData:
        if subnet in line:
            # Write the subnet to the output file
            output = open(OutputFile, 'a')
            output.write(subnet+'\n')
            output.close()


def getIpRange(ip, size):
    return [str(ip) for ip in ipaddress.IPv4Network(str(ip) + '/' + str(size), False)]


def getClassA(ip):
    return ip.split('.')[0]+'.'+ip.split('.')[1]+'.'+ip.split('.')[2]


# Check the CheckList for any subnets that include static adresses in the StaticBlockList
classA = []
staticIpsFromCheckListSubnets = []
with alive_bar(len(subnetsInCheckList), title='Calculating Subnet Class A\'s', dual_line=True) as bar:
    for subnet in subnetsInCheckList:
        subnetIp = subnet.split('/')[0]
        subnetSize = subnet.split('/')[1]
        subnetRange = getIpRange(subnetIp, int(subnetSize))
        # Split subnet by '.' and get the last octet
        data = getIpRange(subnetIp, int(subnetSize))
        for ip in data:
            value = getClassA(ip)
            # bar.text = f'\n-> Checking Class A: {value}, please wait...'
            if value not in classA:
                # print('Class A found in SubnetBlockList: ' + str(value))
                classA.append(value)
        bar()


staticIpBlockList = open(StaticBlockList, 'r')
# Create array from lines in StaticBlockList
staticIpBlockArray = []
twoIps = []
for ip in staticIpBlockList:
    staticIpBlockArray.append(ip)
with alive_bar(len(staticIpBlockArray), title='Checking Static Ips', dual_line=True) as bar2:
    for ip in staticIpBlockArray:
        # bar2.text = f'\n-> Checking Static Ips: {ip}, please wait...'
        # Check if the class A of the ip is within the list of class As
        if getClassA(ip) in classA:
            # Write the static adress to the output file
            output = open(OutputFile, 'a')
            output.write(ip)
            output.close()
        bar2()
output = open(OutputFile, 'r')
print('Found '+str(len(output.readlines())) +
      ' blocked ips found within the blocked static ips and subnets')
print('\nDone!\n\n-> Output file: '+OutputFile)
