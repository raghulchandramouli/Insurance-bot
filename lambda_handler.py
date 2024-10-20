import json
import boto3

# Initialize Bedrock client
bedrock = boto3.client('bedrock-runtime')

# Knowledge base ID (replace with your actual knowledge base ID)
KNOWLEDGE_BASE_ID = ''

# LLM model ID (replace with your preferred model ID)
MODEL_ID = ''

def query_knowledge_base(user_input):
    """Query the Bedrock knowledge base with the user input."""
    bedrock_runtime = boto3.client('bedrock-runtime')
    
    request_body = {
        "prompt": user_input,
        "max_gen_len": 512,
        "temperature": 0.5,
        "top_p": 0.9
    }
    
    response = bedrock_runtime.invoke_model(
        modelId=MODEL_ID,
        contentType='application/json',
        accept='application/json',
        body=json.dumps(request_body)
    )
    
    # Parse the response
    response_body = json.loads(response['body'].read())
    
    # Extract the generated text from the response
    generated_text = response_body.get('generation', '')
    
    return generated_text

def optimize_with_llm(user_input, retrieved_info):
    """Send the query and retrieved info to the LLM for optimization."""
    prompt = f"""
    User query: {user_input}
    Retrieved information: {retrieved_info}

    Please optimize and format the response to the user query based on the retrieved information.
    """

    response = bedrock.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps({
            "prompt": prompt,
            "max_gen_len": 512,
            "temperature": 0.7,
            "top_p": 1,
            "stop_sequences": ["\n\nHuman:"]
        })
    )

    llm_output = json.loads(response['body'].read())['completion']
    return llm_output.strip()

def format_response(user_input, optimized_response):
    """Format the final response."""
    return f"""
    User Query: {user_input}

    Optimized Response:
    {optimized_response}
    """

def lambda_handler(event, context):
    # Get user input from the event
    user_input = event.get('user_input', '')
    
    if not user_input:
        return {
            'statusCode': 400,
            'body': json.dumps('Please provide a user_input in the event payload.')
        }

    try:
        # Query the knowledge base
        retrieved_info = query_knowledge_base(user_input)

        # For now, we'll skip the optimize_with_llm step
        # optimized_response = optimize_with_llm(user_input, retrieved_info)

        # Format the final response
        formatted_response = {
            'user_input': user_input,
            'response': retrieved_info
        }

        return {
            'statusCode': 200,
            'body': json.dumps(formatted_response)
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }

# Add this at the end of the file
if __name__ == '__main__':
    # Test event with user input
    test_event = {
        'user_input': 'What meant by health insurance?'
    }
    
    # Call the lambda_handler function with the test event
    response = lambda_handler(test_event, None)
    
    # Print the response
    print(json.dumps(response, indent=2))
