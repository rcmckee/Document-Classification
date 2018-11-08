## Patent Classification Capstone

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
