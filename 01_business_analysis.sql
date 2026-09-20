USE company_insights_360;

-- 1. Overall Business KPIs
SELECT
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    COUNT(DISTINCT order_id) AS total_orders,
    COUNT(DISTINCT customer_id) AS total_customers,
    SUM(quantity) AS total_quantity,
    ROUND(SUM(profit) / SUM(sales) * 100, 2) AS profit_margin_pct
FROM superstore_sales;


-- 2. Regional Performance
SELECT
    region,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(profit) / SUM(sales) * 100, 2) AS profit_margin_pct
FROM superstore_sales
GROUP BY region
ORDER BY total_sales DESC;


-- 3. Category Performance
SELECT
    category,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    SUM(quantity) AS total_quantity,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(profit) / SUM(sales) * 100, 2) AS profit_margin_pct
FROM superstore_sales
GROUP BY category
ORDER BY total_sales DESC;


-- 4. Sub-Category Profitability
SELECT
    sub_category,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(profit) / SUM(sales) * 100, 2) AS profit_margin_pct
FROM superstore_sales
GROUP BY sub_category
ORDER BY total_profit DESC;


-- 5. Loss-Making Sub-Categories
SELECT
    sub_category,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND(SUM(profit) / SUM(sales) * 100, 2) AS profit_margin_pct
FROM superstore_sales
GROUP BY sub_category
HAVING SUM(profit) < 0
ORDER BY total_profit ASC;


-- 6. Discount vs Profitability
SELECT
    discount,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(profit) / SUM(sales) * 100, 2) AS profit_margin_pct
FROM superstore_sales
GROUP BY discount
ORDER BY discount;


-- 7. High-Discount Loss Analysis
SELECT
    discount,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND(SUM(profit) / SUM(sales) * 100, 2) AS profit_margin_pct
FROM superstore_sales
GROUP BY discount
HAVING SUM(profit) < 0
ORDER BY total_profit ASC;


-- 8. Furniture Discount Analysis
SELECT
    discount,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(profit) / SUM(sales) * 100, 2) AS profit_margin_pct
FROM superstore_sales
WHERE category = 'Furniture'
GROUP BY discount
ORDER BY discount;


-- 9. Customer Performance
SELECT
    customer_id,
    customer_name,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(profit) / SUM(sales) * 100, 2) AS profit_margin_pct
FROM superstore_sales
GROUP BY customer_id, customer_name
ORDER BY total_sales DESC;


-- 10. Top 10 Customers by Sales
SELECT
    customer_name,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM superstore_sales
GROUP BY customer_id, customer_name
ORDER BY total_sales DESC
LIMIT 10;


-- 11. Loss-Making Customers
SELECT
    customer_name,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND(SUM(profit) / SUM(sales) * 100, 2) AS profit_margin_pct
FROM superstore_sales
GROUP BY customer_id, customer_name
HAVING SUM(profit) < 0
ORDER BY total_profit ASC;


-- 12. Product Performance
SELECT
    product_id,
    product_name,
    category,
    sub_category,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    SUM(quantity) AS total_quantity,
    ROUND(SUM(profit) / SUM(sales) * 100, 2) AS profit_margin_pct
FROM superstore_sales
GROUP BY product_id, product_name, category, sub_category
ORDER BY total_sales DESC;


-- 13. Top 10 Products by Sales
SELECT
    product_name,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM superstore_sales
GROUP BY product_id, product_name
ORDER BY total_sales DESC
LIMIT 10;


-- 14. Top 10 Products by Profit
SELECT
    product_name,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM superstore_sales
GROUP BY product_id, product_name
ORDER BY total_profit DESC
LIMIT 10;


-- 15. Bottom 10 Products by Profit
SELECT
    product_name,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM superstore_sales
GROUP BY product_id, product_name
ORDER BY total_profit ASC
LIMIT 10;


-- 16. State Performance
SELECT
    state,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(profit) / SUM(sales) * 100, 2) AS profit_margin_pct
FROM superstore_sales
GROUP BY state
ORDER BY total_sales DESC;


-- 17. Bottom 10 States by Profit
SELECT
    state,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND(SUM(profit) / SUM(sales) * 100, 2) AS profit_margin_pct
FROM superstore_sales
GROUP BY state
ORDER BY total_profit ASC
LIMIT 10;


-- 18. City Performance
SELECT
    city,
    state,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND(SUM(profit) / SUM(sales) * 100, 2) AS profit_margin_pct
