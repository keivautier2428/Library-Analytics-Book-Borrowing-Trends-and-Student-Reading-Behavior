# Presentation Script — Checkpoints 1 & 2
### Library Analytics: Book Borrowing Trends and Student Reading Behavior

This is a word-for-word speaking script for a **screen-recorded video** (someone shares their screen and reads their part while clicking through the files). Three presenters split the work below. Total run time: **roughly 10-12 minutes**.

---

## Before You Hit Record

Open these ahead of time so you can switch tabs smoothly instead of hunting for files mid-recording:

1. `docs/Checkpoint 1 Report - Library Analytics.docx`
2. `diagrams/erd_diagram.png`
3. `SQL/library_db_setup.sql` and `SQL/checkpoint1_queries.sql` (in phpMyAdmin or MySQL Workbench, with the database already imported and queries ready to run)
4. `Excel/Checkpoint2_Spreadsheet_Analytics.xlsx` (open it once first so all the formulas recalculate before recording)
5. `docs/Checkpoint 2 Report - Library Analytics.docx`

**Who says what:**
- **Presenter 1 (Project Lead / Analyst):** Introduction, business problem, wrap-up
- **Presenter 2 (Data Engineer):** Checkpoint 1 — dataset, database, SQL
- **Presenter 3 (Statistician / BI Developer):** Checkpoint 2 — Excel analysis

Swap names in for "Presenter 1/2/3" wherever you see them.

---

## Part 0 — Introduction (Presenter 1) — ~1 minute

**[Screen: title slide or the cover page of the Checkpoint 1 report]**

> "Hi everyone, we're [Group Name], and this is our capstone project for BED 106, Business Analytics. Our topic is Library Analytics: Book Borrowing Trends and Student Reading Behavior.
>
> Our group is made up of three members: [Name 1], [Name 2], and [Name 3]. Today we'll walk you through the first two checkpoints of our project — first the database and SQL work, then the spreadsheet and statistics work.
>
> Let's start with the business problem."

**[Screen: Task 1.1 section of the Checkpoint 1 report]**

> "The library we're studying has no data-driven way of knowing who's actually using their collection, which books get real engagement, and whether their book-recommendation system is treating new patrons fairly. So we set out to answer three questions: which patron types and departments borrow irregularly, which book categories and formats get the most real engagement, and whether new patrons — we call them 'cold-start' patrons — are underserved by the recommendation system compared to regular patrons.
>
> I'll now hand it over to [Presenter 2] to walk through how we built the database."

---

## Part 1 — Checkpoint 1: Database & SQL (Presenter 2) — ~5 minutes

### 1a. The dataset

**[Screen: data/academic_digital_library_book_recommendation_dataset.csv opened in Excel, or the Data Source Report table in the Word doc]**

> "For this checkpoint, we used a real dataset downloaded from Kaggle — the Academic Digital Library Book Recommendation Dataset. It has 12,000 rows, and each row is one interaction between a patron and a book — things like borrowing, viewing, reserving, or renewing.
>
> One thing worth being upfront about: while this file is genuinely from Kaggle, our data quality check showed clear signs it was artificially generated rather than pulled from a real library's records — for example, every single patron ID and book ID appears exactly once, and some numbers don't line up the way they would in a real system. We documented this honestly in our report instead of pretending it's authentic institutional data. It's still perfectly fine to use for this kind of analysis exercise — we just wanted to be transparent about it."

### 1b. The database design

**[Screen: diagrams/erd_diagram.png]**

> "Here's our database design. We split the flat spreadsheet into three connected tables. `users` holds each patron's type — like undergraduate, faculty, or research scholar — and their department. `books` holds each book's category and format. And `borrowing_events` is the middle table that connects them — it records every single interaction, plus things like how long someone read, how many times they searched, and the recommendation score the system gave that event.
>
> One user can appear in many borrowing events, and one book can appear in many borrowing events too — that's the one-to-many relationship you see in the diagram."

### 1c. Setting up the database

**[Screen: SQL/library_db_setup.sql open, then switch to phpMyAdmin/MySQL Workbench showing the created tables]**

> "This script creates the three tables and loads all 12,000 rows into each one. [Run or show it already run.] Here you can see the three tables now exist in our database, and here's a quick preview of the data sitting inside `borrowing_events`."

### 1d. Running the SQL queries

**[Screen: SQL/checkpoint1_queries.sql, run 2-3 of the 8 queries live]**

> "We wrote eight SQL queries in total — the report covers all of them, but let me show you a couple of the interesting ones live.
>
> This first one groups events by department and calculates what percentage were flagged as irregular borrowing. [Run Query 6.] As you can see, Medicine comes out highest at about 17%, and Computer Science is close behind at almost 17% as well. That tells the library which departments might need a more personal reminder system.
>
> This next one compares patrons the system has little history on — we call them cold-start patrons — against everyone else. [Run Query 8.] Cold-start patrons make up about 18.5% of all activity, and even though they search and read just as much as everyone else, they get a noticeably lower average recommendation score — about 0.48 compared to 0.57. So the recommendation system isn't serving new patrons quite as well yet, which directly answers one of our three business questions."

