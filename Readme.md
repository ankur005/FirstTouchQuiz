<h2> Part 1 </h2>
<p> Santa is delivering presents to an infinite two-dimensional grid of houses. </p>
<p> He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north ^, south v, east >, or west <. After each move, he delivers another present to the house at his new location. </p>
<p> However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present? </p>
<p> For example: </p>
<ul>
<li> > delivers presents to 2 houses: one at the starting location, and one to the east. </li>
<li> ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location. </li>
<li> ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses. </li>
<h4> Answer: </h4>
<p> 2081 </p>


<h2> Part 2 </h2>
<p> The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him. </p>
<p> Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year. </p>
<p> This year, how many houses receive at least one present? </p>
<p> For example: </p>
<ul>
<li> ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south. </li>
<li> ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started. </li>
<li> ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other. </li>
<h4> Answer: </h4>
<p> 2341 </p>

<h2> Solution Approach </h2>
<p> The houses are represented using x and y coordinates, just like points on a 2D Coordinate system. A set is used to store the points (or houses) visited by Santa or the robot. We go through the input character by character and according to the input, i.e. the direction provided by elf, the coordinates (location of Santa or the robot) are updated. At the end of each iteration, the updated coordinates are added to the set. Since, a set cannot have duplicates, only distinct pairs of x and y will be stored which will represent all the distinct houses visited by Santa and the robot, effectively providing us with the houses that received atleast one present. </p>


