# Ecommerce Automation Test Project  

This project is an **n8n workflow** that automates ecommerce operations by connecting Gmail, Google Sheets, and Monday.com.  

## Features  
- **Product Sync**: Fetches product data from [DummyJSON API](https://dummyjson.com/products) and updates Google Sheets.  
- **Email Processing**: Extracts customer and order details from Gmail using **Google Gemini AI**.  
- **Order Management**: Cross-checks product data and creates tasks in **Monday.com** boards.  

## Workflow Overview  
1. Trigger: New email received in Gmail.  
2. Fetch products from DummyJSON API.  
3. Store/Update product details in Google Sheets.  
4. Use AI to extract order details from email content.  
5. Validate with product list.  
6. Create tasks in Monday.com with full order details.  

## Requirements  
- n8n instance  
- Google Sheets API credentials  
- Gmail API credentials  
- Monday.com API credentials  
- Google Gemini API access  
