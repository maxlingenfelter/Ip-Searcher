# This program is used to search trough a list of IPv4 static adresses and
# IPv4 subnets and compare them to a list of Static adresses and subnets and
# print a list of the adresses it finds that are found to match.

# Imports
import ipaddress

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
            print('Static adress found in StaticBlockList: ' + str(static))
            # Write the static adress to the output file
            output = open(OutputFile, 'a')
            output.write(static + '\n')
            output.close()

# print('Subnet adresses found in CheckList: ' + str(subnetsInCheckList))
# Checks all ip subnets in CheckList against SubnetBlockList
for subnet in subnetsInCheckList:
    subnetData = open(SubnetBlockList, 'r')
    for line in subnetData:
        if subnet in line:
            print('Subnet found in SubnetBlockList: ' + str(subnet))
            # Write the subnet to the output file
            output = open(OutputFile, 'a')
            output.write(subnet + '\n')
            output.close()


def getIpRange(ip, size):
    return [str(ip) for ip in ipaddress.IPv4Network(str(ip) + '/' + str(size), False)]


# Check the CheckList for any subnets that include static adresses in the StaticBlockList
for subnet in subnetsInCheckList:
    staticIpsInSubnet = []
    subnetIp = subnet.split('/')[0]
    subnetSize = subnet.split('/')[1]
    subnetRange = getIpRange(subnetIp, int(subnetSize))
    print('\nSubnet: ' + str(subnetIp) + ' \nSize: ' +
          str(subnetSize) + ' \nRange: ' + str(len(subnetRange))+'\n')
