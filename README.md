# Todo Backend

This is the backend for a Todo app, built to be fast, secure, and easy to use.

## Architecture and Stack

* **Framework:** Django + Django REST Framework (DRF) for rapid, secure APIs.
* **Authentication:** JSON Web Tokens (JWT) via `djangorestframework-simplejwt` for secure user authentication.
* **Database:**
  * **Development:** SQLite for ease of local setup.
  * **Production (Optional):** PostgreSQL for a more robust and scalable production environment.
* **API Documentation:** `drf-spectacular` for generating OpenAPI 3 schemas, providing interactive Swagger UI and Redoc interfaces for easy API exploration.

## Project Goals

The primary goals of this project are to:

* Provide a complete and functional backend for a Todo application.
* Demonstrate best practices in Django and DRF development.
* Implement secure user authentication and authorization.
* Offer clear and interactive API documentation.
* Be easily deployable and scalable.

## Packages/ libraries used

* **Django:** The core web framework for building the application.
* **Django REST Framework (DRF):** A powerful toolkit for building Restfull APIs.
* **djangorestframework-simplejwt:** Provides JSON Web Token (JWT) authentication for securing API endpoints.
* **django-cors-headers:** Manages Cross-Origin Resource Sharing (CORS), allowing a separate frontend application to communicate with this backend.
* **django-filter:** Enables easy-to-use and powerful filtering for API querysets.
* **drf-spectacular:** Automatically generates OpenAPI 3 schema and provides interactive API documentation (Swagger UI/Redoc).
* **Markdown:** Used by DRF to render descriptions in the browsable API.
