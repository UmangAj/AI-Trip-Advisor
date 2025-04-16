# 🧠 AI Trip Advisor

AI Trip Advisor is an intelligent travel assistant web application that allows users to upload an image or enter text related to a landmark and receive a wealth of travel information. The system utilizes AI models to identify landmarks, provide historical facts, nearby attractions, and travel tips.

## 🌐 Live Demo

🚀 Check out the live app here: [ai-trip-advisor.streamlit.app](https://ai-trip-advisor.streamlit.app/)

## 📌 Features

- 🖼️ Upload an image to detect a landmark  
- 🔍 Search by text input  
- 🏛️ Get historical facts about the landmark  
- 📍 Discover nearby tourist spots  
- 🌍 Receive travel tips  
- ✅ User feedback through a simple checkbox interface  

## 🚀 Tech Stack

- **Frontend:** Streamlit (Python)
- **Backend:**  
  - Google Gemini (for image detection)  
  - Gemma (for content generation)  
  - Custom API (to fetch related images)

## 🔧 Functionalities

- Accepts image or text input
- Detects the location of the image using AI
- Displays historical and cultural information
- Lists nearby must-visit places
- Suggests top-rated tourist spots

## 📐 System Design

### 🖥️ User Interface
- Streamlit-based layout with:
  - File uploader
  - Submit button
  - Text input area
  - Feedback checkbox
  - Dynamic sections for displaying output

### 🧠 Backend Logic
- Gemini for image landmark recognition
- Gemma for generating relevant text information
- Integration with third-party image search APIs

## ✅ Requirements

### Functional
- Upload and analyze image/text
- Identify landmarks accurately
- Provide relevant historical and geographical information

### Non-Functional
- Fast and responsive output
- High accuracy and relevance in content
- Clean and intuitive interface

## 🧪 Testing and Validation

- Tested with various prompts and image qualities
- Validated information for accuracy and usefulness
- Performance measured for speed and efficiency

## 📚 References

- [Tripadvisor](https://www.tripadvisor.in/)
- [Trip Planner AI](https://tripplanner.ai/)
- [Wonderplan](https://wonderplan.ai/)
