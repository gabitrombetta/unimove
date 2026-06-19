from dataclasses import asdict

from sqlalchemy import select

from unimove.models import User


def test_create_user_db(session):
    new_user = User(
        matricula='347892', email='test@example.com', senha='testpwd'
    )

    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.matricula == '347892'))

    assert asdict(user) == {
        'id': 1,
        'matricula': '347892',
        'email': 'test@example.com',
        'senha': 'testpwd',
    }
