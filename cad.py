# https://support.ntop.com/hc/en-us/categories/360003635054

import os
import subprocess 
import json 

#Assuming this script, ntop file, and json files will be in the same folder
Current_Directory = os.path.dirname(os.path.realpath('__file__')) 
exePath = r"C:/Program Files/nTopology/nTopology/nTopCL.exe"  #nTopCL path
nTopFilePath = r"SampleFile.ntop"   #nTop notebook file name
Input_File_Name = "input.json"      #JSON input file name to be saved as
Output_File_Name = "out.json"       #JSON output file name to be saved as

#Input variables in JSON structure
Inputs_JSON = {
    "inputs": [
        {
        	"name": "Output directory",
        	"type": "text",
        	"value": "C:\\Users\\Your Account\\Your Path\\"
       	},
       	{
            "name": "Length",
            "type": "scalar",
            "values": 7,
            "units": "mm"
        },
       	{
            "name": "Width",
            "type": "scalar",
            "values": 2,
            "units": "mm"
        },
       	{
            "name": "Height",
            "type": "scalar",
            "values": 2,
            "units": "mm"
        }
    ]
}

#nTopCL arguments in a list
Arguments = [exePath]               #nTopCL path
Arguments.append("-j")              #json input argument
Arguments.append(Input_File_Name)   #json path
Arguments.append("-o")              #output argument
Arguments.append(Output_File_Name)  #output json path
Arguments.append(nTopFilePath)      #.ntop notebook file path

#Creating in.json file
with open(Input_File_Name, 'w') as outfile:
    json.dump(Inputs_JSON, outfile, indent=4)

#nTopCL call with arguments
print(" ".join(Arguments))
output,error = subprocess.Popen(Arguments,stdout = subprocess.PIPE, 
               stderr= subprocess.PIPE).communicate()

#Print the return messages
print(output.decode("utf-8"))