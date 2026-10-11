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

| **Repository:** `Github Repository <https://github.com/f1tenth/f1tenth_lab3_template/tree/2c559dad05ac06d2352794e4e37ec243d95e4b5f>`_ 

.. raw:: html

	<script src="https://emgithub.com/embed-v2.js?target=https%3A%2F%2Fgithub.com%2Ff1tenth%2Ff1tenth_lab3_template%2Fblob%2F2c559dad05ac06d2352794e4e37ec243d95e4b5f%2FREADME.md&style=default&type=markdown&showBorder=on&showLineNumbers=on&showFileMeta=on&showFullPath=on&showCopy=on"></script>
