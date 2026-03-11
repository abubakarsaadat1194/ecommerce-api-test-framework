MAX_RESPONSE_TIME = 1.5  # seconds


def validate_response_time(response):

    response_time = response.elapsed.total_seconds()

    print(f"Response Time: {response_time:.3f} seconds")

    assert response_time < MAX_RESPONSE_TIME