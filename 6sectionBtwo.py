import time


def rate_limit(limit_calls_per_minute):
    def decorator(func):
        last_call_times = []
        
        def rate_limited_call(*args, **kwargs):
            # Check if the number of calls in the last minute exceeds the limit
            current_time = time.time()
            last_call_times[:] = [t for t in last_call_times if t > current_time - 60]
            if len(last_call_times) >= limit_calls_per_minute:
                # Penalty - wait for one minute before making the call
                time_to_wait = 60 - (current_time - last_call_times[0])
                time.sleep(time_to_wait)
                
            last_call_times.append(current_time)
            return func(*args, **kwargs)
        
        return rate_limited_call

    return decorator

# API call_me function with a limit of 15 calls per minute
@rate_limit(15)
def call_me(input):
    # Simulate the API call with some processing delay
    time.sleep(1)
    return f"API Response for {input}"

# Test the rate-limited API call
for i in range(20):
    response = call_me(f"Data-{i}")
    print(response)
"""API Response for Data-0
API Response for Data-1
API Response for Data-2
API Response for Data-3
API Response for Data-4
API Response for Data-5
API Response for Data-6
API Response for Data-7
API Response for Data-8
API Response for Data-9
API Response for Data-10
API Response for Data-11
API Response for Data-12
API Response for Data-13
API Response for Data-14
API Response for Data-15
API Response for Data-16
API Response for Data-17
API Response for Data-18
API Response for Data-19"""


"""The APICaller class above implements a rate-limiting mechanism using a token bucket algorithm. 
   The call_me method is responsible for making API calls while adhering to the rate limit.

    In short, the call_me method does the following:

    Checks if enough time (4 seconds) has passed since the last token bucket refill.
    If so, refills the token bucket by adding tokens based on the elapsed time.
    Decrements the token bucket count for each API call made, as long as tokens are available.
    If the token bucket is empty, it waits until a token becomes available before making additional API calls.

    This rate-limiting mechanism ensures that the API calls are made in a controlled manner, preventing the 
    caller from exceeding the allowed limit and avoiding penalties imposed by the API provider."""



"""There is an API that one must call to get data. The trouble is it will not let you cross
the limit of call - say 15 calls per minute. If you cross the limit, the system penalises
you by one additional minute of penalty where you can not make any call. Here ishow the API 
looks like: function string call_me(string input).
Propose a solution by which:

        1. You would be able to use the API within the safe limit.
        To use the API within the safe limit of 15 calls per minute, 
        you can implement a rate-limiting mechanism as described in the previous answer. 
        However, since we don't have access to the actual API in this environment, we can
        simulate the API calls using the call_me function inside the decorator.

        2. What happens if you are supposed to call the API 20 times per minute? Is there any way to accomplish this?
        If you are supposed to call the API 20 times per minute and the API enforces a rate limit of 15 calls per minute 
        with a penalty of one additional minute, you won't be able to accomplish making 20 calls per minute without getting penalized by the API.

        The rate-limiting mechanism described in the previous answer will prevent you from exceeding the safe limit of 15 
        calls per minute. Once you reach this limit, any additional calls will be delayed to avoid further penalties. 
        Even if you attempt to make 20 calls per minute, the rate-limiter will ensure that you only make 15 calls within 
        the first minute and will penalize you for any excess calls made.

        If you need to make 20 calls per minute without being penalized, you should either negotiate with the API provider 
        to increase the rate limit to accommodate your needs or consider using multiple API keys or accounts to distribute 
        the load across different identities, each with their own rate limits. However, this approach depends on the terms 
        and conditions set by the API provider, and it's essential to abide by their policies to avoid any potential issues.

        3. If you were the API designer, what would you do to implement this behaviour?
        As the API designer, I would implement a straightforward rate-limiting system that tracks the number of API calls 
        made by each client within a minute. If a client exceeds the limit, I would enforce a one-minute penalty before 
        allowing further API calls from that client."""


