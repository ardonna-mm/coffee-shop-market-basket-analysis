# Coffee Shop Market Basket Analysis

## 📌 Project Overview
This project extends the Daily Grind Coffee Shop dataset by applying **Market Basket Analysis** using the Apriori algorithm.  
The goal is to uncover frequent product combinations and generate actionable insights for **product bundling** and **promotion strategies**.

## ⚙️ Tools & Libraries
- Python (pandas, numpy)
- mlxtend (Apriori & Association Rules)
- matplotlib / seaborn (visualization)
- Jupyter Notebook

## 📊 Workflow
1. **Data Preparation**  
   - Re-engineered dataset into multi-item baskets.  
   - One-hot encoded transactions for Apriori algorithm.  

2. **Frequent Itemset Mining**  
   - Identified popular single items (e.g., Croissants, Muffins).  
   - Discovered item pairs (e.g., Muffin + Cappuccino).  

3. **Association Rules**  
   - Analyzed confidence, lift, and support for product combinations.  
   - Found modest but useful associations (e.g., Latte → Croissant).  

4. **Business Insights**  
   - Suggested bundling opportunities (Latte + Croissant).  
   - Recommended testing promotions to increase average order size.  

## 📈 Results
- Croissants and Muffins appeared in nearly 50% of baskets.  
- Confidence values around **50%** indicate common but weak associations.  
- Lift ≈ **1.0** suggests patterns are slightly better than random chance.  

## 🤔 Reflection
While results were modest due to the dataset structure, this project strengthened my skills in **data preparation, association rule mining, and business interpretation**. It demonstrates how analytics can guide **retail bundling strategies** even when patterns are weak.  

## 🟢 Author
Ardonna Cardines — Data & Decision Analyst

## 🔗 Related Project
This analysis builds on my **Daily Grind Coffee Dashboard Project**, where I designed a Power BI reporting solution for sales, products, and customer insights.  
👉 [Daily Grind Coffee Dashboard Project](https://github.com/aleighcar/coffee-shop-sales-bi-dashboard)
