## Patent Classification Capstone

### Purpose
Classify patent applications by the US Patent and Trademark Office (USPTO) art unit classification. Currently this is the first step in the processing of a patent application sent to the USPTO. 135 people read each application and assign it to an art unit. The turnaround time is 28 days, and the contracting firm costs about 95 million over 5 years (this might have increased). The art unit is a unit with a technological background to understand the technology in the patent application. 

### Problem
It currently takes too long and costs too much for a patent to be classified and assigned to the correct art unit. Additionally, if patent attorneys can write the patent application with the correct wording to direct the application to one art unit over another, they can increase the likelihood of the patent being granted.

**Hardest and Easiest art units as of 2016:**

![image from ipwatchdog.com](http://www.ipwatchdog.com/wp-content/uploads/2015/05/Figure-1.png)
![image from ipwatchdog.com](http://www.ipwatchdog.com/wp-content/uploads/2015/05/Figure-2.png)

### Prior Solutions To This Problem
- [Deep learning and IPC codes](file:///Users/rcm/Downloads/25866373.pdf)
- [Title and abstract used for classification](https://patinformatics.com/machine-learning-in-patent-analytics-part-2-binary-classification-for-prioritizing-search-results/)
- [WIPO patent applications and IPC codes](http://users.softlab.ntua.gr/facilities/public/AD/Text%20Categorization/Automated%20Categorization%20in%20the%20International%20Patent%20Classification.pdf)
- [Automated Patent Categorization and Guided Patent Search using IPC as Inspired by MeSH and PubMed](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3632996/)
- [Automated Patent Classification using IPC codes](http://cs229.stanford.edu/proj2011/ChristopherLinSpieckermann-AutomatedPatentClassification.pdf)
- [Measuring patent claim breadth using Google Patents Public Datasets](https://cloud.google.com/blog/products/ai-machine-learning/measuring-patent-claim-breadth-using-google-patents-public-datasets)

### My Approach
I will be focusing my classification on US Patent Classification codes which are used to assign the application to an art unit in the US. Prior approaches focused on the International Patent Classification.

### Who Cares?
The US is one of the main countries for companies to get patent protection. Because of the expense of patents (ranging from $10,000 - $40,000) it is important for inventors and attorneys to avoid obstacles like a difficult art unit which can increase the cost of the application and lead to an application not getting granted.

If successful, attorneys could draft and file their applications with more confidence that it will avoid immediate rejections from the patent office.

### How I will present my work
I would like to have a classification web app to be used by friends in the legal industry. My minimum viable product would be a presentation showing clusters of patent applications and the accuracy of the classification algorithms.

### Data sources
1) USPTO
	- [USPTO bulkdata data dictionary](https://bulkdata.uspto.gov/data/patent/office/actions/bigdata/2017/USPTO%20Patent%20Prosecution%20Research%20Data_Unlocking%20Office%20Action%20Traits.pdf)
	- [USPTO public pair dataset](https://www.uspto.gov/learning-and-resources/electronic-data-products/patent-examination-research-dataset-public-pair)

2) [Google Big Query](https://cloud.google.com/bigquery/)
	- patents-public-data dataset
	- SQL table (28gb and 1.4tb)
	
### Potential Problems
- Incomplete labeling of art units: I am using USPC codes to assign missing art unit values in the data set.

### Next Step
~~My next step is to construct an SQL query to collect the data I will need from Google Big Query. I will also need to collect additional data from the USPTO office action data bases.~~
- Fill in missing art unit values using USPC codes.
