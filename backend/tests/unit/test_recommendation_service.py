import pytest
from app.services.recommendation_service import recommendation_service

@pytest.mark.asyncio
async def test_get_trending_courses():
    courses = await recommendation_service.get_trending_courses()
    assert len(courses) > 0
    assert "trending_score" in courses[0]

@pytest.mark.asyncio
async def test_get_continue_learning():
    # Pass a dummy db session
    courses = await recommendation_service.get_continue_learning(user_id=1, db=None)
    assert len(courses) > 0
    assert "progress" in courses[0]

@pytest.mark.asyncio
async def test_get_for_you_courses():
    courses = await recommendation_service.get_for_you_courses(user_id=1)
    assert len(courses) > 0
    assert "score" in courses[0]
