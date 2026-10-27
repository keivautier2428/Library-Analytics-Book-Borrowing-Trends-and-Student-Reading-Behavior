# ============================================================
# Checkpoint 3, Task 3.1: Dashboard Design Blueprint (wireframes)
# Draws one wireframe per Power BI page on a 1280 x 720 canvas.
# Numbers in [x, y, w, h] match Power BI: Format visual > General > Properties > Size/Position.
# Run from the project root:  python Python/checkpoint3_wireframe.py
# ============================================================
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

W, H = 1280, 720
NAVY, KPI, CHART, SLICER, SEG = "#1f4e79", "#d6e4f0", "#f4f6f8", "#fff4e0", "#fde2e1"

HEADER = [
    (0, 0, 1280, 60, NAVY, "", "LIBRARY ANALYTICS  |  {title}", "Group 1 - The Data Bookworms", True),
    (900, 12, 110, 36, "#2e86c1", "BUTTON", "Summary", "", True),
    (1020, 12, 110, 36, "#2e86c1", "BUTTON", "Trends", "", True),
    (1140, 12, 120, 36, "#2e86c1", "BUTTON", "Segments", "", True),
    (20, 70, 300, 50, SLICER, "SLICER (dropdown)", "User Type", "", False),
    (330, 70, 300, 50, SLICER, "SLICER (dropdown)", "Department", "", False),
    (640, 70, 300, 50, SLICER, "SLICER (dropdown)", "Semester Period", "", False),
    (950, 70, 310, 50, SLICER, "SLICER (dropdown)", "Segment", "", False),
    (20, 700, 1240, 18, "white", "", "Source: Academic Digital Library Book Recommendation Dataset (Kaggle), n = 12,000", "", False),
]

PAGES = {
    "1 - Executive Summary": {
        "purpose": "Purpose: one-glance health check of patron engagement and the 3 business questions.",
        "boxes": [
            (20, 130, 236, 100, KPI, "KPI CARD", "Total Patrons", "12,000", False),
            (271, 130, 236, 100, KPI, "KPI CARD", "Avg Recommendation Score", "0.556", False),
            (522, 130, 236, 100, KPI, "KPI CARD", "Irregular Borrowing Rate", "16.1%", False),
            (773, 130, 236, 100, KPI, "KPI CARD", "Cold-Start Patrons", "18.5%", False),
            (1024, 130, 236, 100, KPI, "KPI CARD", "Avg Reading Duration", "94.3 min", False),
            (20, 245, 400, 445, CHART, "DONUT CHART", "Patrons by User Type",
             "Legend: User_Type\nValues: Total Patrons", False),
            (435, 245, 410, 445, CHART, "CLUSTERED COLUMN  (BQ3)", "Avg Recommendation Score:\nCold-Start vs Established",
             "X: Patron_Status\nY: Avg Recommendation Score\nData labels ON", False),
            (860, 245, 400, 445, CHART, "CLUSTERED BAR  (BQ1)", "Irregular Borrowing Rate\nby Department",
             "Y: Department\nX: Irregular Borrowing Rate\nSort: highest first", False),
        ],
    },
    "2 - Trend & Comparison Analysis": {
        "purpose": "Purpose: compare engagement across categories, formats and patron types (BQ2) and show the borrowing trend.",
        "boxes": [
            (20, 130, 620, 275, CHART, "LINE CHART", "Avg Recommendation Score by Borrowing Frequency",
             "X: Borrowing_Frequency (1-45)\nY: Avg Recommendation Score\nAnalytics: Trend line ON", False),
            (655, 130, 605, 275, CHART, "CLUSTERED BAR  (BQ2)", "Avg Books Borrowed (6 Months) by Book Category",
             "Y: Book_Category\nX: Avg Books Borrowed 6M\nSort: highest first", False),
            (20, 420, 620, 270, CHART, "MATRIX / HEATMAP  (BQ2)", "Engagement: Book Category x User Type",
             "Rows: Book_Category   Columns: User_Type\nValues: Avg Books Borrowed 6M\nCell elements: background color scale", False),
            (655, 420, 605, 270, CHART, "STACKED COLUMN", "Interactions by Book Format and Type",
             "X: Book_Format\nY: Total Patrons\nLegend: Interaction_Type", False),
        ],
    },
    "3 - Deep Dive: Patron Segmentation": {
        "purpose": "Purpose: show the 4 K-Means patron segments (Task 3.3) and who needs attention.",
        "boxes": [
            (20, 130, 720, 400, SEG, "SCATTER CHART  (CLUSTER VISUAL)", "Patron Segments: Borrowing Frequency vs Reading Duration",
             "X: Borrowing_Frequency\nY: Reading_Duration_Minutes\nValues: User_ID   Legend: Segment", False),
            (755, 130, 505, 195, SEG, "DONUT CHART", "Share of Patrons by Segment",
             "Legend: Segment   Values: Total Patrons", False),
            (755, 335, 505, 195, SEG, "CLUSTERED BAR", "Avg Recommendation Score by Segment",
             "Y: Segment   X: Avg Recommendation Score", False),
            (20, 545, 1240, 145, CHART, "TABLE", "Segment Profile",
             "Segment | Total Patrons | Avg Borrowing Freq | Avg Reading Duration | Avg Rec Score | Cold-Start % | Irregular %", False),
        ],
    },
}


