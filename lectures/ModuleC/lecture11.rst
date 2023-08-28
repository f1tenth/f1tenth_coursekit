.. _doc_lecture11:


Lecture 11 - Particle Filters
=============================================

**Overview:** 
	This is the third installment in the Localization lectures. Given inputs of laser scan data, a control input, and a map, we want to output a pose and some "particles". This lecture is divided into three parts: 1) going over the particle filter localization algorithm, 2) tuning the alrogithm, and 3) additional resources and a hands on tutorial. Expect a dense but extremely informative lecture.

**Topics Covered:**
	-	Particle filters

**Slides:**

	.. raw:: html

		<iframe width="700" height="500" src="https://docs.google.com/presentation/d/e/2PACX-1vSpVRivaWcqH5NwZHO-iNv0VwxsebbraqEySUOEOm8CAe-zFyoudH-OZ7zdT8hXhw/embed?start=false&loop=false&delayms=60000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

.. 
	**Video:**

		.. raw:: html

			<iframe width="560" height="315" src="https://www.youtube.com/embed/zkMelEB3-PY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


**Links to additional resources:**
	- `S. Thrun, W. Burgard. “Probabilistic Robotics.” Chapter 4 and Chapter 8. <http://www.probabilistic-robotics.org/>`_
	- `S. Thrun. “Artificial Intelligence for Robotics, Lesson 3.” Udacity. <https://www.udacity.com/course/artificial-intelligence-for-robotics--cs373>`_
	- `S. Thrun, D. Fox, W. Burgard and F. Dellaert. “Robust Monte Carlo Localization for Mobile Robots.”​ Artificial Intelligence Journal. 2001. <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.71.6016&rep=rep1&type=pdf>`_
	- `D. Fox, W. Burgard, and S. Thrun. “Markov localization for mobile robots in dynamic environments,” ​ Journal of Artificial Intelligence Research ​ , vol. 11, pp. 391427, 1999. <http://www.jair.org/media/616/live-616-1819-jair.pdf>`_
	- `D. Fox. “KLD-sampling: Adaptive particle filters,” Advances in Neural Information Processing Systems 14 (NIPS), Cambridge, MA, 2002. MIT Press. <https://papers.nips.cc/paper/1998-kld-sampling-adaptive-particle-filters.pdf>`_
	- `D. Bagnell “Particle Filters: The Good, The Bad, The Ugly” <http://www.cs.cmu.edu/~16831-f12/notes/F14/16831_lecture05_gseyfarth_zbatts.pdf>`_
	- `C. Walsh, S. Karaman. “CDDT: Fast Approximate 2D Ray Casting for Accelerated Localization.” Arxiv, 2017. <http://arxiv.org/abs/1705.01167>`_