FROM superstore_sales
GROUP BY city, state
ORDER BY total_sales DESC;


-- 19. Customer Segment Performance
SELECT
    segment,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    COUNT(DISTINCT order_id) AS total_orders,
    COUNT(DISTINCT customer_id) AS total_customers,
    ROUND(SUM(profit) / SUM(sales) * 100, 2) AS profit_margin_pct
FROM superstore_sales
GROUP BY segment
ORDER BY total_sales DESC;


-- 20. Yearly Performance
SELECT
    YEAR(order_date) AS order_year,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    COUNT(DISTINCT order_id) AS total_orders,
    COUNT(DISTINCT customer_id) AS total_customers,
    ROUND(SUM(profit) / SUM(sales) * 100, 2) AS profit_margin_pct
FROM superstore_sales
GROUP BY YEAR(order_date)
ORDER BY order_year;


-- 21. Monthly Performance
SELECT
    YEAR(order_date) AS order_year,
    MONTH(order_date) AS order_month,
    MONTHNAME(order_date) AS month_name,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND(SUM(profit) / SUM(sales) * 100, 2) AS profit_margin_pct
FROM superstore_sales
GROUP BY YEAR(order_date), MONTH(order_date), MONTHNAME(order_date)
ORDER BY order_year, order_month;


-- 22. Year-over-Year Sales Growth
WITH yearly_sales AS (
    SELECT
        YEAR(order_date) AS order_year,
        SUM(sales) AS total_sales
    FROM superstore_sales
    GROUP BY YEAR(order_date)
)
SELECT
    order_year,
    ROUND(total_sales, 2) AS total_sales,
    ROUND(
        (total_sales - LAG(total_sales) OVER (ORDER BY order_year))
        / LAG(total_sales) OVER (ORDER BY order_year) * 100,
        2
    ) AS yoy_sales_growth_pct
FROM yearly_sales
ORDER BY order_year;


-- 23. Year-over-Year Profit Growth
WITH yearly_profit AS (
    SELECT
        YEAR(order_date) AS order_year,
        SUM(profit) AS total_profit
    FROM superstore_sales
    GROUP BY YEAR(order_date)
)
SELECT
    order_year,
    ROUND(total_profit, 2) AS total_profit,
    ROUND(
        (total_profit - LAG(total_profit) OVER (ORDER BY order_year))
        / LAG(total_profit) OVER (ORDER BY order_year) * 100,
        2
    ) AS yoy_profit_growth_pct
FROM yearly_profit
ORDER BY order_year;


-- 24. Ship Mode Performance
SELECT
    ship_mode,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(profit) / SUM(sales) * 100, 2) AS profit_margin_pct
FROM superstore_sales
GROUP BY ship_mode
ORDER BY total_sales DESC;


-- 25. High Sales but Low Profit Categories
SELECT
    category,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND(SUM(profit) / SUM(sales) * 100, 2) AS profit_margin_pct
FROM superstore_sales
GROUP BY category
HAVING SUM(sales) > 500000
   AND SUM(profit) / SUM(sales) < 0.10
ORDER BY total_sales DESC;


-- 26. High-Sales Loss-Making Products
SELECT
    product_name,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM superstore_sales
GROUP BY product_id, product_name
HAVING SUM(sales) > 5000
   AND SUM(profit) < 0
ORDER BY total_profit ASC;


-- 27. High-Sales Loss-Making Customers
SELECT
    customer_name,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM superstore_sales
GROUP BY customer_id, customer_name
HAVING SUM(sales) > 5000
   AND SUM(profit) < 0
ORDER BY total_profit ASC;


-- 28. Region + Category Profitability
SELECT
    region,
    category,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND(SUM(profit) / SUM(sales) * 100, 2) AS profit_margin_pct
FROM superstore_sales
GROUP BY region, category
ORDER BY region, total_profit ASC;


-- 29. Furniture Profitability Drill-Down
SELECT
    region,
    sub_category,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND(SUM(profit) / SUM(sales) * 100, 2) AS profit_margin_pct
FROM superstore_sales
WHERE category = 'Furniture'
GROUP BY region, sub_category
ORDER BY total_profit ASC;


-- 30. Loss-Making States with Significant Sales
SELECT
    state,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND(SUM(profit) / SUM(sales) * 100, 2) AS profit_margin_pct
FROM superstore_sales
GROUP BY state
HAVING SUM(sales) > 50000
   AND SUM(profit) < 0
ORDER BY total_profit ASC;