# **Customer Lifetime Value Prediction**
## **Context**

Customer Lifetime Value (CLV) prediction is a crucial aspect of business strategy and financial planning. CLV represents the total revenue a business can expect from a customer over the entire duration of their relationship. Understanding and predicting CLV helps businesses in several key areas:

**Marketing Strategies**: By identifying high-value customers, businesses can tailor their marketing strategies to retain these customers, enhance their satisfaction, and increase their lifetime value. This might include personalized marketing campaigns, exclusive offers, and targeted communication.

**Resource Allocation**: Businesses can allocate resources more effectively by focusing on acquiring and retaining customers with the highest predicted CLV. This ensures that marketing and sales efforts are directed towards segments that provide the most significant return on investment.

**Customer Segmentation**: CLV prediction allows for better customer segmentation. Businesses can classify customers based on their predicted value and develop customized approaches for different segments. High-value customers might receive premium services, while low-value customers might be targeted with cost-effective strategies to boost their value.

**Financial Forecasting**: Accurate CLV prediction aids in financial forecasting and budgeting. It helps in estimating future revenue streams, understanding customer acquisition costs, and planning long-term business strategies.

**Product Development**: Insights from CLV analysis can inform product development and enhancement decisions. Businesses can identify which products or services contribute most to customer value and focus on improving or expanding those offerings.

## Dataset
The dataset includes 22 columns, capturing various aspects of customer demographics, policy details, and claim information. Some key features are:

**CustomerID**: Unique identifier for each customer.

**Customer.Lifetime.Value**: The target variable representing the lifetime value of a customer.

**Coverage**: Type of insurance coverage.

**Education**: Customer's education level.

**EmploymentStatus**: Employment status of the customer.

**Gender**: Gender of the customer.

**Income**: Annual income of the customer.

**Location.Geo**: Geographic location of the customer.

**Location.Code**: Code representing the location.

**Marital.Status:** Marital status of the customer.

**Monthly.Premium.Auto**: Monthly auto insurance premium.

**Months.Since.Last.Claim**: Number of months since the last claim was made.

**Months.Since.Policy.Inception**: Number of months since the policy inception.

**Number.of.Open.Complaints**: Number of open complaints.

**Number.of.Policies**: Number of policies held by the customer.

**Policy.Type**: Type of policy.

**Policy**: Specific policy details.

**Renew.Offer.Type**: Type of renewal offer.

**Sales.Channel**: Channel through which the policy was sold.

**Total.Claim.Amount**: Total amount claimed by the customer.

**Vehicle.Class**: Class of the vehicle.

**Vehicle.Size:** Size of the vehicle.

## Step 1: Data Preprocessing

**Data Loading and Inspection:** Loaded the dataset and inspected the data for any missing or null values or anomalies.

**Feature Engineering**: Coverted date to no of days and took log of target variable CLV

**Data Splitting**: Split the dataset into training and testing sets to evaluate model performance.

## Step 2: Training the Models
We employed various regression algorithms to predict CLV:

**Linear Regression:**

Linear Regression is a basic but powerful algorithm that models the relationship between dependent and independent variables by fitting a linear equation to observed data.

**Decision Tree Regressor:**

Decision Trees split the data into subsets based on the value of input features, making decisions at each node. This non-parametric method is useful for capturing complex relationships.

**Random Forest Regressor:**

Random Forest is an ensemble method that combines multiple decision trees to improve prediction accuracy and control over-fitting.

**Gradient Boosting Regressor:**

Gradient Boosting builds an ensemble of trees sequentially, where each tree corrects the errors of its predecessor. It is known for its high predictive accuracy.

**Model Initialization:**

Initialized the models with default parameters and tuned them using GridSearchCV for optimal performance.

## Step 3: Model Evaluation and Observations

**Model Evaluation:**

Evaluated each model using Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared metrics.
Used cross-validation to ensure the robustness of model performance.

**Observations:**

Linear Regression had a high bias but low variance, making it less suitable for capturing complex patterns in the data.

Decision Tree Regressor performed better than Linear Regression but was prone to overfitting.

Random Forest Regressor struck a balance between bias and variance, providing good predictive performance.

Gradient Boosting Regressor achieved the best performance with the lowest MAE and MSE, and the highest R-squared value, indicating it captured the intricacies of the data effectively.

Linear Regression had a high bias but low variance, making it less suitable for capturing complex patterns in the data.

Decision Tree Regressor performed better than Linear Regression but was prone to overfitting.

Random Forest Regressor struck a balance between bias and variance, providing good predictive performance.

Gradient Boosting Regressor achieved the best performance with the lowest MAE and MSE, and the highest R-squared value, indicating it captured the intricacies of the data effectively.

# Application for CLV Prediction

**Introduction**

This documentation provides a comprehensive guide to deploying a pre-trained Gradient Boosting Regressor model using Streamlit for real-time CLV prediction. The application allows users to input customer transaction details and get instant predictions on the expected lifetime value of the customer.

This code sets up a simple web application using Streamlit to predict credit card fraud based on user input. Here’s a breakdown of what each part does:

**1. Imports:**

**streamlit** is used for creating web applications.

**joblib **is for loading a pre-trained model.

**pandas** is for handling data in DataFrame format.

**2. Load the Model:**

Loads a pre-trained machine learning model from a file named best_model.pkl using joblib

**3. Preprocess Input Data:**

Defines a function to preprocess user input.

Creates a dictionary with the transaction amount and time (and possibly other features).

Converts this dictionary into a DataFrame to match the input format expected by the model.

**4.Define the Streamlit App:**

Sets up the user interface for the Streamlit app.

**st.title** and **st.write** display text and titles on the web page.

**st.number_input** creates input fields for the user to enter the transaction amount and time.

**st.button** triggers the prediction when clicked.

Calls preprocess_input to prepare the data for the model, then uses model.predict to get the prediction.

Displays a message based on the prediction result: error if fraud is predicted, success if the transaction is legitimate.

**5. Run the App:**

Ensures the main function runs if the script is executed directly.

