## Patent Classification Capstone

### Final Notebook and model can be found in [Patent_Classification.ipynb](https://github.com/rcmckee/dsi-Capstone/blob/master/Patent_Classification.ipynb)
Also available as a [google colab notebook](https://colab.research.google.com/github/rcmckee/dsi-Capstone/blob/master/Patent_Classification.ipynb)

A tensorflow version is available in a [google colab notebook](https://colab.research.google.com/drive/1DjOyXyjUF_6kCuTWkow8EMvSiNtD5BIH)

### Purpose
The purpose of this project is to identify which group of people (art unit) at the US patent office (USPTO) will review a new patent application. The art unit is a group of patent examiners with the technological background to understand the technology in the patent application. Currently, this is the first step in the processing of a patent application sent to the USPTO. The USPTO sends the application to a contractor where 135 people read each application and assign it to an art unit. The turnaround time is [28 days](https://www.serco-na.com/news/press-releases/detail/2194/serco-processes-2-millionth-patent-application-for-u-s), and the USPTO pays the contractor 95 million over 5 years ([Citation](https://www.serco-na.com/news/press-releases/detail/12520/serco-awarded-95-million-patent-classification-contract)). 

### Problem
It currently takes too long and costs too much for a patent to be classified and assigned to the correct art unit. Additionally, if patent attorneys can write the patent application with the correct wording to direct the application to one art unit over another, they can increase the likelihood of the patent being granted.

**For example**, patent applications that land in art unit 3681, which handles “transportation, construction, electronic commerce, agriculture, national security and license & review,” have about a 29.8% chance of maturing into a patent.  And even if you are lucky enough to be one of the 29.8%, it is likely to take over four years to grant.  But get your patent applications into art unit 3688, which the USPTO describes as handling the exact same subject matter as 3681, and your chances of allowance jump up to about 81%, with an average time to issuance of around 2 years ([Citation](http://www.ipwatchdog.com/2016/04/14/better-way-file-patent-applications/id=68302/)).

**[The hardest and easiest art units.](http://www.ipwatchdog.com/2015/05/21/hardest-easiest-art-units/id=57864/):**

![image from ipwatchdog.com](http://www.ipwatchdog.com/wp-content/uploads/2015/05/Figure-1.png)
![image from ipwatchdog.com](http://www.ipwatchdog.com/wp-content/uploads/2015/05/Figure-2.png)

**Alice case law is a major factor preventing software related patents**
Alice Corporation Pty. Ltd. v. CLS Bank International, 573 U.S. ___ (2014) is a case that essentially said any patent that relates to performing an economic activity on a computer is possibly an abstract idea and not patentable. Avoiding Alice rejections is a big concern for patent attorneys. Once you receive an Alice rejection you are less likely to get the patent granted.

[**Art units with most Alice rejections**](http://www.ipwatchdog.com/2015/12/14/the-most-likely-art-units-for-alice-rejections/id=63829/)

![image from ipwatchdog.com](http://www.ipwatchdog.com/wp-content/uploads/2015/12/Figure-1.jpg)

### Prior Solutions To This Problem
- [LexisNexis Pathways](https://www.lexisnexisip.com/products/pathways/)
- [Deep learning and IPC codes](https://www.atlantis-press.com/php/download_paper.php?id=25866373)
- [Title and abstract used for classification](https://patinformatics.com/machine-learning-in-patent-analytics-part-2-binary-classification-for-prioritizing-search-results/)
- [WIPO patent applications and IPC codes](http://users.softlab.ntua.gr/facilities/public/AD/Text%20Categorization/Automated%20Categorization%20in%20the%20International%20Patent%20Classification.pdf)
- [Automated Patent Categorization and Guided Patent Search using IPC as Inspired by MeSH and PubMed](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3632996/)
- [Automated Patent Classification using IPC codes](http://cs229.stanford.edu/proj2011/ChristopherLinSpieckermann-AutomatedPatentClassification.pdf)
- [Measuring patent claim breadth using Google Patents Public Datasets](https://cloud.google.com/blog/products/ai-machine-learning/measuring-patent-claim-breadth-using-google-patents-public-datasets)

### My Approach
I will be focusing my classification on art units of the USPTO. The use of classification codes is confusing because they must then be converted into an art unit, which is often used to describe rejection rates. Additionally, the only tools available for lawyers to utilize are behind expensive paywalls.

I will first utilize a binary classification such as, does the application belong in art unit 2100 or not. I will then utilize multi-class classification which will determine which of the hundreds of art units the application belongs in. I will utilize numerous algorithms for multi-class classification, including Decision trees, SVM, KNN classifiers, and nural networks.

**Baseline Metric**
To determine if the model is an improvement over the current solutions I will use two sources as a range for accuracy. On the high end of the range is the [97% accuracy](https://www.serco-na.com/news/press-releases/detail/2194/serco-processes-2-millionth-patent-application-for-u-s) stated by the contracting firm that currently classifies the patent applications. On the low end I will use an estimate by a patent attorney who estimates that the contractor correctly classifies patent applications [90%](http://www.ipwatchdog.com/2014/03/11/when-uspto-classifies-an-application-incorrectly/id=48457/) of the time.

### Who Cares?
The US is one of the main countries for companies to get patent protection. Because of the expense of patents (ranging from $10,000 - $40,000) it is important for inventors and attorneys to avoid obstacles like a difficult art unit which can increase the cost of the application and lead to an application not getting granted.

If successful, attorneys could draft and file their applications with more confidence that it will avoid immediate rejections from the patent office.

Additionally, the US Patent office could reduce costs and turnaround time by utilizing the automated model. 

### How I will present my work
I plan to have a classification web app to be used by friends in the legal industry. Visualizations may include word clouds showing the important words in different classes to give information as to what to include to ensure the patent application gets to the art unit the patent attorney wants. It would be for demonstration purposes only until I could ensure no data is recorded and no data is able to be read by anyone other than the lawyer. This is due to issues of client confidentiality and issues relating to publication date of inventions. These issues require a lot of text to explain, but the summary is: the lawyer doesn't want to risk losing their license or losing any pantent rights for their client.

### Data sources
1) USPTO
	- [USPTO bulkdata data dictionary](https://bulkdata.uspto.gov/data/patent/office/actions/bigdata/2017/USPTO%20Patent%20Prosecution%20Research%20Data_Unlocking%20Office%20Action%20Traits.pdf)
	- [USPTO public pair dataset](https://www.uspto.gov/learning-and-resources/electronic-data-products/patent-examination-research-dataset-public-pair)

2) [Google Big Query](https://cloud.google.com/bigquery/)
	- patents-public-data dataset
	- SQL table (28gb and 1.4tb)
	
### Potential Problems
- Incomplete labeling of art units: I am using USPC codes to assign missing art unit values in the data set. There are hundreds of codes and labels to assign. This could take up a large amount of time.

### Next Step
- Fill in missing art unit values for 3600 and 2100 art units using [USPC codes](https://www.uspto.gov/patents-application-process/patent-search/understanding-patent-classifications/patent-classification).
- Exploratory Data Analysis (EDA) to look for issues of imbalanced classes.
- Build and train models using Google Cloud Platform since I am acquiring the data using SQL from Google BigQuery. I will spend less time moving data between platforms like AWS so I can spend more time on the modeling.
	- Binary Classification: is it 2100 or not?
	- Multi-class Classification: is it 2121, 2129, 3689, 3622, 3629, and other art units in the 3600 range.
- Deploy the model as a web app