def draw(ax, x, y, w, h, color, kind, title, body, dark):
    ax.add_patch(Rectangle((x, y), w, h, facecolor=color, edgecolor="#555", lw=1.2))
    fg = "white" if dark else "#222"
    if kind == "" and body == "" and not dark:        # footer
        ax.text(x + 4, y + h / 2, title, va="center", fontsize=7, color="grey", style="italic")
        return
    if kind == "" and dark:                           # header bar: title left, group name under it
        ax.text(x + 16, y + 24, title, va="center", fontsize=13, weight="bold", color="white")
        ax.text(x + 16, y + 46, body, va="center", fontsize=8, color="#dde")
        return
    if kind:
        ax.text(x + 8, y + 6, kind, va="top", fontsize=7, color="#c05000" if not dark else "#ffe08a", weight="bold")
    big = h >= 100
    ax.text(x + w / 2, y + (h * 0.40 if big else h * 0.62), title, ha="center", va="center",
            fontsize=10 if big else 8.5, weight="bold", color=fg)
    if body:
        ax.text(x + w / 2, y + h * (0.68 if big else 0.62), body, ha="center", va="center",
                fontsize=8 if h > 120 else 9.5, color="#333" if not dark else "#dde")
    if not dark and kind:
        ax.text(x + w - 6, y + h - 5, f"[{x}, {y}, {w}, {h}]", ha="right", va="bottom", fontsize=6.5, color="#888")


for i, (page, spec) in enumerate(PAGES.items(), start=1):
    fig, ax = plt.subplots(figsize=(16, 9.6))
    ax.set_xlim(0, W)
    ax.set_ylim(H + 40, -50)
    ax.axis("off")
    short = page.split(" - ", 1)[1]
    ax.text(0, -38, f"Wireframe - Page {page}", fontsize=15, weight="bold", color=NAVY)
    ax.text(0, -14, spec["purpose"], fontsize=10, color="#333")
    for b in HEADER:
        b = list(b)
        b[6] = b[6].format(title=short.upper())
        if b[6] == {1: "Summary", 2: "Trends", 3: "Segments"}[i]:
            b[4] = "#e07b00"                           # highlight current page button
        draw(ax, *b)
    for b in spec["boxes"]:
        draw(ax, *b)
    ax.text(0, H + 32,
            "Interactive: 4 synced slicers (User Type, Department, Semester Period, Segment) + cross-filter on click + "
            "page navigation buttons.   [x, y, w, h] = Power BI pixel position/size on a 1280 x 720 page.",
            fontsize=8.5, color="#333")
    fig.tight_layout()
    fig.savefig(f"diagrams/cp3_wireframe_page{i}.png", dpi=150)
    plt.close(fig)
    print(f"Wrote diagrams/cp3_wireframe_page{i}.png")


# ------------------------------------------------------------
# Clean canvas backgrounds (exactly 1280 x 720 px) to set as the Power BI page
# background while building: Format page > Canvas background > Image, Fit = Normal.
# Remove the image when the page is finished.
# ------------------------------------------------------------
for i, (page, spec) in enumerate(PAGES.items(), start=1):
    fig = plt.figure(figsize=(12.8, 7.2), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(H, 0)
    ax.axis("off")
    for x, y, w, h, *_rest in HEADER[:-1] + spec["boxes"]:
        kind, title = _rest[1], _rest[2]
        ax.add_patch(Rectangle((x, y), w, h, facecolor="#f7f9fb", edgecolor="#b8c4d0", lw=1, linestyle="--"))
        label = title.format(title=page.split(" - ", 1)[1].upper()).replace("\n", " ")
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center", fontsize=9, color="#9aa8b6")
    fig.savefig(f"diagrams/cp3_bg_page{i}.png", dpi=100)
    plt.close(fig)
    print(f"Wrote diagrams/cp3_bg_page{i}.png")
