

https://github.com/user-attachments/assets/16a3ded2-d026-47af-8d1e-0fcf1c72eb23

<H1>Visual simulation of Flatland</H1>
<H3>Libraries</H3>
<ul><li>Pygame</li></ul>
<H3>How to move</H3>
<ul><li>forward: W</li><li>backward: S</li><li>Turn left: A</li><li>turn right: D</li></ul>

<H2>1D Rendering</H2>
<p>A project based on simulating a 2D environment with a 1D view(similar to way of human recognition 3D space with 2D picture). The main goal of this project is to present another way of perceiving 2D and 3D space</p>
<H3>How it works</H3>
<p>The entire map is divided in tiles. Each ray crosses these small tiles. The algorithm checks ray collisions only in tiles crossed by the current ray (reduces calculations). All line segments are represented by endpoints and everything else is calculated using analytic geometry.</p>
<H3>Benchmark</H3>
<p>
Local benchmark:<br>
<em>python main.py benchmark</em><br>
<pre>
optimized   bruteforce  optimized/bruteforce
476678      2218600     0.2148553141620842
1185841     6776200     0.17500088545202325
1662766     10131000    0.1641265422959234
2129528     12809400    0.16624728714850032
2932485     16479000    0.1779528490806481
3547183     20472400    0.17326659307164768
4154452     24598600    0.1688897742147927
4754368     28621200    0.16611351026511817
5293222     31249400    0.16938635621803938
</pre>
Brute-force approach tests approximately six times more ray collisions than current algorithm approach. With current density of segments it is overall a bit slower than the brute force approach</p>

<H2>Graphical output</H2>
<H3>Flatland view</H3>
<p>The right panel is 1D raycasted view of the Square (player). Shapes fade with distance</p>
<H3>Upper view</H3>
<p>The left panel represents top-down view (our 3D dimensional perception) of the 2D space. The orientation of the player is determined by the green arrow.</p>
<h2>Other information</h2>
<ul><li>Project is based on ideas from book <b>Flatland: A Romance of Many Dimensions</b> (by Edwin Abbott)</li>
<li>There are no collisions, allowing all shapes to move freely across the map.</li>
<li>There are randomly moving characters (inhabitants of Flatland)</li></ul>


