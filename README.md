# 🧩 Odoo Community + Custom Addons & Apps

Welcome to my **Odoo Community Addons & Apps** repository.  
This repo contains my personal custom developments on top of Odoo Community Edition to make business operations smoother, faster, and more tailored to real-world commercial needs.

## 📦 About This Repository

- Base system: **Odoo Community**
- Purpose: To provide practical, business-focused enhancements through custom addons and apps.
- Status: Addons will be added progressively as they’re developed and tested.
- Each custom module has an associated **video demonstration**.
- **Note:** There are other addons in this repo that are open-source from the internet (e.g., web themes, accountant app, Query Deluxe for database). You can ignore those—they are not custom.

## 🚀 Current Custom Addons

### 1. Sale Confirm & Receive Module ✅
Streamlines sales order processing:
- Confirms the order **and** triggers immediate receipt creation in one click (works for Non-Tracked products; lot numbers must be specified manually unless configured otherwise).
- Reduces extra steps in sales-to-stock operations.
- Can be restricted to specific users (permission-based).


https://github.com/user-attachments/assets/10c8ae4a-9a07-4477-bd71-80d1fb50800c


### 2. Sale Price Check Module ✅
Prevents selling products below their **Average Cost (AVCO)**:
- Checks sales orders and prevents confirmation if the unit price is below the product's average cost.
- Ideal for maintaining profitability and avoiding accidental losses.


https://github.com/user-attachments/assets/9230b322-0b80-4d10-93a6-ead80744bcc5


### 3. Barcode Support Module ✅
Enhances the **Purchase** app with barcode scanning:
- Scan barcodes to automatically fetch and add products.
- Eliminates manual search and typing.
- Speeds up stock receipt and purchase order processing.


https://github.com/user-attachments/assets/1380a503-fae0-4de5-a410-e15c7e5597f2


### 4. Product Box Module (In Progress) 📦
Upcoming addon for selling products with packages/boxes:
- introduces a new product named “BOX”.
- When you buy a package of items, the BOX product stock increases by 1.
- Each purchased item placed in a package contributes to incrementing the BOX stock.
- Enables tracking the number of packages (boxes) based on purchases.
- Still under development.

## 🏗️ Roadmap

- [ ] Complete Product Box Module  
- [ ] Add more business-focused modules  
- [ ] Improve UI for faster daily operations  
- [ ] Documentation for each module  

## 🧰 Installation

1. Clone repository modules:
   ```bash
   git clone https://github.com/Hussen-Ali/custom_addons.git
