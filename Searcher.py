# This program is used to search trough a list of IPv4 static adresses and
# IPv4 subnets and compare them to a list of Static adresses and subnets and
# print a list of the adresses it finds that are found to match.

from doctest import OutputChecker

# Defintions
StaticBlockList = 'blocked-static.txt'
SubnetBlockList = 'blocked-subnets.txt'
CheckList = 'checkme.txt'
OutputFile = 'output.txt'

# Clear the output file
output = open(OutputFile, 'a')
output. 

# Start by checking the CheckList for any static that are in the StaticBlockList
checkData = open(CheckList, 'r')
staticAdresses = []
for line in checkData:
    # If the lines does not contain a '/' then push it to the static adress array
    # print('Checking Line:'+str(line))
    if '/' not in line:
        staticAdresses.append(line)

print('Static adresses found in CheckList: ' + str(staticAdresses))

# For each static adress found in the CheckList, check if it is in the StaticBlockList

for static in staticAdresses:
    staticData = open(StaticBlockList, 'r')
    for line in staticData:
        # If the lines does not contain a '/' then push it to the static adress array
        # print('Checking Line:'+str(line))
        if static in line:
            print('Static adress found in StaticBlockList: ' + str(static))
            # Write the static adress to the output file
            output = open(OutputFile, 'a')
            output.write(static + '\n')
            output.close()
