# Presentation Script — Checkpoint 4 (Final Defense)
### Library Analytics: Book Borrowing Trends and Student Reading Behavior

This is a word-for-word speaking script for the **final screen-recorded video**, written in the same style as the Checkpoint 1 & 2 script. Three presenters split the work below. The project guide asks for a **20-25 minute** defense; this script runs about **22 minutes** at a normal speaking pace. It follows the required order: Introduction → Data & SQL → Statistics → Live Dashboard → Predictive & Recommendations → Ethics → Q&A.

---

## Before You Hit Record

Only **two things** appear on screen in this recording: the slide deck and Power BI.

1. `docs/Checkpoint 4 - Final Presentation.pptx` open in PowerPoint in **Slide Show** mode (7 slides)
2. `PowerBI/LIBRARY_ANALYTICS_DASHBOARD.pbix` open in Power BI Desktop on Page 1, **all slicers cleared**, ready to Alt+Tab to

Nothing else needs to be open (no SQL, Excel or Word windows). Every number you say is on a slide or in the dashboard.

**Who says what:**
- **Presenter 1, Peter Paul Polestico (Project Lead / Analyst):** Introduction, ethics, recommendations and closing
- **Presenter 2, Ken T. Lubrico (Data Engineer):** Data and SQL overview, then the live dashboard demo
- **Presenter 3, Johnro Balingit (Statistician / Modeler):** Statistical insights, then the predictive model

Every member speaks more than once, as the rubric requires. Swap names freely, but keep the order.

---

## Part 0 — Introduction & Business Context (Presenter 1) — ~2.5 minutes

**[Screen: Slide 1 — Library Analytics: Borrowing Trends & Reading Behavior]**

> "Good day, everyone. We are Group 1, The Data Bookworms, and this is the final presentation of our capstone project for BED 106, Business Analytics, under Sir Jessie Melendres. Our project is Library Analytics: Book Borrowing Trends and Student Reading Behavior.
>
> I'm Peter Paul Polestico, the Project Lead and Analyst. With me are Ken Lubrico, our Data Engineer, and Johnro Balingit, our Statistician and Modeler, who also built our dashboard.
>
> Over the semester we worked through four checkpoints: SQL and database design, spreadsheet statistics, a Power BI dashboard, and today's final piece, predictive analytics and ethics. In this video we'll walk through all four as one connected story."

**[Screen: stay on Slide 1, point to the three business questions]**

> "Here's the business problem. An academic library wants its collection and its recommendation features to match how patrons actually behave. But it has no data-driven way of seeing who is using the collection, which books earn real engagement, and whether new patrons are treated as well as established ones.
>
> So we asked three questions. One: which patron types and departments borrow irregularly? Two: which book categories and formats drive engagement? And three: are new patrons (we call them cold-start patrons) underserved by the recommendation system, even when they put in the same effort?
>
> One thing we want to be upfront about: our dataset is a real file from Kaggle, but our quality checks showed it is synthetic, meaning generated rather than taken from a real library's records. We say this clearly in our report, and it shapes how carefully we interpret our results. I'll hand it to Ken to show how we built the database."

---

## Part 1 — Data & SQL Overview (Presenter 2) — ~3.5 minutes

**[Screen: Slide 2 — Data & SQL Overview, ERD on the left]**

> "Thanks, Peter. Our data has 12,000 rows, and each row is one interaction between a patron and a book. We split that single flat file into three connected tables. The `users` table holds patron type and department. The `books` table holds category and format. And `borrowing_events` in the middle records each interaction, with the reading time, searches, ratings and the recommendation score. One user and one book can each appear in many events, so these are one-to-many relationships.
>
> We checked the data quality before loading it. There were no missing values and no duplicates. We converted the Yes/No flags to numbers, created an event ID, and confirmed every user and book in the events table exists in its own table."

**[Screen: stay on Slide 2, point to the three result cards: 0.478 vs 0.574, 17.1%, 594-617]**

