# Airbnb-Pricing-and-Crime-in-Seattle
### Team Member: Chenchen Jiang, Hui Du, Jianjian Liu, Jiayang Liu



In this project, we analyzed the relationships between consumer concerned features (accommodates, bedroom number, bathroom number, beds number, review rating score, neighborhood, room type and bathroom type) and lasted Airbnb rental price (2023-2024) in Seattle. We also considered crime data (2008-2024) as a potential factor by merging it into the main Airbnb dataset.  <br>


Raw datasets from [Airbnb](https://insideairbnb.com/) and [Data.Seattle.gov](https://data.seattle.gov/Public-Safety/SPD-Crime-Data-2008-Present/tazs-3rd5/about_data) were cleansed by replacing and dropping missing values, and categorical features were converted into one-hot encoding format. We explored both of Airbnb and Crime datasets through visualization to better understand the data distribution before modelling. <br>

We utilized three machine learning models—Linear Regression, Random Forest, and Gradient Boosting—for predicting suggested listing prices. Techniques such as Stacking and Bagging were applied respectively to optimize model performance. As a result, the Gradient Boosted model showed the best performance, evaluated using parameters including MSE, MAE, R2, and the residual curve. <br>

Furthermore, to provide user-friendly interface in applying our model, an online application was build by Streamlit, and we also generated a docker image for our applicaiton. In summary, this project represents an innovative and beneficial use of data science as it empowers property owners to make data-informed decisions before they list their homes.<br>

<br>

**Workflow Chart**

![workflow](https://github.com/jiangchenchen000/Airbnb-Pricing-and-Crime-in-Seattle/assets/122926291/ad679cb3-ce38-4bde-bf53-822a07ffb68f)

* `Online Streamlit Application`: [Airbnb Pricing and Crime in Seattle](https://airpricing.streamlit.app/)

## File Folder
* `data preprocessing`: dataset cleansing and preprocessing
* `modeling`: model initiation and optimization
* `project-demo`: data exploration and visualization, Steamlit application deployment
* `files`: Business Proposal, Presentation PPT and Final Report
* `assets`: photo used in the final report 
