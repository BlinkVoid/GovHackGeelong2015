# GovHackGeelong2015
participant project for GovHackGeelong2015
https://hackerspace.govhack.org/content/mighty-ducks-stormwater-tracker

Team Name: 
Rubber Ducks
Data Story

Being near the ocean is a big part of what makes life in the Geelong area great. We swim in it, eat fish from it, use it for shipping and recreation, or just watch the waves roll in on a stormy day. But our built urban environment influences ocean health in ways that we might not often think about. If you wash your car in the street, throw a chip packet in the gutter, wash some metal shavings off your factory floor down the drain: where do the detergents, hydrocarbons, plastics and heavy metals end up?

This tool lets us see how our stormwater runoff - and any pollution we add to it - enters the ocean, rivers or wetlands in Greater Geelong, at a super-local scale. It also shows us some of the ocean species that can be affected by stormwater pollution.

Users

The 'Mighty Ducks' Stormwater Tracker can be used by any Geelong resident who wants to understand more about where exactly they are having an environmental impact.

A second use of this kind of tool is tracking the upstream source of pollutants. Local water boards and agencies that monitor water quality frequently need to locate the source of pollution events. With further development, this tool could allow you to highlight the upstream stormwater network and potentially overlay with land use layers to hone in into possible pollution sources.

Data

We used the Geelong Drain Pipes and Drainage Pits (outfall locations) datasets made available by the City of Greater Geelong.

We also mined the FishMap website (CSIRO Marine and Atmospheric Research and Atlas of Living Australia) to find fish species likely to be found in near-coastal waters around Geelong.

Prize Categories

National

This tool combines national-level scientific data with local government data to let the public see their local environment in a new way - to really take ownership over their own habits regarding stormwater runoff, by understanding exactly where any pollution will end up, and what species it can impact. It also has huge potential for scientific and applied research use by water monitoring agencies both locally and Australia-wide. We think this makes our project an excellent candidate for both the Best Science Hack and the Scientific Data Bounty prize categories.

We used open-source tools to explore and extract data from the datasets and to build our web resource, so we're also entering the Open Source Bounty category. R was used to subset datasets. Python 3.4.2 was used to process the data and calculate water flow from a point to an outlet. Pyramid and Django were used as the scaffold frameworks for the website hosting.  We also used Inkscape for image editing, HTML, Javascript and CSS for building the website,  and Google Maps API for map customization. All data and scripts are publicly available in our Github repository.

Victoria

We've combined two totally different data types that also differ in geographic scale and information content - to produce a useful and fun tool greater than the sum of its parts, that helps people understand the local impact of stormwater pollution on ocean wildlife.

Stormwater drain data

geographic data
super-local (Greater Geelong area)
urban planning / water monitoring data from the City of Greater Geelong
Fish species data [unfortunately we could not access the images on the 4th or 5th July due to server issues on the FishMap end]

filtered list of species names with associated images
from FishMap, a nation-wide data portal
biological / fisheries /species distribution modelling data
This makes us fantastic candidates for the Most innovative use of interdisciplinary data award.

Geelong

The Environmental Geelong award supports 'the best hack that highlights the environmental assets of Geelong'. Our project highlights the amazing fish diversity found in Geelong oceans and engages locals at a super-local scale to think about the impact of their stormwater on the Geelong ocean environment. We think this project does a fantastic job of highlighting environmental assets that aren't otherwise visible to everyone (since they're underwater!) and empowering people to protect them.

We'd also like to enter the Geelong Open Data Creative Challenge category. Expanding this tool to map upstream source flow would be of huge help to environmental monitoring agencies, catchment management authorities and local councils who deal with stormwater pollution impacts all around Australia. We see it as having commercial potential and believe we've come up with a really creative solution combining different data types to engage local communities in an important environmental management issue.

Planning for land use and population change in Future Geelong definitely needs to consider environmental impacts, and this tool can help predict pollution impact sites and help consider how to redirect stormwater through wetlands and other cleanup locations.

Team Prizes

We are three University students (at Deakin University) and a researcher (University of Melbourne) and would like to enter the Best Higher Education Team category. Email addresses to prove it: griffinp@unimelb.edu.au; thanhbi@deakin.edu.au; rgoliver@deakin.edu.au; rogerz@deakin.edu.au

Video URL: 
https://youtu.be/1naTkYjDLEE
Proof of Concept Repository URL - Code Repository, source material or stages of development records: 
Mighty Ducks Stormwater Tracker
Datasets Used: 
Stormwater drain locations in Greater Geelong http://data.gov.au/dataset/geelong-drain-pipes; Stormwater drainage pits (outfalls) in Greater Geelong http://data.gov.au/dataset/geelong-drainage-pits; Fish species list accessed at FishMap http://fish.ala.org.au/search by selecting all fishes found within 25 km of the Geelong area in coastal/shallow water (0-40 m)