> "We wrote eight queries. Let me run three that answer our business questions.
>
> This first one compares cold-start patrons with established patrons. [Point to the first card.] Cold-start patrons are about 18.5 percent of all events. They give almost exactly the same average rating, 2.99 for both groups, but their average recommendation score is 0.478 compared with 0.574. So new patrons put in the same effort and the same satisfaction, but get lower-quality recommendations.
>
> Next, irregular borrowing by department. [Point to the second card.] Medicine is highest at 17.1 percent and Computer Science is next at 16.7 percent. But the lowest, Science, is 14.9 percent. When we tested this later, the differences between departments were too small to be statistically significant, so we'll be careful not to overstate it.
>
> And finally, borrows by book format. [Point to the third card.] Printed books, reference books, journals and e-books are all between 594 and 617 borrows. Format simply isn't a differentiator of demand in this data."

**[Screen: stay on Slide 2]**

> "The final report has all eight queries with their interpretations. Now I'll pass it to Johnro for the statistics."

---

## Part 2 — Statistical Insights (Presenter 3) — ~3.5 minutes

**[Screen: Slide 3 — Statistical Insights, histogram and three cards]**

> "Thank you, Ken. For the statistics we used the same dataset in Excel and focused on three variables: borrowing frequency, reading duration and recommendation score.
>
> Patrons average about 19 borrows, read for about 94 minutes per session, and receive an average recommendation score of 0.556 out of 1. Borrowing frequency is right-skewed. About 35 percent of events come from patrons who borrow nine times or fewer, but 11 percent are very frequent borrowers in the 40-to-45 range. So the library has many light borrowers and a smaller core of heavy ones."

**[Screen: stay on Slide 3, point to the right-hand bullets]**

> "Next, correlation. Borrowing frequency and recommendation score have a moderate positive correlation of 0.51. We then built a simple regression: recommendation score equals 0.48 plus 0.0038 times borrowing frequency. The slope is highly significant, but R-squared is only 0.256. So borrowing frequency alone explains about a quarter of the variation in the score.
>
> That left a question: what explains the other three quarters? That is exactly what our predictive model in Checkpoint 4 answers, and I'll show it in a few minutes, after Ken walks us through the dashboard."

*(Presenter 3 pauses here; the recording moves directly to the dashboard.)*

---

## Part 3 — Live Dashboard Demo (Presenter 2) — ~5.5 minutes

**[Screen: Slide 4 — Live Dashboard Demo, show for about 10 seconds, then switch to Power BI Desktop, Page 1, no filters]**

> "Now the dashboard. It has three pages connected by these navigation buttons, and four slicers (User Type, Department, Semester Period and Segment) that stay synchronized across every page.
>
> On Page 1, our five KPI cards: 12,000 patrons, an average recommendation score of 0.556, an irregular borrowing rate of 16.1 percent, a cold-start share of 18.5 percent, and an average reading duration of 94.3 minutes. These match our SQL and Excel results exactly, which is how we checked our accuracy.
>
> The middle chart shows the cold-start gap we talked about: 0.478 for cold-start against 0.574 for established patrons. The bar chart on the right is irregular borrowing by department, sorted highest first."

**[Action: Live filter demo 1 — Department slicer → Medicine]**

> "Let me demonstrate the interactivity. I'll select Medicine in the Department slicer. [Click.] All the cards and charts update together. We now see only Medicine's 1,524 events, and the irregular rate is 17.1 percent, matching Query 6. Let me clear that."

**[Click Trends button → Page 2 — Trend & Comparison]**

> "Page 2 compares patterns. The line chart shows average recommendation score climbing steadily as borrowing frequency goes up, with a trend line. The bar chart shows average books borrowed by category. Artificial Intelligence and Data Science are slightly ahead, but the bars are close. The matrix shows category against patron type, and the stacked column shows interactions by format. Everything looks balanced, which supports our earlier finding that format and patron type are not demand drivers."

**[Click Segments button → Page 3 — Segmentation]**

> "Page 3 is our data mining work. We used K-Means clustering on borrowing frequency and reading duration. We chose four clusters using the elbow method and silhouette score. This scatter plot shows the four segments by color, and the table gives each profile.
>
> Devoted Readers are 23 percent of patrons. They borrow often, about 33 times, and read long, about 137 minutes, and have the best recommendation score at 0.641. Quick Borrowers borrow just as often but read only about 51 minutes. Occasional Deep Readers read for 138 minutes but borrow only about 8 times. And Casual and At-Risk Patrons borrow rarely and read briefly, with the lowest score, 0.478."

