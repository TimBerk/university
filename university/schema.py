import graphene

from courses.schema import Query as CourseQuery
from schedule.schema import Query as ScheduleQuery


class Query(CourseQuery, ScheduleQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
