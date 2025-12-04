import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

st.markdown(
    """
    <h1 style='text-align: center; color: #4CAF50;'>
        🔮 Universal K-Means Clustering App
    </h1>
    <h3 style='text-align: center;'>
        Upload ANY dataset and cluster any two numeric columns.
    </h3>
    <br>
    """,
    unsafe_allow_html=True
)

# ------------------------------
# Upload the dataset
# ------------------------------
uploaded_file = st.file_uploader("Upload a CSV File", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📌 Dataset Preview")
    st.dataframe(df.head())

    st.subheader("📊 Dataset Information")
    st.write(df.describe())

    # ------------------------------
    # Detect numeric columns
    # ------------------------------
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

    if len(numeric_cols) < 2:
        st.error("❌ Not enough numeric columns for K-Means clustering!")
    else:
        st.success(f"Found numeric columns: {numeric_cols}")

        # ------------------------------
        # Select Features
        # ------------------------------
        st.subheader("🎯 Choose Columns for Clustering")

        col1 = st.selectbox("Select X-axis Column", numeric_cols, index=0)
        col2 = st.selectbox("Select Y-axis Column", numeric_cols, index=1)
        
        X = df[[col1, col2]].dropna().values

        # ------------------------------
        # Elbow Method
        # ------------------------------
        st.subheader("📉 Elbow Method to Choose Optimal K")

        wcss = []
        for i in range(1, 11):
            kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
            kmeans.fit(X)
            wcss.append(kmeans.inertia_)

        fig, ax = plt.subplots()
        ax.plot(range(1, 11), wcss, marker="o", linestyle="--")
        ax.set_xlabel("Number of Clusters (K)")
        ax.set_ylabel("WCSS")
        ax.set_title("Elbow Method")
        st.pyplot(fig)

        # ------------------------------
        # Choose number of clusters
        # ------------------------------
        k = st.slider("Select Number of Clusters (K)", 2, 10, 5)

        kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42)
        labels = kmeans.fit_predict(X)

        # ------------------------------
        # Plot clusters
        # ------------------------------
        st.subheader("🎨 Visualizing Clusters")

        fig2, ax2 = plt.subplots(figsize=(7, 7))

        colors = ["red", "blue", "green", "purple", "orange", "yellow",
                  "pink", "gray", "cyan", "brown"]

        for cluster in range(k):
            ax2.scatter(X[labels == cluster, 0],
                        X[labels == cluster, 1],
                        s=50,
                        c=colors[cluster],
                        label=f"Cluster {cluster+1}")

        # Centroids
        ax2.scatter(kmeans.cluster_centers_[:, 0],
                    kmeans.cluster_centers_[:, 1],
                    s=200, c="black", marker="X", label="Centroids")

        ax2.set_xlabel(col1)
        ax2.set_ylabel(col2)
        ax2.set_title("K-Means Clustering Result")
        ax2.legend()
        st.pyplot(fig2)

        # ------------------------------
        # Output cluster labels
        # ------------------------------
        df["Cluster"] = labels
        st.subheader("📑 Clustered Data Preview")
        st.dataframe(df.head())

        # Download Option
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="⬇ Download Clustered Dataset",
            data=csv,
            file_name="clustered_output.csv",
            mime="text/csv"
        )

else:
    st.info("⬆ Upload a CSV file to start.")