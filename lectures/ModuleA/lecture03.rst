.. _doc_lecture03:


Lecture 3 - Rigid Body Transformation
============================================================

**Overview:** 
	A point in the real world can be defined in different ways from different perspectives. If the lidar, which is attached to a moving vehicle, detects an obstacle, we might want to know the obstacle's position in the real world. As the vehicle traverses the environment to create a map of the environment, the algorithm on the vehicle is actually creating multiple submaps and then tying all these submaps together and creating one global solution. In both of these applications, we will need to understand and use reference frames and frame transformations. This lecture will shed light on these two topics.

**Topics Covered:**
	-	Coordinate Frames and Reference Frames
	-	Rigid Body Transformations
	-	Frames and Transformations in ROS

**Slides:**

	.. raw:: html

		<iframe width="700" height="500" src="https://docs.google.com/presentation/d/e/2PACX-1vRclUfx3b4KNQ55Lm8_BtI-Fcv2jDwlDg9ezxcbxE1QHwH-IbOh39B8JL5zmcVZNw/embed?start=false&loop=false&delayms=60000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

.. **Video:**

	.. raw:: html

		<iframe width="560" height="315" src="https://www.youtube.com/embed/zkMelEB3-PY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


**Links to additional resources:**
	- `Robot Modeling and Control <https://www.amazon.com/Robot-Modeling-Control-Mark-Spong/dp/0471649902/ref=sr_1_1?keywords=Robot+Modeling+and+Control&link_code=qs&qid=1583440764&sr=8-1>`_
	- `tf2_ros <http://wiki.ros.org/tf2_ros>`_