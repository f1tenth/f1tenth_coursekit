.. _doc_lab8:


Lab 8 - Perception and Planning
=================================

.. tip:: Before starting this lab, review the :ref:`Lecture 17 <doc_lecture17>` and :ref:`Lecture 18 <doc_lecture18>` to ensure you are familiar with the material.

| **Goals:**
| Most racing series feature multiple vehicles competing simultaneously on a single track. As such, safely overtaking and navigating in the presence of other vehicles is paramount to performing well. Since the strategy and decisions of of other vehicles cannot be known ahead of time and may, in fact, be stochastic it is necessary for your car to react to new constraints imposed by other vehicles online. Thus, the goal of this lab is to track and predict the pose of an opponent vehicle.

| **Learning Outcomes:**
| The following fundamental should be understood by the students upon completion of this lab:
	
	* Vision and Perception
		
		* *Camera model and parameters:* You should be able to understand how the real camera model and the pin hole camera model are related and what assumptions are made while going from the former to the latter.
		* *Transformations:* You should be able to understand 3 dimensional transformations and know the representations of transformations.
		* *Single View Geometry:* You should be able to understand and work with single view geometry and how world coordinate frame points translate to camera coordinate frame points.
		* *Homography:* You should be able to work with homography and how it can be used to calculate pose of the camera given the world coordinate correspondances.

	* Programming skills

		* Working with images on ROS
		* Transformations using tf and implementation of AprilTags and similar libraries.
		* Implementing nodelets in ROS and their advantages.

**Required Skills:** ROS, Python/C++

**Allotted Time:** 1 week

| **Repository:** `Github Repository <https://github.com/f1tenth/f1tenth_labs/tree/master/lab8/latex>`_ 
|	The repository contains the latex source files as well as any skeleton code. Compile the latex source files to view the most up to date handout.

.. raw:: html

	<iframe width="700" height="800" src="https://drive.google.com/file/d/1XWkdkkCTt072qkzR3WIgROplf0Ay1QoY/preview?usp=drive_link" width="640" height="480"></iframe>
