from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

# Mount static files (CSS, images, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configure Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Placeholder for MongoDB connection string (replace with actual Atlas URI)
# MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017/")
# Placeholder for database operations (will be implemented later)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "school_name": "International Kidz World Montessori Play School"})

@app.get("/about", response_class=HTMLResponse)
async def view_about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request, "school_name": "International Kidz World Montessori Play School"})

@app.get("/programs", response_class=HTMLResponse)
async def view_programs(request: Request):
    return templates.TemplateResponse("programs.html", {"request": request, "school_name": "International Kidz World Montessori Play School"})

@app.get("/contact", response_class=HTMLResponse)
async def view_contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request, "school_name": "International Kidz World Montessori Play School"})

@app.get("/gallery", response_class=HTMLResponse)
async def view_gallery(request: Request):
    # Sample data for albums - in a real app, this would come from MongoDB
    albums = [
        {
            "event_name": "Annual Sports Day",
            "date": "March 10, 2025",
            "images": [
                {"src": "/images/gallery1.jpg", "alt": "Sports Day Fun 1"},
                {"src": "/images/gallery2.jpg", "alt": "Sports Day Fun 2"},
                {"src": "/images/gallery3.jpg", "alt": "Sports Day Fun 3"},
            ]
        },
        {
            "event_name": "Christmas Celebration",
            "date": "December 20, 2024",
            "images": [
                {"src": "/images/gallery4.jpg", "alt": "Christmas Fun 1"},
                {"src": "/images/gallery5.jpg", "alt": "Christmas Fun 2"},
                {"src": "/images/gallery6.jpg", "alt": "Christmas Fun 3"},
            ]
        },
        {
            "event_name": "Graduation Ceremony",
            "date": "April 25, 2025",
            "images": [
                {"src": "/images/about-us.jpg", "alt": "Graduation 1"},
                {"src": "/images/toddler.jpg", "alt": "Graduation 2"},
            ]
        }
    ]
    return templates.TemplateResponse("gallery.html", {"request": request, "school_name": "International Kidz World Montessori Play School", "albums": albums})

@app.post("/contact", response_class=HTMLResponse)
async def handle_contact_form(request: Request, name: str = Form(...), email: str = Form(...), message: str = Form(...)):
    # In a real application, you would save this data to MongoDB Atlas
    print(f"New Contact Form Submission:")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Message: {message}")
    # For now, just redirect back to the contact page with a success message
    return templates.TemplateResponse("contact.html", {
        "request": request,
        "school_name": "International Kidz World Montessori Play School",
        "message": "Thank you for your message! We will get back to you soon."
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
