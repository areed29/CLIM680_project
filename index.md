# Examining Changes and Relationships between Clouds, Precipitation, and Precipitable Water in the African Monsoon Region
# Austin Reed
# Introduction
My dataset of choice is ERA5 monthly averaged data on single levels from 1979 to present, which is the fifth generation ECMWF renalysis for the global climate and weather for the past 4 to 7 decades. I plan to look at the variables of total cloud cover, total precipitation, column cloud liquid water, as well as total column cloud water vapor in Africa to answer the question: Has mean precipitable water changed significantly in the African monsoon region over the last 70 years? In which season? And how is that change related to changes in clouds? Some tools that I could use to help solve this question include looking at monthly, and seasonal anomalies over continental Africa, and explore the variance in these anomalies over recent years. This can help to pinpoint statistically significant trends in precipitation, total column precipitable water, cloud cover, and total column liquid water over continental Africa. The continent can be further broken up into sub-regions to highlight the impact of the African monsoon. 
# Data
The dataset that is used in my project is
### ERA 5 Monthly Mean Data on Single Levels, from 1979-present
Replacing the ERA-interim reanalysis, ERA5 is the fifth generation ECMWF reanalysis for the global climate and weather for the past 4 to 7 decades. Using data from 1979 onwards, ERA5 provides monthly estimates for a large number of atmospheric, ocean-wave, and land-surface quantities. Data has been regridded to a regular lat-lon grid of 0.25 degrees for the reanalysis and 0.5 degrees for the uncertainty estimate. 
Variables utilized are 'total precipitation', the sum of large scale and convective precipitation that is the accumulated liquid and frozen water, comprising rain and snow, that falls to the Earth's surface, with 1 day accumulation period for monthly averaged reanalysis. Units are meters. 'Total cloud cover' is also used as a dimensionless quantity that varies from 0 to 1, being the proportion of a grid box covered by cloud. 'Total column water vapor', more commonly called precipitable water, is also utilized, defined as the total amount of water vapor in a colun extending from the surface of the Earth to the top of the atmosphere. This is measured in kgm^-2. A land-sea mask, a dimensionless quantity, that represents the proportion of land, as opposed to ocean or inland waters in a grid box, is also utilized. Values above 0.5 can be comprised of a mixture of land and inland water, but not ocean. 
### North Atlantic Oscillation (NAO) Index
Monthly means of the NAO index, from 1948-2021 are utilized to calculate composites for positive, negative, and neutral NAO events with total precipitation over the African monsoon land region. 
# Results and Analysis
### Project Notebook via Github
This jupyter notebook file, located in my CLIM680_project repository, contains all of the commented code that is used to fufill all aspects of the project.
Link: https://github.com/areed29/CLIM680_project/blob/master/Final_project.ipynb 
### Conda Environment 
The environment.yml file is shown to define the environment needed to run all code successfully. 
### Figures
The figures from my project notebook are saved in a seperate 'figures' subdirectory, as well as shown in the project notebook.
# Summary



