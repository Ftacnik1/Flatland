<H1>Visual simulation of Flatland</H1>
<H2>1D Rendering</H2>
<p>A project based on simulating a 2D environment with a 1D view(similar to way of human recognition 3D space with 2D picture). The main goal of this project is to present another way of perceiving 2D and 3D space</p>
<H3>Optimization</H3>
<p>The entire map is divided in tiles. Each ray crosses these small tiles. The algorithm, checks ray collisions only in tiles crossed by the current ray (reduces calculations). All line segments are represented by endpoints and everything else is calculated using analytic geometry</p>

<H2>Graphical output</H2>
<H3>Flatland view</H3>
<p>The right panel is 1D raycasted view of the Square. Shapes fade with distance</p>
<H3>Upper view</H3>
<p>The left panel represents top-down view (our 3D dimensional perception) of the 2D space. The orientation of the player is determined by the green arrow.</p>
<h2>Other information</h2>
<ul><li>The map is randomly generated each time. There are larger area that can be empty,a forest or a town. (The structure at the beginning of the game is house based on Flatland[by Edwin Abbott]) There are no doors for women because they are not included in the game yet</li>
<li>There are no collisions, allowing all shapes to move freely across the map.</li>
<li>There are randomly moving characters(inhabitants of Flatland)</li></ul>


