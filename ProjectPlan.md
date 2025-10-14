# Project Plan - NBA Salary and Performance Data Management

## Overview - 
The goal for our project is to design and implement a reproducible data management lifecycle. Our project will apply several modules and aspects of IS 477 on the game of Basketball, exploring the relationship between player performance and salaries in the NBA. Basketball has grown into a Sport that utilizes analytics and data for many different decisions. Our team will act as a Data Analyst for a NBA team, creating a structured and repeataable workflow that will follow the FAIR principles. We will follow Data Management and Curation techniques and best practices to get the best results in our project. Our goal is to be able to create a reproducible project by creating documentation and providing sufficient information while making sure we comply with terms of use and accurately cite any data and software used. Overall we want to create a well organized and quality Data Analaysis on the game of Basketball.

## Research Question - Is there a Correlation between Basketball Salary and Player Efficiency? Which Performance metrics are most predictive of a higher Salary? 
These questions are significant because it connects Data with real decisions NBA General Managers have to make everyday. Being able to understand which metrics are most important for higher salaries will allow Executives to craft the best team they can. The questions can be answered utilizing the correct datasets and data science techniques. 

## Team - We will be splitting responsibilities by Module.
Michael Parinas - Lead work on Even Modules (Ethical Data Handling, Storage and Organization, Extraction and Enrichment, Data Integration, Data Cleaning, Workflow Automation and Provenance, Metadata and Data Documentation)

Richard Taing - Lead work on Odd Modules (Data Lifecycle, Data Collection and Acquisition, Storage and Organization, Data Integration, Data Quality, Workflow Automation and Provenance, Reproducibility and Transparency)

Both members will be supporting the lead to make sure each member has coverage on all modules.

## Datasets - 
Dataset 1 - https://www.kaggle.com/datasets/ratin21/nba-player-salaries-2000-2025. This Dataset contains NBA salaries from the Season 2000 to the Season 2025. Includes Player Name, Salary, and Season. This dataset will be used to  analyze salary trends. This will serve as the foundation for our dependent variable of Salary. We will evaluate the dataset's ethical and legal compliance, also making sure it follows FAIR principles. Any concerns or gaps will be documented.

Dataset 2 - https://www.kaggle.com/datasets/flynn28/historical-nba-player-stats-database/data This Dataset contains seasonal statistics for NBA players. Stats include points, rebounds, assists, steals, blocks, and other performance stats. This dataset will be used to measure correlations between salaries. These metrics will serve as the independent variable for our analysis. We will evaluate the dataset's ethical and legal compliance, also making sure it follows FAIR principles. Any concerns or gaps will be documented.

## Timeline - Our Project will span the final weeks of the class. (6 - 7 Weeks)

Week 1 - Finalize research questions, confirm datasets, initial dataset inspection to identify key variables. Create script to acquire data and check integrity, along with documentation. (Both)

Week 2 - Identify Ethical, Legal, and Policy constraints. Select and describe a specific storage and organization strategy. Create Script to load data into a relational database, along with documentation. (Michael)

Week 3 - Extraction and Enrichment and Data Integration. Create scripts used to integrate datasets. Create models, along with documentation. (Richard)

Week 4 - Document data quality and Clean Data. Create scripts use to profile and clean data, along with documentation. Scripts used to create regression analysis and find correlation. Create visualizations, along with documentation. (Michael)

Week 5 - Workflow automation and Provenance. Automate end-to-end analysis workflow. Document describing how to repeat our project. (Richard)

Week 6 - Reproducibility and Transparency and Metadata and Data Documentation. Create Data Dictionary and Codebook. Create descriptive metadata that describes our project. (Both)

## Constraints - 
- Data limitations: The Kaggle datasets we plan to use may not include complete or up-to-date data for the 2025 NBA season, since community-contributed data does not update as fast as the official documented data. There are also some missing records or inconsistent updates that could affect the accuracy of our analysis, especially for recent players.
- Ethical/legal restrictions: Dataset 1 is licensed under CC0: Public Domain, allowing free use and redistribution. Dataset 2 is licensed under MIT License, which permits use with attribution. We must ensure proper citation and comply with Kaggle's terms of service, which may restrict how we redistribute raw data files in our GitHub repository. Also, even though the data is publicly available, using player names and salary information involves privacy and fairness considerations. Players’ salaries are public because of league transparency policies, but we must avoid misuse or misrepresentation of this information. 


## Gaps - 
First, we need to confirm data licenses and whether redistribution or transformation is allowed. Checking rules for Data Licensing and Redistribution of raw Kaggle data may be limited by terms of use, requiring clear documentation instead of direct sharing. We must ensure that we are in compliance with these terms and will avoid including copyrighted or restricted data directly in our GitHub repository. We will review the dataset pages for license details and reach out to the dataset creators if necessary. If redistribution is restricted, we will provide documentation and code for data acquisition instead of including the raw data in our repository. 

Second, the historical stats dataset may lack advanced analytics metrics (e.g., Win Shares, Player Efficiency Rating, Box Plus/Minus, Usage Rate) that could provide stronger predictive power for salary analysis. If the initial correlation results are weak with basic statistics, we may need to calculate derived metrics or source additional data to enhance our analysis.

Finally, we need to finalize our approach for integrating the two datasets effectively. This involves determining the most reliable way to join player salary data with historical performance statistics, ensuring consistency across both sources. Some challenges include name and date formatting discrepancies between datasets. To address these issues, we plan to design a data integration schema that defines clear rules for merging, including name normalization methods, season alignment logic, and handling of unmatched entries. Before implementing the full data pipeline, we will consult our instructor for feedback to ensure our schema is both technically sound and analytically appropriate for our project goals.

