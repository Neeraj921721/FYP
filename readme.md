
                                                     CRG: CONDITION RANK GENERATOR FOR PROGRAM REPAIR
=======
<h1>CRG: CONDITION RANK GENERATOR FOR PROGRAM REPAIR</h1>
<h3>Instructions To Run The Program In Local Machine</h3>
<ol>
	<li>Dowload the file</li>
	<li>Unzip the file</li>
	<li>Open the terminal from the path inside the folder(CBMC)</li>
</ol>

<h4>Run The Below Command On the Terminal To Generate The CBMC Condition Coverage Report</h4>
<p><code><b>./cbmc --cover condition your-cprog-path</b></code>
>>>>>>> 7738b23ecaeb6e2e2efd443bcee250f248ac89e9

<p>
	e.g.: if the c program is inside desktop folder then</p> 
 	<code><b>./cbmc --cover condition home/Desktop/cprog.c</b></code>
</p>

<p>
<b>N.B. : You can see the result on terminal but you can redirect the output to a file by using below command</b>

<code><b> ./cbmc --cover condition your-cprog-path > cbmc-report-path </b></code>

<p>
	e.g.: if you want to store the output at the desktop folder then</p> 
 	<code><b>./cbmc --cover condition /home/Desktop/cprog.c > /home/Desktop/output.txt </b></code>
</p>

</p>

<h4> For generating info(Final Report) from CBMC report : </h4>
<ol>
	<li>open terminal in the folder FYP</li>
	<li>type the below command : </li>
<ol>
	
<code><b>$ python3 FaultLocBasedOnConditionCoverage.py /home/neeraj/Desktop/FYP/CBMCReport/cprog1report.txt /home/neeraj/Desktop/FYP/C_Programs/cprog1.c /home/neeraj/Desktop/FYP/FinalCCreports/cprog1final.txt</b></code>

<h4>To push files upstream : git push -u origin master </h4>
