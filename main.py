import uvicorn


def main() -> None:
    """Run the ChatPDF application."""

    uvicorn.run(
        "app.application:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )


if __name__ == "__main__":
    main()
