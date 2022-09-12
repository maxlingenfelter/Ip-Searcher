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

print('Static adresses found in CheckList: ' + str(staticAdressesInChecklist))

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


# Checks all ip subnets in CheckList against SubnetBlockList

print('Subnet adresses found in CheckList: ' + str(subnetsInCheckList))
