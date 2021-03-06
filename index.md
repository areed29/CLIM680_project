# Examining Changes and Relationships between Clouds, Precipitation, and Precipitable Water in the African Monsoon Region
# By Austin Reed

# Introduction

The West African monsoon is a very interesting atmospheric phenomena that is characterized by westward propogating synoptic scale disturbances that cross Western Africa during the Summer, approximately May through October (Pedgley et al 1975). It has been suggested that the kinetic energy in these cyclonic wave troughs may be derived from instabilities in the horizontal and vertical shears of the lower tropospheric African Easterly Jet, usually present near 700mb and 15 degrees North (Burpee 1972). First recognized in the 1920s, there are many unanswered questions in the persuit of fully understanding the monsoon cycle. This includes struggles in fully representing the extensive and presistent low-level clouds over southern West Africa during the Boreal Summer. It has been shown that relatively minor errors, variations, or trends in low-level cloudiness over southern West Africa can have substantial impacts on precipitation (Kniffka et al. 2019). With a warming world, it is very relevant to ask how this phenomena has changed in the past, and how it will continue to change. In this project, the monthly averaged variables of total cloud cover, total precipitation, and total column water vapor will be analyzed over the domain of Africa to tackle if these variables have changed significantly in the African monsoon region. Analysis will include but are not limited to climatology and anomaly calcuations, correlations, linear regressions, and composites.

Oceanic patterns can also have a significant impact on climate variability in Africa. This work looks at the Atlantic Multidecadal Oscillation (AMO), which refers to the near global scale mode of observed multidecadal climate variability with alternating warm and cool SST phases over large parts of the Northern Hemisphere. Previous work has shown that warm AMO phases have a direct linkage to increased precipitation in the Sahel region, with cold AMO phases causing decreased precipitation in this region (Knight et al 2006). With this motivation, impacts of the AMO on cloud cover, precipitation, and precipitable water over the African monsoon region will be analyzed.

# Data
The datasets used in my project are:
### ERA 5 Monthly Mean Data on Single Levels, from 1979-present

Replacing the ERA-interim reanalysis, ERA5 is the fifth generation ECMWF reanalysis for the global climate and weather for the past 4 to 7 decades. Using data from 1979 onwards, ERA5 provides monthly estimates for a large number of atmospheric, ocean-wave, and land-surface quantities. Data has been regridded to a regular lat-lon grid of 0.25 degrees for the reanalysis and 0.5 degrees for the uncertainty estimate. 

Variables utilized are 'total precipitation', the sum of large scale and convective precipitation that is the accumulated liquid and frozen water, comprising rain and snow, that falls to the Earth's surface, with 1 day accumulation period for monthly averaged reanalysis. Units are meters. 'Total cloud cover' is also used as a dimensionless quantity that varies from 0 to 1, being the proportion of a grid box covered by cloud. 'Total column water vapor', more commonly called precipitable water, is also utilized, defined as the total amount of water vapor in a colun extending from the surface of the Earth to the top of the atmosphere. This is measured in kgm^-2. A land-sea mask, a dimensionless quantity, that represents the proportion of land, as opposed to ocean or inland waters in a grid box, is also utilized. Values above 0.5 can be comprised of a mixture of land and inland water, but not ocean (Hersbach et al 2019). 

[Link to dataset description](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels-monthly-means?tab=overview)
### Atlantic Meridional Oscillation (AMO) Index

Monthly means of the *detrended* AMO index, from 1979-2020 are utilized to calculate composites for positive and negative AMO events with total precipitation over the African monsoon land region. This is further explored for the Sahel region, where worldwide SST anomalies are found to modulate summer Sahel rainfall.

![AMO Index (with warming signal)](figures/AMO_defined.png)

