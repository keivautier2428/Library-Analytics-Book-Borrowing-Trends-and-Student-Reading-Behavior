-- ============================================================
-- Library Analytics: Book Borrowing Trends and Student Reading Behavior
-- BED 106 - Business Analytics | Checkpoint 1, Task 1.4: SQL Query Report
-- Run library_db_setup.sql first to create and populate the database.
-- Source data: Academic Digital Library Book Recommendation Dataset (Kaggle,
-- synthetic/simulated - see Data Source Report, Task 1.2)
-- ============================================================

USE library_analytics_db;

-- ------------------------------------------------------------
-- 1. BASIC DATA RETRIEVAL (SELECT + WHERE + ORDER BY)
-- ------------------------------------------------------------

-- Query 1: The 10 most frequent borrowers among users flagged with
-- irregular borrowing behavior.
SELECT event_id, user_id, book_id, borrowing_frequency, irregular_borrowing_flag
FROM borrowing_events
WHERE irregular_borrowing_flag = 1
ORDER BY borrowing_frequency DESC
LIMIT 10;
-- Business interpretation: Surfaces the patrons who borrow very often yet are
-- still flagged as irregular, an edge case worth a manual review since high
-- frequency alone does not guarantee healthy, predictable borrowing behavior.

-- Query 2: The 10 longest reading sessions among actual "Borrowed" interactions.
SELECT event_id, user_id, book_id, reading_duration_minutes
FROM borrowing_events
WHERE interaction_type = 'Borrowed'
  AND reading_duration_minutes >= 150
ORDER BY reading_duration_minutes DESC
LIMIT 10;
-- Business interpretation: Identifies the most deeply engaged borrowing
-- sessions, useful for spotting which specific loans represent the library's
-- most invested readers rather than quick browsers.


-- ------------------------------------------------------------
-- 2. AGGREGATE ANALYSIS (GROUP BY + aggregate functions)
-- ------------------------------------------------------------

-- Query 3: Average recommendation score for cold-start (new/low-history)
-- users versus established users.
SELECT cold_start_user,
       COUNT(*) AS total_events,
       ROUND(AVG(recommendation_score), 3) AS avg_recommendation_score,
       ROUND(AVG(search_count), 1) AS avg_search_count,
       ROUND(AVG(reading_duration_minutes), 1) AS avg_reading_duration_minutes
FROM borrowing_events
GROUP BY cold_start_user;
-- Business interpretation: Cold-start users (1) search and read for roughly
-- the same amount of time as established users (0), but receive a noticeably
-- lower average recommendation score (about 0.48 vs 0.57) - the recommendation
-- engine is not yet serving new patrons as well as it serves returning ones.

-- Query 4: Average borrowing frequency and reading duration by feedback level.
SELECT feedback_level,
       COUNT(*) AS total_events,
       ROUND(AVG(borrowing_frequency), 1) AS avg_borrowing_frequency,
       ROUND(AVG(reading_duration_minutes), 1) AS avg_reading_duration_minutes
FROM borrowing_events
GROUP BY feedback_level
ORDER BY avg_borrowing_frequency DESC;
-- Business interpretation: Compares borrowing intensity across patrons who
-- gave low, medium, and high feedback, showing whether more active borrowers
-- also tend to be more satisfied with the library experience.


-- ------------------------------------------------------------
-- 3. MULTI-TABLE JOINS
-- ------------------------------------------------------------

-- Query 5: Average engagement (views, reservations, 6-month borrow count)
-- per book category.
SELECT b.book_category,
       COUNT(*) AS total_events,
       ROUND(AVG(e.book_view_count), 1) AS avg_views,
       ROUND(AVG(e.reservation_count), 1) AS avg_reservations,
       ROUND(AVG(e.books_borrowed_last_6_months), 1) AS avg_borrowed_last_6mo
FROM borrowing_events e
JOIN books b ON e.book_id = b.book_id
GROUP BY b.book_category
ORDER BY avg_borrowed_last_6mo DESC;
-- Business interpretation: Ranks book categories by real engagement rather
-- than raw title count, showing Artificial_Intelligence and Data_Science
-- lead in average 6-month borrowing activity, useful for acquisition
-- planning.

-- Query 6: Irregular-borrowing rate by department, worst first.
SELECT u.department,
       COUNT(*) AS total_events,
       SUM(e.irregular_borrowing_flag) AS irregular_count,
       ROUND(100.0 * SUM(e.irregular_borrowing_flag) / COUNT(*), 1) AS irregular_rate_pct
FROM borrowing_events e
JOIN users u ON e.user_id = u.user_id
GROUP BY u.department
ORDER BY irregular_rate_pct DESC;
-- Business interpretation: Medicine (17.1%) and Computer_Science (16.7%) show
-- the highest irregular-borrowing rates, pinpointing which departments would
-- benefit most from a targeted borrowing-behavior outreach program.


-- ------------------------------------------------------------
-- 4. BUSINESS-RELEVANT INSIGHTS (directly answer the key business questions)
-- ------------------------------------------------------------

-- Query 7 (answers: "Which book formats generate the most actual borrowing,
-- and does it vary meaningfully by format?")
SELECT b.book_format,
       COUNT(*) AS times_borrowed
FROM borrowing_events e
JOIN books b ON e.book_id = b.book_id
WHERE e.interaction_type = 'Borrowed'
GROUP BY b.book_format
ORDER BY times_borrowed DESC;
-- Business interpretation: Printed_Book, Reference_Book, Journal, and E_Book
-- are borrowed at nearly identical rates (594-617 events each), so format is
-- not a meaningful differentiator of demand in this dataset - the library
-- does not need to shift budget toward or away from any single format.

-- Query 8 (answers: "Are cold-start (new) patrons underserved compared to
-- established patrons, despite putting in similar effort?")
SELECT cold_start_user,
       COUNT(*) AS total_events,
       ROUND(AVG(recommendation_score), 3) AS avg_recommendation_score,
       ROUND(AVG(user_rating), 2) AS avg_user_rating
FROM borrowing_events
GROUP BY cold_start_user;
-- Business interpretation: 18.5% of all events come from cold-start users.
-- Despite giving essentially the same average rating as established users
-- (2.99 vs 2.99), their average recommendation score is about 17% lower
-- (0.478 vs 0.574) - concrete evidence the library's recommendation/discovery
-- experience needs a better onboarding path for new patrons, which the team
-- will explore further in the Checkpoint 4 predictive model.
