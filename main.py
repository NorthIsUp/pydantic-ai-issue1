from pydantic import BaseModel
from pydantic_ai import Agent


class ImBroke(BaseModel):
    agent: Agent[None, BaseModel]


def main():
    print("Hello from pydantic-ai-issue!")


if __name__ == "__main__":
    main()
