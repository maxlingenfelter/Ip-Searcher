# This program is used to search trough a list of IPv4 static adresses and 
# IPv4 subnets and compare them to a list of Static adresses and subnets and 
# print a list of the adresses it finds that are found to match.

from doctest import OutputChecker

#Defintions
StaticBlockList = 'blocked-static.txt'
SubnetBlockList = 'blocked-subnets.txt'
CheckList = 'checkme.txt'
OutputFile = 'output.txt'

# Start by checking the CheckList for any static that are in the StaticBlockList

