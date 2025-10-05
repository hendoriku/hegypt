# Hegypt - Ideal AI Prompt Generator 🚀

![Hegypt App Screenshot](https://i.ibb.co/6P6XyL6/hegypt-ss.png)

*Read this in other languages: [Indonesian](#-versi-bahasa-indonesia)*

**Hegypt** is a web application designed to tackle one of the biggest challenges in AI interaction: **crafting the perfect prompt**. This application acts as your personal assistant, guiding you through a structured form to design, save, manage, and reuse ideal prompts for various technical and creative needs.

This project is a complete solution, from brainstorming a prompt in a local environment to making it accessible over the network with a custom domain via a reverse proxy.

---

## ✨ Key Features

-   **Structured Prompt Form**: A methodically designed form with fields for AI Persona, Core Objective, Context, Output Format, and Rules to ensure every generated prompt is rich in detail.
-   **History Management (CRUD)**: Save every prompt you create to a database. Easily review, **Edit**, **Update**, and **Delete** old prompts through the history page.
-   **Automatic Prompt Text Generation**: Intelligently combines all inputs from the form into a single, coherent prompt text ready to be copied.
-   **Network & Custom Domain Accessibility**: Designed to be accessible over a local network using the **Waitress** WSGI server and can be pointed to from a public domain (e.g., `hegypt.dix.my.id`) using **Nginx Proxy Manager**.
-   **One-Click Windows Launcher**: Comes with a `.bat` script that automates the entire startup process—activating the virtual environment and starting the server—with a single click from a desktop shortcut.

---

## 🛠️ Tech Stack & Architecture

This application is built with a modern and reliable tech stack, suitable for both development and self-hosted deployment.

| Category          | Technology                                                                              |
| ----------------- | --------------------------------------------------------------------------------------- |
| **Backend** | Python, Flask, Flask-SQLAlchemy                                                         |
| **Frontend** | HTML5, CSS3, JavaScript (Vanilla)                                                       |
| **Database** | MySQL (for local development)                                                           |
| **WSGI Server** | Waitress (Cross-platform, ideal for Windows & local networks)                           |
| **Reverse Proxy** | Nginx Proxy Manager (for domain management, SSL, and forwarding)                        |

### Local Network Architecture
The request flow when accessed via a domain:
