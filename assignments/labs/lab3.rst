.. _doc_lab3:


Lab 3 - Wall Following
=======================

.. tip:: Before starting this lab, review :ref:`Lecture 4 <doc_lecture04>` to ensure you are familiar with the material.

| **Goals:**
| In this lab, you will implement a PID (proportional integral derivative) controller to make the car drive parallel to the walls of a corridor at a fixed distance. At a high level, you will accomplish this by taking laser scan distances from the Hokuyo LiDAR, computing the required steering angle and speed (drive parameters), an publishing these to the VESC to drive the car. 

| **Learning Outcomes:**
| The following fundamentals should be understood by the students upon completion of this lab:

	* PID controllers
	* Driving the car autonomously via Wall Following

**Required Skills:** ROS, Python/C++

**Allotted Time:** 1 Week

| **Repository:** `Github Repository <https://github.com/f1tenth/f1tenth_labs/tree/master/lab3>`_ 
|	The repository contains the latex source files as well as any skeleton code. Compile the latex source files to view the most up to date handout.

.. raw:: html

	<iframe width="700" height="800" src="https://drive.google.com/file/d/1WZ4ou14iQLI6VUU8btDTlc9bbsxkQMA_/preview?usp=drive_link" width="640" height="480"></iframe>
