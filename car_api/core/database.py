from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from car_api.core.settings import Settings

engine = create_async_engine(Settings().DATABASE_URL)

# Co-routine for conect and obtain database session (execution cursor for commit changes)
async def get_session():
    async with AsyncSession(engine, expire_on_commit=False) as session:
        yield session
