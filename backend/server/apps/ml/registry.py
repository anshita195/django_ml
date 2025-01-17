from apps.endpoints.models import Endpoint
from apps.endpoints.models import MLAlgorithm
from apps.endpoints.models import MLAlgorithmStatus

class MLRegistry:
    def __init__(self):
        self.endpoints={}
        #dictionary with key as ML model IDs and value as actual ML object

    def add_algorithm(
            self,
            endpoint_name,
            algorithm_object,
            algorithm_name,
            algorithm_status,
            algorithm_version,
            owner,
            algorithm_description,
            algorithm_code):
        #get endpoint
        endpoint,_= Endpoint.objects.get_or_create(name=endpoint_name,owner=owner)
            # The result of get_or_create() is a tuple:
            # The first value (endpoint) is the Endpoint object (either the existing one or the newly created one).
            # The second value (_) is a boolean indicating whether a new record was created (True if created, False if fetched from the database). 
            # The underscore (_) is a convention in Python to indicate that this value is being ignored.
        
        #get algorithm
        database_object,algorithm_created=MLAlgorithm.objects.get_or_create(
            name=algorithm_name,
            description=algorithm_description,
            code=algorithm_code,
            version=algorithm_version,
            owner=owner,
            parent_endpoint=endpoint)
        
        if algorithm_created:
            status=MLAlgorithmStatus(
                status=algorithm_status,
                created_by=owner,
                parent_mlalgorithm=database_object,
                active=True)
            status.save()
    
        self.endpoints[database_object.id]=algorithm_object