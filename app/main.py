from app.config import APP_NAME


def hello():
    return f"Welcome to {APP_NAME}"


if __name__ == "__main__":
    print(hello())