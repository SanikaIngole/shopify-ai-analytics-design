# AI-Powered Shopify Analytics (Design-Focused)

## Overview
This project is a design-focused implementation of an AI-powered Shopify analytics system.
The goal is to allow users to ask natural language questions and receive business-friendly insights.

Due to API credential and scope limitations, Shopify APIs and LLM integrations are mocked.

## System Architecture
1. User sends a question via API
2. Rails API receives and validates the request
3. Rails forwards the question to Python AI service
4. Python service:
   - Identifies intent (sales / inventory / customers)
   - Generates ShopifyQL (mock)
   - Processes results
   - Returns simple explanation
5. Rails sends final response to user

## Agent Workflow
- Understand user intent
- Select required Shopify data
- Build ShopifyQL query
- Validate query
- Explain result in simple language

## Sample API Request
POST /api/v1/questions
{
  "store_id": "example-store.myshopify.com",
  "question": "How much inventory should I reorder next week?"
}

## Sample API Response
{
  "answer": "Based on the last 30 days, you sell around 10 units per day. You should reorder 70 units.",
  "confidence": "medium"
}

## Sample ShopifyQL Queries
- Top selling products last 7 days
- Inventory levels by product
- Repeat customers in last 90 days

## Limitations
- Shopify OAuth and APIs are mocked
- LLM responses are simulated
- Focus is on architecture and reasoning, not production code
