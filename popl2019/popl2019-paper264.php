<?php
        require_once('config.php');
        require_once(__INCLUDE__.'/functions.php');
        require_once(__INCLUDE__.'/header.php');
?>


        <div id="content">

                <div class="post">

                         <h3>CAV18-Artifact-Paper259</h3>

<b>Artifact </b><br><br>

We provide our artifact in the form of a virtual machine running Ubuntu 18.04 which can be downloaded <a href="http://files.srl.inf.ethz.ch/CAV2018.ova">here</a>.
We prepared the virtual machine on a 10 Core 3.3 GHz  Intel i9-7900X Processor running Ubuntu 17.10. We allocated 4 GB of RAM to the virtual machine.

<br><br><b>Paper #264</b><br>
An Abstract Domain for Certifying Neural Networks <br><a href="http://files.srl.inf.ethz.ch/cav18-paper259.pdf" class="pdf"><img src="images/pdf.png" class=pdf-load border="0" alt="PDF" noborder></a> </li>
 

<br><br><br><b>System Requirements<br> </b>
 
	<ol>
	<li>Make sure you have 64-bit VirtualBox from Oracle.</li>
	<li> The virtual machine requires at least 4 GB of disk space. </li>
	<li>We recommend allocating at least 4 GB RAM to the virtual machine for analyzing larger benchmarks. </li>
	</ol>

<br><b>Instructions<br> </b>
<ol>
<li> Import the virtual machine in VirtualBox. More information on importing virtual machine in VirtualBox can be found <a href="https://docs.oracle.com/cd/E26217_01/E26796/html/qs-import-vm.html">here.</a>
<li>The login credentials for the Virtual Machine are:
		<ul>username: popl19-paper264</ul>
		<ul>password: paper264</ul></li>
<li> The benchmarks used in the paper can be found in "CAV2018/Benchmarks" directory.</li>
<li> As the Virtual machine is already large, we did not include the learning data as well as the benchmarks used for training. </li>
 </ol>
<br><b> Analyzer <br></b>
<li>The Source code for our abstract domain can be found in "DeepPoly/ELINA/fppoly" directory.</li>
<li>We have precompiled SeaHorn as it has a number of dependencies. The executable is located in "seahorn/build/run/bin" directory.</li>

<br><b>Polyhedra libraries<br> </b>
<ol>
<li> Our approximate Polyhedra implementations build on top of ELINA.
<li> The source code for ELINA Polyhedra library, Poly-RL, Poly-Fixed and Poly-Init can be found in "ELINA/elina_poly", "ELINA/poly_rl", "ELINA/poly_fixed" and "ELINA/poly_init" directories respectively. </li>
<li> The "ELINA/poly_rl" directory contains "weights.txt" file which contains the learned weights for the Q-function with linear function approximation. Poly-RL requires "weights.txt" to be in the folder in which the analysis is running. We have copied "weights.txt" in the directories containing benchmarks.</li>
<li> It is possible to test our operators outside the seahorn analyzer. The test file "elina_test_poly.c" in the respective directories generates random test cases for a number of Polyhedra operators. The corresponding executable "elina_test_poly" requires two command line arguments : (a) dim: number of variables and (b) nbcons: number of constraints. </li>

</ol>



<br><b>Reproducing results<br> </b>
<ol>
<li>For reproducing results reported in the paper, run "sudo run.sh" in "CAV2018" directory. It compiles, installs and runs the ELINA Polyhedra analysis on all benchmarks followed by Poly-RL, Poly-Fixed and Poly-Init.  </li>
 <li>  The invariants and runtimes are collected in "results" directory. </li>
<li>After completing the analysis, the script first shows the runtimes in cycles of all libraries on all benchmarks. The timings can be converted to seconds through dividing by CPU frequency. No runtime is reported in case of a timeout or crash.</li>
<li>The script then shows the precision in percentage of all approximate libraries on all benchmarks with respect to ELINA. It also shows the number of program points on which an approximate implementation produces same or better fixpoints and the total number of program points on which invariants are comapred.</li>
<li>SeaHorn can be invoked with Polyhedra analysis without "run.sh" by using the command "/home/cav2018/seahorn/build/run/bin/sea pf --crab --crab=opt-pk-elina filename". The shared object produced by all Polyhedra implementations has the same name so make sure to first install the desired implementation in "/usr/local/lib".  </li>
<li> We also included 5 benchmarks from product lines category in the directory "CAV2018/product-lines". ELINA times out on all of these. It is possible to run them directly as explained above or by modifying "run.sh" to use "product-lines" instead of "Benchmarks" directory. More benchmarks on which ELINA times out can be found <a href="https://github.com/sosy-lab/sv-benchmarks/tree/master/c/product-lines">here</a> with the prefix "email_spec0", "email_spec1", "email_spec8", and "email_spec9" and "email_spec11".</li>
<li> We set a default timeout limit of 3600 sec per benchmark, it is trivial to change this limit as per convenience in "run.sh".</li>
</ol>

<br><b>Caveats<br> </b><ol>
	<li> The analysis runs slower on the virtual machine and the timings vary considerably. For benchmarks that run faster with ELINA, we observed that there was little speedup with Poly-RL. </li>
<li> Since Poly-Init takes random actions, the timing and precision varies. Thus, the obtained timing and precision values from the virtual machine may be significantly different than the ones reported in the paper.</li>
	<li> For some benchmarks, seahorn crashes after the Polyhedra analysis completes. However, this is due to the SMT solver and not because of Polyhedra analysis.</li>
<li> For "ata_pata", "ideapad_laptop" and "net_ppp" benchmarks, the analysis seems to crash before it can write all invariants on the virtual machine (the Polyhedra analysis finishes), thus the number of program points at which the fixpoints are compared are less than reported in the paper. We found that on the virtual machine, invariants were produced for 230, 377 and 580 program points respectively on these benchmarks instead of 262, 461 and 680 as reprted in the paper. Thus, the precision of our approximations on these benchmarks may differ from the ones reported in the paper.</li>
<li>If less memory is available than recommended, then the analysis may crash before it completes and thus the reported precision will be significanlty less. </li>

	</ol>

	  





                </div>
        </div>
<?php
        require_once(__INCLUDE__.'/sidebar.php');
        require_once(__INCLUDE__.'/footer.php');
?>

