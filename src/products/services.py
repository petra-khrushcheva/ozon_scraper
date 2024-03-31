from uuid import UUID

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import contains_eager, selectinload

from src.products.models import Product
from src.products.schemas import Product, ProductsCount


async def start_scraping():
    pass


async def get_products(session: AsyncSession):
    pass


async def get_product(session: AsyncSession):
    pass


# class WorkspaceCRUD:

#     @staticmethod
#     async def create_workspace(
#         session: AsyncSession, ws_data: WorkspaceCreate, current_user: User
#     ):
#         workspace = Workspace(**ws_data.model_dump())
#         workspace_role = WorkspaceUserAssociation(
#             user=current_user, user_role=GroupRole.admin.value
#         )
#         workspace.users.append(workspace_role)
#         session.add(workspace)
#         await session.commit()
#         await session.refresh(workspace)
#         return workspace

#     @staticmethod
#     async def get_workspace(session: AsyncSession, ws_id: UUID):
#         return await session.get(Workspace, ws_id)

#     @staticmethod
#     async def get_workspace_with_tasks(
#         session: AsyncSession,
#         ws_id: UUID,
#         # current_user: User
#     ):
#         stmt = (
#             select(Workspace)
#             .options(selectinload(Workspace.tasks).selectinload(Task.executor))
#             .filter_by(id=ws_id)
#         )
#         result = await session.execute(stmt)
#         return result.scalar_one_or_none()

#     # здесь можно будет добавить функционал, показывающий,
#     # является ли каррент юзер исполнителем или создателем задачи.

#     @staticmethod
#     async def get_workspaces(session: AsyncSession, current_user: User):
#         subq = (
#             select(Task.id.label("task_id"))
#             .filter(Task.workspace_id == Workspace.id)
#             .order_by(Task.created_at.desc())
#             .limit(TASKS_PER_WS_FRONT_PAGE_LIMIT)
#             .scalar_subquery()
#             .correlate(Workspace)
#         )
#         stmt = (
#             select(Workspace)
#             .join(WorkspaceUserAssociation)
#             .join(Task, Task.id.in_(subq), isouter=True)
#             .where(WorkspaceUserAssociation.user_id == current_user.id)
#             .options(contains_eager(Workspace.tasks).joinedload(Task.executor))
#         )
#         result: Result = await session.execute(stmt)
#         workspaces = result.unique().scalars().all()
#         print(list(workspaces))
#         return list(workspaces)


# class WSMembershipCRUD:

#     @staticmethod
#     async def add_member_to_ws(
#         session: AsyncSession,
#         workspace: Workspace,
#         membership: MembershipCreate,
#     ):
#         ws_membership = WorkspaceUserAssociation(
#             workspace_id=workspace.id, **membership.model_dump()
#         )
#         session.add(ws_membership)
#         await session.commit()

#     @staticmethod
#     async def get_ws_user(session: AsyncSession, ws_id: UUID, user_id: UUID):
#         stmt = (
#             select(User)
#             .join(WorkspaceUserAssociation)
#             .where(
#                 User.id == user_id,
#                 WorkspaceUserAssociation.workspace_id == ws_id,
#             )
#         )
#         user: Result = await session.execute(stmt)
#         return user.scalar_one_or_none()

#     @staticmethod
#     async def get_ws_user_with_tasks(
#         session: AsyncSession, user: User, workspace: Workspace
#     ):
#         stmt = (
#             select(User)
#             .where(User.id == user.id)
#             .options(
#                 selectinload(
#                     User.appointed_tasks.and_(
#                         Task.workspace_id == workspace.id,
#                         Task.executor_id == User.id,
#                     )
#                 )
#             )
#             .options(
#                 selectinload(
#                     User.workspaces.and_(
#                         WorkspaceUserAssociation.workspace_id == workspace.id
#                     )
#                 )
#             )
#         )
#         result: Result = await session.execute(stmt)
#         return result.scalar_one()

#     @staticmethod
#     async def get_all_ws_members(session: AsyncSession, ws_id: UUID):
#         stmt = (
#             select(User)
#             .join(WorkspaceUserAssociation)
#             .where(WorkspaceUserAssociation.workspace_id == ws_id)
#             .options(
#                 selectinload(
#                     User.workspaces.and_(
#                         WorkspaceUserAssociation.workspace_id == ws_id
#                     )
#                 )
#             )
#         )
#         result: Result = await session.execute(stmt)
#         return result.scalars().all()
