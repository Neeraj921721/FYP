                                                     CRG: CONDITION RANK GENERATOR FOR PROGRAM REPAIR

1. Dowload the file
2. Unzip the file
3. Open the terminal from the path inside the folder(CBMC)
4. Run the below command

./cbmc --cover condition your-cprog-path

Eg: if the c program is inside desktop folder then 
 ./cbmc --cover condition home/Desktop/test14.c

5. You can see the result on terminal but you can redirect the output to a file by using below command
./cbmc --cover condition your-cprog-path > /cbmcReport-path/ConditionCovReport.txt


For generating info(Final Report) from CBMC report :
1. open terminal in the folder FYP
2. type the below command :
	$ python3 FaultLocBasedOnConditionCoverage.py /home/neeraj/Desktop/FYP/CBMCReport/cprog1report.txt /home/neeraj/Desktop/FYP/C_Programs/cprog1.c /home/neeraj/Desktop/FYP/FinalCCreports/cprog1final.txt
	
To push files upstream : git push -u origin master