**[Action: Live filter demo 2 — Segment slicer → Casual / At-Risk Patrons]**

> "Watch what happens when I filter to Casual and At-Risk Patrons. [Click.] That's 3,285 patrons, about 27 percent of the total, and about 34 percent of them are cold-start patrons. Now compare with Devoted Readers. [Click.] Their score jumps to 0.641 and none of them are cold-start. So the segments connect directly to our cold-start question. This group is where the library should focus its onboarding. Back to Johnro for the predictive model."

---

## Part 4 — Predictive Analytics (Presenter 3) — ~4.5 minutes

**[Screen: Slide 5 — Predictive Analytics (switch back from Power BI to the slide deck)]**

> "Thanks, Ken. For Checkpoint 4 we extended the simple regression into two models using Python. We split the data 70-30 into training and test sets, so every performance number I'll give you comes from data the model never saw.
>
> Model A is a multiple linear regression. It predicts the recommendation score using 13 predictors, including borrowing frequency, reading duration, interest score, metadata match, similarity, popularity, renewals, views, reservations, rating, searches, and the cold-start flag."

**[Screen: stay on Slide 5, point to the actual-vs-predicted chart on the left]**

> "This chart plots actual scores against predicted scores on the test data. The points hug the diagonal line, which means the model predicts well. R-squared is 0.914, a big jump from 0.256 in the simple model, and the typical error is only about 0.02 on a zero-to-one scale."

**[Screen: stay on Slide 5, point to the predictor-importance bar chart]**

> "This chart shows which predictors matter most. Ten of the thirteen are highly significant. Borrowing frequency is the strongest, followed by reading duration, book views and renewals. Three predictors are not significant: books borrowed in the last six months, search count, and, importantly, the cold-start flag itself.
>
> That's a key insight. Once you account for how often someone borrows, being flagged as new adds nothing. New patrons score lower because they have little borrowing history. The typical new patron, with about three borrows, is predicted at 0.50, compared with 0.57 for a typical established patron."

**[Screen: stay on Slide 5, point to the 94.6% accuracy card]**

> "Model B is a logistic regression that predicts whether a patron will receive a low recommendation. It reaches 94.6 percent accuracy, compared with 84 percent if we just guessed 'not low' every time. It catches about 78 percent of the truly low cases, and when it flags someone, it's right about 87 percent of the time.
>
> A few honest limits. Our data is synthetic, and the recommendation score is itself produced by an algorithm, so the high R-squared mostly shows we've recovered how the score is calculated. It describes association, not cause. And the models only apply within the ranges we observed. I'll hand it back to Peter for the recommendations and ethics."

---

## Part 5 — Recommendations (Presenter 1) — ~2 minutes

**[Screen: Slide 6 — Recommendations]**

> "Thank you, Johnro. Based on all four checkpoints, we have five recommendations.
>
> One: build a fast-start onboarding path for new patrons: guided first-loan lists, a short interest profile at sign-up, and a prompt after the first borrow. Our model says this should close most of the roughly 0.07 score gap.
>
> Two: use segment-specific nudges. Loan reminders for Occasional Deep Readers, 'read next' lists for Quick Borrowers, and friendly check-ins for Casual and At-Risk Patrons.
>
> Three: run irregular-borrowing reminders library-wide, not department by department, because the department differences aren't statistically significant.
>
> Four: improve book metadata and collect richer patron interests, since both are significant predictors.
>
> And five: use our classifier as a weekly early-warning list, with a librarian reviewing each case rather than acting automatically."

---

## Part 6 — Ethics & Governance (Presenter 1) — ~1.5 minutes

**[Screen: Slide 7 — Ethics, Governance & Conclusion]**

> "On ethics. Our dataset has no names or direct identifiers, only coded patron IDs, and it's synthetic, so no real person's reading history is exposed. But reading records are sensitive in real life, so with real data we'd need the library's permission, no direct identifiers, and aggregation to prevent re-identification.
>
> The biggest ethical issue is the finding itself. New patrons get lower recommendation scores for equal effort, so if those scores were used to allocate attention or resources, newcomers would be disadvantaged. We also warn against using segments or the irregular flag to label or penalize individuals, and our classifier makes mistakes, so people must review its output.
>
> For governance, we propose a defined purpose, data minimization, role-based access, retention limits, regular fairness checks and transparency with patrons. In the Philippines, the Data Privacy Act of 2012, Republic Act 10173, applies, and its principles of transparency, legitimate purpose and proportionality guide our recommendations."

