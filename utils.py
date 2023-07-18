import replicate
import time

# Initialize debounce variables
last_call_time = 0
debounce_interval = 1  # Set the debounce interval (in seconds) to your desired value

def debounce_replicate_run(llm, prompt, max_len, temperature, top_p, API_TOKEN):
    global last_call_time
    print("last call time: ", last_call_time)

    # Get the current time
    current_time = time.time()

    # Calculate the time elapsed since the last call
    elapsed_time = current_time - last_call_time

    # Check if the elapsed time is less than the debounce interval
    if elapsed_time < debounce_interval:
        print("Debouncing")
        return "¡Hola! Está enviando solicitudes demasiado rápido. Espere unos segundos antes de enviar otra solicitud."


    # Update the last call time to the current time
    last_call_time = time.time()
    
    output = replicate.run(llm, input={"prompt": prompt + "Assistant: ", "max_length": max_len, "temperature": temperature, "top_p": top_p, "repetition_penalty": 1}, api_token=API_TOKEN)
    return output
