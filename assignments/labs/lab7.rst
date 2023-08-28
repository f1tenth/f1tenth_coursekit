.. _doc_lab7:


Lab 7 - Motion Planning (RRT)
=================================

.. tip:: Before starting this lab, review :ref:`Lecture 14 <doc_lecture14>` to ensure you are familiar with the material.

| **Goals:**
| The goal of this lab is to provide you with tools that will help you in a head-to-head race on a race track. After finishing this lab, your car should be able to do something like `this <https://www.youtube.com/watch?v=llHCRqwIllM>`_.

| **Learning Outcomes:**
| The following fundamentals should be understood by the students upon completion of this lab:

	* Motion Planning basic concepts.

		* Configuration space vs. Workspace: you should understand the difference between configuration space and workspace, and the advantages and disadvantages of planning in each of them.
		* Free space vs. Obstacle space: you should understand the difference between free space and obstacle space.
		* Occupancy grids and Costmaps: you should understand what occupancy grids and costmaps are, how to use them, and how to create them.

	* Motion Planning algorithms. You should understand the basic ideas of these following planning algorithms, their advantages and disadvantages, and when to use them.

		* Grid-based search: Dijkstra’s, A*, and their variants
		* Sampling based algorithms: RRT and its variants

**Required Skills:** ROS, Python/C++

**Allotted Time:** 1.5 week

| **Repository:** `Github Repository <https://github.com/f1tenth/f1tenth_labs/tree/master/lab7>`_ 
|	The repository contains the latex source files as well as any skeleton code. Compile the latex source files to view the most up to date handout.

.. raw:: html

	<iframe width="700" height="800" src="https://drive.google.com/file/d/1LkVwC3PJYvULnBVjGecho8BsW3bbis4N/view?usp=drive_link" width="640" height="480"></iframe>