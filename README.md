**#Innomatics Research Lab Hackathon**
# Food Delivery Data Analysis 

## Project Overview
This project integrates multiple datasets from a food delivery system to generate actionable insights.  
It combines **orders**, **user information**, and **restaurant details** to analyze:

- User behavior patterns
- City-wise & cuisine-wise performance
- Membership impact (Gold vs Regular)
- Revenue trends and seasonality

All analyses are implemented in **Python** using **Pandas** and **SQLite**, with results presented in a **Jupyter Notebook**.

---

## Dataset Details

| Dataset | Format | Key Info |
|---------|--------|----------|
| `orders.csv` | CSV | Transactional data: order_id, user_id, restaurant_id, order_date, total_amount |
| `users.json` | JSON | User info: name, city, membership |
| `restaurants.sql` | SQL | Restaurant details: name, cuisine, rating |

**Final Merged Dataset:** `final_food_delivery_dataset.csv` (orders + user info + restaurant info)

---

## How to Run

### 1️⃣ Jupyter Notebook
- Open `Food_Delivery_Analysis.ipynb` in VS Code or Jupyter Notebook.  
- Run all cells to see:
  - Merged dataset
  - All analysis results
  - Answers to hackathon questions

### 2️⃣ Python Scripts
- Run `data_merge.py` → creates `final_food_delivery_dataset.csv`.  
- Run `analysis.py` → prints all insights and answers.  

---

## Key Insights

- **City with highest revenue (Gold members):** Chennai  
- **Cuisine with highest average order value:** Mexican  
- **Top revenue combination:** Regular + Mexican  
- **Orders for high-rated restaurants (≥4.5):** 4.6-5.0  
- **Total Gold member orders:**  Chennai 

> Full analysis and answers to all hackathon questions are in the notebook.

---

## Tools & Libraries

- Python 3.x  
- Pandas  
- SQLite3  
- Jupyter Notebook  

---

## Repository

[GitHub Link](https://github.com/Codearti76/Innomatics_Hackathon)

---

**Author:** Aarti Dinkar Chopade  
Hackathon Submission – Real-world Data Analysis 🏆
