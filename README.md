# Fungarium Dashboard

This project is a Streamlit dashboard for Fungarium, designed to provide customers with an interactive experience. The dashboard includes user authentication, a sidebar, and two main components: a RAG chat and a form for data submission.

## Project Structure

The project is organized as follows:

```
fungarium-dashboard
├── src
│   ├── app.py                # Main entry point for the Streamlit application
│   ├── auth                  # Package for user authentication
│   │   ├── __init__.py       # Empty initializer for the auth package
│   │   └── authentication.py  # User authentication logic
│   ├── components            # UI components for the dashboard
│   │   ├── __init__.py       # Empty initializer for the components package
│   │   ├── chat.py           # RAG chat component
│   │   ├── form.py           # Form component for data submission
│   │   └── sidebar.py        # Sidebar layout and branding
│   ├── config                # Configuration settings
│   │   ├── __init__.py       # Empty initializer for the config package
│   │   └── settings.py       # Application configuration settings
│   ├── services              # Services for handling business logic
│   │   ├── __init__.py       # Empty initializer for the services package
│   │   ├── n8n_webhook.py    # Webhook integration with n8n
│   │   └── rag_service.py     # RAG service logic
│   ├── styles                # Styling and theming
│   │   ├── __init__.py       # Empty initializer for the styles package
│   │   └── theme.py          # Dashboard styling
│   └── utils                 # Utility functions
│       ├── __init__.py       # Empty initializer for the utils package
│       └── helpers.py        # Helper functions
├── requirements.txt          # Python dependencies
├── .env.example              # Example environment variables
├── .gitignore                # Files to ignore by Git
└── README.md                 # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/One80-dashboard.git
   cd One80-dashboard
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables by copying `.env.example` to `.env` and filling in the necessary values.

5. Run the Streamlit application:
   ```
   streamlit run src/app.py
   ```

## Usage

- Users can log in using their credentials.
- The sidebar provides navigation and branding elements.
- The RAG chat allows users to interact and receive insights.
- The form enables users to submit data for processing.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.