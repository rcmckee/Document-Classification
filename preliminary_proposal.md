# Patent Classification

### Purpose
Classify patent applications by the US Patent and Trademark Office (USPTO) art unit classification. Currently this is the first step in the processing of a patent application sent to the USPTO. 135 people read each application and assign it to an art unit. The turnaround time is 28 days, and the contracting firm costs about 95 million over 5 years (this might have increased). The art unit is a unit with a technological background to understand the technology in the patent application. 

### Problem
It currently takes too long and costs too much for a patent to be classified and assigned to the correct art unit. Additionally, if patent attorneys can write the patent application with the correct wording to direct the application to one art unit over another, they can increase the likelihood of the patent being granted.

### How I will present my work
I would like to have a web app to be used by friends in the legal industry. My minimum viable product would be a presentation.

### Data sources
1) USPTO
	- [USPTO bulkdata data dictionary](https://bulkdata.uspto.gov/data/patent/office/actions/bigdata/2017/USPTO%20Patent%20Prosecution%20Research%20Data_Unlocking%20Office%20Action%20Traits.pdf)
	- [USPTO public pair dataset](https://www.uspto.gov/learning-and-resources/electronic-data-products/patent-examination-research-dataset-public-pair)

2) [Google Big Query](https://cloud.google.com/bigquery/)
	- patents-public-data dataset

### Next Step
My next step is to construct an SQL query to collect the data I will need from Google Big Query. I will also need to collect additional data from the USPTO office action data bases.

#
# Art Price Prediction

### Purpose
Predict the price of art, or predict up and coming artists, specifically for western art. 

### Problem
Predicting what a painting will go for at auction or what artist would be a good investment is difficult even for a professional.

### How I will present my work
I would present a slide show

### Data sources
1) [Artnet price database](https://www.artnet.com/price-database/)
2) [Stark Museum of Art](http://starkculturalvenues.org/starkmuseum/) (Specializes in western art and buys western art regularly.)
3) [Invaluable](https://www.invaluable.com/features/artfact1000.cfm?sgID=3&groupName=American%20Painting%3A%2018th%2F19th%20Century)
4) [Mutualart](https://www.mutualart.com)
5) [Mearto](https://www.mearto.com/search)

### Next Step
My next step is to gather the data and speak with experts to get a better idea on features to target for data acquisition.

#
# College Football Quarterback Prediction

### Purpose
Predict if a high school football quarterback will perform well at the college level.

### Problem
UT seems to have great difficulty finding a good quarterback even though the Texas high schools are noted as being a top field for recruiting. If UT could more accurately predict if a high school quarterback will perform well at the college level, maybe…maybe….they could have more wins each season.

### How I will present my work
I would present a slide show or visualization.

### Data sources
1) [Maxpreps](http://www.maxpreps.com)
2) [Houston Chronical](https://www.chron.com/sports/highschool/scoreboard/)
3) [ESPN](http://www.espn.com/college-football/statistics)
4) [CBS Sports](https://www.cbssports.com/collegefootball/stats/playersort/NCAAF/QB)
5) [Football Outsiders](https://www.footballoutsiders.com/stats/qb)

### Next Step
My next step is to gather the data and speak with experts to get a better idea on features to target for data acquisition.
