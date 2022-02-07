# Cornershop´s Data Science Test

Cornershop has operations in several cities and countries, delivering thousands of orders every day. In order to deliver these orders on time we depend on good estimations of how much time the shopper needs to complete the order.

In this technical test you will be creating a machine learning model to make these estimation. As we internally build our machine learning solutions using python, we ask you to do the same in this technical test. However you are free to use the libraries you are most comfortable with.

## Before you begin ##
You will need to create a new repository and invite @ThomasSve and @Camiloez as collaborators.

## Data

In this repository, we have included data representing the order, shopper and the store branch. 

### File description and data fields
***order_products.csv:***
- order_id: ID of the order
- product_id: ID of the product
- quantity: The quantity ordered of this product
- buy_unit: The unit of the product (KG/UN)

***orders.csv:***
- order_id: ID of the order
- lat: The latitude of the delivery location
- lng: The longitude of the delivery location
- promised_time: The delivery time promised to the user
- on_demand: If true, the order was promised to be delivered in less than X minutes
- shopper_id: ID representing the shopper completed the order.
- store_branch_id: ID of the store branch
- total_minutes: The total minutes it took to complete the order (label)

***shopper.csv***
- shopper_id: ID of the shopper
- seniority: The experience level of the shopper.
- found_rate: Percentage of products found by shopper historical.
- picking_speed: Historical picking speed, products pr minutes.
- accepted_rate: Percentage of orders historically accepted by shopper
- rating: client rating of shopper

***storebranch.csv:***
- store_branch_id: ID of the store branch
- store: ID representing the store
- lat: Latitude of the branch location
- lng: Longitude of the branch location

*All the data has been anonymized*

### Objective

The objective is to predict the `total_minutes` a order takes to complete, where the rows not containing a `total_minutes` value should be set aside as a part of the submission file, containing the `order_id` with the predicted values. 

As we are interested in seeing how you attacked the problem, we also ask you to include your code together with the submission file. The code needs to be well documented, explaining the decisions made. With these explanations, we will be looking at everything from how the data was processed, features used to the completed model and predictions. 

Good luck!
