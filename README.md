# 📘 **Customer Segmentation Using K-Means Clustering**

A complete project covering **data analysis**, **cluster selection**, **model training**, **visualization**, and a **Streamlit deployment**.

---

## 📂 **Project Overview**

This project focuses on applying **K-Means Clustering**, an unsupervised machine learning algorithm, to segment customers based on their shopping behavior. The aim is to identify distinct customer groups that share similar characteristics, allowing businesses to tailor marketing strategies, improve customer experience, and better understand purchasing patterns.

The dataset used contains basic customer information including **Age**, **Gender**, **Annual Income**, and **Spending Score**. These features help in identifying purchasing habits and economic profiles.

---

## 🧰 **Steps Followed in the Project**

### 1️⃣ **Importing Dependencies**

A set of scientific and analysis-focused Python libraries were used to handle data processing, numerical calculations, visualization, and clustering. These include tools for data manipulation, plotting, and machine learning-based clustering.

---

### 2️⃣ **Data Collection & Initial Inspection**

The dataset was loaded and examined to understand its structure. Key steps included:

* Previewing the first few records
* Checking dataset shape (rows & columns)
* Viewing detailed information such as data types & memory usage
* Confirming the absence of missing values

This ensures the data is clean, structured, and ready for clustering.

---

### 3️⃣ **Feature Selection**

For clustering, two essential attributes were selected:

* **Annual Income**
* **Spending Score**

These two features are ideal for customer segmentation since they highlight spending ability and behavior.

---

### 4️⃣ **Choosing the Optimal Number of Clusters (K)**

To determine the best number of clusters, the **Elbow Method** was used.
📉 This method evaluates the **WCSS** (Within-Cluster Sum of Squares) for different cluster counts.

The “elbow point” in the graph signified that **5 clusters** provided the most meaningful segmentation for this dataset.

---

### 5️⃣ **Training the K-Means Model**

A K-Means model was trained using the selected features and optimal cluster number.

Each customer was assigned to a specific cluster, allowing clear distinction between customer groups.

---

### 6️⃣ **Visualizing the Clusters**

A scatter plot was created where:

* Each cluster was represented by a different color
* Data points showed customer distribution
* The cluster centroids were highlighted to show group centers

This visual helps interpret how customers naturally group together based on income and spending behavior.

---

### 7️⃣ **Sample of the Dataset**

A small portion of the dataset includes entries such as:

| CustomerID | Gender | Age | Annual Income | Spending Score |
| ---------- | ------ | --- | ------------- | -------------- |
| 1          | Male   | 19  | 15            | 39             |
| 2          | Male   | 21  | 15            | 81             |
| 3          | Female | 20  | 16            | 6              |
| 4          | Female | 23  | 16            | 77             |

This demonstrates variations in income and shopping tendencies, essential for segmentation.

---

## 🌐 **Streamlit App Deployment**

A user-friendly **Streamlit application** was developed to make clustering interactive and universal.
The app allows users to:

* Upload **any CSV dataset**
* Automatically detect numeric columns
* Select two numeric attributes for clustering
* View the Elbow Method for choosing cluster count
* Visualize the final clusters in a scatter plot
* Download the dataset with cluster labels added

✨ This tool transforms the project from a static model into a fully interactive clustering platform.

---

## 🎯 **Purpose & Benefits**

This project helps businesses:

* Understand customer behavior
* Identify high-value or low-spending groups
* Personalize marketing strategies
* Improve decision-making through data-driven segmentation

From a technical perspective, it demonstrates:

* End-to-end data analysis
* Effective feature selection
* Practical clustering methodology
* Interactive deployment using Streamlit

---

## 🌐 Live Demo

You can try the interactive version of the clustering tool live at:
[Customer Segmentation K‑Means Clustering App](https://customer-segmentation-using-k-means-clustering-app.streamlit.app/) 🚀

---

## 🚀 **Conclusion**

This project brings together data analysis, machine learning, and interactive visualization to create a comprehensive customer segmentation system. With the addition of a Streamlit web app, it becomes a scalable and adaptable tool for any dataset containing numeric features.

---
