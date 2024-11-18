Stock Spectrum: AI-Assisted Business Valuation Tool
Project Overview:

Stock Spectrum is a project developed during the college hackathon Datathon 1.0 by our team, where we chose the finance track to create an intuitive tool for understanding and analyzing stock data. Our objective was to provide a user-friendly solution that simplifies the complex world of company stocks, leveraging AI and machine learning to provide actionable insights for both financial experts and non-experts alike.

Description:
The finance track focused on leveraging financial and market data to build AI-assisted tools for business valuation. The dataset we worked with included U.S. companies' Ticker IDs and Standard Industrial Classification (SIC) codes, alongside their descriptions.

Objective:
Data Source: The project utilized publicly available datasets, primarily containing SIC codes and Ticker IDs.
Goal:
To design interactive dashboards and tools that allow users to easily perform data aggregation, financial analysis, and business valuation.
Our solution aimed to simplify complex financial concepts for non-experts, providing clear and actionable insights about company stock performance and market trends.
Key Features:
1. Data Gathering & Consolidation
We started with limited data (SIC codes and Ticker IDs) and collected additional information from:
Historical Stock Data: Public data repositories.
Yahoo Finance API: For company-specific financial details and stock performance.
2. Machine Learning Models
We trained predictive models to forecast:
Stock Prices for the next day.
Company Performance Metrics using models such as:
Linear Regression
Random Forest Regressor
3. AI-Assisted Insights
Integrated Google Gemini LLM to offer AI-driven insights. Users can upload CSV files (up to 200MB) and receive detailed analysis and actionable feedback from the model.
4. Interactive Visualizations
Used Tableau to create interactive visualizations for better understanding of stock performance, trends, and predictions.
5. Web Application Interface
Developed a Streamlit-based UI that provides an intuitive, user-friendly interface to interact with the data and AI insights.
Technology Stack:
Streamlit: For building the web application interface.
Python: For data analysis, machine learning model development, and API integration.
Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
Tableau: For creating interactive visualizations and dashboards.
Google Gemini API: For providing AI-assisted insights and analysis.
How It Works:
Upload CSV: Users can upload a CSV file containing company data, and the system will analyze it.
Data Analysis: Python scripts process and analyze the data, applying machine learning models for stock price prediction and performance metrics.
Visualization: The processed data is displayed through interactive Tableau dashboards.
AI Insights: The system offers insights powered by Google Gemini, helping users understand the data in an easy-to-digest format.
Challenges Faced:
Data Gathering & Consolidation: We faced the challenge of collecting and consolidating the necessary stock and company data. However, using public repositories and the Yahoo Finance API, we were able to gather comprehensive data to build our solution.
Model Training: Training accurate predictive models on historical stock data is inherently difficult due to market volatility, but we employed regression techniques and evaluated the models based on their performance.
Future Improvements:
Model Enhancement: Explore more advanced machine learning techniques like LSTM for stock price predictions.
User Experience: Improve the user interface for better interaction and customization options.
Data Sources: Expand to include more diverse datasets such as real-time stock prices, market news, and social media sentiment analysis.
Getting Started:
Prerequisites:
Python (>= 3.8)
Libraries:
Streamlit
Pandas
NumPy
Scikit-learn
Matplotlib
Seaborn
Tableau (for visualizations)
Google Gemini API (for AI-powered insights)
Installation:
Clone the repository:

bash
Copy code
git clone https://github.com/your-repo/stock-spectrum.git
cd stock-spectrum
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Streamlit app:

bash
Copy code
streamlit run ui.py

Contributors:
[Nuzhat Fatima]: 
[Praveen Bhandari]: 
[Navdeep Singh]: 
[Aditya Chache]: 

Acknowledgments:
Datathon 1.0 for organizing the hackathon and providing the opportunity to develop this solution.
Yahoo Finance API for stock and financial data.
Google Gemini for powerful AI insights.

License:
This project is licensed under the MIT License - see the LICENSE file for details.

