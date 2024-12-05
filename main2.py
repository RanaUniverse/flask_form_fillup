"""
This is for testing of sqlmodel
"""

"""
This is the sqlmodel practise code to store notes making by users
"""

from faker import Faker
from sqlmodel import (
    create_engine,
    Field,  # type: ignore
    select,
    SQLModel,
    Session,
)
from sqlalchemy.exc import IntegrityError

fake = Faker()


class User(SQLModel, table=True):

    __tablename__ = "user_data"  # type: ignore

    id: int | None = Field(default=None, primary_key=True)
    full_name: str | None = Field(default=None)
    username: str = Field(index=True, unique=True)
    user_id: int = Field(default=None, unique=True, index=True)
    password: str | None = Field(default=None)


sqlite_file_name = "database_checking.db"

sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=0)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)



def add_user_data(
    user_obj: User | None = None,
    full_name: str | None = None,
    username: str | None = None,
    user_id: int | None = None,
    password: str | None = None,
):
    """
    Adds a user to the database.
    if user class instance pass it will use these instance obj
    otherwise it will use my values
    """

    if user_obj is None:
        print(f"No user obj is passed making a new row based on the others values")
        user_obj = User(
            full_name=full_name,
            username=username or f"{fake.word('noun')}",
            user_id=user_id or fake.random_number(digits=5),
            password=password,
        )

    with Session(engine) as session:
        try:
            session.add(user_obj)
            session.commit()
            session.refresh(user_obj)
            print(f"\033[32m✅ User added: {user_obj} ✅\033[0m")

        except IntegrityError as e:
            # ❗❗❗ Here i not understand how i can differentiate if the error
            # coming for the username or user_id column's value.❗❗❗
            session.rollback()
            print(
                "\033[31m❌ Warning: User with user_id "
                f"{user_obj.user_id} already exists. ❌\033[0m"
            )

        except Exception as e:
            print(f"Error: {e}")


def search_user_by_username(username_to_find: str | None = None):
    """
    Practise Function Making
    This will show a result of the given usrename, it will
    return User OBJ
    Here i will write the username and it will search in table and return this
    """
    if not username_to_find:
        print("❌ Warning: No username provided. Please provide a valid username. ❌")
        print("Username Example: 'ice', 'picture', 'rana_123' etc.")
        return None

    # ❗❗❗ This below has some warning issue i dont understand ❗❗❗
    if not isinstance(username_to_find, str):  # type: ignore
        print("❌ Warning: Username must be a string. ❌")
        print("Username Example: 'ice', 'picture', 'rana_123' etc.")
        return None

    with Session(engine) as session:
        statement = select(User).where(User.username == username_to_find)
        result = session.exec(statement).first()

        if result:
            print(f"✅User found✅: {result}")
        else:
            print("❌No user found with the provided username.❌")

        return result


def main():
    create_db_and_tables()
    add_user_data(password="ldkfjdl")
    # search_user_by_username("manik")


if __name__ == "__main__":
    main()