**[Screen: brief flash of the remaining query results in the Word report, scrolling]**

> "The full report has all eight queries with their SQL code, their results, and a short explanation of what each one means for the library. Now I'll pass it to [Presenter 3] for Checkpoint 2."

---

## Part 2 — Checkpoint 2: Spreadsheet & Statistical Analysis (Presenter 3) — ~5-6 minutes

### 2a. The workbook overview

**[Screen: Excel/Checkpoint2_Spreadsheet_Analytics.xlsx, Cleaned_Data tab]**

> "For Checkpoint 2, we kept using the same dataset — that's a requirement from the project guide, groups have to stick with their Checkpoint 1 data. We brought the cleaned 12,000-row dataset into Excel and built eight sheets around it, all using live formulas so everything recalculates automatically."

### 2b. Pivot tables and charts

**[Screen: Pivot_Analysis tab, then Pivot_Charts tab]**

> "Here are our three pivot-style tables. This one breaks down engagement by patron type, this one by book category, and this one shows the irregular-borrowing rate by department — matching what [Presenter 2] showed earlier from SQL, just now visualized. And here are the charts we built straight from those tables — a simple bar chart makes it a lot easier to see at a glance which department has the higher irregular rate."

### 2c. Formulas showcase

**[Screen: Formulas_Showcase tab]**

> "The project also asked us to demonstrate five different Excel functions. We used COUNTIF to count how many events were actual borrows, SUMIF to total up borrowing activity just for faculty, an IF statement to flag a patron as high or low engagement, TEXT to format a score as a percentage, and VLOOKUP to look up a patron's department from their ID."

### 2d. Descriptive statistics

**[Screen: Descriptive_Stats tab]**

> "Next we picked three variables that mattered most to our business questions: how often someone borrows, how long they read per session, and their recommendation score. On average, patrons borrow about 19 times, read for about 94 minutes per session, and get a recommendation score of about 0.56 out of 1. The borrowing frequency numbers are skewed — a lot of patrons only borrow a handful of times, but there's also a solid chunk of very frequent borrowers, which you can see in this histogram."

### 2e. Correlation

**[Screen: Correlation_Analysis tab, both scatter charts]**

> "We looked at two relationships. First, how often someone borrows versus their recommendation score — there's a moderate positive correlation, about 0.51. So more frequent borrowers tend to get somewhat better recommendations, though it's far from a perfect relationship. Second, we compared how many books someone borrowed in the last six months against how many they returned on time, which also came out moderately positive, around 0.50."

### 2f. Regression

**[Screen: Regression tab, scatter chart with trendline visible]**

> "Finally we built a simple regression model to predict recommendation score from borrowing frequency. Our equation came out to Recommendation Score equals 0.48 plus 0.0038 times Borrowing Frequency. That means about 26% of the variation in someone's recommendation score can be explained just by how often they borrow — the rest comes from other factors we didn't include in this simple model, like reading interest or how closely a book matches their profile.
>
> One honest caveat we noted in our report: since Recommendation Score is itself generated by an algorithm, this relationship is more of a 'these two move together' pattern than solid proof that borrowing more *causes* a better score."

---

## Part 3 — Wrap-Up (Presenter 1) — ~1 minute

**[Screen: back to the title slide, or a simple summary slide if you made one]**

> "So to summarize: across both checkpoints, we found that the library's recommendation system moderately rewards frequent borrowers, that certain departments like Medicine show higher irregular-borrowing rates worth addressing, and that new patrons aren't yet getting recommendations as good as everyone else's — even though they're putting in the same effort.
>
> That wraps up Checkpoints 1 and 2. Next, in Checkpoint 3, we'll be turning this into an interactive BI dashboard. Thanks for watching!"

---

## Quick Timing Recap

| Part | Presenter | Approx. Time |
|---|---|---|
| Introduction & Business Problem | Presenter 1 | 1 min |
| Checkpoint 1 — Database & SQL | Presenter 2 | 5 min |
| Checkpoint 2 — Excel Analysis | Presenter 3 | 5-6 min |
| Wrap-up | Presenter 1 | 1 min |
| **Total** | | **~12-13 min** |

## Recording Tips

- Practice reading each part once out loud before recording — it'll sound more natural and you'll catch spots where you stumble over a number.
- It's fine to trim pauses in editing afterward, but try to speak at a normal, unhurried pace on the first take.
- If your screen recording software supports it, zoom in slightly on the Excel/SQL windows so small text (like formula bars) is readable on video.
- Every teammate should say at least a few sentences on camera/mic — some rubrics for later checkpoints specifically check that every member speaks.
