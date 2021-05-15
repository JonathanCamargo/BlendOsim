---
title: 'BlendOsim: A Blender add-on for visualization of Opensim models and motion capture data'
tags:
  - Python
  - Biomechanics
  - Motion capture
  
authors:
  - name: Jonathan Camargo^[Custom footnotes for e.g. denoting who the corresponding author is can be included like this.]
    orcid: 0000-0001-5219-2110
    affiliation: "1" # (Multiple affiliations must be quoted)
  - name: Aaron Young
    orcid:     
    affiliation: "1" # (Multiple affiliations must be quoted)
	
affiliations:
 - name: Georgia Institute of Technology
   index: 1 
date: 14 May 2021
bibliography: paper.bib

# Optional fields if submitting to a AAS journal too, see this blog post:
# #https://blog.joss.theoj.org/2018/12/a-new-collaboration-with-aas-publishing
#aas-doi: 10.3847/xxxxx <- update this with the DOI from AAS once you know it.
#aas-journal: Astrophysical Journal <- The name of the AAS journal.
---

# Summary
`BlendOsim` is an Python add-on for the opensource 3D creation suite `Blender` for improved visualizations in biomechanics research.  The add-on allows to import motion capture markers and forceplate data. Furthermore, it allows importing OpenSim models and motion trajectories, enabling a complete visualization tool for biomechanics experiments based on motion capture.

With `BlendOsim` the user can surpass the limited visualization from OpenSim by leveraging on the more robust 3D visuals from `Blender` and its advanced rendering features. For example, you can create renders and multi-camera video sequences that illustrate the experiment, or use the annotate functions to put 3D notes and support the scientific discussion of the biomechanics data.


# Statement of need

Biomechanic analysis of human locomotion requires the observation of the trajectories of a system with multiple degrees of freedom. This is often achieved by recording the kinematics and external forces of the task with motion capture tools. Motion capture solutions includes specialized proprietary software with rudimentary visualization that is limited to the raw marker data \cite{Vicon, Optitrack}.

OpenSim has achieved recognition in the field for developing models and perform motion analysis including inverse kinematics, inverse dynamics and even forward dynamics simulations \cite{opensim}. However, the visualization tools of the software are still limited offering low resolution images, no user 3D scope or loading of background and external objects that exist in the experimental terrain. 

As more complex scenarios are studied in the literature (e.g. obstacles, stairs, ramps) \cite{sawicki, otros}, the dissemination of information would benefit from better visualization tools of the locomotion where the 3D configuration of the human body is presented instead of 2D plots with the joint angle profiles. 

 We release `BlendOsim` as an open-source add-on for the 3D suite `Blender`. `BlendOsim` could help the visualization and disemination of biomechanics in the classroom and publications. With this add-on the user can easily import OpenSim models, motion capture marker data and forceplate data into the 3D environment and use it to generate scientific illustrations and animations.

# `BlendOsim` add-on

The `BlendOsim` add-on exposes the interface as tools tab containing options to import four data types.

**Markers file**: a csv file containing the xyz trajectories of the markers in the motion capture recorded in the experiment.

**Forces file**: a csv file containing the force, moments and center of pressure for the forceplate data recorded in the experiment.

**Model file**: corresponds to the description of the biomechanics model in .osim format. Adding the model will add STL surfaces parented to empty objects that can be later used for animation. 

**Motion file**: a csv file containing the location and rotation for every segment in the model at each animation keyframe.

![User interface for BlendOsim. The user can import markers, forces, models and motion files](preview.png){ width=20% } 

# Dependencies

`BlendOsim` is written in Python and works directly with the `Blender` version 2.80 or greater (latest version tested is 2.92). Since Blender does not support the vtp format, the add-on is preloaded with STL surface files for the Simbody model from Opensim. For new models, the user can refer to \cite{Paraview} or any CAD software with vtp support to convert the model surfaces to stl. 


# Citations

Citations to entries in paper.bib should be in
[rMarkdown](http://rmarkdown.rstudio.com/authoring_bibliographies_and_citations.html)
format.

If you want to cite a software repository URL (e.g. something on GitHub without a preferred
citation) then you can do it with the example BibTeX entry below for @fidgit.

For a quick reference, the following citation commands can be used:
- `@author:2001`  ->  "Author et al. (2001)"
- `[@author:2001]` -> "(Author et al., 2001)"
- `[@author1:2001; @author2:2001]` -> "(Author1 et al., 2001; Author2 et al., 2002)"



# Acknowledgements

We acknowledge the support and funding for Jonathan Camargo by the Fulbright fellowship and Minciencias Colombia.

# References