import enum
from uuid import UUID

from sqlalchemy import ForeignKey, String, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.basemodels import Base


class Product(Base):
    __tablename__ = "products"

    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str | None] = mapped_column(Text)


# class Workspace(Base):
#     __tablename__ = "workspaces"

#     name: Mapped[str] = mapped_column(String(50))
#     description: Mapped[str | None] = mapped_column(Text)

#     users: Mapped[list["WorkspaceUserAssociation"]] = relationship(
#         back_populates="workspace", cascade="all, delete"
#     )
#     tasks: Mapped[list["Task"]] = relationship(  # noqa: F821
#         back_populates="workspace",
#         primaryjoin=(
#             "and_(Workspace.id==Task.workspace_id, Task.is_active==True)"
#         ),
#         order_by="Task.created_at.desc()",
#     )


# class WorkspaceUserAssociation(Base):
#     __tablename__ = "workspace_user_association"
#     __table_args__ = (
#         UniqueConstraint(
#             "user_id",
#             "workspace_id",
#             name="unique_workspace_user",
#         ),
#     )

#     workspace_id: Mapped[UUID] = mapped_column(
#         ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=False
#     )
#     user_id: Mapped[UUID] = mapped_column(
#         ForeignKey("users.id", ondelete="CASCADE"), nullable=False
#     )
#     user_role: Mapped[GroupRole] = mapped_column(
#         default=GroupRole.user.value, server_default=GroupRole.user.value
#     )

#     workspace: Mapped["Workspace"] = relationship(
#         back_populates="users",
#     )

#     user: Mapped["User"] = relationship(  # noqa: F821
#         back_populates="workspaces",
#     )
