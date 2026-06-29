
# 🛒 Flipkart Laptop Market Analysis Dashboard
## Project Overview
This project involves a full end-to-end data pipeline: from **web scraping** real-time laptop data from Flipkart using Python to creating an **interactive business intelligence dashboard** in Power BI. The goal was to analyze market trends, brand positioning, and pricing strategies in the Indian e-commerce landscape.
## 📊 Live Dashboard Preview
*
<img width="1178" height="617" alt="image" src="https://github.com/user-attachments/assets/72e08950-2947-4a06-892c-19b453bd4cb0" />

## 🔄 Data Life Cycle: Flipkart Market Analysis
In this project, the data moved through five distinct stages, mirroring a real-world enterprise data pipeline:
### 1. Data Generation & Extraction (The Source)
 * **Action:** Web Scraping.
 * **Process:** Used Python (BeautifulSoup/Selenium) to send requests to Flipkart's servers, navigating through paginated results to capture raw HTML.
 * **Result:** Raw, unstructured data including product titles, prices, and ratings.
### 2. Data Storage (The Raw Layer)
 * **Action:** Data Persistance.
 * **Process:** Converted the extracted Python lists/dictionaries into a structured **CSV file**.
 * **Result:** A flat-file database that serves as the "Single Source of Truth" for the analysis.
### 3. Data Processing & Cleaning (ETL)
 * **Action:** Power Query Transformation.
 * **Process:**
   * **Cleaning:** Removed currency symbols (₹) and commas to convert "Price" from Text to Decimal.
   * **Feature Engineering:** Created a **Conditional Column** for "Price Segments" (Budget/Mid/Premium).
   * **Parsing:** Used the "Split Delimiter" method to extract the **Brand Name** from long product descriptions.
 * **Result:** A "Clean Room" dataset ready for mathematical calculation.
### 4. Data Visualization & Analysis (Insights)
 * **Action:** Dashboard Development.
 * **Process:** Applied DAX to calculate **Average Prices** and **Market Share**. Built interactive visuals (Donut charts, Treemaps) to identify trends.
 * **Result:** A high-level visual summary that makes complex data easy for stakeholders (like a CEO or CMO) to understand.
### 5. Data Archiving & Communication (The Final Stage)
 * **Action:** Documentation & Reporting.
 * **Process:** Documented the process on **GitHub** and prepared the dashboard for portfolio presentation.
 * **Result:** The project is shared as a professional asset, providing proof of technical competency.

## 🛠️ Tech Stack
 * **Data Extraction:** Python (BeautifulSoup / Selenium)
 * **Data Cleaning:** Power Query (M Language)
 * **Data Visualization:** Power BI Desktop
 * **Analytics:** DAX (Data Analysis Expressions)
## 🚀 Key Features & Analysis
 *1. Brand Price Analysis (Bar Chart)
 * Analyzed the **Average Price** across major brands.
 * Identified premium vs. budget market leaders (e.g., Apple/Microsoft vs. Acer/HP).
 * Used **Data Labels** and **Top N Filters** for scannability.
### 2. Price Segmentation (Donut Chart)
 * Engineered a **Conditional Column** to categorize products into:
   * **Budget:** < ₹40,000
   * **Mid-Range:** ₹40,000 - ₹90,000
   * **Premium:** > ₹90,000
 * Visualized market concentration showing that ~45% of listings are in the Mid-Range segment.
### 3. Inventory Distribution (Treemap)
 * Extracted **Brand Names** from complex product titles using string manipulation.
 * Mapped the volume of listings to identify which brands have the highest "Shelf Space" on Flipkart.
### 4. Interactive Exploration
 * Integrated **Slicers** for brand-specific deep dives.
 * Enabled **Cross-Filtering** across all visuals for a dynamic user experience.
## 📈 Business Insights Derived
 * **Premium Dominance:** High-end models from Microsoft and ASUS dominate the ₹1Lakh+ segment.
 * **Market Gap:** There is a significant density of products in the ₹50k-₹70k range, indicating high competition.
 * **Volume vs. Value:** While some brands have fewer listings, their average price point remains significantly higher than volume-focused brands.

