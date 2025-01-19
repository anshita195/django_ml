from django.urls import re_path  # Use path() from django.urls
from rest_framework.routers import DefaultRouter

from apps.endpoints.views import EndpointViewSet
from apps.endpoints.views import MLAlgorithmStatusViewSet
from apps.endpoints.views import MLAlgorithmViewSet
from apps.endpoints.views import MLRequestViewSet
from apps.endpoints.views import PredictView

# Define the router
router = DefaultRouter(trailing_slash=False)
router.register(r"endpoints", EndpointViewSet, basename="endpoints")
router.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register(r"mlalgorithmstatuses", MLAlgorithmStatusViewSet, basename="mlalgorithmstatuses")
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")

# Use path() instead of url() (for Django 2.0+)
# urlpatterns = [
#     path("api/v1/", include(router.urls)),
# ]

# urlpatterns = router.urls

urlpatterns=[
    *router.urls,
#     re-path is path using regex
#     re_path(pattern, view, name)
        # pattern: The regex pattern to match the URL.
        # view: The view function or class that will handle the matched URL.
        # name: An optional name for the route, used for reverse URL lookups.
    re_path(
        r"^(?P<endpoint_name>[^/]+)/predict$",
        PredictView.as_view(),
        name="predict",
    ),
]


# from django.conf.urls import include,url
# from django.urls import path
# from rest_framework.routers import DefaultRouter

# from apps.endpoints.views import EndpointViewSet
# from apps.endpoints.views import MLAlgorithmStatusViewSet
# from apps.endpoints.views import MLAlgorithmViewSet
# from apps.endpoints.views import MLRequestViewSet

# router = DefaultRouter(trailing_slash=False)
# router.register(r"endpoints",EndpointViewSet,basename="endpoints")
# router.register(r"mlalgorithms",MLAlgorithmViewSet,basename="mlalgorithms")
# router.register(r"mlalgorithmstatuses",MLAlgorithmStatusViewSet,basename="mlalgorithmstatuses")
# router.register(r"mlrequests",MLRequestViewSet,basename="mlrequests")

# urlpatterns = [
#     url(r"^api/v1/", include(router.urls)),
# ]

# # urlpatterns=[
# #     path("api/v1/",include(router.urls))
# # ]