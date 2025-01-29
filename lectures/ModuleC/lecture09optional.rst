.. _doc_lecture09optional:


Lecture 9 (Optional) - Scan Matching I & II
================================

**Overview:** 
	This lecture is part one of three localization lectures. We'll learn how to determine the state (position and orietnation) of a robot with respect to its environment. The RoboRacer vehicle uses range measurements from the lidar to localize. The iterative closest point algorithm and fast correspondence search are explained. At the end of the lecture, there is an overview of Lab 5.

**Topics Covered:**
	-	Localization/SLAM
	- 	Scan Matching
	-	Iterative Closest Point
	-	Fast Correspondence Search

**Associated Assignment:** 
	* :ref:`Lab 5 (Optional): Scan Matching <doc_lab05>`

**Slides:**

	.. raw:: html

		<iframe width="700" height="500" src="https://docs.google.com/presentation/d/e/2PACX-1vTJQKzyQOxeJsqH8wkLAE_QtmCWj1FozCkn1_EBZfwOXxwTcyPjRr2OSrjG9rTILg/embed?start=false&loop=false&delayms=60000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

**Video:**

	.. raw:: html

		<iframe width="700" height="500" src="https://www.youtube.com/embed/tuQXuTe8KK4?list=PL7rtKJAz_mPdFDJtufKmqfWRNu55s_LMc" title="RoboRacer L07 - Scan Matching" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
		<iframe width="700" height="500" src="https://www.youtube.com/embed/WmoOA1XXh_o?list=PL7rtKJAz_mPdFDJtufKmqfWRNu55s_LMc" title="RoboRacer L07 - Scan Matching Lab (Part 1I)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
		<iframe width="700" height="500" src="https://www.youtube.com/embed/wnll231Y0LY?list=PL7rtKJAz_mPdFDJtufKmqfWRNu55s_LMc" title="RoboRacer L07 - Scan Matching Lab (Part II)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

**Links to additional resources:**
	- `An ICP variant using a point-to-line metric <https://censi.science/pub/research/2008-icra-plicp.pdf>`_
	- `Convex Optimization course <https://see.stanford.edu/Course/EE364A>`_