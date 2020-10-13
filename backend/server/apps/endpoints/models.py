from django.db import models

# Create your models here.
class Endpoint(models.Model):
    '''
    Endpoint object represents ML API endpoint

    Attributes:
        name: The name of the endpoint, used in API URL
        owner: String that has the owner name
        created_at: The date of the endpoint's creation
    '''

    name = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

class MLAlgorithm(models.Model):
    '''
    MLAlgorithm represents our machine learning algo object

    Attributes:
        name: name of the algorithm 
        description: how the algorithm functions
        code: code of the algorithm
        version: the version of the algorithm
        owner: name of the owner
        created_at: date when MLAlgorithm was added
        parent_endpoint: reference to the Endpoint
    '''

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1000)
    code = models.CharField(max_length=50000)
    version = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_endpoint = models.ForeignKey(Endpoint, on_delete=models.CASCADE)

class MLAlgorithmStatus(models.Model):
    '''
    Represents the status of the MLAlgorithm as it changes

    Attributes:
        status: The status at the endpoint, values can be staging, testing, ab_testing, production
        active: boolean, current active status
        created_by: name of creator
        created_at: date of creation of the status
        parent_algorithm: referencing to the MLAlgorithm

    '''

    status = models.CharField(max_length=128)
    active = models.BooleanField()
    created_by = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE, related_name = "status")

class MLRequest(models.Model):
    '''
    Keeps the information about all requests made to the algorithms

    Attributes:
        input_data: The input data to ML algorithm in JSON.
        full_response: The response of the ML algorithm.
        response: The response of the ML algorithm in JSON.
        feedback: The feedback about the response in JSON.
        created_at: The date when request was created.
        parent_mlalgorithm: referencing to the MLAlgorithm used to create response

    '''
    input_data = models.CharField(max_length=10000)
    full_response = models.CharField(max_length=10000)
    response = models.CharField(max_length=10000)
    feedback = models.CharField(max_length=10000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE)

class ABTest(models.Model):
    '''
    Keeps information about A/B tests that we perform

    Attributes:
        title: test's title
        created_by: creator name
        created_at: data of creation
        ended_at: data when test is stopped
        summary: description with summary that is created when test is stopped
        parent_mlalgorithm_1: 1st MLAlgorithm reference
        parent_mlalgorithm_2: 2nd MlAlgorithm reference
    '''
    title = models.CharField(max_length=10000)
    created_by = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    summary = models.CharField(max_length=10000, blank=True, null=True)

    parent_mlalgorithm_1 = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE, related_name="parent_mlalgorithm_1")
    parent_mlalgorithm_2 = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE, related_name="parent_mlalgorithm_2")
