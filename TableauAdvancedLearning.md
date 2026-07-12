2. Tableau Bridge
    * Designed a star schema in Tableau Prep by splitting the Sample – Superstore Orders dataset into FACT_ORDERS, DIM_CUSTOMERS, DIM_PRODUCTS, and DIM_DATES, with duplicate records removed from the dimension tables.
    * Published each fact and dimension table as a separate published data source to Tableau Cloud for enterprise reporting and dashboard development.
    * Explored the role of Tableau Bridge in securely connecting Tableau Cloud to on-premises or local data sources, enabling scheduled extract refreshes and live connections for data behind private networks or firewalls.
    * Understood that Bridge is only required for on-premises/local data sources, whereas cloud-hosted platforms such as Snowflake, Amazon Redshift, Google BigQuery, and Azure SQL Database can be accessed directly by Tableau Cloud without Bridge.
    ![alt text](image-9.png)
---

9. Row-Level Filtering using Embedded SDKs
    * Developed a custom Enterprise Sales Portal with a login page where users enter their credentials and select an authorized region before accessing analytics.
    * Embedded a Tableau Cloud dashboard into the web application using the Tableau Embedding API, providing a seamless analytics experience within the custom portal.
    * Implemented dynamic row-level filtering by automatically applying the selected region to the embedded dashboard using the JavaScript applyFilterAsync() method, ensuring users view only region-specific data.
    * Simulated an enterprise embedded analytics workflow, with the understanding that in a production environment, the custom login would be replaced by OAuth/Single Sign-On (SSO) for secure authentication and automatic user-based access control.

    ![alt text](image-10.png)
    ![alt text](image-11.png)
---
10. Custom Tableau Extensions
    * Developed a custom Tableau Dashboard Extension using the Tableau Extensions SDK (vanilla JavaScript) with HTML, CSS, and JavaScript to create an interactive Region Filter Panel that applies filters to dashboard worksheets through the Extensions API.
    * Hosted the extension on GitHub Pages and created a valid `.trex` manifest containing the extension metadata, source URL, author information, and API version, enabling Tableau Cloud to recognize and attempt to load the extension.
    * Configured a simple CI/CD workflow by storing the extension files in a GitHub repository, allowing updates to be automatically deployed to GitHub Pages whenever changes are pushed.
    * Successfully integrated the extension with Tableau Cloud; however, execution was blocked by the site's Extension Allowlist (Safe List) security policy, demonstrating that deployment was successful and only a Site Administrator can authorize third-party extensions for execution.
    ![alt text](image-13.png)
    ![alt text](image-12.png)

---
12. Real-Time Analytics with Tableau & Streaming Data
    * Created a SALES_STREAM table in Snowflake, loaded initial sales records, and connected Tableau to the table using a Live Connection.
    * Built and published a Tableau Cloud dashboard based on the live Snowflake data source.
    * Inserted additional records into Snowflake after publication and verified that the dashboard reflected the latest data upon refresh, demonstrating near real-time analytics using a live connection.
---

13. Geospatial Analytics & Spatial Calculations.
    * Connected a store location shapefile (.shp) and customer location dataset containing latitude and longitude coordinates in Tableau.
    * Used a spatial join with BUFFER() and INTERSECTS() to associate customers with nearby store locations based on a 50 km catchment area.
    * Created geospatial visualizations including customer/store maps and a density map (heatmap) to analyze spatial distribution and event concentration.

---

14. AI-Powered Insights: Explain Data and ML Integration
    * Connected Tableau Desktop to the live Snowflake SALES_STREAM table containing streaming sales events and created a dashboard to visualize incoming data.
    * Used Tableau's Explain Data feature by selecting marks in the Sales by Product visualization to explore automatically generated explanations for anomalies and trends. Learned that these explanations can also be added as a separate worksheet to facilitate deeper analysis within the workbook.
    * Explored Tableau's Explain Data feature by analyzing the Sales by Product visualization and understanding the automatically generated explanations for selected marks.
    * Created a historical sales dataset in Snowflake and trained a Random Forest Regressor in Python to predict sales based on date, product, and region features.
    * Encoded categorical variables, generated sales predictions, and stored the trained model and encoders locally using joblib for reuse.
    * Configured TabPy as Tableau's Analytics Extension and established a successful connection between Tableau and the Python environment.
    * Implemented a SCRIPT_REAL() calculated field in Tableau to load the trained model, perform real-time predictions on the streaming sales data, and return the predicted sales values directly within the visualization.
    * Resolved issues related to field aggregation, categorical encoding, and JSON serialization (numpy.ndarray to Python list), enabling seamless integration between Tableau and the external machine learning model.
    * Built a visualization comparing Actual Sales and Predicted Sales, demonstrating how Tableau can leverage external Python models through TabPy to provide AI-powered insights alongside live business data.
    ![alt text](image.png)
    ![alt text](image-1.png)

---

15. Github to Tableau Cloud
    * Developed a Tableau workbook `(Sales Dashboard.twbx)` connected to the streaming sales dataset and stored it in a GitHub repository for version control. Generated a Tableau Cloud Personal Access Token (PAT) and configured GitHub Actions secrets for secure authentication.
    * Implemented a CI/CD pipeline using GitHub Actions and the Tableau Server Client (TSC) Python library. A custom deployment script (deploy.py) authenticated with Tableau Cloud, checked for an existing workbook, captured a pre-deployment permission snapshot (when applicable) using the Tableau REST API, published or updated the workbook, and generated a post-deployment permission snapshot for comparison.
    * Simulated an enterprise change management workflow by creating a feature branch, modifying the workbook locally (adding a new worksheet), committing the changes, creating a Pull Request, and merging it into the main branch. The merge automatically triggered the GitHub Actions workflow, which deployed the updated workbook to Tableau Cloud and verified the new version in the cloud environment.

    ![alt text](image-2.png)
    ![alt text](image-4.png)
    ![alt text](image-3.png)
    Logs:
    ![alt text](image-5.png)
    New version of dashboard added to git with separate branch - created pull request:
    ![alt text](image-6.png)
    New logs:
    ![alt text](image-7.png)
    Published to cloud:
    ![alt text](image-8.png)






                         
                                                                                       
  