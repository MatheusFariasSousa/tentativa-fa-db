"""teste

Revision ID: e3b448ba5cb4
Revises: 0912f01c5419
Create Date: 2024-10-13 14:01:03.803748

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e3b448ba5cb4'
down_revision: Union[str, None] = '0912f01c5419'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
