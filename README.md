# Log Monitoring and Alert System using AWS Lambda

This project is a mini log monitoring and alert system built using AWS services including **API Gateway**, **Lambda**, **DynamoDB**, and **SES**.

## Features

- Accepts log events through a REST API.
- Filters for critical keywords like `CRITICAL`, `ERROR`, or `FAILURE`.
- Sends alert emails using **Amazon SES** when critical logs are detected.
- Stores all log entries in **Amazon DynamoDB**.

## Technologies Used

- AWS Lambda (Python 3.12)
- AWS API Gateway (HTTP trigger)
- AWS DynamoDB
- AWS SES (Simple Email Service)
- Postman (for testing)

## API Endpoint
POST  https://xxx.execute-api..amazonaws.com/dev
> Replace `xxx` with the actual endpoint ID from your API Gateway.  
> You can find the full URL in the AWS Console by navigating to:  
**API Gateway → Your API Name → Stages → [Stage Name] → Invoke URL**

### Sample Request Body (JSON)

```json
{
  "service": "MyApp",
  "level": "CRITICAL",
  "message": "Test error from Postman",
  "customerEmail": "your_verified_email@example.com",
  "timestamp": "2025-06-27T22:30:00Z"
}