[Link to NOAA PSL AMO index description](https://psl.noaa.gov/data/timeseries/AMO/)
# Results and Analysis
### Project Notebook via Github
Located within my CLIM680_project repository is a series of jupyter notebooks that contain all of the labeled and commented code that was used in my analysis. 
[Link:](https://github.com/areed29/CLIM680_project/) 

Each topic will be discussed seperately, along with a link to each relevant notebook. 
### Conda Environment 
The environment.yml file is shown to define the environment needed to run all code successfully. 
### Function creation
A function was created to calculate climatologies and anomalies in the file climo_anoms_function.py, labeled as climo and anoms in each jupyter notebook. This is in addition to the clim680 function generated in class to calculate xyticks.

[Link to xyticks function](https://github.com/areed29/CLIM680_project/blob/master/clim680_function.py)

[Link to climo,anoms function](https://github.com/areed29/CLIM680_project/blob/master/climo_anoms_function.py)
### Figures
The figures from my project notebook are saved in a seperate 'figures' subdirectory, as well as shown in the project notebook.

[Link to figures](https://github.com/areed29/CLIM680_project/tree/master/figures)
### Climatology and Anomalies 

A panel plot of the climatology of monthly averaged precipitation (in meters), monthly averaged cloud cover, and monthly averaged precipitable water (in kg/m^2) was plotted for each month, in order to observe differences in the monthly/seasonal cycle, and spatial variability. The largest amount of cloud cover is located around 0-20S in DJF (December, Janurary, February), gradually shifting north by MAM (March, April, May), and then furthest north in a band between 5S-15N by the JJA (June, July, August) rainy season. Precipitable water shows similar patterns, with highest values concentrated near the Gulf of Ginuea. The precipitation climatology, which is plotted in powers of 2 to highlight nonlinearity, also shows this northward shift in the rainy season.

![Climatology of Monthly averaged cloud cover over Africa](figures/12panelclimo_clouds.png)

![Climatology of Monthly averaged Precipitation over Africa (in meters)](figures/12panelclimo_precip.png)

![Climatology of Monthly averaged cloud cover over Africa (in kg/m^2)](figures/12panelclimo_tcwv.png)

[Jupyter notebook link](https://github.com/areed29/CLIM680_project/blob/master/Africamonthlyclimo_assignment2.ipynb)



### Subsetting: Exploring Climatology/Anomalies for Sahel region

For the Sahel lat/lon point of 15N,10E, the climatology was compared with data for the starting and ending years of the dataset (1979 and 2020) for each variable. For precipitation and precipitable water, the peak in climatology comes during the midst of the rainy season during the months of JJA. Cloud cover is the most variable over each month, still peaking on average in the rainy season. The anomaly space is then visualized for each of the 3 variables for the Sahel grid point, with a best-fit trend line superimposed over each time series. The most significant trend is for cloud cover anomalies over the Sahel region, with a trend of 0.03 (fraction/month).

![Sahel climatology](figures/Sahel_climo.png)
[Jupyter notebook link](https://github.com/areed29/CLIM680_project/blob/master/Sahel_climo_anoms.ipynb)
### Composites and mean differences with AMO

Next, composite analysis is performed on continetal Africa precipitation, precipitable water, and cloud cover anomalies with the AMO index. Warm and cold AMO events are respectively categorized as an SSTA (Sea Surface Temperature Anomaly) as being greater than or less than 0. For the precipitation data, the climatology and anomlaies were calculated exclusively for land data, masking out grid cells in the domain for the ocean. Precipitation anomalies were then normalized by the standard deviation, in order to reduce data redundancy and create unitless anomalies, which also makes comparison amongst variables easier. The precipitation anomalies were then selected according to if they matched a month containing a warm or cold AMO index, where a mean was then taken over the time dimension. This method was followed for both the cloud cover and precipitable water variables as well. Composite precipitation anomalies during warm and cold AMO events over continental Africa were then plotted. The plot indicates that for warm AMO events, negative precipitation anomalies seem to be found from 5N-15S, with positive precipitation anomalies found in this region for cold AMO events. A plot of mean differences between warm AMO precipitation composites and cold AMO precipitation composites were visualized, with areas of statistical significance hatched off using the 95th confidence interval. The resulting plot indicates statistically significant areas of composite precipitation differences between warm AMO and cold AMO events found in inland Africa from 5N- ~15S. I plan to further investigate the composite between AMO events and precipitation anomalies looking specifically at the JJA rainy season. For total cloud cover, this area of significance follows, except that it extends further south to 15S. For precipitable water, it is interesting to note that the mean difference of Warm AMO-Cold AMO was not deemed different enough to be significant at the 95th confidence level. 


![Composites and mean differences with the AMO, with areas of statistical significance hatched off](figures/composite_anoms_differences_significance_allvars.png)

[Jupyter notebook link](https://github.com/areed29/CLIM680_project/blob/master/AMO_composite-all_vars.ipynb)
### Correlation Analysis with AMO

For correlation analysis, correlation of each of the 3 variables (total cloud cover, total precipitation, and precipitable water) with the AMO index was investigated. After loading in the AMO index, precipitation data was selected to match the same amount of months as the AMO index. The dataset was once again masked to include only land values, with the resulting climatologies and anomalies calculated. Anomalies were once again normalzied by the standard deviation of each variable. A grid point representing the Sahel region was then selected to analyze correlation between normalized precipitation anomalies with the AMO index. The correlation coefficient was determined to be 0.14, so it was determined that these 2 variables have a very weak linear relationship. This will motivate the next part of my project, as I will seperate the data into seasons, where I suspect that these 2 variables will become much more correlated. For each of the 3 variables, correlation with the AMO index was then plotted over the entire domain of Africa, with areas of statistical significance at the 95% confidence level hatched off. From 0-10S, there seems to be a statistically significant negative correlation between clouds and the AMO index and precipitation and the AMO index, with a weak statistically significant positive correlation found in the Sahel region. For precipitable water, there is a somewhat stronger statistically significant positive correlation found with the AMO index in the region from 10N-35N. 

![Sahel Time series of normalized AMO index with normalized precipitation anomalies](figures/Sahel_AMO_precip_timeseries.png)
![Correlation Analysis with the AMO, with areas of statistical significance hatched off](figures/Correlation_AMO_allanoms_withsig.png)

[Jupyter notebook link](https://github.com/areed29/CLIM680_project/blob/master/CorrelationAnalysis_AMO_precip.ipynb)
### Regression Analysis with AMO

For linear regression analysis, anomalies were once again calculated for each of the 3 variables, first applied without any masking or weighting. Next, the anomalies were once again normalized by each variable's standard deviation. Then, the masking over land and area-weighting was applied. Weighting over the domain was applied using the cosine of the latitude. Using these normalized, masked, and area-weighted anomalies, a linear regression was applied between each of the 3 variables, as well as each of the variables with the AMO index. First, the regression was applied between the cloud cover anomaly and precipitation anomaly time series. A slope of 0.36 and r-squared value of 0.4 was found as a result. For a linear regression between precipitation anomalies and precipitable water anomalies, a slope of 1.04 was found, with an r-squared value of 0.19. Between cloud cover and precipitable water, a slope of 0.82 was found, with an r-squred value of 0.36. When each of these variables were regressed with the AMO index, negative trends were found for both precipitation anomalies and total cloud cover anomalies, with slopes of -0.27/degC and -0.06/degC respectively. The only variable that had a positive trend when regressed with the AMO index was precipitable water, with a slope value of 0.13/degC. A panel plot map of linear regression with each of the 3 variables (total cloud cover, total precipitation, and precipitable water) is then shown, with statistically significant regression coefficients at the 95% confidence level indicated by the hatchings. Based on this map, areas of significance of the negative slope between precipitation anomalies and the AMO Index are found in the rainforest/grassland region of Central Africa, with similar results for the negative slope between cloud cover anomalies and the AMO Index. Notably, as expected, an area of statistical significance is found in the positive trend area between precipitation anomalies and the AMO index in the Sahel region. If further broken into seasons, I hypothesize that this statistically significant positive trend area would be greatly enhanced for the JJA rainy season. For precipitable water, statistically significant positive trends are found to be more zonally symmetric between 10N-30N. The slope for each variable are then written to an xarray dataset and a seperate netcdf file.

![Normalized, Continental,Weighted Anomalies over Africa, with a best fit trend line](figures/cont_norm_weighted_anoms_withtrend.png)
![Regression with clouds and precip](figures/regression_clouds_precip.png)

![Regression with clouds and precipitable water](figures/regression_clouds_tcwv.png)

![Regression with precip and precipitable water](figures/regression_precip_tcwv.png)
![Regression Analysis with the AMO, with areas of statistical significance hatched off](figures/regressionmap_AMO_allanoms_withsig.png)

[Jupyter notebook link](https://github.com/areed29/CLIM680_project/blob/master/Regression_Analysis_AMO_precip.ipynb)
# Summary, Discussion, and Future Work

Each result found from the various calculations can be further broken down, and attributed to a physical/dynamical cause. For the correlation analysis, there is no real correlation found between precipitation and the AMO index over the Sahara region. Although there is a statistically significant positive correlation found here with the AMO Index, it can be stated that changes in cloudiness are not producing rainfall. It is also noticeable that there is reduced rainfall in the Congo region during warm AMO events, with a statistically significant negative correlation found between the AMO Index and precipitation. This would pose the question: has there been any shift in rainfall as a result of the AMO phase? In order to fully answer this, the analysis would have to be performed with an unmasked array, and the domain would have to be extended out in order to see if rainfall was focused over water, or if there are shifts found in the variability present. Additionally, looking at smaller samples would be more fruitful, since all zones of Africa were averaged in this analysis, with each zone containing unique relationships with different climatology and annual/seasonal cycles present.

It can also be noted that in this analysis, the spatial regression and correlation maps are not exact (albeit close). This is attributed to the fact that the normalized anomalies are used for the calcuations. The covariance that is used to calculate correlation intrinsically creates normalization; so including a normalized anomaly before the covariance is calculated is redundant. It would also be more fruitful to de-trend both time series, effectively reducing any trend present in both the precipitation, cloud cover, and precipitable water variables, in addition to the AMO when performing these analyses. *Regarding the AMO analysis itself, although the NOAA PSL claims that the time series is de-trended, there still appears to be a significant warming signal present in the evolution of the index from 1979-2020. In order to subtract out that warming signal, a linear regression can be performed on the AMO time series, with the trend line subtracted out of the index. It appears that the de-trending is calculated on the much longer time series, with data extending back to 1861, so this warming signal is still present on this shorter time scale.* Future work includes a more reliable calculation of the AMO, where an area-average of the North Atlantic SSTs can be performed from 0 to 70N using data from ERA5 (consistent with other variables), with a global warming signal subtracted out.

Other future work includes the use of a Thiel-Sen Regression as opposed to an ordinary least-squares estimator, which would be more robust against outliers. Additionally, a wavelet analysis can be performed, effectively creating a 2D plot of variance (power function) as a function of period and time. In addition to fitting a line to each time series, it would be equally interesting to fit another periodic function, such as a sine wave, to compare results. 

Although this analysis looked at anoamlies for the annual cycle, it would be of great interest to explore seasonal variability, especially since the West African monsoon is a seasonal phenomena that has a rainy season in JJA (June, July, August) when the ITCZ shifts northward. Isolating each calcuation for seasons can yield some more interesting results that can be compared to previous findings in the literature. 

# References
AMO unsmoothed, detrended from the Kaplan SST V2, Calculated at NOAA PSL1. http://www.psl.noaa.gov/data/timeseries/AMO/

Hersbach, H., Bell, B., Berrisford, P., Biavati, G., Hor??nyi, A., Mu??oz Sabater, J., Nicolas, J., Peubey, C., Radu, R., Rozum, I., Schepers, D., Simmons, A., Soci, C., Dee, D., Th??paut, J-N. (2019): ERA5 monthly averaged data on single levels from 1979 to present. Copernicus Climate Change Service (C3S) Climate Data Store (CDS). (Accessed on < 13-10-2021 >), 10.24381/cds.f17050d7

Kniffka, A., Knippertz, P., &amp; Fink, A. H. (2019). The role of low-level clouds in the West African Monsoon System. Atmospheric Chemistry and Physics, 19(3), 1623???1647. https://doi.org/10.5194/acp-19-1623-2019 

Knight, J. R.,C. K. Folland, and A. A. Scaife (2006), Climate impacts of the Atlantic Multidecadal Oscillation, Geophys. Res. Lett., 33, L17706, doi:10.1029/2006GL026242. 

Pedgley, D. E., & Krishnamurti, T. N. (1976). Structure and Behavior of a Monsoon Cyclone over West Africa, Monthly Weather Review, 104(2), 149-167. Retrieved Dec 1, 2021, from https://journals.ametsoc.org/view/journals/mwre/104/2/1520-0493_1976_104_0149_saboam_2_0_co_2.xml

# Acknowledgements
I would like to thank both the CLIM680 instructors Prof. Dirmeyer and Prof. Burls for coding assistance and answering questions, as well as my advisor Prof. Kinter for dataset selection, project inspiration, and interesting discussions this semester.