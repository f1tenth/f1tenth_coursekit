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

| **Repository:** `Github Repository <https://github.com/f1tenth/f1tenth_lab3_template/tree/62a7a3d687d00ba1dd25cf7025c13a623bafdb5b>`_ 

.. raw:: html
	
	<iframe frameborder="10" scrolling="no" style="width:100%; height:3439px;" allow="clipboard-write" src="https://emgithub.com/iframe.html?target=https%3A%2F%2Fgithub.com%2Ff1tenth%2Ff1tenth_lab3_template%2Fblob%2F62a7a3d687d00ba1dd25cf7025c13a623bafdb5b%2FREADME.md&style=default&type=markdown&showBorder=on&showLineNumbers=on&showFileMeta=on&showFullPath=on&showCopy=on"></iframe>