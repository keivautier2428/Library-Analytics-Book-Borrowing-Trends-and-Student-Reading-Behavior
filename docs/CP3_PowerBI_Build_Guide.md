# Checkpoint 3 — Power BI Build Guide

Wireframes: `diagrams/cp3_wireframe_page1.png`, `page2.png`, `page3.png`
Data file: `data/powerbi_library_data.csv` (12,000 rows, includes `Segment`)

## Setup
1. Get Data → Text/CSV → `powerbi_library_data.csv` → Load. Rename the table to **Library**.
2. View → Page view → Canvas settings: **16:9 (1280 × 720)**.
3. Sort-by-column (Column tools → Sort by column):
   - `Segment` by `Segment_Order`
   - `Semester_Period` by `Semester_Order`
4. Set `Borrowing_Frequency` → Summarization: **Don't summarize** (used as an axis).

## DAX measures (Home → New measure)
```DAX
Total Patrons = COUNTROWS(Library)
Avg Recommendation Score = AVERAGE(Library[Recommendation_Score])
Irregular Borrowing Rate = DIVIDE(SUM(Library[Irregular_Flag]), [Total Patrons])
Cold-Start Share = DIVIDE(SUM(Library[Cold_Start_Flag]), [Total Patrons])
Avg Reading Duration = AVERAGE(Library[Reading_Duration_Minutes])
Avg Books Borrowed 6M = AVERAGE(Library[Books_Borrowed_Last_6_Months])
Avg Borrowing Frequency = AVERAGE(Library[Borrowing_Frequency])
```
Format the two rates as **Percentage, 1 decimal**, and Avg Recommendation Score as **3 decimals**.

## Expected values (no filters) — use to check accuracy
| Measure | Value |
|---|---|
| Total Patrons | 12,000 |
| Avg Recommendation Score | 0.556 |
| Irregular Borrowing Rate | 16.1% |
| Cold-Start Share | 18.5% |
| Avg Reading Duration | 94.3 min |

## Segments (Task 3.3, K-Means k = 4 on Borrowing Frequency + Reading Duration)
| Segment | Patrons | Avg Borrow Freq | Avg Reading (min) | Avg Rec Score | Cold-Start % |
|---|---|---|---|---|---|
| Devoted Readers | 2,760 | 33.0 | 136.6 | 0.641 | 0% |
| Quick Borrowers | 2,665 | 32.9 | 51.0 | 0.575 | 0% |
| Occasional Deep Readers | 3,290 | 8.0 | 138.1 | 0.547 | 33.6% |
| Casual / At-Risk Patrons | 3,285 | 7.8 | 50.0 | 0.478 | 33.9% |

k chosen with the elbow + silhouette chart: `diagrams/cp3_elbow_silhouette.png`.
Re-run anytime: `python Python/checkpoint3_clustering.py`

## Interactivity (at least 2 required)
- 4 dropdown slicers → View → **Sync slicers** across all 3 pages
- Page navigation buttons (Insert → Buttons → Navigator → Page navigator)
- Cross-filtering by clicking visuals (default)

## Theme colors
Navy `#1F4E79` · Blue `#2E86C1` · Orange `#E07B00` · Red `#C0392B` (use the same segment colors on every visual)
