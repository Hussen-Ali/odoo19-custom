# 🧩 Odoo Community + Custom Addons & Apps

Welcome to my **Odoo Community Addons & Apps** repository.  
This repo contains my personal custom developments on top of Odoo Community Edition to make business operations smoother, faster, and more tailored to real-world commercial needs.

## 📦 About This Repository

- Base system: **Odoo Community**
- Purpose: To provide practical, business-focused enhancements through custom addons and apps.
- Status: Addons will be added progressively as they’re developed and tested.

## 🚀 Current Addons

### 1. Confirm & Receive Module ✅ (Still need some edits such as giving this perm to specific users)
This addon streamlines sales order processing:
- Replaces the standard **“Confirm”** button in the Sales Order with **“Confirm & Receive”**.
- Confirms the order **and** triggers immediate receipt creation in one click (keep in mind this is only for Non-Tracked products, where Lot need to be specified manualy in order to be recieved in the inventory (maybe we can put lot automatically depending on a user specification)).
- Ideal for businesses that require quick sales and stock operations without extra steps.

### 2. Item Box Module (In Progress) 📦
This upcoming addon introduces flexible item packaging options:
- Adds a **“Box” field** for each product.
- Allows defining **custom packaging names** (e.g., Box, Carton, Bag, or any user-defined name).
- Assigns a **box price** for better inventory and pricing control.

## 🏗️ Roadmap

- [ ] Complete Item Box Module  
- [ ] Add more business-focused modules  
- [ ] Improve UI for faster daily operations  
- [ ] Documentation for each module

## 🧰 Installation

1. Clone repository modules:
   ```bash
   git clone https://github.com/Hussen-Ali/custom_addons/sale_confirm_receive
