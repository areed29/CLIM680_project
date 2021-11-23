# Examining Changes and Relationships between Clouds, Precipitation, and Precipitable Water in the African Monsoon Region
# Austin Reed
# Introduction
My dataset of choice is ERA5 monthly averaged data on single levels from 1979 to present, which is the fifth generation ECMWF renalysis for the global climate and weather for the past 4 to 7 decades. I plan to look at the variables of total cloud cover, total precipitation, column cloud liquid water, as well as total column cloud water vapor in Africa to answer the question: Has mean precipitable water changed significantly in the African monsoon region over the last 70 years? In which season? And how is that change related to changes in clouds? Some tools that I could use to help solve this question include looking at monthly, and seasonal anomalies over continental Africa, and explore the variance in these anomalies over recent years. This can help to pinpoint statistically significant trends in precipitation, total column precipitable water, cloud cover, and total column liquid water over continental Africa. The continent can be further broken up into sub-regions to highlight the impact of the African monsoon. 
# Data
The datasets used in my project are:
### ERA 5 Monthly Mean Data on Single Levels, from 1979-present
Replacing the ERA-interim reanalysis, ERA5 is the fifth generation ECMWF reanalysis for the global climate and weather for the past 4 to 7 decades. Using data from 1979 onwards, ERA5 provides monthly estimates for a large number of atmospheric, ocean-wave, and land-surface quantities. Data has been regridded to a regular lat-lon grid of 0.25 degrees for the reanalysis and 0.5 degrees for the uncertainty estimate. 
Variables utilized are 'total precipitation', the sum of large scale and convective precipitation that is the accumulated liquid and frozen water, comprising rain and snow, that falls to the Earth's surface, with 1 day accumulation period for monthly averaged reanalysis. Units are meters. 'Total cloud cover' is also used as a dimensionless quantity that varies from 0 to 1, being the proportion of a grid box covered by cloud. 'Total column water vapor', more commonly called precipitable water, is also utilized, defined as the total amount of water vapor in a colun extending from the surface of the Earth to the top of the atmosphere. This is measured in kgm^-2. A land-sea mask, a dimensionless quantity, that represents the proportion of land, as opposed to ocean or inland waters in a grid box, is also utilized. Values above 0.5 can be comprised of a mixture of land and inland water, but not ocean. 
### Atlantic Meridioal Oscillation (AMO) Index
Monthly means of the detrended AMO index, from 1979-2020 are utilized to calculate composites for positive and negative AMO events with total precipitation over the African monsoon land region. This is further explored for the Sahel region, where worldwide SST anomalies are found to modulate summer Sahel rainfall.
# Results and Analysis
### Project Notebook via Github
Located within my CLIM680_project repository is a series of jupyter notebooks that contain all of the labeled and commented code that was used in my analysis. 
[Link:] (https://github.com/areed29/CLIM680_project/) 
Each topic will be discussed, along with a link to each relevant notebook. 
### Conda Environment 
The environment.yml file is shown to define the environment needed to run all code successfully. 
### Figures
The figures from my project notebook are saved in a seperate 'figures' subdirectory, as well as shown in the project notebook.
### Climatology and Anomalies 
A panel plot of the climatology of monthly averaged precipitation (in meters), monthly averaged cloud cover, and monthly averaged precipitable water was plotted for each month, in order to observe differences in the monthly/seasonal cycle, and spatial variability. The largest amount of cloud cover is located around 0-20S in DJF, gradually shifting north by MAM, and then furthest north in a band between 5S-15N by the JJA rainy season. Precipitable water shows similar patterns, with highest values concentrated near the Gulf of Ginuea. The precipitation climatology also shows this northward shift in the rainy season.
### Subsetting: Exploring Climatology/Anomalies for Sahel region
For the Sahel lat/lon point of 15N,10E, the climatology was compared with data for the starting and ending years of the dataset (1979 and 2020) for each variable. For precipitation and precipitable water, the peak in climatology comes during the midst of the rainy season during the months of JJA. Cloud cover is the most variable over each month, still peaking on average in the rainy season. The anomaly space is then visualized for each of the 3 variables for the Sahel grid point, with a best-fit trend line superimposed over each time series. The most significant trend is for cloud cover anomalies over the Sahel region, with a trend of 0.03 (fraction/month).
### Composites and mean differences with AMO
Next, composite analysis is performed on continetal Africa precipitation anomalies with the detrended AMO index. Warm and cold AMO events are respectively categorized as an SSTA (Sea Surface Temperature Anomaly) as being greater than or less than 0. For the precipitation data, the climatology and anomlaies were calculated exclusively for land data, masking out grid cells in the domain for the ocean. Precipitation anomalies were then normalized by the standard deviation, in order to reduce data redundancy and create unitless anomalies, which also makes comparison amongst variables easier. The precip anomalies were then selected according to if they matched a month containing a warm or cold AMO index, where a mean was then taken over the time dimension. Composite precipitation anomalies during warm and cold AMO events over continental Africa were plotted. The plot indicates that for warm AMO events, negative precipitation anomalies seem to be found from 5N-15S, with positive precipitation anomalies found in this region for cold AMO events. A plot of mean differences between warm AMO precip composites and cold AMO precip composites was plotted, with areas of statistical significance hatched off using the 95th confidence interval. 
### Correlation Analysis with AMO

### Regression Analysis with AMO


# Summary



