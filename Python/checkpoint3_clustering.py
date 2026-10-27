# ============================================================
# Library Analytics: Book Borrowing Trends and Student Reading Behavior
# BED 106 - Business Analytics | Checkpoint 3, Task 3.3: Clustering / Segmentation
# K-Means clustering of patrons on Borrowing_Frequency and Reading_Duration_Minutes.
# Outputs:
#   data/powerbi_library_data.csv      -> cleaned dataset + Segment column (load into Power BI)
#   data/cp3_segment_summary.csv       -> one row per segment (profile table for the report)
#   diagrams/cp3_elbow_silhouette.png  -> how k = 4 was chosen
#   diagrams/cp3_segment_scatter.png   -> the four segments
# Run from the project root:  python Python/checkpoint3_clustering.py
# ============================================================
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

RAW = "data/academic_digital_library_book_recommendation_dataset.csv"
FEATURES = ["Borrowing_Frequency", "Reading_Duration_Minutes"]
K = 4
SEED = 42

df = pd.read_csv(RAW)

# --- 1. Scale features (both on very different ranges: 1-45 vs 8-180 minutes)
X = StandardScaler().fit_transform(df[FEATURES])

# --- 2. Choose k: elbow (inertia) + silhouette score for k = 2..8
ks = range(2, 9)
inertia, silhouette = [], []
for k in ks:
    km = KMeans(n_clusters=k, n_init=10, random_state=SEED).fit(X)
    inertia.append(km.inertia_)
    silhouette.append(silhouette_score(X, km.labels_, sample_size=4000, random_state=1))

fig, ax1 = plt.subplots(figsize=(8, 4.5))
ax1.plot(list(ks), inertia, "o-", color="#1f4e79", label="Inertia (elbow)")
ax1.set_xlabel("Number of clusters (k)")
ax1.set_ylabel("Inertia (within-cluster sum of squares)")
ax2 = ax1.twinx()
ax2.plot(list(ks), silhouette, "s--", color="#e07b00", label="Silhouette score")
ax2.set_ylabel("Silhouette score (higher = better separated)")
ax1.axvline(K, color="grey", linestyle=":")
ax1.set_title("Choosing k: Elbow Method and Silhouette Score (k = 4 selected)")
fig.legend(loc="upper right", bbox_to_anchor=(0.88, 0.88))
fig.text(0.01, 0.01, "Source: Academic Digital Library Book Recommendation Dataset (Kaggle), n = 12,000",
         fontsize=7, color="grey")
fig.tight_layout()
fig.savefig("diagrams/cp3_elbow_silhouette.png", dpi=200)
plt.close(fig)

# --- 3. Final model
km = KMeans(n_clusters=K, n_init=10, random_state=SEED).fit(X)
df["Cluster_ID"] = km.labels_

# Name clusters from their centroids (not from label numbers, which are arbitrary)
cent = df.groupby("Cluster_ID")[FEATURES].mean()
freq_cut = cent["Borrowing_Frequency"].median()
dur_cut = cent["Reading_Duration_Minutes"].median()
NAMES = {
    (True, True): ("Devoted Readers", 1),          # borrow often, read long
    (True, False): ("Quick Borrowers", 2),         # borrow often, read short
    (False, True): ("Occasional Deep Readers", 3), # borrow rarely, read long
    (False, False): ("Casual / At-Risk Patrons", 4),  # borrow rarely, read short
}
seg_map = {
    cid: NAMES[(row.Borrowing_Frequency > freq_cut, row.Reading_Duration_Minutes > dur_cut)]
    for cid, row in cent.iterrows()
}
df["Segment"] = df["Cluster_ID"].map(lambda c: seg_map[c][0])
df["Segment_Order"] = df["Cluster_ID"].map(lambda c: seg_map[c][1])

# --- 4. Segment profile table
df["Cold_Start_Flag"] = (df["Cold_Start_User"] == "Yes").astype(int)
df["Irregular_Flag"] = (df["Irregular_Borrowing_Flag"] == "Yes").astype(int)
summary = (df.groupby(["Segment_Order", "Segment"])
             .agg(Patrons=("User_ID", "count"),
                  Avg_Borrowing_Frequency=("Borrowing_Frequency", "mean"),
                  Avg_Reading_Duration_Min=("Reading_Duration_Minutes", "mean"),
                  Avg_Books_Borrowed_6M=("Books_Borrowed_Last_6_Months", "mean"),
                  Avg_Recommendation_Score=("Recommendation_Score", "mean"),
                  Cold_Start_Pct=("Cold_Start_Flag", "mean"),
                  Irregular_Pct=("Irregular_Flag", "mean"),
                  Avg_Feedback_Score=("Feedback_Score", "mean"))
             .reset_index())
summary["Share_Pct"] = summary["Patrons"] / len(df)
summary[["Cold_Start_Pct", "Irregular_Pct", "Share_Pct"]] *= 100
summary = summary.round(3)
summary.to_csv("data/cp3_segment_summary.csv", index=False)
print(summary.to_string(index=False))

# --- 5. Scatter plot of segments
colors = {1: "#1f4e79", 2: "#2e86c1", 3: "#e07b00", 4: "#c0392b"}
fig, ax = plt.subplots(figsize=(8, 5.5))
for order, g in df.groupby("Segment_Order"):
    ax.scatter(g["Borrowing_Frequency"], g["Reading_Duration_Minutes"], s=4, alpha=0.35,
               color=colors[order], label=f"{g['Segment'].iat[0]} (n={len(g):,})")
ax.set_xlabel("Borrowing Frequency")
ax.set_ylabel("Reading Duration (minutes)")
ax.set_title("Patron Segments from K-Means Clustering (k = 4)")
ax.legend(markerscale=4, fontsize=8, loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=2)
fig.text(0.01, 0.01, "Source: Academic Digital Library Book Recommendation Dataset (Kaggle), n = 12,000",
         fontsize=7, color="grey")
fig.tight_layout()
fig.savefig("diagrams/cp3_segment_scatter.png", dpi=200)
plt.close(fig)

# --- 6. Power BI-ready file: readable labels, numeric flags, sort helpers
out = df.drop(columns=["Cluster_ID"]).copy()
text_cols = ["User_Type", "Department", "Book_Category", "Book_Format", "Interaction_Type",
             "Access_Mode", "Semester_Period", "Recommendation_Level"]
for c in text_cols:
    out[c] = out[c].str.replace("_", " ")
out["Patron_Status"] = out["Cold_Start_User"].map({"Yes": "Cold-Start", "No": "Established"})
out["Semester_Order"] =out["Semester_Period"].map({"Odd Semester": 1, "Even Semester": 2, "Vacation Period": 3})
out["Borrow_Freq_Band"] = pd.cut(out["Borrowing_Frequency"], bins=[0, 9, 18, 27, 36, 45],
                                 labels=["01-09", "10-18", "19-27", "28-36", "37-45"]).astype(str)
out.to_csv("data/powerbi_library_data.csv", index=False)
print(f"\nWrote data/powerbi_library_data.csv ({len(out):,} rows, {out.shape[1]} columns)")
