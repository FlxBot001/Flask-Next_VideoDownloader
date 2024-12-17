# 🎥 **Flask Video Downloader**

A simple and powerful **Video Downloader** built using **Flask** and APIs to fetch video metadata and allow easy downloading. This app takes a video URL, processes it to extract video details (like title and thumbnail), and provides options to download it.

---

## 📋 **Features**

- 🔗 Input a video URL and retrieve metadata.
- 🖼️ Display video title and thumbnail.
- 🚀 Download video content seamlessly.
- 🔥 Lightweight and built with Flask.
- 🧩 API-driven architecture for clean separation.

---

## 🛠️ **Technologies Used**

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS (Bootstrap optional)
- **APIs**: YouTube or other video metadata extraction APIs
- **Environment Management**: Virtualenv

---

## 🚀 **Getting Started**

Follow the steps below to set up and run the Flask Video Downloader locally.

### **1. Prerequisites**

Make sure you have the following installed:

- **Python 3.x**  
- **pip** (Python package manager)

---

### **2. Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/FlxBot001/Flask-Next_VideoDownloader.git
   cd Flask-Next_VideoDownloader
   ```

2. Set up a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate     # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

### **3. Run the Application**

1. Start the Flask server:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

---

## 📂 **Project Structure**

```
video-downloader-flask/
│
├── templates/
│   ├── index.html           # Home page with video URL form
│   └── download.html        # Video metadata and download page
│
├── extractor.py             # Contains logic for video metadata extraction
├── app.py                   # Flask application routes
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## 🔧 **How it Works**

1. **Input**: Enter a valid video URL in the form on the homepage.
2. **Processing**: The server uses the `extractor.py` script to fetch metadata (title, thumbnail, etc.) via APIs.
3. **Output**: The video details are displayed, and the user can proceed to download the video.

---

## 🎯 **Endpoints**

| **Route**       | **Method** | **Description**                  |
|-----------------|------------|----------------------------------|
| `/`             | `GET`      | Home page with URL input form    |
| `/download`     | `POST`     | Processes URL and fetches video metadata |

---

## 📦 **Dependencies**

The key dependencies used in this project are:

- Flask  
- Requests  
- (Optional) APIs like `pytube` for YouTube video extraction  

Install all dependencies via:
```bash
pip install -r requirements.txt
```

---

## 🎨 **UI Example**

- **Home Page**:  
  ![Home Page](https://via.placeholder.com/600x300?text=Input+Video+URL+Here)

- **Video Details Page**:  
  ![Video Download](https://via.placeholder.com/600x300?text=Video+Details+and+Download)

---

## 🐛 **Troubleshooting**

1. **Method Not Allowed**:
   - Ensure the form uses `method="POST"` and not `methord`.

2. **KeyError in metadata**:
   - Validate video metadata keys like `title`, `thumbnail` before using.

3. **API Issues**:
   - Check that the video API or library (`pytube` or others) is properly configured.

---

## 🌟 **Future Enhancements**

- Add support for multiple video platforms.
- Allow video quality and format selection.
- Include a progress bar for downloads.
- Dockerize the application for easy deployment.

---

## 🤝 **Contributing**

Contributions are welcome! Feel free to fork this repository and submit a pull request.

---

## 📝 **License**

This project is licensed under the MIT License.  

---

## 💬 **Contact**

For any questions or issues, reach out via:

- **GitHub**: [FlxBot001](https://github.com/FlxBot001)
- **Email**: njugunafelix79@gmail.com 
- **Contact**: +254 1112-55301 