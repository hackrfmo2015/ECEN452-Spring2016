ECEN 452-500: Ultra High Frequency Techniques
Spring 2016 – Prof. Huff
Lab 6

Pull the Lab 6 subdirectory in the ECEN 452 GitHub directory Labs and locate the HFSS project files “ECEN452_Lab6_Filters.hfss”. Open each project file (File-Open…), then save them to the local drive of the computer you are running your simulations on and rename it by appending your team number to each file (e.g., “ECEN452_LabX_TopicY_TeamZ”).<br>
In this lab you will be completing two designs of a low pass filter and the design of a band stop. These are found in your “ECEN452_Lab6_Filters_GroupX.hfss” project file. These design files are named “N5_MaxFlat_LPF_T-Line”, “N5_MaxFlat_LPF_TLine_Tapped”, and “N5_MaxFlat_BSF_T-Line”. You will be designing these for a Z0 = 50 Ohm reference impedance on the 62 mil thick FR4 (er = 4.1, tan_d = 0.01) substrate.<br>
Task 1: Synthesis and implementation of a maximally-flat low-pass filter.<br>
In this exercise you will synthesize a maximally-flat low-pass filter with a cut-off frequency fc = 2.5 GHz and a minimum attenuation of 10 dB at 3.25 GHz.<br>
<br>Step 1: First, calculate the order N of the filter required to meet the specifications of providing 10 dB isolation at 3.25 GHz using abs(w/w_c)-1 = abs(f_10dB/f_c)-1 and the figure below.<br>
<b>Ans:<br>
abs(w/wc) - 1= abs(3.25-2.5) - 1 = 0.3<br>
After check the table, n =5 to have at leat 10 dB attenuation at 3.25 GHz.<br></b>

<br>Step 2: Next, use the table on the following page to determine the filter coefficients for the (hint: five-element) low-pass prototype.<br>
<b>Ans:<br>
For n = 5, g1 = 0.6180, g2 = 1.6180, g3 = 2.0000, g4 = 1.6180, g5 = 0.6180, g6 = 1.0000<br></b>

<br>Step 3: Assemble the prototype LC ladder network.
To simplify the analysis (visually), we will replace this ladder network will the table shown below.



<br>Step 4: Use Richard’s Transformation to convert the capacitors into open circuit stubs and the inductors into short circuit stubs.



<br>Step 5: Use Kuroda’s identities to convert series stubs to shunt stubs. This is a multi-step process, but the filter coefficients are symmetric in so we only need to transform one side of the filter and then capitalize on the symmetry. This will begin at the load and/or source side and work to the center of the filter (note: the center element is a shunt open-circuit stub, so it will remain untouched in this process).


<br>Step 5.1 Insert unit elements source and load sides of the circuit to separate z1 from z2 and z5 from z4.


<br>Step 5.2 Insert two more unit element source and load sides of the circuit. This will separate z2 from z3 and z4 from z3, then separate z4 from z5 and z1 from z2. This process will also convert z1, z2, z4, and z5 into shunt OC stubs.


<br>Step 5.3 Perform impedance scaling for the transmission line.


<br>Step 6: Calculate the widths of the transmission lines and enter these into the design “N5_MaxFlat_LPF_T-Line” within the HFSS project “ECEN452_Lab6_Filters.hfss”. You will also need to enter this information into the “N5_MaxFlat_LPF_T-Line.zov” Z0lver assignment.


<br>Step 7: Perform impedance and frequency scaling for the lumped element prototype you found in Step 2 and enter these into the “N5_MaxFlat_LPF_LC.zov” Z0lver assignment.


<br>Step 8: Calculate the values x1, x2, x3, x4, and x5 (e.g., the electrical length of the stubs) for the modified low pass filter design “N5_MaxFlat_LPF_T-Line_Tapped_Stubs” that uses tapped stubs with a 1 mm width (Z0 = 89 W).


<br>Task 2: Synthesis and implementation of an equi-ripple band-stop filter.
In this exercise you will synthesize a fifth-order 0.5 dB equi-ripple band-pass filter with a center frequency fc = 3.0 GHz and a bandwidth of 2.25 GHz to 3.75 GHz (e.g.,  = 0.5), and then implement your design using microstrip transmission lines for a Z0 = 50  reference impedance on a 62 mil thick FR4 (r = 4.1, tan  = 0.01).

<br>Step 1: First, use the table on the following page to determine the element values of the low pass prototype.


<br>Step 2: Assemble the prototype LC ladder network.
To simplify the analysis (visually), we will replace this ladder network will the table shown below.


<br>Step 3: Convert this to a band-stop filter topology by replacing shunt elements with shunted LC series networks, and series LC parallel networks.


<br>Step 4: Use inverters (e.g., quarter-wave transformers) to provide separation between the series elements and convert series stubs into shunt stubs.


<br>Step 5: Calculate the scaled impedance values of the equivalent open-circuit stubs using