---

## Part 7 — Closing (Presenter 1) — ~0.5 minute

**[Screen: stay on Slide 7, closing line at the bottom]**

> "To close: new patrons are underserved not because they're new, but because they have little borrowing history, and the library can fix that with onboarding. Irregular borrowing is library-wide, format and category matter little, and four patron segments give the library clear targets for outreach. All of this needs validation with real circulation data.
>
> Thank you for watching. We're happy to take your questions."

---

## Timing Recap

| Part | Presenter | Approx. Time |
|---|---|---|
| Introduction & Business Context | Presenter 1 (Peter) | 2.5 min |
| Data & SQL Overview | Presenter 2 (Ken) | 3.5 min |
| Statistical Insights | Presenter 3 (Johnro) | 3.5 min |
| Live Dashboard Demo | Presenter 2 (Ken) | 5.5 min |
| Predictive Analytics | Presenter 3 (Johnro) | 4.5 min |
| Recommendations | Presenter 1 (Peter) | 2 min |
| Ethics & Governance | Presenter 1 (Peter) | 1.5 min |
| Closing | Presenter 1 (Peter) | 0.5 min |
| **Total** | | **~23.5 min** |

If you need to trim toward 20 minutes, shorten the Page 2 walkthrough and the Excel correlation talk first.

---

## Anticipated Q&A (the guide allows 5 minutes of questions)

**Q: Your data is synthetic. Why should we trust the findings?**
A: We don't claim these are proven facts about real patrons. We disclosed the synthetic nature in Checkpoint 1 and used the data to demonstrate the full analytics process. The findings describe how the recommendation system behaves in this data, and we recommend validating them on real circulation records.

**Q: Why is R-squared so high (0.91)? Is the model overfitted?**
A: No, because the 0.914 is measured on a held-out test set and is nearly the same as the training value of 0.918. It is high because the recommendation score is generated by an algorithm from these same inputs, so we've essentially recovered its formula. That is why we describe it as association, not causation.

**Q: Why did you choose four clusters?**
A: We tested two to eight clusters using the elbow method and silhouette score, and chose four because they gave a useful business split: high or low borrowing combined with long or short reading. The features are fairly evenly spread, so the segments are practical groupings for targeting rather than naturally separated groups.

**Q: Why is the cold-start flag not significant if cold-start patrons score lower?**
A: Because cold-start patrons all have very low borrowing frequency, at most 5. Borrowing frequency already captures the effect, so once it's in the model the flag adds nothing. That means the gap comes from limited history, and helping new patrons borrow sooner should narrow it.

**Q: Are Medicine and Computer Science really the problem departments?**
A: They're highest, at 17.1 and 16.7 percent, but the spread between departments is small and a chi-square test gave p = 0.81, so the difference isn't statistically significant. That's why we recommend library-wide reminders.

**Q: How does your work comply with the Data Privacy Act?**
A: The data has no direct identifiers and is synthetic, so RA 10173 doesn't restrict this project. For real data we'd follow its principles of transparency, legitimate purpose and proportionality, and its requirements for security, access rights and breach reporting.

**Q: Why didn't you do the time-series forecast in Checkpoint 2?**
A: The dataset has no dates, only three categorical semester periods with no ordering, so a forecast wasn't possible. We compared average borrowing across those periods instead and found no meaningful difference.

---

## Recording Tips

- Do one full read-through before recording, especially for the numbers (0.478 vs 0.574, 0.914, 94.6%).
- Before recording the dashboard part, clear all slicers and check the KPI cards show 12,000 / 0.556 / 16.1% / 18.5% / 94.3 min.
- Zoom in on Power BI so small text is readable on video.
- Run the slideshow from Slide 1 and only switch windows at the Slide 4 dashboard demo and back to Slide 5.
- Each member should say at least a few sentences, and the video should show every member's name or voice clearly.
- Speak at a normal pace. Pauses can be trimmed in editing.
